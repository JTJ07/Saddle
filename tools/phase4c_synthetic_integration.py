"""Phase 4C deterministic Saddle -> Executor -> Evidence integration proof.

This module deliberately uses synthetic intelligence: a deterministic proposal for
immutable CASE-001. It proves system composition, not model quality. The proposal
has no authority and execution occurs only after the existing Phase-5 exact
effect-authority gate allows it.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.model_gateway import validate_worker_proposal
from tools.phase5_boundaries import authorize_effect, raw_intent_hash, with_boundary_identity
from tools.protocol_v01 import sha256_ref, validate_bundle, with_derived_identity

EXECUTOR_REPOSITORY = "JTJ07/Executor"
EXECUTOR_COMMIT = "788443c3ed5b290ac8f1de145a93d02d2dd15317"
FIXTURE_REPOSITORY = "JTJ07/executor-pilot-target"
FIXTURE_COMMIT = "3934a94a5eebf750079200589d6dc40e024d44a0"
CASE_ID = "CASE-001"
TARGET_PATH = "project_registry/registry.py"
NOW = datetime(2026, 8, 10, 20, 30, 0, tzinfo=timezone.utc)

OLD_BLOCK = '''    def add_many(self, projects: Iterable[Project]) -> None:\n        """Add projects one by one, leaving earlier writes after a late duplicate."""\n\n        for project in projects:\n            if project.project_id in self._projects:\n                raise DuplicateProjectError(\n                    f"duplicate project_id: {project.project_id}"\n                )\n            self._projects[project.project_id] = project\n'''

NEW_BLOCK = '''    def add_many(self, projects: Iterable[Project]) -> None:\n        """Add a batch atomically after validating all project identifiers."""\n\n        batch = list(projects)\n        seen = set(self._projects)\n        for project in batch:\n            if project.project_id in seen:\n                raise DuplicateProjectError(\n                    f"duplicate project_id: {project.project_id}"\n                )\n            seen.add(project.project_id)\n        for project in batch:\n            self._projects[project.project_id] = project\n'''


class Phase4CError(RuntimeError):
    pass


def _ref(ref_id: str, kind: str = "EVIDENCE", content_hash: str | None = None) -> dict[str, Any]:
    value: dict[str, Any] = {"ref_id": ref_id, "kind": kind}
    if content_hash is not None:
        value["content_hash"] = content_hash
    return value


def _synthetic_hash(seed: str) -> str:
    return "sha256:" + hashlib.sha256(seed.encode("utf-8")).hexdigest()


def _git_head(root: Path) -> str:
    import subprocess

    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=False,
        timeout=30,
    )
    if result.returncode != 0:
        raise Phase4CError(f"cannot resolve git HEAD for {root}: {result.stderr.strip()}")
    return result.stdout.strip()


def build_intent() -> dict[str, Any]:
    return with_derived_identity({
        "schema_version": "saddle-intent/0.1",
        "raw_human_intent": "Napraw CASE-001 tylko w project_registry/registry.py; nie zmieniaj testów ani innych plików.",
        "origin": {
            "status": "VERIFIED",
            "principal_ref": "synthetic-principal:phase4c-project-owner",
            "evidence_refs": [_ref("synthetic-origin:phase4c-case001")],
        },
        "desired_outcome": "CASE-001 i pełny zestaw testów przechodzą bez wyjścia poza jeden dozwolony plik.",
        "success_evidence": [{"description": "target test, full tests and scope verification pass"}],
        "human_owned_constraints": [
            f"Only {TARGET_PATH} may change.",
            "Tests and protected material must not change.",
            "No network or secrets.",
        ],
        "context_refs": [
            _ref(f"repo:{FIXTURE_REPOSITORY}@{FIXTURE_COMMIT}", "REPOSITORY"),
            _ref("decision:DEC-SAD-014"),
        ],
        "budget": {"max_duration_ms": 900000},
        "created_at": "2026-08-10T20:20:00Z",
    })


def build_binding(intent: dict[str, Any]) -> dict[str, Any]:
    return with_boundary_identity({
        "schema_version": "saddle-verified-intent-binding/0.1",
        "intent_id": intent["intent_id"],
        "intent_content_hash": intent["content_hash"],
        "raw_intent_hash": raw_intent_hash(intent["raw_human_intent"]),
        "principal_ref": "synthetic-principal:phase4c-project-owner",
        "origin_event": {
            "ref_id": "synthetic-origin-event:phase4c-case001",
            "content_hash": _synthetic_hash("phase4c-case001-origin-event"),
            "observed_at": "2026-08-10T20:20:00Z",
        },
        "status": "ACTIVE",
        "issued_at": "2026-08-10T20:21:00Z",
        "expires_at": "2026-08-10T22:21:00Z",
    })


def controlled_worker_proposal(before_text: str) -> dict[str, Any]:
    if before_text.count(OLD_BLOCK) != 1:
        raise Phase4CError("CASE-001 deterministic proposal no longer matches pinned source")
    replacement = before_text.replace(OLD_BLOCK, NEW_BLOCK, 1)
    return {
        "case_id": CASE_ID,
        "target_path": TARGET_PATH,
        "replacement_text": replacement,
        "reason": "Validate the complete add_many batch before the first registry mutation.",
        "evidence_plan": [
            "reproduce the target failure before mutation",
            "run the target test after mutation",
            "run full unit tests and compile checks",
            "verify exactly one allowlisted file changed",
        ],
    }


def normalize_effect_proposal(intent: dict[str, Any], worker: dict[str, Any], before_text: str) -> tuple[dict[str, Any], dict[str, Any]]:
    mutation = validate_worker_proposal(
        worker,
        case_id=CASE_ID,
        target_path=TARGET_PATH,
        before_text=before_text,
        max_patch_lines=80,
    )
    proposal = with_derived_identity({
        "schema_version": "saddle-effect-proposal/0.1",
        "intent_id": intent["intent_id"],
        "action": "WRITE_REPOSITORY_FILE",
        "target": {"kind": "FILE", "ref": TARGET_PATH},
        "expected_effect": "CASE-001 fixed by atomic batch validation in the one allowlisted source file.",
        "required_capabilities": ["READ_REPOSITORY", "WRITE_REPOSITORY"],
        "risk": {"level": "LOW", "notes": ["Synthetic integration fixture; one allowlisted file."]},
        "reason": worker["reason"],
        "evidence_plan": [{"description": item} for item in worker["evidence_plan"]],
        "created_at": "2026-08-10T20:22:00Z",
    })
    return proposal, mutation


def proposal_scope_reasons(proposal: dict[str, Any]) -> list[str]:
    """Compare only explicit machine-readable scope; never infer human meaning."""
    reasons: list[str] = []
    if proposal.get("action") != "WRITE_REPOSITORY_FILE":
        reasons.append("PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE")
    target = proposal.get("target") if isinstance(proposal.get("target"), dict) else {}
    if target != {"kind": "FILE", "ref": TARGET_PATH}:
        reasons.append("PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE")
    return sorted(set(reasons))


def build_authority(binding: dict[str, Any], proposal: dict[str, Any]) -> dict[str, Any]:
    return with_boundary_identity({
        "schema_version": "saddle-effect-authority/0.1",
        "decision": "ALLOW",
        "intent_binding_id": binding["binding_id"],
        "intent_binding_hash": binding["content_hash"],
        "effect_id": proposal["effect_id"],
        "effect_content_hash": proposal["content_hash"],
        "authorized_action": proposal["action"],
        "authorized_target": {"kind": proposal["target"]["kind"], "ref": proposal["target"]["ref"]},
        "evidence_requirements": [
            "Executor input identity matches pinned CASE-001 commit",
            "pre-change target test fails",
            "post-change target and regression tests pass",
            "exactly the allowlisted file changes",
            "result remains human-review-required",
        ],
        "issuer_kind": "POLICY",
        "issuer_ref": "policy:phase4c-synthetic-fixture",
        "source_refs": ["decision:DEC-SAD-014", "fixture:CASE-001"],
        "status": "ACTIVE",
        "max_uses": 1,
        "issued_at": "2026-08-10T20:23:00Z",
        "expires_at": "2026-08-10T22:23:00Z",
        "reason": "Synthetic integration policy permits only the exact CASE-001 one-file effect for this proof.",
    })


def authorize_declared_effect(
    intent: dict[str, Any],
    binding: dict[str, Any],
    proposal: dict[str, Any],
    authority: dict[str, Any] | None,
    *,
    consumed: set[str] | None = None,
) -> dict[str, Any]:
    scope_reasons = proposal_scope_reasons(proposal)
    if scope_reasons:
        return {"status": "BLOCK", "reasons": scope_reasons}
    return authorize_effect(
        intent,
        binding,
        proposal,
        authority,
        now=NOW,
        consumed_authority_ids=consumed,
    )


def build_receipt_and_delta(
    intent: dict[str, Any],
    proposal: dict[str, Any],
    authority: dict[str, Any],
    executor_report: dict[str, Any],
    *,
    duration_ms: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    report_hash = sha256_ref(executor_report)
    report_ref = _ref("executor-report:phase4c-case001", "EVIDENCE", report_hash)
    receipt = with_derived_identity({
        "schema_version": "saddle-effect-receipt/0.1",
        "effect_id": proposal["effect_id"],
        "authorization_ref": {
            "authority_id": authority["authority_id"],
            "authority_kind": "EFFECT_PERMISSION",
            "status": "ACTIVE",
            "binds_to": {
                "object_type": "EFFECT",
                "object_id": proposal["effect_id"],
                "content_hash": proposal["content_hash"],
            },
            "source_refs": [_ref("authority:phase4c-synthetic-fixture")],
            "issued_at": authority["issued_at"],
        },
        "status": "SUCCEEDED",
        "actual_effect": {
            "summary": "Executor changed exactly project_registry/registry.py and returned review-required evidence.",
            "result_refs": [report_ref],
        },
        "changed_objects": [_ref(TARGET_PATH, "FILE")],
        "evidence_refs": [report_ref],
        "tests": [{"name": "executor-gp001-verification", "status": "PASS", "evidence_refs": [report_ref]}],
        "duration_ms": max(0, int(duration_ms)),
        "observed_at": "2026-08-10T20:25:00Z",
    })
    delta = with_derived_identity({
        "schema_version": "saddle-state-delta/0.1",
        "intent_id": intent["intent_id"],
        "effect_id": proposal["effect_id"],
        "facts_added": [{
            "fact_id": "fact:phase4c-case001-executor-evidence",
            "statement": "Synthetic CASE-001 proposal crossed the exact authority gate and Executor returned bounded review-required evidence.",
            "source_refs": [report_ref],
            "observed_at": "2026-08-10T20:25:00Z",
        }],
        "decisions_added": [],
        "hypotheses_added": [],
        "superseded": [],
        "project_status_change": None,
        "blockers": [],
        "next_step": "Human/system evaluation of Phase-4C evidence; do not infer model quality from synthetic intelligence.",
        "source_refs": [report_ref],
        "created_at": "2026-08-10T20:26:00Z",
    })
    return receipt, delta


def _require_executor_success(report: dict[str, Any]) -> None:
    if report.get("status") != "ACTION_COMPLETED_REVIEW_REQUIRED":
        raise Phase4CError(f"Executor did not complete bounded effect: {report.get('status')} {report.get('error')}")
    if report.get("changed_paths") != [TARGET_PATH]:
        raise Phase4CError(f"Executor scope mismatch: {report.get('changed_paths')}")
    if report.get("human_decision_required") is not True:
        raise Phase4CError("Executor lost human review requirement")
    expected = {
        "fixture_authority": "BOUND",
        "input_identity": "MATCH",
        "pre_change_target_test": "FAIL",
        "post_change_target_test": "PASS",
        "regression_checks": "PASS",
        "diff_scope": "ALLOWED",
        "protected_material": "UNCHANGED",
        "execution_limits": "RESPECTED",
        "result_artifact": "PRESENT",
    }
    if report.get("evidence") != expected:
        raise Phase4CError(f"Executor evidence mismatch: {report.get('evidence')}")


def run_integration(*, root: Path, executor_root: Path, workspace: Path, runs_root: Path, image: str) -> dict[str, Any]:
    if _git_head(executor_root) != EXECUTOR_COMMIT:
        raise Phase4CError("Executor checkout is not the pinned Phase-4C commit")
    if _git_head(workspace) != FIXTURE_COMMIT:
        raise Phase4CError("CASE-001 checkout is not the pinned fixture commit")

    before_text = (workspace / TARGET_PATH).read_text(encoding="utf-8")
    intent = build_intent()
    binding = build_binding(intent)
    worker = controlled_worker_proposal(before_text)
    proposal, mutation = normalize_effect_proposal(intent, worker, before_text)
    authority = build_authority(binding, proposal)
    consumed: set[str] = set()

    happy_auth = authorize_declared_effect(intent, binding, proposal, authority, consumed=consumed)
    if happy_auth.get("status") != "ALLOW":
        raise Phase4CError(f"happy-path authority unexpectedly blocked: {happy_auth}")

    # Import the existing Executor runtime only after binding to the exact checkout.
    sys.path.insert(0, str(executor_root))
    from executor.gp001_runtime import AuthorizedFileMutation, GP001Runtime  # type: ignore

    executor_mutation = AuthorizedFileMutation(
        path=mutation["path"],
        expected_before_sha256=mutation["expected_before_sha256"],
        replacement_text=mutation["replacement_text"],
        expected_after_sha256=mutation["expected_after_sha256"],
    )
    runtime = GP001Runtime(
        executor_root=executor_root,
        executor_commit=EXECUTOR_COMMIT,
        runs_root=runs_root,
        image=image,
    )
    started = time.monotonic()
    executor_report = runtime.execute(
        workspace=workspace,
        mutation=executor_mutation,
        run_id="phase4c-synthetic-happy",
        now=NOW,
    )
    duration_ms = round((time.monotonic() - started) * 1000)
    _require_executor_success(executor_report)

    receipt, delta = build_receipt_and_delta(
        intent, proposal, authority, executor_report, duration_ms=duration_ms
    )
    validate_bundle(intent, proposal, receipt, delta, root / "protocol" / "v0.1")

    # Negative 1: explicit scope drift is blocked without semantic mind-reading.
    drift = with_derived_identity({
        "schema_version": "saddle-effect-proposal/0.1",
        "intent_id": intent["intent_id"],
        "action": "REBUILD_MODULE",
        "target": {"kind": "DIRECTORY", "ref": "project_registry"},
        "expected_effect": "Rebuild the entire module.",
        "required_capabilities": ["WRITE_REPOSITORY"],
        "risk": {"level": "HIGH", "notes": ["Exceeds the declared one-file synthetic fixture scope."]},
        "reason": "Synthetic drift attack.",
        "evidence_plan": [{"description": "not applicable; must block before execution"}],
        "created_at": "2026-08-10T20:22:00Z",
    })
    drift_result = authorize_declared_effect(intent, binding, drift, None, consumed=set())
    if drift_result != {"status": "BLOCK", "reasons": ["PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE"]}:
        raise Phase4CError(f"scope-drift attack did not fail closed: {drift_result}")

    # Negative 2: authority for another exact proposal cannot authorize this proposal.
    other = with_derived_identity({
        **{k: v for k, v in proposal.items() if k not in {"effect_id", "content_hash"}},
        "expected_effect": "Different exact effect identity for mismatch attack.",
    })
    mismatched_authority = build_authority(binding, other)
    mismatch_result = authorize_declared_effect(intent, binding, proposal, mismatched_authority, consumed=set())
    if mismatch_result.get("status") != "BLOCK" or not any(
        reason in mismatch_result.get("reasons", [])
        for reason in ("AUTHORITY_EFFECT_ID_MISMATCH", "AUTHORITY_EFFECT_HASH_MISMATCH")
    ):
        raise Phase4CError(f"authority-mismatch attack did not fail closed: {mismatch_result}")

    # Negative 3: the exact authority used for the happy path is single-use.
    replay_result = authorize_declared_effect(intent, binding, proposal, authority, consumed=consumed)
    if replay_result.get("status") != "BLOCK" or "EFFECT_AUTHORITY_REPLAYED" not in replay_result.get("reasons", []):
        raise Phase4CError(f"authority replay did not fail closed: {replay_result}")

    return {
        "schema_version": "saddle-phase4c-synthetic-integration-evidence/0.1",
        "evidence_class": "SYNTHETIC_INTEGRATION_EVIDENCE",
        "worker_evidence": False,
        "model_performance_claim": False,
        "maturity_claim": "NONE",
        "functional_saddle_accepted": False,
        "executor_repository": EXECUTOR_REPOSITORY,
        "executor_commit": EXECUTOR_COMMIT,
        "fixture_repository": FIXTURE_REPOSITORY,
        "fixture_commit": FIXTURE_COMMIT,
        "synthetic_generator": "DETERMINISTIC_CASE001_PROPOSAL",
        "executor_calls": 1,
        "cases": {
            "happy_path": {"status": "PASS", "authority": happy_auth, "executor_status": executor_report["status"], "receipt_id": receipt["receipt_id"], "state_delta_id": delta["state_delta_id"]},
            "intent_scope_drift": drift_result,
            "authority_mismatch": mismatch_result,
            "authority_replay": replay_result,
        },
        "protocol_bundle": "PASS",
        "scriptops_note": "ScriptOps Phase-6 remains separate proven workflow evidence; it is not forced into the GP001 code-effect path because its accepted v2 substrate is scene-domain specific.",
        "next_gate": "PHASE_4B_API_WORKER_BENCHMARK_AFTER_HUMAN_SYSTEM_EVALUATION",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--executor-root", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--runs-root", type=Path, required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        evidence = run_integration(
            root=args.root.resolve(),
            executor_root=args.executor_root.resolve(),
            workspace=args.workspace.resolve(),
            runs_root=args.runs_root.resolve(),
            image=args.image,
        )
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error_type": type(exc).__name__, "error": str(exc)}, sort_keys=True))
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "evidence": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
