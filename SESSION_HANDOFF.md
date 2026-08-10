---
project: Saddle
status: PHASE_5_ACCEPTED / PHASE_6_AWAITING_REAL_WORKFLOW_BASE_DECISION / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phases 0–3 are canonical foundations. Phase-4 AI-worker direction/scaffold is frozen as PASS direction while its live external-model benchmark evidence remains open. Phase 5 strict intent/effect boundary proof has passing local deterministic evidence on this change set. Saddle remains `NOT_YET_FUNCTIONAL`.

## ACTIVE GATE

`PHASE 6 — FIRST REAL USER WORKFLOW / HUMAN BASE-SELECTION DECISION`

## WHAT CHANGED

- recorded `DEC-SAD-008`: Saddle preserves intent integrity; it does not understand/authorize meaning;
- recorded `DEC-SAD-009`: freeze Phase 1–4 foundations and advance to strict Phase 5 while preserving the unexecuted Phase-4 live benchmark evidence requirement;
- added independent `raw_intent_hash` anchor for exact human UTF-8 input;
- added provider-independent `VerifiedIntentBinding`;
- added separate exact `EffectAuthority`;
- added deterministic fail-closed boundary evaluator;
- added 15 adversarial/positive-control tests;
- added Phase-5 eval lane and evidence;
- updated roadmap so real user workflow follows Phase 5 without adding capability layers.

## CONSTITUTIONAL INVARIANT

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Saddle does not infer permission from semantic similarity, AI interpretation, USER labels or model confidence.

## PHASE 5 EVIDENCE

Artifacts:
- `authority/v0.1/verified-intent-binding.schema.json`;
- `authority/v0.1/effect-authority.schema.json`;
- `tools/phase5_boundaries.py`;
- `tests/test_phase5_boundaries.py`;
- `docs/PHASE5_STRICT_BOUNDARIES_v0.1.md`;
- `evidence/PHASE5_STRICT_BOUNDARY_TEST_2026-08-10.md`.

Local deterministic evidence:

```text
python -m compileall -q tools tests
PASS

python -m unittest discover -s tests -p 'test_phase5_boundaries.py' -v
Ran 15 tests
OK
```

Negative cases block for missing authority, goal-expanding interpretation, raw-intent mutation, unverified origin, wrong/mutated effect, action/target mismatch, expiry, deny, replay and wrong intent. Exact active binding + exact active one-use ALLOW authority is the positive control.

## OPEN EVIDENCE / NOT CLAIMED

- no production request-origin/identity provider selected;
- no live Sol/Terra benchmark executed;
- no real-model proposal routed through Executor yet;
- no first real ScriptOps workflow executed;
- no functional Saddle claim.

## BLOCKER / HUMAN SEMANTIC GATE

The next real workflow needs an explicit base selection.

Current technical recommendation remains:

`legacy/scriptops-v2-single.py` = **YES, reuse as Phase-6 base**.

Earlier governance explicitly reserved that base selection to the human; it has not yet been promoted to a decision.

## ONE NEXT STEP

Human selects or rejects `legacy/scriptops-v2-single.py` as the Phase-6 real-workflow implementation base. If selected, implement only the smallest task -> context -> candidate -> validation -> impact -> human approve/reject/revision with why -> accepted hash -> Git commit -> smoke-evidence path.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `EXECUTION_PLAN.md` — Phase 6
3. `TODO.md` — T8
4. `DECISION_LOG.md` — DEC-SAD-008/009
5. `docs/PHASE5_STRICT_BOUNDARIES_v0.1.md`
6. `evidence/PHASE5_STRICT_BOUNDARY_TEST_2026-08-10.md`
7. `litrgratis-pixel/scriptops` main `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`
8. ScriptOps `legacy/scriptops-v2-single.py`
