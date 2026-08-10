# PHASE 3 — AUDIT + EVAL FOUNDATION TEST EVIDENCE

Date: 2026-08-10
Status: `LOCAL DETERMINISTIC EVIDENCE / NO GITHUB CI CLAIM`
Branch: `agent/phase3-audit-eval-foundation`

## Unit/compile evidence

```text
python -m compileall -q tools tests
PASS
```

```text
python -m unittest discover -s tests -v
```

New Phase-3 harness tests:

```text
Ran 12 tests
OK
```

The repository also retains the 14 Protocol-v0.1 tests from Phase 2; this evidence entry specifically records the Phase-3 harness test slice run during implementation.

## Phase-3 harness behaviors tested

- valid eval record accepted;
- content-addressed `run_id` detects mutation;
- empty aggregation is `BLOCKED`, never PASS;
- all-PASS aggregation is PASS;
- one FAIL cannot be hidden by PASS records;
- scope violation forces effective FAIL;
- policy violation forces effective FAIL;
- unknown eval fields are rejected;
- good repository continuity fixture audits PASS;
- active-phase mismatch audits FAIL;
- multiple `READY / NEXT` items audit FAIL;
- missing completion lock audits FAIL.

## CLI smoke — historical cold-start baseline

Input: `eval/examples/phase3-smoke.jsonl`.

Validation command:

```text
python tools/eval_harness.py validate eval/examples/phase3-smoke.jsonl
```

Observed output:

```json
{"records": 1, "status": "PASS"}
```

Aggregation command:

```text
python tools/eval_harness.py aggregate eval/examples/phase3-smoke.jsonl --output evidence/PHASE3_SMOKE_SUMMARY.json
```

Observed summary:

```json
{
  "overall": "PASS",
  "total": 1,
  "counts": {"PASS": 1, "FAIL": 0, "BLOCKED": 0, "ERROR": 0}
}
```

The encoded cold-start record is historical evidence. Latency/tokens/cost were not measured in that original audit and remain `null`; no metrics were invented.

## Fail-closed CLI smoke

A synthetic copy of the PASS record was given one scope violation while retaining a declared task result of PASS.

Aggregation returned:

```text
exit code: 1
overall: FAIL
reason contains: SCOPE_VIOLATION
```

This synthetic negative file is not committed as project evidence because it is a test input, not an observed project event.

## What Phase 3 proves

The project now has a minimal plain-file mechanism to:

- record later model/eval results;
- preserve missing metrics as unknown rather than inventing them;
- aggregate results fail-closed;
- surface scope/policy violations independently of task success;
- audit basic Saddle continuity/governance state;
- maintain a named lane registry for later evidence.

## What Phase 3 does not prove

- real model performance on CASE-001–003;
- model/provider selection;
- ModelGateway implementation;
- real Executor integration;
- verified intent/effect authority;
- ScriptOps real-domain E2E;
- functional Saddle acceptance.
