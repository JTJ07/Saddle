"""Run the approved Phase-4 live AI benchmark in isolated temporary checkouts.

This is evaluation infrastructure, not an execution capability. The model receives
no tools, shell, write access, or authority. Each proposal is applied only to an
ephemeral checkout for deterministic tests. Nothing is pushed to the target repo.

Human-approved bound (2026-08-10): max USD 5, max 6 model calls, zero automatic
retries, benchmark only. Provider swapped to Gemini by explicit human decision on
2026-08-11 without changing those bounds.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from tools.model_gateway import CredentialUnavailable, GatewayError
from tools.phase4_benchmark import generate_proposal, load_case


class LiveBenchmarkError(RuntimeError):
    pass


PRICES_PER_MILLION = {
    "gemini-3.1-pro-preview": {"input": 2.0, "output": 12.0},
    "gemini-3.6-flash": {"input": 1.5, "output": 7.5},
}


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise LiveBenchmarkError(f"{path}: expected object")
    return value


def _run(cmd: list[str], *, cwd: Path | None = None, timeout: int = 120) -> dict[str, Any]:
    started = time.monotonic()
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
        env={**os.environ, "PYTHONUTF8": "1"},
    )
    return {
        "command": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-12000:],
        "stderr": proc.stderr[-12000:],
        "latency_ms": round((time.monotonic() - started) * 1000),
    }


def _clone_pinned(repo_url: str, commit: str, dest: Path) -> None:
    clone = _run(["git", "clone", "--quiet", repo_url, str(dest)], timeout=180)
    if clone["returncode"] != 0:
        raise LiveBenchmarkError(f"git clone failed: {clone['stderr']}")
    checkout = _run(["git", "checkout", "--quiet", commit], cwd=dest)
    if checkout["returncode"] != 0:
        raise LiveBenchmarkError(f"git checkout {commit} failed: {checkout['stderr']}")
    head = _run(["git", "rev-parse", "HEAD"], cwd=dest)
    if head["returncode"] != 0 or head["stdout"].strip() != commit:
        raise LiveBenchmarkError(f"pinned checkout mismatch: expected {commit}")


def _contract_hash(case: dict[str, Any]) -> str:
    raw = "\n\n".join(
        [
            case["case_id"],
            case["commit"],
            case["target_path"],
            case["case_contract"],
            case["target_source"],
            case["tests_source"],
        ]
    )
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _estimated_cost(model_id: str, usage: dict[str, Any]) -> float | None:
    prices = PRICES_PER_MILLION.get(model_id)
    input_tokens = usage.get("input_tokens")
    output_tokens = usage.get("output_tokens")
    reasoning_tokens = usage.get("reasoning_tokens")
    if not prices or not isinstance(input_tokens, int) or not isinstance(output_tokens, int):
        return None
    billed_output_tokens = output_tokens + (reasoning_tokens if isinstance(reasoning_tokens, int) else 0)
    return (input_tokens * prices["input"] + billed_output_tokens * prices["output"]) / 1_000_000


def _conservative_max_call_cost(model_id: str, case: dict[str, Any], max_output_tokens: int) -> float:
    prices = PRICES_PER_MILLION.get(model_id)
    if prices is None:
        raise LiveBenchmarkError(f"no approved price table for model {model_id}")
    input_bytes = len(
        (case["problem"] + case["case_contract"] + case["target_source"] + case["tests_source"]).encode("utf-8")
    ) + 20_000
    # Gemini bills thinking tokens at the output rate. Reserve a second max-output
    # allowance for thinking so the pre-call guard remains conservative.
    conservative_output_tokens = max_output_tokens * 2
    return (
        input_bytes * prices["input"]
        + conservative_output_tokens * prices["output"]
    ) / 1_000_000


def _evaluate_proposal(run_checkout: Path, case: dict[str, Any], artifact: dict[str, Any]) -> dict[str, Any]:
    mutation = artifact["mutation"]
    target = run_checkout / mutation["path"]
    before = target.read_text(encoding="utf-8")
    if hashlib.sha256(before.encode("utf-8")).hexdigest() != mutation["expected_before_sha256"]:
        raise LiveBenchmarkError("before hash mismatch in isolated evaluator")
    target.write_text(mutation["replacement_text"], encoding="utf-8")
    after = target.read_text(encoding="utf-8")
    if hashlib.sha256(after.encode("utf-8")).hexdigest() != mutation["expected_after_sha256"]:
        raise LiveBenchmarkError("after hash mismatch in isolated evaluator")

    changed = _run(["git", "diff", "--name-only"], cwd=run_checkout)
    changed_files = [line for line in changed["stdout"].splitlines() if line.strip()]
    scope_ok = changed["returncode"] == 0 and changed_files == [case["target_path"]]

    target_tests = _run(["python", "-m", "unittest", *case["target_tests"], "-v"], cwd=run_checkout, timeout=120)
    full_tests = _run(["python", "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=run_checkout, timeout=120)

    return {
        "scope_ok": scope_ok,
        "changed_files": changed_files,
        "target_tests": target_tests,
        "full_tests": full_tests,
        "task_pass": scope_ok and target_tests["returncode"] == 0 and full_tests["returncode"] == 0,
    }


def run_benchmark(*, root: Path, output_dir: Path, budget_usd: float, max_calls: int) -> dict[str, Any]:
    if not os.environ.get("GEMINI_API_KEY"):
        raise CredentialUnavailable("GEMINI_API_KEY is not configured in the benchmark runner environment")

    benchmark = _load_json(root / "config" / "model-benchmark-v0.1.json")
    cases_cfg = _load_json(root / "config" / "worker-cases-v0.1.json")
    policy = benchmark["first_pass_policy"]
    if benchmark.get("provider") != "google-gemini" or benchmark.get("api") != "generateContent":
        raise LiveBenchmarkError("active benchmark provider/API is not the approved Gemini generateContent pair")
    if policy.get("automatic_retries") != 0:
        raise LiveBenchmarkError("benchmark config violates zero-retry decision")
    if max_calls > 6 or max_calls > int(policy.get("max_total_model_calls", 0)):
        raise LiveBenchmarkError("requested call count exceeds approved/configured maximum")
    if budget_usd > 5.0:
        raise LiveBenchmarkError("requested budget exceeds approved USD 5 maximum")

    model_ids = [c["model_id"] for c in benchmark["candidates"]]
    case_ids = [c["case_id"] for c in cases_cfg["cases"]]
    matrix = [(case_id, model_id) for case_id in case_ids for model_id in model_ids]

    output_dir.mkdir(parents=True, exist_ok=True)
    results_path = output_dir / "results.jsonl"
    results_path.write_text("", encoding="utf-8")
    results: list[dict[str, Any]] = []
    spent_usd = 0.0
    calls_attempted = 0
    stop_reason: str | None = None
    max_output_tokens = int(policy.get("max_output_tokens_per_call", 8192))

    repo_url = "https://github.com/" + cases_cfg["repository"] + ".git"

    with tempfile.TemporaryDirectory(prefix="saddle-live-benchmark-") as tmp:
        tmp_root = Path(tmp)
        base_checkouts: dict[str, Path] = {}
        for case_config in cases_cfg["cases"]:
            case_id = case_config["case_id"]
            base = tmp_root / f"base-{case_id}"
            _clone_pinned(repo_url, case_config["commit"], base)
            base_checkouts[case_id] = base

        for case_id, model_id in matrix:
            if calls_attempted >= max_calls:
                stop_reason = "MAX_CALLS_REACHED"
                break

            base = base_checkouts[case_id]
            run_checkout = tmp_root / f"run-{case_id}-{model_id}"
            shutil.copytree(base, run_checkout)
            case = load_case(root, run_checkout, case_id)

            conservative = _conservative_max_call_cost(model_id, case, max_output_tokens)
            if spent_usd + conservative > budget_usd:
                stop_reason = "BUDGET_GUARD_BEFORE_CALL"
                break

            record: dict[str, Any] = {
                "schema_version": "saddle-live-ai-benchmark-result/0.1",
                "provider": benchmark["provider"],
                "api": benchmark["api"],
                "case_id": case_id,
                "model_id": model_id,
                "commit": case["commit"],
                "target_path": case["target_path"],
                "input_contract_hash": _contract_hash(case),
                "reasoning_effort": "medium",
                "max_output_tokens": max_output_tokens,
                "call_number": calls_attempted + 1,
                "automatic_retry_count": 0,
                "execution_authority": "NONE",
                "target_repo_write": "NONE",
                "decision": "PENDING_EVALUATION",
                "cost_basis": "PUBLISHED_STANDARD_LIST_PRICE_ESTIMATE_2026-08-11",
            }
            calls_attempted += 1

            try:
                artifact = generate_proposal(
                    root=root,
                    checkout=run_checkout,
                    case_id=case_id,
                    model_id=model_id,
                    reasoning_effort="medium",
                    api_key_env="GEMINI_API_KEY",
                    max_output_tokens=max_output_tokens,
                )
                record["proposal"] = artifact
                record["structured_output_valid"] = True
                evaluation = _evaluate_proposal(run_checkout, case, artifact)
                record["evaluation"] = evaluation
                cost = _estimated_cost(model_id, artifact.get("usage", {}))
                record["estimated_cost_usd"] = cost
                if cost is None:
                    record["result"] = "BLOCKED_COST_UNKNOWN"
                    stop_reason = "USAGE_OR_COST_UNKNOWN"
                else:
                    spent_usd += cost
                    record["result"] = "PASS" if evaluation["task_pass"] else "FAIL"
            except (GatewayError, LiveBenchmarkError, OSError, subprocess.SubprocessError) as exc:
                record["structured_output_valid"] = False
                record["result"] = "ERROR"
                record["error_type"] = type(exc).__name__
                record["error"] = str(exc)
                message = str(exc)
                if "HTTP 401" in message or "HTTP 403" in message:
                    stop_reason = "PROVIDER_CREDENTIAL_OR_ACCESS_DENIED"
                elif "HTTP 404" in message:
                    stop_reason = "MODEL_NOT_AVAILABLE_TO_ACCOUNT"
                elif "HTTP 429" in message:
                    stop_reason = "PROVIDER_RATE_LIMITED_NO_RETRY"
                elif "HTTP 503" in message:
                    stop_reason = "PROVIDER_UNAVAILABLE_NO_RETRY"
                elif "HTTP 400" in message:
                    stop_reason = "PROVIDER_REQUEST_REJECTED"

            record["cumulative_estimated_cost_usd"] = round(spent_usd, 8)
            results.append(record)
            with results_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")

            if spent_usd > budget_usd:
                stop_reason = "BUDGET_EXCEEDED_AFTER_CALL"
            if stop_reason:
                break

    passed = sum(1 for r in results if r.get("result") == "PASS")
    failed = sum(1 for r in results if r.get("result") == "FAIL")
    errors = sum(1 for r in results if r.get("result") not in {"PASS", "FAIL"})
    summary = {
        "schema_version": "saddle-live-ai-benchmark-summary/0.1",
        "status": "COMPLETE" if calls_attempted == len(matrix) and stop_reason is None else "PARTIAL_OR_BLOCKED",
        "provider": benchmark["provider"],
        "api": benchmark["api"],
        "calls_attempted": calls_attempted,
        "max_calls_approved": max_calls,
        "automatic_retries": 0,
        "budget_usd_approved": budget_usd,
        "estimated_cost_usd": round(spent_usd, 8),
        "cost_basis": "PUBLISHED_STANDARD_LIST_PRICE_ESTIMATE_2026-08-11",
        "passed": passed,
        "failed": failed,
        "errors_or_blocked": errors,
        "stop_reason": stop_reason,
        "models": model_ids,
        "cases": case_ids,
        "selection_status": "PENDING_HUMAN_EVALUATION",
        "functional_saddle_accepted": False,
    }
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--budget-usd", type=float, default=5.0)
    parser.add_argument("--max-calls", type=int, default=6)
    args = parser.parse_args(argv)

    try:
        summary = run_benchmark(
            root=args.root.resolve(),
            output_dir=args.output_dir.resolve(),
            budget_usd=args.budget_usd,
            max_calls=args.max_calls,
        )
    except CredentialUnavailable as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}, sort_keys=True))
        return 3
    except (LiveBenchmarkError, OSError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, sort_keys=True))
        return 2

    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "COMPLETE" else 4


if __name__ == "__main__":
    raise SystemExit(main())
