"""Deterministic Phase-5 intent-integrity and effect-authority boundary.

This module deliberately does not infer what a human "really meant".
It verifies integrity/bindings and requires an explicit authority object
for the exact proposed effect.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Any

HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
INTENT_ID_RE = re.compile(r"^intent:sha256:[0-9a-f]{64}$")
EFFECT_ID_RE = re.compile(r"^effect:sha256:[0-9a-f]{64}$")
BINDING_ID_RE = re.compile(r"^verified-intent:sha256:[0-9a-f]{64}$")
AUTHORITY_ID_RE = re.compile(r"^effect-authority:sha256:[0-9a-f]{64}$")
TS_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")


class BoundaryError(ValueError):
    pass


def canonical_bytes(value: Any) -> bytes:
    def normalize(item: Any, path: str = "$") -> Any:
        if item is None or isinstance(item, bool) or isinstance(item, str):
            return item
        if isinstance(item, int) and not isinstance(item, bool):
            if not -(2**53 - 1) <= item <= (2**53 - 1):
                raise BoundaryError(f"{path}: integer outside safe range")
            return item
        if isinstance(item, float):
            raise BoundaryError(f"{path}: floating-point values are forbidden")
        if isinstance(item, list):
            return [normalize(v, f"{path}[]") for v in item]
        if isinstance(item, dict):
            if any(not isinstance(k, str) for k in item):
                raise BoundaryError(f"{path}: object keys must be strings")
            return {k: normalize(item[k], f"{path}.{k}") for k in sorted(item)}
        raise BoundaryError(f"{path}: unsupported value type {type(item).__name__}")

    return json.dumps(
        normalize(value), ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def _sha256_prefixed(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def raw_intent_hash(raw_human_intent: str) -> str:
    if not isinstance(raw_human_intent, str) or not raw_human_intent:
        raise BoundaryError("raw_human_intent must be a non-empty string")
    return _sha256_prefixed(raw_human_intent.encode("utf-8"))


def _identity_payload(value: dict[str, Any], id_field: str) -> dict[str, Any]:
    payload = copy.deepcopy(value)
    payload.pop(id_field, None)
    payload.pop("content_hash", None)
    return payload


def _derive_identity(value: dict[str, Any], id_field: str, prefix: str) -> tuple[str, str]:
    digest = hashlib.sha256(canonical_bytes(_identity_payload(value, id_field))).hexdigest()
    return f"{prefix}:sha256:{digest}", f"sha256:{digest}"


def with_boundary_identity(value: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(value)
    version = result.get("schema_version")
    if version == "saddle-verified-intent-binding/0.1":
        field, prefix = "binding_id", "verified-intent"
    elif version == "saddle-effect-authority/0.1":
        field, prefix = "authority_id", "effect-authority"
    else:
        raise BoundaryError(f"unsupported boundary schema_version: {version}")
    object_id, content_hash = _derive_identity(result, field, prefix)
    result[field] = object_id
    result["content_hash"] = content_hash
    return result


def _validate_identity(value: dict[str, Any], id_field: str, prefix: str) -> None:
    expected_id, expected_hash = _derive_identity(value, id_field, prefix)
    if value.get(id_field) != expected_id or value.get("content_hash") != expected_hash:
        raise BoundaryError(f"{id_field}: content-addressed identity mismatch")


def _timestamp(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or TS_RE.fullmatch(value) is None:
        raise BoundaryError(f"{field}: expected UTC second-resolution timestamp")
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def _hash(value: Any, field: str) -> None:
    if not isinstance(value, str) or HASH_RE.fullmatch(value) is None:
        raise BoundaryError(f"{field}: expected sha256:<64hex>")


def _text(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value:
        raise BoundaryError(f"{field}: expected non-empty string")


def validate_verified_intent_binding(binding: dict[str, Any]) -> None:
    fields = {
        "schema_version", "binding_id", "content_hash", "intent_id",
        "intent_content_hash", "raw_intent_hash", "principal_ref",
        "origin_event", "status", "issued_at", "expires_at"
    }
    if not isinstance(binding, dict) or set(binding) != fields:
        raise BoundaryError("VerifiedIntentBinding: exact fields required")
    if binding["schema_version"] != "saddle-verified-intent-binding/0.1":
        raise BoundaryError("VerifiedIntentBinding: unsupported schema_version")
    if BINDING_ID_RE.fullmatch(str(binding["binding_id"])) is None:
        raise BoundaryError("binding_id: invalid")
    _hash(binding["content_hash"], "content_hash")
    if INTENT_ID_RE.fullmatch(str(binding["intent_id"])) is None:
        raise BoundaryError("intent_id: invalid")
    _hash(binding["intent_content_hash"], "intent_content_hash")
    _hash(binding["raw_intent_hash"], "raw_intent_hash")
    _text(binding["principal_ref"], "principal_ref")
    event = binding["origin_event"]
    if not isinstance(event, dict) or set(event) != {"ref_id", "content_hash", "observed_at"}:
        raise BoundaryError("origin_event: exact immutable ref fields required")
    _text(event["ref_id"], "origin_event.ref_id")
    _hash(event["content_hash"], "origin_event.content_hash")
    _timestamp(event["observed_at"], "origin_event.observed_at")
    if binding["status"] not in {"ACTIVE", "REVOKED", "EXPIRED"}:
        raise BoundaryError("status: invalid")
    issued = _timestamp(binding["issued_at"], "issued_at")
    expires = _timestamp(binding["expires_at"], "expires_at")
    if expires <= issued:
        raise BoundaryError("expires_at must be after issued_at")
    _validate_identity(binding, "binding_id", "verified-intent")


def validate_effect_authority(authority: dict[str, Any]) -> None:
    fields = {
        "schema_version", "authority_id", "content_hash", "decision",
        "intent_binding_id", "intent_binding_hash", "effect_id",
        "effect_content_hash", "authorized_action", "authorized_target",
        "evidence_requirements", "issuer_kind", "issuer_ref", "source_refs",
        "status", "max_uses", "issued_at", "expires_at", "reason"
    }
    if not isinstance(authority, dict) or set(authority) != fields:
        raise BoundaryError("EffectAuthority: exact fields required")
    if authority["schema_version"] != "saddle-effect-authority/0.1":
        raise BoundaryError("EffectAuthority: unsupported schema_version")
    if AUTHORITY_ID_RE.fullmatch(str(authority["authority_id"])) is None:
        raise BoundaryError("authority_id: invalid")
    _hash(authority["content_hash"], "content_hash")
    if authority["decision"] not in {"ALLOW", "DENY"}:
        raise BoundaryError("decision: invalid")
    if BINDING_ID_RE.fullmatch(str(authority["intent_binding_id"])) is None:
        raise BoundaryError("intent_binding_id: invalid")
    _hash(authority["intent_binding_hash"], "intent_binding_hash")
    if EFFECT_ID_RE.fullmatch(str(authority["effect_id"])) is None:
        raise BoundaryError("effect_id: invalid")
    _hash(authority["effect_content_hash"], "effect_content_hash")
    _text(authority["authorized_action"], "authorized_action")
    target = authority["authorized_target"]
    if not isinstance(target, dict) or set(target) != {"kind", "ref"}:
        raise BoundaryError("authorized_target: exact kind/ref required")
    _text(target["kind"], "authorized_target.kind")
    _text(target["ref"], "authorized_target.ref")
    reqs = authority["evidence_requirements"]
    if not isinstance(reqs, list) or not reqs or any(not isinstance(x, str) or not x for x in reqs):
        raise BoundaryError("evidence_requirements: non-empty string array required")
    if authority["issuer_kind"] not in {"HUMAN", "POLICY"}:
        raise BoundaryError("issuer_kind: invalid")
    _text(authority["issuer_ref"], "issuer_ref")
    refs = authority["source_refs"]
    if not isinstance(refs, list) or not refs or any(not isinstance(x, str) or not x for x in refs):
        raise BoundaryError("source_refs: non-empty string array required")
    if authority["status"] not in {"ACTIVE", "REVOKED", "EXPIRED"}:
        raise BoundaryError("status: invalid")
    if authority["max_uses"] != 1:
        raise BoundaryError("max_uses must equal 1 in Phase 5")
    issued = _timestamp(authority["issued_at"], "issued_at")
    expires = _timestamp(authority["expires_at"], "expires_at")
    if expires <= issued:
        raise BoundaryError("expires_at must be after issued_at")
    _text(authority["reason"], "reason")
    _validate_identity(authority, "authority_id", "effect-authority")


def verify_intent_integrity(intent: dict[str, Any], binding: dict[str, Any], *, now: datetime) -> list[str]:
    reasons: list[str] = []
    try:
        validate_verified_intent_binding(binding)
    except BoundaryError as exc:
        return [f"INVALID_VERIFIED_INTENT_BINDING:{exc}"]
    if binding["status"] != "ACTIVE":
        reasons.append("VERIFIED_INTENT_BINDING_NOT_ACTIVE")
    if now.astimezone(timezone.utc) >= _timestamp(binding["expires_at"], "expires_at"):
        reasons.append("VERIFIED_INTENT_BINDING_STALE")
    if intent.get("schema_version") != "saddle-intent/0.1":
        reasons.append("UNSUPPORTED_INTENT_ENVELOPE")
        return reasons
    if binding["intent_id"] != intent.get("intent_id"):
        reasons.append("INTENT_ID_BINDING_MISMATCH")
    if binding["intent_content_hash"] != intent.get("content_hash"):
        reasons.append("INTENT_CONTENT_HASH_BINDING_MISMATCH")
    try:
        actual_raw_hash = raw_intent_hash(intent.get("raw_human_intent"))
    except BoundaryError:
        reasons.append("RAW_HUMAN_INTENT_INVALID")
    else:
        if binding["raw_intent_hash"] != actual_raw_hash:
            reasons.append("RAW_INTENT_HASH_BINDING_MISMATCH")
    origin = intent.get("origin")
    if not isinstance(origin, dict):
        reasons.append("INTENT_ORIGIN_MISSING")
    else:
        if origin.get("status") != "VERIFIED":
            reasons.append("INTENT_ORIGIN_NOT_VERIFIED")
        if origin.get("principal_ref") != binding["principal_ref"]:
            reasons.append("PRINCIPAL_BINDING_MISMATCH")
    return reasons


def authorize_effect(
    intent: dict[str, Any],
    binding: dict[str, Any],
    proposal: dict[str, Any],
    authority: dict[str, Any] | None,
    *,
    now: datetime,
    consumed_authority_ids: set[str] | None = None,
) -> dict[str, Any]:
    """Fail closed. Semantic similarity between intent and proposal never creates permission."""
    reasons = verify_intent_integrity(intent, binding, now=now)
    if proposal.get("schema_version") != "saddle-effect-proposal/0.1":
        reasons.append("UNSUPPORTED_EFFECT_PROPOSAL")
    if proposal.get("intent_id") != intent.get("intent_id"):
        reasons.append("PROPOSAL_INTENT_MISMATCH")
    if authority is None:
        reasons.append("EXPLICIT_EFFECT_AUTHORITY_REQUIRED")
        return {"status": "BLOCK", "reasons": sorted(set(reasons))}
    try:
        validate_effect_authority(authority)
    except BoundaryError as exc:
        reasons.append(f"INVALID_EFFECT_AUTHORITY:{exc}")
        return {"status": "BLOCK", "reasons": sorted(set(reasons))}
    if authority["status"] != "ACTIVE":
        reasons.append("EFFECT_AUTHORITY_NOT_ACTIVE")
    if authority["decision"] != "ALLOW":
        reasons.append("EFFECT_AUTHORITY_DENIES")
    if now.astimezone(timezone.utc) >= _timestamp(authority["expires_at"], "expires_at"):
        reasons.append("EFFECT_AUTHORITY_STALE")
    if authority["intent_binding_id"] != binding["binding_id"]:
        reasons.append("AUTHORITY_INTENT_BINDING_ID_MISMATCH")
    if authority["intent_binding_hash"] != binding["content_hash"]:
        reasons.append("AUTHORITY_INTENT_BINDING_HASH_MISMATCH")
    if authority["effect_id"] != proposal.get("effect_id"):
        reasons.append("AUTHORITY_EFFECT_ID_MISMATCH")
    if authority["effect_content_hash"] != proposal.get("content_hash"):
        reasons.append("AUTHORITY_EFFECT_HASH_MISMATCH")
    if authority["authorized_action"] != proposal.get("action"):
        reasons.append("AUTHORITY_ACTION_MISMATCH")
    target = proposal.get("target") if isinstance(proposal.get("target"), dict) else {}
    if authority["authorized_target"] != {"kind": target.get("kind"), "ref": target.get("ref")}:
        reasons.append("AUTHORITY_TARGET_MISMATCH")
    if consumed_authority_ids is not None and authority["authority_id"] in consumed_authority_ids:
        reasons.append("EFFECT_AUTHORITY_REPLAYED")
    if reasons:
        return {"status": "BLOCK", "reasons": sorted(set(reasons))}
    if consumed_authority_ids is not None:
        consumed_authority_ids.add(authority["authority_id"])
    return {
        "status": "ALLOW",
        "reasons": ["EXACT_EFFECT_AUTHORITY_MATCH"],
        "authority_id": authority["authority_id"],
        "verified_intent_binding_id": binding["binding_id"],
    }
