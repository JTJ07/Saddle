"""Recover Phase-7 acceptance from the already-consumed real Gemini call.

No model/provider code is imported or called here. The immutable model result from
GitHub Actions run 31564368431 is represented by its persisted hashes, exact patch,
usage and provider response id. Recovery fixes only the invalid Protocol v0.1
sourceRef kind, derives a new exact effect authority, re-executes the same mutation
on a fresh controlled CASE-001 checkout, validates the protocol bundle, and stops
at the required human-review boundary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from tools.phase5_boundaries import authorize_effect, raw_intent_hash, with_boundary_identity
from tools.protocol_v01 import sha256_ref, validate_bundle, with_derived_identity
from tools.phase7_functional_acceptance import (
    EXECUTOR_COMMIT,
    EXECUTOR_REPOSITORY,
    FIXTURE_COMMIT,
    FIXTURE_REPOSITORY,
    RAW_HUMAN_INTENT,
    TARGET_PATH,
    require_executor_report,
)

ATTEMPT_PATH = Path("evidence/phase7/attempt-001.json")
PATCH_PATH = Path("evidence/phase7/attempt-001-model.patch")
CONFIG_PATH = Path("config/phase7-acceptance-run-v0.1.json")
PATCH_SHA256 = "f801d2d3201b2b3fecc036b9ad423bf2434227e92b18c7c90388387a20051838"
OLD_BLOCK = '''    def add_many(self, projects: Iterable[Project]) -> None:\n        """Add projects one by one, leaving earlier writes after a late duplicate."""\n\n        for project in projects:\n            if project.project_id in self._projects:\n                raise DuplicateProjectError(\n                    f"duplicate project_id: {project.project_id}"\n                )\n            self._projects[project.project_id] = project\n'''
NEW_BLOCK = '''    def add_many(self, projects: Iterable[Project]) -> None:\n        """Add projects atomically after validating the entire batch."""\n\n        items = list(projects)\n        seen = set(self._projects)\n        to_add: dict[str, Project] = {}\n        for project in items:\n            if project.project_id in seen:\n                raise DuplicateProjectError(\n                    f"duplicate project_id: {project.project_id}"\n                )\n            seen.add(project.project_id)\n            to_add[project.project_id] = project\n\n        self._projects.update(to_add)\n'''


class RecoveryError(RuntimeError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RecoveryError(f"{path}: expected object")
    return value


def _write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _ts(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ref(ref_id: str, kind: str = "EVIDENCE", content_hash: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"ref_id": ref_id, "kind": kind}
    if content_hash:
        result["content_hash"] = content_hash
    return result


def _head(root: Path) -> str:
    import subprocess
    p = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, capture_output=True, timeout=30)
    if p.returncode:
        raise RecoveryError(p.stderr.strip() or "cannot resolve git HEAD")
    return p.stdout.strip()


def validate_recovery_inputs(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str, str]:
    config = _load(root / CONFIG_PATH)
    attempt = _load(root / ATTEMPT_PATH)
    if config.get("status") != "MODEL_CALL_CONSUMED_RECOVERY_ONLY":
        raise RecoveryError("model call gate is not consumed/recovery-only")
    if config.get("raw_human_intent") != RAW_HUMAN_INTENT:
        raise RecoveryError("raw human intent drift")
    if attempt.get("github_run_id") != 31564368431 or attempt.get("status") != "EFFECT_SUCCEEDED_FINAL_PROTOCOL_VALIDATION_FAILED":
        raise RecoveryError("unexpected Phase-7 attempt evidence")
    if attempt["recovery_rule"] != {
        "additional_model_calls_allowed": 0,
        "reuse_exact_worker_mutation": True,
        "correct_origin_reference_kind_to": "EVIDENCE",
        "new_exact_effect_authority_required_before_reexecution": True,
    }:
        raise RecoveryError("recovery rule drift")
    patch_bytes = (root / PATCH_PATH).read_bytes()
    if hashlib.sha256(patch_bytes).hexdigest() != PATCH_SHA256:
        raise RecoveryError("frozen model patch hash mismatch")
    worker = attempt["worker"]
    if worker["model_id"] != "gemini-3.6-flash" or worker["automatic_retries"] != 0:
        raise RecoveryError("persisted worker identity/retry evidence mismatch")
    origin = {
        "actor": attempt["actor"],
        "event_name": attempt["event"],
        "head_sha": attempt["saddle_sha"],
        "observed_at": attempt["origin_event"]["observed_at"],
        "principal_ref": attempt["origin_event"]["principal_ref"],
        "provider": attempt["origin_event"]["provider"],
        "raw_intent_hash": attempt["origin_event"]["raw_intent_hash"],
        "ref": attempt["ref"],
        "repository": "JTJ07/Saddle",
        "run_attempt": attempt["github_run_attempt"],
        "run_id": attempt["github_run_id"],
        "schema_version": "saddle-phase7-origin-event/0.1",
    }
    origin_hash = sha256_ref(origin)
    if origin_hash != attempt["origin_event"]["content_hash"]:
        raise RecoveryError("persisted origin event hash mismatch")
    origin_ref = f"github-actions:JTJ07/Saddle:push:{attempt['github_run_id']}:{attempt['github_run_attempt']}:{attempt['saddle_sha']}"
    return config, attempt, origin, origin_ref, origin_hash


def build_corrected_intent(config: dict[str, Any], origin: dict[str, Any], origin_ref: str, origin_hash: str, now: datetime) -> tuple[dict[str, Any], dict[str, Any]]:
    intent = with_derived_identity({
        "schema_version": "saddle-intent/0.1",
        "raw_human_intent": config["raw_human_intent"],
        "origin": {
            "status": "VERIFIED",
            "principal_ref": origin["principal_ref"],
            "evidence_refs": [_ref(origin_ref, "EVIDENCE", origin_hash)],
        },
        "desired_outcome": "Execute the canonical Phase-7 bounded real-AI-to-Executor acceptance path without expanding authority.",
        "success_evidence": [{"description": "reuse the single immutable real-model proposal, exact authority, bounded Executor effect, valid protocol evidence and preserved human-review boundary"}],
        "human_owned_constraints": [
            f"Only {TARGET_PATH} may change in the controlled acceptance fixture.",
            "No additional model call is permitted during recovery.",
            "The model output remains proposal-only and receives no effect authority.",
            "Executor network and secrets remain disabled.",
            "Human review and second zero-history resume remain required before functional acceptance.",
        ],
        "context_refs": [
            _ref(f"repo:{EXECUTOR_REPOSITORY}@{EXECUTOR_COMMIT}", "REPOSITORY"),
            _ref(f"repo:{FIXTURE_REPOSITORY}@{FIXTURE_COMMIT}", "REPOSITORY"),
            _ref("evidence:phase7-attempt-001"),
        ],
        "budget": {"max_duration_ms": 900000},
        "created_at": _ts(now),
    })
    binding = with_boundary_identity({
        "schema_version": "saddle-verified-intent-binding/0.1",
        "intent_id": intent["intent_id"],
        "intent_content_hash": intent["content_hash"],
        "raw_intent_hash": raw_intent_hash(intent["raw_human_intent"]),
        "principal_ref": origin["principal_ref"],
        "origin_event": {"ref_id": origin_ref, "content_hash": origin_hash, "observed_at": origin["observed_at"]},
        "status": "ACTIVE",
        "issued_at": _ts(now),
        "expires_at": _ts(now + timedelta(hours=2)),
    })
    return intent, binding


def reconstruct_exact_mutation(workspace: Path, attempt: dict[str, Any]) -> dict[str, str]:
    target = workspace / TARGET_PATH
    before = target.read_text(encoding="utf-8")
    mutation = attempt["worker"]["mutation"]
    if hashlib.sha256(before.encode("utf-8")).hexdigest() != mutation["expected_before_sha256"]:
        raise RecoveryError("fresh fixture before hash does not match consumed worker evidence")
    if before.count(OLD_BLOCK) != 1:
        raise RecoveryError("cannot reconstruct exact consumed worker patch")
    replacement = before.replace(OLD_BLOCK, NEW_BLOCK, 1)
    if hashlib.sha256(replacement.encode("utf-8")).hexdigest() != mutation["expected_after_sha256"]:
        raise RecoveryError("reconstructed model output does not match consumed after hash")
    return {
        "path": TARGET_PATH,
        "expected_before_sha256": mutation["expected_before_sha256"],
        "replacement_text": replacement,
        "expected_after_sha256": mutation["expected_after_sha256"],
    }


def build_effect(intent: dict[str, Any], binding: dict[str, Any], attempt: dict[str, Any], now: datetime) -> tuple[dict[str, Any], dict[str, Any]]:
    proposal = with_derived_identity({
        "schema_version": "saddle-effect-proposal/0.1",
        "intent_id": intent["intent_id"],
        "action": "WRITE_REPOSITORY_FILE",
        "target": {"kind": "FILE", "ref": TARGET_PATH},
        "expected_effect": "CASE-001 is fixed by the exact already-consumed Gemini 3.6 Flash mutation.",
        "required_capabilities": ["READ_REPOSITORY", "WRITE_REPOSITORY"],
        "risk": {"level": "LOW", "notes": ["Recovery reuses one immutable worker mutation; no model call; human review required."]},
        "reason": attempt["worker"]["reason"],
        "evidence_plan": [
            {"description": "run pinned pre-change target test and require FAIL"},
            {"description": "run pinned post-change target and full regression tests and require PASS"},
            {"description": "verify exactly one allowlisted file changed"},
        ],
        "created_at": _ts(now),
    })
    authority = with_boundary_identity({
        "schema_version": "saddle-effect-authority/0.1",
        "decision": "ALLOW",
        "intent_binding_id": binding["binding_id"],
        "intent_binding_hash": binding["content_hash"],
        "effect_id": proposal["effect_id"],
        "effect_content_hash": proposal["content_hash"],
        "authorized_action": proposal["action"],
        "authorized_target": proposal["target"],
        "evidence_requirements": ["recovered origin uses Protocol-v0.1 EVIDENCE kind", "no additional model call", "exact consumed after-hash matches", "current Executor identity matches", "pre-change FAIL", "post-change target and regression PASS", "one-file diff", "human review required"],
        "issuer_kind": "POLICY",
        "issuer_ref": "policy:phase7-consumed-worker-recovery-only",
        "source_refs": ["evidence:phase7-attempt-001", "artifact:9128908360"],
        "status": "ACTIVE",
        "max_uses": 1,
        "issued_at": _ts(now),
        "expires_at": _ts(now + timedelta(hours=2)),
        "reason": "Recover the already-consumed Phase-7 model proposal after a post-effect schema-kind bug; no new model authority or call is permitted.",
    })
    return proposal, authority


def build_receipt_delta(intent: dict[str, Any], proposal: dict[str, Any], authority: dict[str, Any], attempt: dict[str, Any], report: dict[str, Any], now: datetime, duration_ms: int) -> tuple[dict[str, Any], dict[str, Any]]:
    worker_ref = _ref("worker-proposal:phase7-run-31564368431", "EVIDENCE", attempt["worker"]["proposal_content_hash"])
    report_ref = _ref("executor-report:phase7-recovery", "EVIDENCE", sha256_ref(report))
    artifact_ref = _ref("github-actions-artifact:9128908360", "EVIDENCE", attempt["artifact"]["digest"])
    receipt = with_derived_identity({
        "schema_version": "saddle-effect-receipt/0.1",
        "effect_id": proposal["effect_id"],
        "authorization_ref": {
            "authority_id": authority["authority_id"],
            "authority_kind": "EFFECT_PERMISSION",
            "status": "ACTIVE",
            "binds_to": {"object_type": "EFFECT", "object_id": proposal["effect_id"], "content_hash": proposal["content_hash"]},
            "source_refs": [_ref("authority:phase7-recovery")],
            "issued_at": authority["issued_at"],
        },
        "status": "SUCCEEDED",
        "actual_effect": {"summary": "Reused the single immutable Gemini 3.6 Flash mutation and current Executor returned bounded review-required evidence.", "result_refs": [worker_ref, report_ref, artifact_ref]},
        "changed_objects": [_ref(TARGET_PATH, "FILE")],
        "evidence_refs": [worker_ref, report_ref, artifact_ref],
        "tests": [{"name": "executor-gp001-recovery-verification", "status": "PASS", "evidence_refs": [report_ref]}],
        "duration_ms": max(0, int(duration_ms)),
        "observed_at": _ts(now),
    })
    delta = with_derived_identity({
        "schema_version": "saddle-state-delta/0.1",
        "intent_id": intent["intent_id"],
        "effect_id": proposal["effect_id"],
        "facts_added": [{"fact_id": "fact:phase7-recovered-real-worker-e2e", "statement": "The one consumed real Gemini 3.6 Flash proposal was recovered without another model call, crossed a new exact authority gate, and current Executor returned bounded review-required evidence with a valid Protocol v0.1 bundle.", "source_refs": [worker_ref, report_ref, artifact_ref], "observed_at": _ts(now)}],
        "decisions_added": [], "hypotheses_added": [], "superseded": [], "project_status_change": None,
        "blockers": ["Required human review of recovered Phase-7 evidence is open.", "Second zero-history resume remains required before final functional acceptance."],
        "next_step": "Human review of recovered Phase-7 evidence; if accepted, persist the human decision and perform the required second zero-history repository-only resume.",
        "source_refs": [worker_ref, report_ref, artifact_ref],
        "created_at": _ts(now),
    })
    return receipt, delta


def run(root: Path, executor_root: Path, workspace: Path, runs_root: Path, image: str, output: Path) -> dict[str, Any]:
    config, attempt, origin, origin_ref, origin_hash = validate_recovery_inputs(root)
    if _head(executor_root) != EXECUTOR_COMMIT or _head(workspace) != FIXTURE_COMMIT:
        raise RecoveryError("Executor or fixture identity mismatch")
    now = datetime.now(timezone.utc).replace(microsecond=0)
    intent, binding = build_corrected_intent(config, origin, origin_ref, origin_hash, now)
    mutation = reconstruct_exact_mutation(workspace, attempt)
    proposal, authority = build_effect(intent, binding, attempt, now)
    consumed: set[str] = set()
    auth = authorize_effect(intent, binding, proposal, authority, now=now, consumed_authority_ids=consumed)
    if auth.get("status") != "ALLOW":
        raise RecoveryError(f"recovery exact authority blocked: {auth}")
    sys.path.insert(0, str(executor_root))
    from executor.gp001_runtime import AuthorizedFileMutation, GP001Runtime  # type: ignore
    m = AuthorizedFileMutation(**mutation)
    runtime = GP001Runtime(executor_root=executor_root, executor_commit=EXECUTOR_COMMIT, runs_root=runs_root, image=image)
    started = time.monotonic()
    report = runtime.execute(workspace=workspace, mutation=m, run_id="phase7-recovery-consumed-worker", now=now)
    duration_ms = round((time.monotonic() - started) * 1000)
    require_executor_report(report)
    end = datetime.now(timezone.utc).replace(microsecond=0)
    receipt, delta = build_receipt_delta(intent, proposal, authority, attempt, report, end, duration_ms)
    validate_bundle(intent, proposal, receipt, delta, root / "protocol" / "v0.1")
    output.mkdir(parents=True, exist_ok=True)
    for name, value in (("origin_event.json", origin), ("intent.json", intent), ("verified_intent_binding.json", binding), ("effect_proposal.json", proposal), ("effect_authority.json", authority), ("authority_result.json", auth), ("executor_report.json", report), ("effect_receipt.json", receipt), ("state_delta.json", delta)):
        _write(output / name, value)
    summary = {
        "schema_version": "saddle-phase7-recovery-summary/0.1",
        "status": "E2E_EFFECT_COMPLETE_REVIEW_REQUIRED",
        "recovery_of_run_id": 31564368431,
        "original_model_calls": 1,
        "recovery_model_calls": 0,
        "total_phase7_model_calls": 1,
        "automatic_model_retries": 0,
        "model_id": "gemini-3.6-flash",
        "original_provider_response_id": attempt["worker"]["provider_response_id"],
        "original_estimated_cost_usd": attempt["worker"]["estimated_cost_usd"],
        "original_worker_proposal_hash": attempt["worker"]["proposal_content_hash"],
        "origin_event_hash": origin_hash,
        "effect_id": proposal["effect_id"],
        "authority_id": authority["authority_id"],
        "executor_commit": EXECUTOR_COMMIT,
        "changed_paths": report["changed_paths"],
        "executor_report_hash": sha256_ref(report),
        "receipt_id": receipt["receipt_id"],
        "state_delta_id": delta["state_delta_id"],
        "protocol_bundle": "PASS",
        "human_review_required": True,
        "second_zero_history_resume_required": True,
        "explicit_final_human_acceptance_required": True,
        "functional_saddle_accepted": False,
        "completion_lock_release_authorized": False,
        "next_gate": "HUMAN_REVIEW_THEN_SECOND_ZERO_HISTORY_RESUME",
    }
    _write(output / "summary.json", summary)
    return summary


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(); p.add_argument("--root", type=Path, default=Path(".")); p.add_argument("--executor-root", type=Path, required=True); p.add_argument("--workspace", type=Path, required=True); p.add_argument("--runs-root", type=Path, required=True); p.add_argument("--image", required=True); p.add_argument("--output-dir", type=Path, required=True); a = p.parse_args(argv)
    try:
        result = run(a.root.resolve(), a.executor_root.resolve(), a.workspace.resolve(), a.runs_root.resolve(), a.image, a.output_dir.resolve())
    except (RecoveryError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, sort_keys=True)); return 2
    print(json.dumps(result, sort_keys=True)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
