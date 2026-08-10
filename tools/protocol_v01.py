"""Minimal deterministic utilities for Saddle Protocol v0.1.

No third-party dependency. The schema validator intentionally implements only the
JSON Schema 2020-12 keywords used by protocol/v0.1/*.schema.json.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

SAFE_INTEGER_MAX = 9007199254740991
SAFE_INTEGER_MIN = -SAFE_INTEGER_MAX

ID_FIELDS = {
    "saddle-intent/0.1": ("intent_id", "intent"),
    "saddle-effect-proposal/0.1": ("effect_id", "effect"),
    "saddle-effect-receipt/0.1": ("receipt_id", "receipt"),
    "saddle-state-delta/0.1": ("state_delta_id", "state-delta"),
}

SCHEMA_FILES = {
    "saddle-intent/0.1": "intent-envelope.schema.json",
    "saddle-effect-proposal/0.1": "effect-proposal.schema.json",
    "saddle-effect-receipt/0.1": "effect-receipt.schema.json",
    "saddle-state-delta/0.1": "state-delta.schema.json",
}


class ProtocolError(ValueError):
    pass


class SchemaValidationError(ProtocolError):
    pass


def _assert_valid_string(value: str, path: str) -> None:
    try:
        value.encode("utf-8", "strict")
    except UnicodeEncodeError as exc:
        raise ProtocolError(f"{path}: invalid Unicode string") from exc


def _utf16_sort_key(value: str) -> bytes:
    _assert_valid_string(value, "object key")
    return value.encode("utf-16-be", "strict")


def _canonical_tree(value: Any, path: str = "$") -> Any:
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, int):
        if not SAFE_INTEGER_MIN <= value <= SAFE_INTEGER_MAX:
            raise ProtocolError(f"{path}: integer outside I-JSON safe range")
        return value
    if isinstance(value, float):
        raise ProtocolError(f"{path}: floating-point JSON numbers are forbidden in Saddle Protocol v0.1")
    if isinstance(value, str):
        _assert_valid_string(value, path)
        return value
    if isinstance(value, list):
        return [_canonical_tree(item, f"{path}[{idx}]") for idx, item in enumerate(value)]
    if isinstance(value, dict):
        for key in value:
            if not isinstance(key, str):
                raise ProtocolError(f"{path}: JSON object key must be a string")
            _assert_valid_string(key, f"{path}.<key>")
        ordered: dict[str, Any] = {}
        for key in sorted(value.keys(), key=_utf16_sort_key):
            ordered[key] = _canonical_tree(value[key], f"{path}.{key}")
        return ordered
    raise ProtocolError(f"{path}: unsupported JSON value type {type(value).__name__}")


def canonicalize(value: Any) -> bytes:
    """Return RFC-8785-compatible bytes for the v0.1 restricted data model.

    Protocol v0.1 rejects floats, integers outside the interoperable I-JSON
    safe range, invalid Unicode, and duplicate keys at parsing time. With that
    restriction, Python's primitive JSON rendering plus explicit UTF-16 key
    ordering matches the JCS requirements needed by the protocol.
    """
    tree = _canonical_tree(value)
    text = json.dumps(tree, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return text.encode("utf-8")


def sha256_ref(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonicalize(value)).hexdigest()


def identity_payload(document: dict[str, Any]) -> dict[str, Any]:
    version = document.get("schema_version")
    if version not in ID_FIELDS:
        raise ProtocolError(f"unsupported schema_version: {version!r}")
    id_field, _prefix = ID_FIELDS[version]
    payload = copy.deepcopy(document)
    payload.pop(id_field, None)
    payload.pop("content_hash", None)
    return payload


def derive_identity(document: dict[str, Any]) -> tuple[str, str]:
    version = document.get("schema_version")
    if version not in ID_FIELDS:
        raise ProtocolError(f"unsupported schema_version: {version!r}")
    _id_field, prefix = ID_FIELDS[version]
    content_hash = sha256_ref(identity_payload(document))
    return f"{prefix}:{content_hash}", content_hash


def with_derived_identity(document: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(document)
    version = result.get("schema_version")
    if version not in ID_FIELDS:
        raise ProtocolError(f"unsupported schema_version: {version!r}")
    id_field, _prefix = ID_FIELDS[version]
    object_id, content_hash = derive_identity(result)
    result[id_field] = object_id
    result["content_hash"] = content_hash
    return result


def validate_identity(document: dict[str, Any]) -> None:
    version = document.get("schema_version")
    if version not in ID_FIELDS:
        raise ProtocolError(f"unsupported schema_version: {version!r}")
    id_field, _prefix = ID_FIELDS[version]
    expected_id, expected_hash = derive_identity(document)
    if document.get("content_hash") != expected_hash:
        raise ProtocolError("content_hash does not match canonical identity payload")
    if document.get(id_field) != expected_id:
        raise ProtocolError(f"{id_field} does not match content_hash")


def _no_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ProtocolError(f"duplicate JSON object property: {key}")
        result[key] = value
    return result


def _reject_float(token: str) -> float:
    raise ProtocolError(f"floating-point number forbidden: {token}")


def loads_strict(text: str) -> Any:
    try:
        value = json.loads(text, object_pairs_hook=_no_duplicate_pairs, parse_float=_reject_float)
    except json.JSONDecodeError as exc:
        raise ProtocolError(f"invalid JSON: {exc}") from exc
    _canonical_tree(value)
    return value


class SchemaRegistry:
    def __init__(self, schema_dir: Path):
        self.schema_dir = schema_dir
        self.by_id: dict[str, dict[str, Any]] = {}
        for path in sorted(schema_dir.glob("*.schema.json")):
            schema = loads_strict(path.read_text(encoding="utf-8"))
            schema_id = schema.get("$id")
            if not isinstance(schema_id, str):
                raise SchemaValidationError(f"{path}: missing $id")
            self.by_id[schema_id] = schema

    def schema_for_document(self, document: dict[str, Any]) -> dict[str, Any]:
        filename = SCHEMA_FILES.get(document.get("schema_version"))
        if not filename:
            raise SchemaValidationError("unsupported schema_version")
        schema_id = loads_strict((self.schema_dir / filename).read_text(encoding="utf-8"))["$id"]
        return self.by_id[schema_id]

    def resolve_ref(self, ref: str, current_schema: dict[str, Any]) -> dict[str, Any]:
        if ref.startswith("#"):
            target = current_schema
            fragment = ref[1:]
        else:
            base, marker, fragment = ref.partition("#")
            if base not in self.by_id:
                raise SchemaValidationError(f"unresolved $ref base: {base}")
            target = self.by_id[base]
            fragment = fragment if marker else ""
        if not fragment:
            return target
        if not fragment.startswith("/"):
            raise SchemaValidationError(f"unsupported $ref fragment: #{fragment}")
        node: Any = target
        for raw in fragment.lstrip("/").split("/"):
            token = raw.replace("~1", "/").replace("~0", "~")
            if not isinstance(node, dict) or token not in node:
                raise SchemaValidationError(f"unresolved $ref token: {token}")
            node = node[token]
        if not isinstance(node, dict):
            raise SchemaValidationError("$ref target must be a schema object")
        return node


def _type_matches(instance: Any, expected: str) -> bool:
    if expected == "null":
        return instance is None
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return (isinstance(instance, int) and not isinstance(instance, bool)) or isinstance(instance, float)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "object":
        return isinstance(instance, dict)
    return False


def validate_against_schema(instance: Any, schema: dict[str, Any], registry: SchemaRegistry, path: str = "$", root_schema: dict[str, Any] | None = None) -> None:
    root_schema = root_schema or schema

    if "$ref" in schema:
        ref = schema["$ref"]
        target = registry.resolve_ref(ref, root_schema)
        if ref.startswith("urn:"):
            base = ref.partition("#")[0]
            target_root = registry.by_id[base]
        else:
            target_root = root_schema
        validate_against_schema(instance, target, registry, path, target_root)
        return

    if "allOf" in schema:
        for sub in schema["allOf"]:
            validate_against_schema(instance, sub, registry, path, root_schema)
    if "anyOf" in schema:
        errors = []
        for sub in schema["anyOf"]:
            try:
                validate_against_schema(instance, sub, registry, path, root_schema)
                break
            except SchemaValidationError as exc:
                errors.append(str(exc))
        else:
            raise SchemaValidationError(f"{path}: no anyOf branch matched: {' | '.join(errors)}")
    if "oneOf" in schema:
        matches = 0
        for sub in schema["oneOf"]:
            try:
                validate_against_schema(instance, sub, registry, path, root_schema)
                matches += 1
            except SchemaValidationError:
                pass
        if matches != 1:
            raise SchemaValidationError(f"{path}: expected exactly one oneOf match, got {matches}")

    expected_type = schema.get("type")
    if expected_type is not None:
        allowed = [expected_type] if isinstance(expected_type, str) else expected_type
        if not any(_type_matches(instance, item) for item in allowed):
            raise SchemaValidationError(f"{path}: expected type {allowed}, got {type(instance).__name__}")

    if "const" in schema and instance != schema["const"]:
        raise SchemaValidationError(f"{path}: expected const {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        raise SchemaValidationError(f"{path}: value {instance!r} not in enum")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            raise SchemaValidationError(f"{path}: string shorter than minLength")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            raise SchemaValidationError(f"{path}: string does not match pattern")

    if isinstance(instance, int) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise SchemaValidationError(f"{path}: value below minimum")
        if "maximum" in schema and instance > schema["maximum"]:
            raise SchemaValidationError(f"{path}: value above maximum")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            raise SchemaValidationError(f"{path}: array shorter than minItems")
        if schema.get("uniqueItems"):
            seen: set[bytes] = set()
            for item in instance:
                marker = canonicalize(item)
                if marker in seen:
                    raise SchemaValidationError(f"{path}: duplicate array item")
                seen.add(marker)
        if "items" in schema:
            for idx, item in enumerate(instance):
                validate_against_schema(item, schema["items"], registry, f"{path}[{idx}]", root_schema)

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                raise SchemaValidationError(f"{path}: missing required property {key}")
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                validate_against_schema(value, properties[key], registry, f"{path}.{key}", root_schema)
            elif schema.get("additionalProperties") is False:
                raise SchemaValidationError(f"{path}: additional property not allowed: {key}")


def validate_document(document: dict[str, Any], schema_dir: Path) -> None:
    registry = SchemaRegistry(schema_dir)
    schema = registry.schema_for_document(document)
    validate_against_schema(document, schema, registry, root_schema=schema)
    validate_identity(document)

    version = document["schema_version"]
    if version == "saddle-intent/0.1":
        origin = document["origin"]
        if origin["status"] == "VERIFIED":
            if not origin.get("principal_ref"):
                raise ProtocolError("verified intent origin requires principal_ref")
            if not origin.get("evidence_refs"):
                raise ProtocolError("verified intent origin requires evidence_refs")
    if version == "saddle-effect-receipt/0.1":
        auth = document["authorization_ref"]
        if auth["status"] != "ACTIVE":
            raise ProtocolError("effect receipt requires ACTIVE authorization reference")
        if auth["authority_kind"] != "EFFECT_PERMISSION":
            raise ProtocolError("effect receipt authorization must be EFFECT_PERMISSION")
        if auth["binds_to"]["object_type"] != "EFFECT":
            raise ProtocolError("effect receipt authorization must bind to EFFECT")


def validate_bundle(intent: dict[str, Any], proposal: dict[str, Any], receipt: dict[str, Any], delta: dict[str, Any], schema_dir: Path) -> None:
    for doc in (intent, proposal, receipt, delta):
        validate_document(doc, schema_dir)

    if proposal["intent_id"] != intent["intent_id"]:
        raise ProtocolError("EffectProposal.intent_id does not match IntentEnvelope.intent_id")
    if receipt["effect_id"] != proposal["effect_id"]:
        raise ProtocolError("EffectReceipt.effect_id does not match EffectProposal.effect_id")
    binding = receipt["authorization_ref"]["binds_to"]
    if binding["object_id"] != proposal["effect_id"]:
        raise ProtocolError("effect authorization does not bind to exact EffectProposal.effect_id")
    if binding["content_hash"] != proposal["content_hash"]:
        raise ProtocolError("effect authorization does not bind to exact EffectProposal.content_hash")
    if delta["intent_id"] != intent["intent_id"]:
        raise ProtocolError("StateDelta.intent_id does not match IntentEnvelope.intent_id")
    if delta["effect_id"] != proposal["effect_id"]:
        raise ProtocolError("StateDelta.effect_id does not match EffectProposal.effect_id")

    status_change = delta["project_status_change"]
    if status_change is not None:
        decision_ids = {item["decision_id"] for item in delta["decisions_added"]}
        if status_change["decision_ref"] not in decision_ids:
            raise ProtocolError("project status change must reference a human decision added in the same StateDelta")
