# SADDLE AUDIT + EVAL FOUNDATION v0.1

Status: `PHASE 3 MINIMUM FOUNDATION`

Purpose: make later Saddle progress measurable with plain files and deterministic code before introducing any observability platform.

## 1. Eval record

Schema: `eval/v0.1/eval-result.schema.json`.

Each run records:

- `run_id` — content-addressed eval record identity;
- lane and case;
- subject/source under test;
- result: `PASS / FAIL / BLOCKED / ERROR`;
- model/provider/version when a model is actually used, otherwise `null`;
- prompt version when relevant;
- latency/tokens/cost/retries/human corrections when measured;
- explicit scope and policy violations;
- evidence refs;
- timestamps and notes.

Unknown/unmeasured metrics remain `null`; they must not be fabricated.

## 2. Fail-closed aggregation

`tools/eval_harness.py aggregate` cannot silently turn missing/bad results into PASS.

Rules:

- zero records → `BLOCKED`;
- any `ERROR` → overall `ERROR`;
- otherwise any `FAIL` → overall `FAIL`;
- otherwise any `BLOCKED` → overall `BLOCKED`;
- only all-PASS → overall `PASS`;
- any non-empty `scope_violations` or `policy_violations` forces that record's effective result to `FAIL`, even if its declared task result says `PASS`.

## 3. Repository audit

`tools/eval_harness.py audit --root .` checks the minimum continuity/control invariants:

- required root state/governance files exist;
- `PROJECT_STATE.md` and `SESSION_HANDOFF.md` agree on active phase;
- completion lock remains active before functional acceptance;
- exactly one next-step section exists in state and handoff;
- exactly one `READY / NEXT` item exists in TODO;
- frozen Protocol v0.1 exists;
- historical protocol draft is marked superseded;
- `config/source-repos.json` is machine-readable and contains valid observed commit SHAs.

The audit output also includes a machine-readable source snapshot.

This is a local repository-state audit. It does not claim that observed remote SHAs are still current; live GitHub must be rechecked before using a source ref for implementation.

## 4. Initial lane registry

`config/eval-lanes.json` currently registers:

- `saddle-cold-start`;
- `reconstructor-regression`;
- `executor-policy-security`;
- `pilot-case-001`;
- `pilot-case-002`;
- `pilot-case-003`;
- `scriptops-smoke` (deferred until T8).

The lane registry names where evidence belongs. It does not itself run remote repositories.

## 5. CLI

Validate a JSONL result set:

```text
python tools/eval_harness.py validate path/to/results.jsonl
```

Aggregate:

```text
python tools/eval_harness.py aggregate path/to/results.jsonl --output evidence/summary.json
```

Audit the local Saddle checkout:

```text
python tools/eval_harness.py audit --root . --output evidence/repo-audit.json
```

Exit behavior:

- `0` only for PASS;
- `1` for valid but non-PASS aggregate/audit (`FAIL` or `BLOCKED`);
- `2` for malformed/invalid evidence.

## 6. Evidence discipline

A historical result may be encoded into the harness only with the metrics that actually exist. Missing latency/tokens/cost remain null.

A task-success PASS with a scope or policy violation is not a Saddle PASS.

Evidence refs must be non-empty.

No dashboard/database is required for v0.1.

## 7. Explicit non-goals

Phase 3 does not add:

- Langfuse or another observability platform;
- LangGraph/agent orchestration;
- a database;
- automatic remote GitHub crawling;
- provider selection;
- a model worker;
- a trust/authority provider.

The foundation exists only to make the next gates objectively measurable.
