"""Saddle Phase-3 stdlib-only audit/eval foundation."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

SAFE_MAX = 9007199254740991
RESULTS = {"PASS", "FAIL", "BLOCKED", "ERROR"}
METRIC_KEYS = {"latency_ms", "input_tokens", "output_tokens", "cost_minor", "currency", "retries", "human_corrections"}
TOP_KEYS = {
    "schema_version", "run_id", "lane_id", "case_id", "subject_ref", "result",
    "model", "prompt_version", "metrics", "scope_violations", "policy_violations",
    "evidence_refs", "started_at", "finished_at", "notes"
}
TS_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
READY_NEXT_STATUS_RE = re.compile(r"^Status:\s*`READY / NEXT(?: / [^`]*)?`\s*$", re.MULTILINE)
HUMAN_REVIEW_OPEN_STATUS_RE = re.compile(
    r"^Status:\s*`TECHNICAL E2E COMPLETE THROUGH HUMAN-REVIEW BOUNDARY / HUMAN REVIEW OPEN`\s*$",
    re.MULTILINE,
)
RUN94_EXECUTOR_IMPLEMENTATION = "3cd0c8d747fef06f82c01cdab8449c7c8a100038"
RUN94_EXECUTOR_TREE = "c739aaa989a15eaed65996d7a0b5242a0ec26d7e"
HISTORICAL_EXECUTOR_FIRST_TARGET = "f60829f90ea2f69dc501582daf109b59676be07e"
HUMAN_OPERATING_CONTRACT_PATH = "docs/HUMAN_OPERATING_CONTRACT.md"


class EvalError(ValueError):
    pass


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise EvalError(f"duplicate JSON property: {key}")
        out[key] = value
    return out


def _reject_float(token: str) -> float:
    raise EvalError(f"floating-point JSON number forbidden: {token}")


def strict_loads(text: str) -> Any:
    try:
        return json.loads(text, object_pairs_hook=_pairs, parse_float=_reject_float)
    except json.JSONDecodeError as exc:
        raise EvalError(f"invalid JSON: {exc}") from exc


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def derive_run_id(record: dict[str, Any]) -> str:
    payload = copy.deepcopy(record)
    payload.pop("run_id", None)
    digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    return f"eval:sha256:{digest}"


def with_run_id(record: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(record)
    result["run_id"] = derive_run_id(result)
    return result


def _nonempty_string(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value:
        raise EvalError(f"{field}: expected non-empty string")


def _nullable_nonnegative_int(value: Any, field: str) -> None:
    if value is None:
        return
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= SAFE_MAX:
        raise EvalError(f"{field}: expected null or safe non-negative integer")


def validate_result(record: dict[str, Any]) -> None:
    if not isinstance(record, dict):
        raise EvalError("eval result must be an object")
    missing = TOP_KEYS - set(record)
    extra = set(record) - TOP_KEYS
    if missing:
        raise EvalError(f"missing fields: {sorted(missing)}")
    if extra:
        raise EvalError(f"unknown fields: {sorted(extra)}")
    if record["schema_version"] != "saddle-eval-result/0.1":
        raise EvalError("unsupported schema_version")
    if record["run_id"] != derive_run_id(record):
        raise EvalError("run_id does not match result content")
    for field in ("lane_id", "case_id", "subject_ref"):
        _nonempty_string(record[field], field)
    if record["result"] not in RESULTS:
        raise EvalError("invalid result")
    model = record["model"]
    if model is not None:
        if not isinstance(model, dict) or set(model) - {"provider", "model_id", "model_version"}:
            raise EvalError("model: invalid object")
        if "provider" not in model or "model_id" not in model:
            raise EvalError("model: provider and model_id required")
        _nonempty_string(model["provider"], "model.provider")
        _nonempty_string(model["model_id"], "model.model_id")
        if "model_version" in model:
            _nonempty_string(model["model_version"], "model.model_version")
    if record["prompt_version"] is not None:
        _nonempty_string(record["prompt_version"], "prompt_version")
    metrics = record["metrics"]
    if not isinstance(metrics, dict) or set(metrics) != METRIC_KEYS:
        raise EvalError("metrics: exact metric fields required")
    for key in ("latency_ms", "input_tokens", "output_tokens", "cost_minor"):
        _nullable_nonnegative_int(metrics[key], f"metrics.{key}")
    for key in ("retries", "human_corrections"):
        _nullable_nonnegative_int(metrics[key], f"metrics.{key}")
        if metrics[key] is None:
            raise EvalError(f"metrics.{key}: must be an integer")
    currency = metrics["currency"]
    if currency is not None and (not isinstance(currency, str) or re.fullmatch(r"[A-Z]{3}", currency) is None):
        raise EvalError("metrics.currency: expected null or ISO-like three-letter code")
    if metrics["cost_minor"] is not None and currency is None:
        raise EvalError("metrics.currency required when cost_minor is present")
    for field in ("scope_violations", "policy_violations", "evidence_refs", "notes"):
        values = record[field]
        if not isinstance(values, list) or any(not isinstance(item, str) or not item for item in values):
            raise EvalError(f"{field}: expected array of non-empty strings")
    if not record["evidence_refs"]:
        raise EvalError("evidence_refs must not be empty")
    for field in ("started_at", "finished_at"):
        if not isinstance(record[field], str) or TS_RE.fullmatch(record[field]) is None:
            raise EvalError(f"{field}: expected UTC second-resolution timestamp")


def effective_result(record: dict[str, Any]) -> str:
    validate_result(record)
    if record["scope_violations"] or record["policy_violations"]:
        return "FAIL"
    return record["result"]


def aggregate(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    items = list(records)
    if not items:
        return {
            "schema_version": "saddle-eval-summary/0.1",
            "overall": "BLOCKED",
            "total": 0,
            "counts": {key: 0 for key in ("PASS", "FAIL", "BLOCKED", "ERROR")},
            "lanes": {},
            "reasons": ["NO_RESULTS"]
        }
    counts = {key: 0 for key in ("PASS", "FAIL", "BLOCKED", "ERROR")}
    lanes: dict[str, dict[str, int]] = {}
    reasons: list[str] = []
    for record in items:
        eff = effective_result(record)
        counts[eff] += 1
        lane = lanes.setdefault(record["lane_id"], {key: 0 for key in counts})
        lane[eff] += 1
        if record["scope_violations"]:
            reasons.append(f"{record['run_id']}:SCOPE_VIOLATION")
        if record["policy_violations"]:
            reasons.append(f"{record['run_id']}:POLICY_VIOLATION")
    if counts["ERROR"]:
        overall = "ERROR"
    elif counts["FAIL"]:
        overall = "FAIL"
    elif counts["BLOCKED"]:
        overall = "BLOCKED"
    else:
        overall = "PASS"
    return {
        "schema_version": "saddle-eval-summary/0.1",
        "overall": overall,
        "total": len(items),
        "counts": counts,
        "lanes": lanes,
        "reasons": sorted(set(reasons))
    }


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        value = strict_loads(raw)
        if not isinstance(value, dict):
            raise EvalError(f"line {line_no}: expected object")
        validate_result(value)
        records.append(value)
    return records


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _frontmatter_status(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    for line in text[4:end].splitlines():
        if line.startswith("status:"):
            return line.split(":", 1)[1].strip()
    return None


def _active_phase(status: str | None) -> int | None:
    if not status:
        return None
    match = re.search(r"PHASE_(\d+)_ACTIVE", status)
    return int(match.group(1)) if match else None


def audit_repository(root: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, passed: bool, evidence: str) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if passed else "FAIL", "evidence": evidence})

    required = ["AGENTS.md", "PROJECT_STATE.md", "EXECUTION_PLAN.md", "TODO.md", "RESTRICTIONS.md", "SESSION_HANDOFF.md", "DECISION_LOG.md", "ECOSYSTEM_MAP.md", "SOURCE_REGISTRY.md"]
    for rel in required:
        check(f"required:{rel}", (root / rel).is_file(), rel)

    state_path = root / "PROJECT_STATE.md"
    handoff_path = root / "SESSION_HANDOFF.md"
    todo_path = root / "TODO.md"
    functional_accepted = False
    if state_path.is_file() and handoff_path.is_file():
        state_text = state_path.read_text(encoding="utf-8")
        handoff_text = handoff_path.read_text(encoding="utf-8")
        state_status = _frontmatter_status(state_text)
        handoff_status = _frontmatter_status(handoff_text)
        check("state-status-present", state_status is not None, str(state_status))
        check("handoff-status-present", handoff_status is not None, str(handoff_status))
        state_functional = "FUNCTIONAL_SADDLE_ACCEPTED" in (state_status or "")
        handoff_functional = "FUNCTIONAL_SADDLE_ACCEPTED" in (handoff_status or "")
        check(
            "functional-state-match",
            state_functional == handoff_functional,
            f"state={state_status}; handoff={handoff_status}",
        )
        functional_accepted = state_functional and handoff_functional
        state_phase = _active_phase(state_status)
        handoff_phase = _active_phase(handoff_status)
        if functional_accepted:
            check(
                "terminal-no-active-phase",
                state_phase is None and handoff_phase is None,
                f"state={state_status}; handoff={handoff_status}",
            )
            check("completion-lock-released", "completion_lock: RELEASED" in state_text, "PROJECT_STATE.md")
        else:
            check(
                "active-phase-match",
                state_phase == handoff_phase and state_phase is not None,
                f"state={state_status}; handoff={handoff_status}",
            )
            check("completion-lock-active", "completion_lock: ACTIVE" in state_text, "PROJECT_STATE.md")
        check("state-one-next-step-section", state_text.count("## 9. One next step") == 1, "PROJECT_STATE.md")
        check("handoff-one-next-step-section", handoff_text.count("## ONE NEXT STEP") == 1, "SESSION_HANDOFF.md")

        # Narrow currentness checks for the canonical post-acceptance Saddle repository.
        # These are intentionally concrete regression guards, not a general semantic engine.
        if functional_accepted and "project: Saddle" in state_text:
            run94_state = RUN94_EXECUTOR_IMPLEMENTATION in state_text and RUN94_EXECUTOR_TREE in state_text
            run94_handoff = RUN94_EXECUTOR_IMPLEMENTATION in handoff_text and RUN94_EXECUTOR_TREE in handoff_text
            historical_preserved = HISTORICAL_EXECUTOR_FIRST_TARGET in state_text and HISTORICAL_EXECUTOR_FIRST_TARGET in handoff_text
            observed_not_live_lock = "OBSERVED SHA != LIVE LOCK" in state_text and "OBSERVED SHA != LIVE LOCK" in handoff_text
            stale_current_phrase = f"The exact Human-accepted Executor product candidate remains `{HISTORICAL_EXECUTOR_FIRST_TARGET}`"
            check("semantic-currentness:executor-run94-state", run94_state, "PROJECT_STATE.md")
            check("semantic-currentness:executor-run94-handoff", run94_handoff, "SESSION_HANDOFF.md")
            check("semantic-currentness:executor-historical-identity-preserved", historical_preserved, HISTORICAL_EXECUTOR_FIRST_TARGET)
            check("semantic-currentness:observed-sha-not-live-lock", observed_not_live_lock, "PROJECT_STATE.md + SESSION_HANDOFF.md")
            check("semantic-currentness:no-stale-f608-current-claim", stale_current_phrase not in handoff_text, "SESSION_HANDOFF.md")

            human_contract_path = root / HUMAN_OPERATING_CONTRACT_PATH
            human_contract_text = human_contract_path.read_text(encoding="utf-8") if human_contract_path.is_file() else ""
            human_contract_ok = all(
                marker in human_contract_text
                for marker in (
                    "semantic_owner: \"HUMAN\"",
                    "AKCJA = co jest robione + granice + wynik, jeśli już istnieje.",
                    "GDZIE = dokładna tożsamość scope; PINNED albo LIVE, gdy ma to znaczenie.",
                    "ODESŁAĆ = dokładnie jedna następna rzecz / decyzja / autoryzacja potrzebna teraz od Human albo NIC.",
                    "CAPABILITY != PERMISSION",
                )
            )
            human_contract_recovered = HUMAN_OPERATING_CONTRACT_PATH in state_text and HUMAN_OPERATING_CONTRACT_PATH in handoff_text
            check("human-operating-contract:present-current", human_contract_ok, HUMAN_OPERATING_CONTRACT_PATH)
            check("human-operating-contract:recovery-pointer", human_contract_recovered, "PROJECT_STATE.md + SESSION_HANDOFF.md")

    if todo_path.is_file():
        todo_text = todo_path.read_text(encoding="utf-8")
        ready_count = len(READY_NEXT_STATUS_RE.findall(todo_text))
        human_review_count = len(HUMAN_REVIEW_OPEN_STATUS_RE.findall(todo_text))
        expected_gate_count = 0 if functional_accepted else 1
        check(
            "todo-active-gate-count",
            ready_count + human_review_count == expected_gate_count,
            f"expected={expected_gate_count}; ready_next={ready_count}; human_review_open={human_review_count}",
        )

    lock_path = root / "config" / "completion-lock.json"
    if lock_path.is_file():
        try:
            lock = strict_loads(lock_path.read_text(encoding="utf-8"))
            expected_lock_status = "RELEASED" if functional_accepted else "ACTIVE"
            valid_lock = (
                isinstance(lock, dict)
                and lock.get("schema_version") == "saddle-completion-lock/0.1"
                and lock.get("status") == expected_lock_status
            )
            check(
                "completion-lock-config",
                valid_lock,
                f"expected={expected_lock_status}; observed={lock.get('status') if isinstance(lock, dict) else type(lock).__name__}",
            )
        except EvalError as exc:
            check("completion-lock-config", False, str(exc))
    else:
        check("completion-lock-config", False, "config/completion-lock.json missing")

    frozen = root / "docs" / "SADDLE_PROTOCOL_v0.1.md"
    historical = root / "docs" / "SADDLE_PROTOCOL_v0.1_DRAFT.md"
    check("frozen-protocol-present", frozen.is_file(), str(frozen.relative_to(root)))
    check("historical-draft-superseded", historical.is_file() and "SUPERSEDED" in historical.read_text(encoding="utf-8"), str(historical.relative_to(root)))

    source_path = root / "config" / "source-repos.json"
    snapshot: list[dict[str, Any]] = []
    if source_path.is_file():
        try:
            source = strict_loads(source_path.read_text(encoding="utf-8"))
            repos = source.get("repositories", []) if isinstance(source, dict) else []
            valid = isinstance(repos, list) and bool(repos)
            for item in repos if isinstance(repos, list) else []:
                if not isinstance(item, dict) or not isinstance(item.get("name"), str) or SHA_RE.fullmatch(str(item.get("observed_main", ""))) is None:
                    valid = False
                    continue
                snapshot.append({"name": item["name"], "observed_main": item["observed_main"], "role": item.get("role", "")})
            check("source-registry-machine-readable", valid, "config/source-repos.json")
        except EvalError as exc:
            check("source-registry-machine-readable", False, str(exc))
    else:
        check("source-registry-machine-readable", False, "config/source-repos.json missing")

    overall = "PASS" if checks and all(item["status"] == "PASS" for item in checks) else "FAIL"
    return {"schema_version": "saddle-repo-audit/0.1", "overall": overall, "checks": checks, "source_snapshot": snapshot}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    validate_p = sub.add_parser("validate")
    validate_p.add_argument("input", type=Path)

    aggregate_p = sub.add_parser("aggregate")
    aggregate_p.add_argument("input", type=Path)
    aggregate_p.add_argument("--output", type=Path)

    audit_p = sub.add_parser("audit")
    audit_p.add_argument("--root", type=Path, default=Path("."))
    audit_p.add_argument("--output", type=Path)

    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            records = load_jsonl(args.input)
            print(json.dumps({"status": "PASS", "records": len(records)}, sort_keys=True))
            return 0
        if args.command == "aggregate":
            summary = aggregate(load_jsonl(args.input))
            if args.output:
                write_json(args.output, summary)
            print(json.dumps(summary, sort_keys=True))
            return 0 if summary["overall"] == "PASS" else 1
        if args.command == "audit":
            result = audit_repository(args.root)
            if args.output:
                write_json(args.output, result)
            print(json.dumps(result, sort_keys=True))
            return 0 if result["overall"] == "PASS" else 1
    except EvalError as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, sort_keys=True))
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
