"""Generate bounded model proposals for pinned Phase-4 benchmark cases.

This tool does not execute the proposal. It verifies the local checkout identity,
feeds only the pinned case/target/tests to ModelGateway, validates the returned
proposal, and writes a proposal artifact suitable for the later Executor bridge.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Any

from tools.model_gateway import (
    CredentialUnavailable,
    GatewayError,
    OpenAIResponsesGateway,
    validate_worker_proposal,
)


class BenchmarkError(RuntimeError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BenchmarkError(f"{path}: expected JSON object")
    return value


def _git_head(checkout: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(checkout), "rev-parse", "HEAD"],
            check=False,
            text=True,
            capture_output=True,
            timeout=15,
            env={"PATH": __import__("os").environ.get("PATH", "")},
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise BenchmarkError(f"cannot verify checkout identity: {exc}") from exc
    if result.returncode != 0:
        raise BenchmarkError("cannot resolve local benchmark checkout HEAD")
    return result.stdout.strip()


def load_case(root: Path, checkout: Path, case_id: str) -> dict[str, Any]:
    config = _load_json(root / "config" / "worker-cases-v0.1.json")
    cases = config.get("cases")
    if not isinstance(cases, list):
        raise BenchmarkError("worker case config is invalid")
    selected = next((item for item in cases if isinstance(item, dict) and item.get("case_id") == case_id), None)
    if selected is None:
        raise BenchmarkError(f"unknown case_id: {case_id}")

    expected_commit = selected["commit"]
    actual_commit = _git_head(checkout)
    if actual_commit != expected_commit:
        raise BenchmarkError(
            f"benchmark checkout mismatch for {case_id}: expected {expected_commit}, got {actual_commit}"
        )

    target_path = selected["target_path"]
    case_doc_path = selected["case_doc"]
    tests_paths = selected["tests_paths"]
    if not isinstance(tests_paths, list) or not tests_paths:
        raise BenchmarkError(f"{case_id}: tests_paths missing")

    try:
        target_source = (checkout / target_path).read_text(encoding="utf-8")
        case_contract = (checkout / case_doc_path).read_text(encoding="utf-8")
        tests_source = "\n\n".join(
            f"### {path}\n{(checkout / path).read_text(encoding='utf-8')}"
            for path in tests_paths
        )
    except OSError as exc:
        raise BenchmarkError(f"{case_id}: cannot read pinned case inputs: {exc}") from exc

    return {
        "case_id": case_id,
        "repository": config["repository"],
        "commit": expected_commit,
        "target_path": target_path,
        "case_contract": case_contract,
        "problem": case_contract,
        "target_source": target_source,
        "tests_source": tests_source,
        "target_tests": selected["target_tests"],
        "max_patch_lines": selected["max_patch_lines"],
    }


def generate_proposal(
    *,
    root: Path,
    checkout: Path,
    case_id: str,
    model_id: str,
    reasoning_effort: str,
    api_key_env: str = "OPENAI_API_KEY",
) -> dict[str, Any]:
    case = load_case(root, checkout, case_id)
    gateway = OpenAIResponsesGateway(
        model_id=model_id,
        reasoning_effort=reasoning_effort,
        api_key_env=api_key_env,
    )
    result = gateway.generate(
        case_id=case_id,
        target_path=case["target_path"],
        problem=case["problem"],
        case_contract=case["case_contract"],
        target_source=case["target_source"],
        tests_source=case["tests_source"],
    )
    mutation = validate_worker_proposal(
        result.proposal,
        case_id=case_id,
        target_path=case["target_path"],
        before_text=case["target_source"],
        max_patch_lines=case["max_patch_lines"],
    )
    return {
        "schema_version": "saddle-phase4-proposal-artifact/0.1",
        "case_id": case_id,
        "repository": case["repository"],
        "commit": case["commit"],
        "model_id": result.model_id,
        "reasoning_effort": reasoning_effort,
        "latency_ms": result.latency_ms,
        "usage": asdict(result.usage),
        "provider_response_id": result.response_id,
        "mutation": mutation,
        "execution_status": "NOT_EXECUTED",
        "authority_status": "NOT_GRANTED_BY_MODEL",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--case", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    try:
        artifact = generate_proposal(
            root=args.root,
            checkout=args.checkout,
            case_id=args.case,
            model_id=args.model,
            reasoning_effort=args.reasoning_effort,
            api_key_env=args.api_key_env,
        )
    except CredentialUnavailable as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}, sort_keys=True))
        return 1
    except (OSError, json.JSONDecodeError, BenchmarkError, GatewayError) as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, sort_keys=True))
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(artifact, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PROPOSAL_READY", "output": str(args.output)}, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
