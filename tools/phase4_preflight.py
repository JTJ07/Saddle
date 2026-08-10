"""Phase-4 preflight without model inference or secret disclosure."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

SHA40 = re.compile(r"^[0-9a-f]{40}$")


class PreflightError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise PreflightError(f"{path}: expected object")
    return value


def run_preflight(root: Path, *, credential_env: str = "OPENAI_API_KEY") -> dict[str, Any]:
    models = _load(root / "config" / "model-benchmark-v0.1.json")
    cases = _load(root / "config" / "worker-cases-v0.1.json")

    candidates = models.get("candidates")
    if not isinstance(candidates, list) or len(candidates) < 2:
        raise PreflightError("benchmark must contain at least two model candidates")
    model_ids: list[str] = []
    for item in candidates:
        if not isinstance(item, dict) or not isinstance(item.get("model_id"), str) or not item["model_id"]:
            raise PreflightError("candidate model_id missing")
        model_ids.append(item["model_id"])
    if len(set(model_ids)) != len(model_ids):
        raise PreflightError("candidate model IDs must be unique")

    case_items = cases.get("cases")
    if not isinstance(case_items, list) or len(case_items) != 3:
        raise PreflightError("Phase 4 first benchmark must pin exactly CASE-001–003")
    case_ids: list[str] = []
    for item in case_items:
        if not isinstance(item, dict):
            raise PreflightError("case config entry must be an object")
        case_id = item.get("case_id")
        commit = item.get("commit")
        target_path = item.get("target_path")
        tests_paths = item.get("tests_paths")
        if not isinstance(case_id, str) or not case_id:
            raise PreflightError("case_id missing")
        if not isinstance(commit, str) or SHA40.fullmatch(commit) is None:
            raise PreflightError(f"{case_id}: exact 40-hex commit required")
        if target_path != "project_registry/registry.py":
            raise PreflightError(f"{case_id}: unexpected target path")
        if not isinstance(tests_paths, list) or not tests_paths:
            raise PreflightError(f"{case_id}: tests_paths required")
        case_ids.append(case_id)
    if case_ids != ["CASE-001", "CASE-002", "CASE-003"]:
        raise PreflightError("case order/identity must be CASE-001, CASE-002, CASE-003")

    credential_present = bool(os.environ.get(credential_env))
    status = "READY_FOR_EXTERNAL_BENCHMARK" if credential_present else "BLOCKED"
    reasons = [] if credential_present else ["PROVIDER_CREDENTIAL_NOT_CONFIGURED"]
    return {
        "schema_version": "saddle-phase4-preflight/0.1",
        "status": status,
        "candidate_models": model_ids,
        "cases": case_ids,
        "credential_env": credential_env,
        "credential_present": credential_present,
        "reasons": reasons,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--credential-env", default="OPENAI_API_KEY")
    args = parser.parse_args(argv)
    try:
        result = run_preflight(args.root, credential_env=args.credential_env)
    except (OSError, json.JSONDecodeError, PreflightError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "READY_FOR_EXTERNAL_BENCHMARK" else 1

if __name__ == "__main__":
    raise SystemExit(main())
