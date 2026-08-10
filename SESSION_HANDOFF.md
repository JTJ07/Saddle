---
project: Saddle
status: PHASE_3_ACCEPTED / PHASE_4_ACTIVE / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phases 0–3 have recorded evidence on the current change set. Saddle remains `NOT YET FUNCTIONAL`.

## ACTIVE GATE

`PHASE 4 — FIRST REAL AI WORKER`

## WHAT CHANGED

- added `eval/v0.1/eval-result.schema.json`;
- added `config/eval-lanes.json` for cold-start, Reconstructor, Executor, pilot CASE-001–003 and later ScriptOps;
- added stdlib `tools/eval_harness.py` with validate / aggregate / audit commands;
- aggregation is fail-closed: zero results => BLOCKED; scope/policy violations => effective FAIL; FAIL/ERROR cannot be hidden by PASS records;
- repository audit checks phase/state agreement, completion lock, one-next-step discipline, frozen protocol and machine-readable source SHAs;
- refreshed ScriptOps observed main in `config/source-repos.json`;
- encoded one historical cold-start baseline smoke without inventing missing metrics.

## EVIDENCE

- `docs/EVAL_FOUNDATION_v0.1.md`;
- `evidence/PHASE3_AUDIT_EVAL_TEST_2026-08-10.md`;
- `eval/examples/phase3-smoke.jsonl`;
- `evidence/PHASE3_SMOKE_SUMMARY.json`;
- Phase-3 tests: 12/12 PASS;
- combined Phase-2+3 tests: 26/26 PASS;
- synthetic scope-violation aggregate: overall FAIL, exit code 1.

No GitHub CI result is claimed for Phase 3.

## BOUNDARIES PRESERVED

- completion lock ACTIVE;
- no model/provider selected;
- no observability platform/database/dashboard added;
- no remote result is inferred from local evidence;
- missing latency/token/cost fields remain `null`, never invented.

## BLOCKERS

Current blocker: no real model-backed worker path exists yet.

## ONE NEXT STEP

Verify current official model/API options, define the thinnest ModelGateway needed only for CASE-001–003, and determine whether the available control plane has an authorized credential path that keeps provider secrets outside worker prompts/sandbox/evidence.

## EXACT FILES / REFS TO OPEN NEXT

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md` — Phase 4
4. `TODO.md` — T6
5. `docs/SADDLE_PROTOCOL_v0.1.md`
6. `docs/EVAL_FOUNDATION_v0.1.md`
7. `tools/eval_harness.py`
8. `litrgratis-pixel/Executor` main
9. `litrgratis-pixel/executor-pilot-target` CASE-001–003
