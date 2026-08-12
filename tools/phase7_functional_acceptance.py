"""Bounded fresh-session Phase-7 Saddle acceptance runner.

This runner performs one real Gemini 3.6 Flash proposal for immutable CASE-001,
binds it to an authenticated acceptance-only GitHub origin event, requires a
separate exact EffectAuthority, executes only through the reconciled current
Executor, validates protocol evidence, and stops at HUMAN REVIEW REQUIRED.
It cannot release the completion lock or declare functional acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

from tools.model_gateway import CredentialUnavailable, GatewayError, GeminiGenerateContentGateway, validate_worker_proposal
from tools.phase4_benchmark import BenchmarkError, load_case
from tools.phase5_boundaries import authorize_effect, raw_intent_hash, with_boundary_identity
from tools.protocol_v01 import sha256_ref, validate_bundle, with_derived_identity

CONFIG_PATH = Path("config/phase7-acceptance-run-v0.1.json")
CASE_ID = "CASE-001"
TARGET_PATH = "project_registry/registry.py"
MODEL_ID = "gemini-3.6-flash"
EXECUTOR_REPOSITORY = "JTJ07/Executor"
EXECUTOR_COMMIT = "728d23e56ec9f76fb7a37673ceb20efccf91e03d"
FIXTURE_REPOSITORY = "litrgratis-pixel/executor-pilot-target"
FIXTURE_COMMIT = "3934a94a5eebf750079200589d6dc40e024d44a0"
RAW_HUMAN_INTENT = "Kontynuuj Saddle od canonical GitHub state i wykonaj Phase 7"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


class Phase7Error(RuntimeError):
    pass


def _json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise Phase7Error(f"{path}: expected object")
    return value


def _write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _ts(now: datetime) -> str:
    return now.astimezone(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def _head(root: Path) -> str:
    p = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, capture_output=True, timeout=30)
    if p.returncode:
        raise Phase7Error(f"cannot resolve git HEAD: {p.stderr.strip()}")
    return p.stdout.strip()


def _diff(root: Path) -> str:
    p = subprocess.run(["git", "-C", str(root), "diff", "--no-ext-diff", "--", TARGET_PATH], text=True, capture_output=True, timeout=30)
    if p.returncode:
        raise Phase7Error(f"cannot capture candidate diff: {p.stderr.strip()}")
    return p.stdout


def _ref(ref_id: str, kind: str = "EVIDENCE", content_hash: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"ref_id": ref_id, "kind": kind}
    if content_hash:
        result["content_hash"] = content_hash
    return result


def validate_config(c: dict[str, Any]) -> None:
    if c.get("schema_version") != "saddle-phase7-acceptance-run/0.1" or c.get("status") != "ARMED_ONCE_FOR_PHASE7_ACCEPTANCE":
        raise Phase7Error("Phase-7 config is not armed")
    if c.get("case_id") != CASE_ID or c.get("raw_human_intent") != RAW_HUMAN_INTENT:
        raise Phase7Error("raw intent or bounded case drift")
    if c.get("origin") != {
        "provider": "github-actions-push-actor/acceptance-only",
        "principal_ref": "github-user:JTJ07",
        "repository": "JTJ07/Saddle",
        "required_ref": "refs/heads/main",
        "required_actor": "JTJ07",
    }:
        raise Phase7Error("acceptance-only origin config drift")
    if c.get("worker") != {
        "provider": "google-gemini", "api": "generateContent", "model_id": MODEL_ID,
        "reasoning_effort": "medium", "max_output_tokens": 8192,
    }:
        raise Phase7Error("selected worker config drift")
    if c.get("executor") != {"repository": EXECUTOR_REPOSITORY, "commit": EXECUTOR_COMMIT}:
        raise Phase7Error("Executor binding drift")
    if c.get("fixture") != {"repository": FIXTURE_REPOSITORY, "commit": FIXTURE_COMMIT, "target_path": TARGET_PATH}:
        raise Phase7Error("controlled fixture binding drift")
    limits = c.get("limits")
    if limits != {"max_model_calls": 1, "automatic_retries": 0, "max_estimated_model_spend_usd": "0.50"}:
        raise Phase7Error("Phase-7 call/retry/spend bounds drift")
    if c.get("review") != {
        "required": True, "second_zero_history_resume_required": True,
        "functional_acceptance_requires_explicit_human_decision": True,
    }:
        raise Phase7Error("human acceptance boundary weakened")


def origin_evidence(c: dict[str, Any], env: dict[str, str], now: datetime) -> tuple[dict[str, Any], str, str]:
    required = ["PHASE7_EVENT_NAME", "PHASE7_REPOSITORY", "PHASE7_ACTOR", "PHASE7_REF", "PHASE7_SHA", "PHASE7_RUN_ID", "PHASE7_RUN_ATTEMPT"]
    if any(not env.get(k) for k in required):
        raise Phase7Error("incomplete GitHub origin environment")
    o = c["origin"]
    if env["PHASE7_EVENT_NAME"] != "push" or env["PHASE7_REPOSITORY"] != o["repository"] or env["PHASE7_ACTOR"] != o["required_actor"] or env["PHASE7_REF"] != o["required_ref"]:
        raise Phase7Error("GitHub origin is not the required authenticated main push")
    if not SHA40.fullmatch(env["PHASE7_SHA"]):
        raise Phase7Error("invalid GitHub event SHA")
    run_id, attempt = int(env["PHASE7_RUN_ID"]), int(env["PHASE7_RUN_ATTEMPT"])
    event = {
        "schema_version": "saddle-phase7-origin-event/0.1",
        "provider": o["provider"], "event_name": "push", "repository": env["PHASE7_REPOSITORY"],
        "actor": env["PHASE7_ACTOR"], "principal_ref": o["principal_ref"], "ref": env["PHASE7_REF"],
        "head_sha": env["PHASE7_SHA"], "run_id": run_id, "run_attempt": attempt,
        "raw_intent_hash": raw_intent_hash(c["raw_human_intent"]), "observed_at": _ts(now),
    }
    h = sha256_ref(event)
    ref_id = f"github-actions:{env['PHASE7_REPOSITORY']}:push:{run_id}:{attempt}:{env['PHASE7_SHA']}"
    return event, ref_id, h


def intent_and_binding(c: dict[str, Any], origin_ref: str, origin_hash: str, now: datetime) -> tuple[dict[str, Any], dict[str, Any]]:
    intent = with_derived_identity({
        "schema_version": "saddle-intent/0.1", "raw_human_intent": c["raw_human_intent"],
        "origin": {"status": "VERIFIED", "principal_ref": c["origin"]["principal_ref"], "evidence_refs": [_ref(origin_ref, "ORIGIN", origin_hash)]},
        "desired_outcome": "Execute the canonical Phase-7 bounded real-AI-to-Executor acceptance path without expanding authority.",
        "success_evidence": [{"description": "one real selected-model proposal, exact authority, bounded Executor effect, verifier evidence and preserved human-review boundary"}],
        "human_owned_constraints": [
            f"Only {TARGET_PATH} may change in the controlled acceptance fixture.",
            "The model is proposal-only and receives no effect authority.", "Exactly one model call and zero automatic retries.",
            "Executor network and secrets remain disabled.", "Human review and second zero-history resume remain required before functional acceptance.",
        ],
        "context_refs": [_ref(f"repo:{EXECUTOR_REPOSITORY}@{EXECUTOR_COMMIT}", "REPOSITORY"), _ref(f"repo:{FIXTURE_REPOSITORY}@{FIXTURE_COMMIT}", "REPOSITORY"), _ref("decision:DEC-SAD-016")],
        "budget": {"max_duration_ms": 900000}, "created_at": _ts(now),
    })
    binding = with_boundary_identity({
        "schema_version": "saddle-verified-intent-binding/0.1", "intent_id": intent["intent_id"],
        "intent_content_hash": intent["content_hash"], "raw_intent_hash": raw_intent_hash(intent["raw_human_intent"]),
        "principal_ref": c["origin"]["principal_ref"],
        "origin_event": {"ref_id": origin_ref, "content_hash": origin_hash, "observed_at": _ts(now)},
        "status": "ACTIVE", "issued_at": _ts(now), "expires_at": _ts(now + timedelta(hours=2)),
    })
    return intent, binding


def real_worker(root: Path, workspace: Path, c: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], str]:
    if not os.environ.get("GEMINI_API_KEY"):
        raise CredentialUnavailable("GEMINI_API_KEY is absent")
    case = load_case(root, workspace, CASE_ID)
    if case["commit"] != FIXTURE_COMMIT or case["target_path"] != TARGET_PATH:
        raise Phase7Error("pinned CASE-001 input mismatch")
    max_out = int(c["worker"]["max_output_tokens"])
    # Same conservative list-price basis used by the accepted Phase-4B runner.
    input_bytes = len((c["raw_human_intent"] + case["case_contract"] + case["target_source"] + case["tests_source"]).encode("utf-8")) + 20000
    conservative = (Decimal(input_bytes) * Decimal("1.5") + Decimal(max_out * 2) * Decimal("7.5")) / Decimal(1000000)
    if conservative > Decimal(c["limits"]["max_estimated_model_spend_usd"]):
        raise Phase7Error("pre-call spend guard blocks model call")
    gateway = GeminiGenerateContentGateway(model_id=MODEL_ID, reasoning_effort="medium", max_output_tokens=max_out)
    result = gateway.generate(case_id=CASE_ID, target_path=TARGET_PATH, problem=c["raw_human_intent"], case_contract=case["case_contract"], target_source=case["target_source"], tests_source=case["tests_source"])
    mutation = validate_worker_proposal(result.proposal, case_id=CASE_ID, target_path=TARGET_PATH, before_text=case["target_source"], max_patch_lines=case["max_patch_lines"])
    usage = asdict(result.usage)
    if not isinstance(usage.get("input_tokens"), int) or not isinstance(usage.get("output_tokens"), int):
        raise Phase7Error("missing model usage evidence; block execution")
    billed_out = usage["output_tokens"] + (usage.get("reasoning_tokens") or 0)
    cost = (Decimal(usage["input_tokens"]) * Decimal("1.5") + Decimal(billed_out) * Decimal("7.5")) / Decimal(1000000)
    if cost > Decimal(c["limits"]["max_estimated_model_spend_usd"]):
        raise Phase7Error("observed model cost exceeds Phase-7 cap; block execution")
    worker = {
        "schema_version": "saddle-phase7-worker-proposal/0.1", "provider": "google-gemini", "api": "generateContent",
        "model_id": result.model_id, "case_id": CASE_ID, "provider_response_id": result.response_id,
        "latency_ms": result.latency_ms, "usage": usage, "estimated_cost_usd": format(cost.quantize(Decimal("0.000001")), "f"),
        "automatic_retries": 0, "proposal": result.proposal, "mutation": mutation,
        "authority_status": "NOT_GRANTED_BY_MODEL", "execution_status": "NOT_EXECUTED_AT_PROPOSAL_TIME",
    }
    return worker, mutation, worker["estimated_cost_usd"]


def effect_and_authority(intent: dict[str, Any], binding: dict[str, Any], worker: dict[str, Any], origin_ref: str, now: datetime) -> tuple[dict[str, Any], dict[str, Any]]:
    p = worker["proposal"]
    proposal = with_derived_identity({
        "schema_version": "saddle-effect-proposal/0.1", "intent_id": intent["intent_id"],
        "action": "WRITE_REPOSITORY_FILE", "target": {"kind": "FILE", "ref": TARGET_PATH},
        "expected_effect": "CASE-001 is fixed inside the single allowlisted registry source file.",
        "required_capabilities": ["READ_REPOSITORY", "WRITE_REPOSITORY"],
        "risk": {"level": "LOW", "notes": ["Controlled Phase-7 acceptance fixture; human review required."]},
        "reason": p["reason"], "evidence_plan": [{"description": x} for x in p["evidence_plan"]], "created_at": _ts(now),
    })
    authority = with_boundary_identity({
        "schema_version": "saddle-effect-authority/0.1", "decision": "ALLOW",
        "intent_binding_id": binding["binding_id"], "intent_binding_hash": binding["content_hash"],
        "effect_id": proposal["effect_id"], "effect_content_hash": proposal["content_hash"],
        "authorized_action": proposal["action"], "authorized_target": proposal["target"],
        "evidence_requirements": ["current Executor identity matches", "pinned CASE-001 identity matches", "pre-change target test fails", "post-change target and regression tests pass", "exactly one allowlisted file changes", "human review remains required"],
        "issuer_kind": "POLICY", "issuer_ref": "policy:phase7-case001-acceptance-only",
        "source_refs": ["decision:DEC-SAD-016", "config:phase7-acceptance-run-v0.1", origin_ref],
        "status": "ACTIVE", "max_uses": 1, "issued_at": _ts(now), "expires_at": _ts(now + timedelta(hours=2)),
        "reason": "Active Phase-7 policy permits only this exact controlled CASE-001 effect after verified origin and selected-worker validation.",
    })
    return proposal, authority


def require_executor_report(r: dict[str, Any]) -> None:
    expected = {"fixture_authority": "BOUND", "input_identity": "MATCH", "pre_change_target_test": "FAIL", "post_change_target_test": "PASS", "regression_checks": "PASS", "diff_scope": "ALLOWED", "protected_material": "UNCHANGED", "execution_limits": "RESPECTED", "result_artifact": "PRESENT"}
    if r.get("status") != "ACTION_COMPLETED_REVIEW_REQUIRED" or r.get("changed_paths") != [TARGET_PATH] or r.get("human_decision_required") is not True or r.get("evidence") != expected:
        raise Phase7Error(f"Executor evidence failed closed: {r}")


def receipt_and_delta(intent: dict[str, Any], proposal: dict[str, Any], authority: dict[str, Any], worker: dict[str, Any], report: dict[str, Any], now: datetime, duration_ms: int) -> tuple[dict[str, Any], dict[str, Any]]:
    report_ref = _ref("executor-report:phase7-case001", "EVIDENCE", sha256_ref(report))
    worker_ref = _ref("worker-proposal:phase7-gemini36flash-case001", "EVIDENCE", sha256_ref(worker))
    receipt = with_derived_identity({
        "schema_version": "saddle-effect-receipt/0.1", "effect_id": proposal["effect_id"],
        "authorization_ref": {"authority_id": authority["authority_id"], "authority_kind": "EFFECT_PERMISSION", "status": "ACTIVE", "binds_to": {"object_type": "EFFECT", "object_id": proposal["effect_id"], "content_hash": proposal["content_hash"]}, "source_refs": [_ref("authority:phase7-case001-acceptance-only")], "issued_at": authority["issued_at"]},
        "status": "SUCCEEDED", "actual_effect": {"summary": "Current Executor executed exactly the one-file real-Gemini proposal and returned review-required evidence.", "result_refs": [worker_ref, report_ref]},
        "changed_objects": [_ref(TARGET_PATH, "FILE")], "evidence_refs": [worker_ref, report_ref],
        "tests": [{"name": "executor-gp001-verification", "status": "PASS", "evidence_refs": [report_ref]}],
        "duration_ms": max(0, int(duration_ms)), "observed_at": _ts(now),
    })
    delta = with_derived_identity({
        "schema_version": "saddle-state-delta/0.1", "intent_id": intent["intent_id"], "effect_id": proposal["effect_id"],
        "facts_added": [{"fact_id": "fact:phase7-real-worker-executor-evidence", "statement": "Real Gemini 3.6 Flash proposal crossed exact authority and current Executor returned bounded review-required evidence.", "source_refs": [worker_ref, report_ref], "observed_at": _ts(now)}],
        "decisions_added": [], "hypotheses_added": [], "superseded": [], "project_status_change": None,
        "blockers": ["Required human review is open.", "Second zero-history resume is required before final functional acceptance."],
        "next_step": "Human review of Phase-7 evidence; if accepted, persist that decision and perform the required second zero-history repository-only resume.",
        "source_refs": [worker_ref, report_ref], "created_at": _ts(now),
    })
    return receipt, delta


def run(root: Path, executor_root: Path, workspace: Path, runs_root: Path, image: str, output: Path) -> dict[str, Any]:
    c = _json(root / CONFIG_PATH); validate_config(c)
    env = dict(os.environ); now = datetime.now(timezone.utc).replace(microsecond=0)
    origin, origin_ref, origin_hash = origin_evidence(c, env, now)
    if _head(root) != env["PHASE7_SHA"] or _head(executor_root) != EXECUTOR_COMMIT or _head(workspace) != FIXTURE_COMMIT:
        raise Phase7Error("repository identity mismatch")
    output.mkdir(parents=True, exist_ok=True); _write(output / "origin_event.json", origin)
    intent, binding = intent_and_binding(c, origin_ref, origin_hash, now); _write(output / "intent.json", intent); _write(output / "verified_intent_binding.json", binding)
    worker, mutation, cost = real_worker(root, workspace, c); _write(output / "worker_proposal.json", worker)
    t = datetime.now(timezone.utc).replace(microsecond=0); proposal, authority = effect_and_authority(intent, binding, worker, origin_ref, t)
    consumed: set[str] = set(); auth = authorize_effect(intent, binding, proposal, authority, now=t, consumed_authority_ids=consumed)
    if auth.get("status") != "ALLOW": raise Phase7Error(f"exact authority blocked: {auth}")
    _write(output / "effect_proposal.json", proposal); _write(output / "effect_authority.json", authority); _write(output / "authority_result.json", auth)
    sys.path.insert(0, str(executor_root)); from executor.gp001_runtime import AuthorizedFileMutation, GP001Runtime  # type: ignore
    m = AuthorizedFileMutation(path=mutation["path"], expected_before_sha256=mutation["expected_before_sha256"], replacement_text=mutation["replacement_text"], expected_after_sha256=mutation["expected_after_sha256"])
    runtime = GP001Runtime(executor_root=executor_root, executor_commit=EXECUTOR_COMMIT, runs_root=runs_root, image=image)
    started = time.monotonic(); report = runtime.execute(workspace=workspace, mutation=m, run_id="phase7-gemini36flash-case001", now=t); duration = round((time.monotonic()-started)*1000)
    require_executor_report(report); _write(output / "executor_report.json", report)
    end = datetime.now(timezone.utc).replace(microsecond=0); receipt, delta = receipt_and_delta(intent, proposal, authority, worker, report, end, duration)
    validate_bundle(intent, proposal, receipt, delta, root / "protocol" / "v0.1"); _write(output / "effect_receipt.json", receipt); _write(output / "state_delta.json", delta)
    (output / "candidate.patch").write_text(_diff(workspace), encoding="utf-8")
    summary = {
        "schema_version": "saddle-phase7-functional-acceptance-summary/0.1", "status": "E2E_EFFECT_COMPLETE_REVIEW_REQUIRED", "context_recovery": "REPOSITORY_ONLY",
        "saddle_sha": env["PHASE7_SHA"], "origin": {"provider": c["origin"]["provider"], "principal_ref": c["origin"]["principal_ref"], "ref_id": origin_ref, "content_hash": origin_hash, "actor": env["PHASE7_ACTOR"], "github_run_id": int(env["PHASE7_RUN_ID"])},
        "worker": {"provider": "google-gemini", "model_id": MODEL_ID, "model_calls": 1, "automatic_retries": 0, "latency_ms": worker["latency_ms"], "usage": worker["usage"], "estimated_cost_usd": cost, "proposal_hash": sha256_ref(worker)},
        "effect": {"effect_id": proposal["effect_id"], "authority_id": authority["authority_id"], "executor_repository": EXECUTOR_REPOSITORY, "executor_commit": EXECUTOR_COMMIT, "fixture_repository": FIXTURE_REPOSITORY, "fixture_commit": FIXTURE_COMMIT, "changed_paths": report["changed_paths"], "executor_report_hash": sha256_ref(report), "receipt_id": receipt["receipt_id"], "state_delta_id": delta["state_delta_id"], "protocol_bundle": "PASS"},
        "human_review_required": True, "second_zero_history_resume_required": True, "explicit_final_human_acceptance_required": True,
        "functional_saddle_accepted": False, "completion_lock_release_authorized": False, "next_gate": "HUMAN_REVIEW_THEN_SECOND_ZERO_HISTORY_RESUME",
    }
    _write(output / "summary.json", summary); return summary


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(); p.add_argument("--root", type=Path, default=Path(".")); p.add_argument("--executor-root", type=Path, required=True); p.add_argument("--workspace", type=Path, required=True); p.add_argument("--runs-root", type=Path, required=True); p.add_argument("--image", required=True); p.add_argument("--output-dir", type=Path, required=True); a = p.parse_args(argv)
    try:
        result = run(a.root.resolve(), a.executor_root.resolve(), a.workspace.resolve(), a.runs_root.resolve(), a.image, a.output_dir.resolve())
    except CredentialUnavailable as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}, sort_keys=True)); return 3
    except (Phase7Error, GatewayError, BenchmarkError, OSError, subprocess.SubprocessError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, sort_keys=True)); return 2
    print(json.dumps(result, sort_keys=True)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
