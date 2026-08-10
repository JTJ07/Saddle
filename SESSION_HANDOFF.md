---
project: Saddle
status: PHASE_2_ACCEPTED / PHASE_3_ACTIVE / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phase 0 durable memory, Phase 1 reconciliation and Phase 2 protocol freeze have passing recorded evidence on the current change set. Saddle remains `NOT YET FUNCTIONAL`.

## ACTIVE GATE

`PHASE 3 — AUDIT + EVAL FOUNDATION`

## WHAT CHANGED

- froze Saddle Protocol v0.1 as four provider/model/agent-independent JSON Schemas;
- defined content-addressed IDs using SHA-256 over a restricted RFC-8785/JCS canonical JSON profile;
- added provider-independent source/evidence/authority refs;
- added stdlib-only canonicalizer/schema-subset validator/cross-object binding validator;
- made `EffectProposal` structurally unable to carry executable authority;
- made `EffectReceipt` require active `EFFECT_PERMISSION` bound to exact proposal ID+hash;
- enforced HUMAN ownership for StateDelta decisions and decision binding for project-status changes;
- marked the original illustrative protocol draft superseded.

## EVIDENCE

- `docs/SADDLE_PROTOCOL_v0.1.md`;
- `protocol/v0.1/`;
- `tools/protocol_v01.py`;
- `tests/test_protocol_v01.py`;
- `evidence/PHASE2_PROTOCOL_V01_TEST_2026-08-10.md`.

Local deterministic test evidence:

```text
python -m compileall -q tools tests
PASS

python -m unittest discover -s tests -v
Ran 14 tests
OK
```

No GitHub CI result is claimed for Phase 2.

## DECISIONS / BOUNDARIES PRESERVED

- HUMAN OWNS INTENT.
- SADDLE PRESERVES AND BINDS INTENT.
- INTELLIGENCE PROPOSES HOW.
- EXECUTOR GOVERNS CONSEQUENCES.
- VERIFIER ESTABLISHES FACTS.
- NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.
- completion lock remains ACTIVE.
- no provider/model/framework/trust technology was selected by Phase 2.

## IDEAS PARKED

All existing future ideas remain parked, including resource/reinvestment and bounded self-improvement.

## BLOCKERS

Current blocker: no unified minimal audit/eval harness yet exists to produce and aggregate machine-readable evidence for later AI-worker and end-to-end runs.

## ONE NEXT STEP

Implement Phase-3 stdlib-only audit/eval foundation with:

- state/handoff invariant audit;
- JSON/JSONL eval-result record;
- fail-closed aggregation;
- model/prompt/version, success/failure, scope/policy violations, tokens/cost/latency/retries/human corrections/evidence refs;
- initial lane registry for cold-start, Reconstructor, Executor, pilot CASE-001–003 and later ScriptOps.

## EXACT FILES TO OPEN NEXT

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md` — Phase 3
4. `TODO.md` — T5
5. `docs/SADDLE_PROTOCOL_v0.1.md`
6. `tools/protocol_v01.py`
7. `RESTRICTIONS.md`
