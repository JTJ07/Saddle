---
project: Saddle
status: PHASE_1_ACCEPTED / PHASE_2_ACTIVE / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phase 0 durable-memory bootstrap is canonical and accepted. Phase 1 ecosystem reconciliation is complete on the current canonical-sync change set. Saddle remains `NOT YET FUNCTIONAL`.

## ACTIVE GATE

`PHASE 2 — FREEZE SADDLE PROTOCOL v0.1`

## WHAT CHANGED

- merged Phase-0 cold-start closure to Saddle `main` (`b950660c...`);
- merged ScriptOps GitHub-side access-check/v2 gap analysis (`33c9d15a...`) without selecting v2 as runtime base;
- preserved six-part Saddle test questions/raw answers/analysis;
- preserved IDEA-SAD-014 and IDEA-SAD-015 as `PARKED` only;
- recorded DEC-SAD-006 responsibility ownership boundary;
- recorded DEC-SAD-007 operational delegation through the existing completion path;
- reconciled Executor #51–#57, older Executor experimental debt, COS #18 and ScriptOps state;
- remapped request-origin/meaning findings to the Saddle intent boundary and consequence authority to Executor;
- updated ecosystem/source registry and operational TODO.

## EVIDENCE

- `evidence/COLD_START_AUDIT_001.md`;
- `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`;
- `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md`;
- `analysis/SADDLE_TEST_SESSION_2026-08-10.md`;
- `evidence/TEST_SESSION_2026-08-10/`;
- `ECOSYSTEM_MAP.md`;
- `SOURCE_REGISTRY.md`.

## HUMAN DECISIONS RECORDED

See `DECISION_LOG.md`, especially:

- DEC-SAD-001 GitHub durable memory;
- DEC-SAD-002 completion lock;
- DEC-SAD-003 universal Saddle direction;
- DEC-SAD-004 intelligence freedom / effect control;
- DEC-SAD-005 reuse before rewrite;
- DEC-SAD-006 responsibility boundary:
  `HUMAN OWNS INTENT / SADDLE PRESERVES AND BINDS INTENT / INTELLIGENCE PROPOSES HOW / EXECUTOR GOVERNS CONSEQUENCES / VERIFIER ESTABLISHES FACTS`;
- DEC-SAD-007 operational delegation: continue the scheduled completion path without repeated user interruption, while preserving reserved semantic/security/acceptance boundaries.

## IDEAS PARKED

- IDEA-SAD-014 human-controlled value/reinvestment flywheel;
- IDEA-SAD-015 bounded self-improvement loop;
- all earlier future ideas remain parked.

## IMPORTANT CLASSIFICATIONS

- Executor `main` is canonical implementation; #51–#57 are draft/research/reusable trust material, not merged runtime.
- Executor #57 trust findings survive; its global `USER -> EXECUTOR` front-door placement is superseded by Saddle.
- strengthened-A2 principle is retained at Saddle intent boundary; naive A2 rejected; A1 valid delegated/enterprise variant; provider unselected.
- COS #18 supplies reusable Ginseng semantics but stale global status/placement; do not activate runtime.
- ScriptOps access-check is canonical; v2 is recommended but not yet human-selected as runtime base.
- executor-pilot-target broken benchmark branches must remain reproducible; do not merge CASE-001 repair into `case-001-broken`.
- direct Codex CASE-001 solve is AI-worker capability evidence, not full Saddle execution.

## BLOCKERS

Current blocker: Saddle Protocol v0.1 is still a draft, not a frozen/tested provider-independent contract.

## ONE NEXT STEP

Implement and deterministically test the four Phase-2 protocol schemas:

1. `IntentEnvelope`;
2. `EffectProposal`;
3. `EffectReceipt`;
4. `StateDelta`.

Do not select provider/model/agent framework/UI/database to solve this gate.

## EXACT FILES / REFS TO OPEN NEXT

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md` — Phase 2
4. `TODO.md` — T4
5. `DECISION_LOG.md`
6. `docs/SADDLE_PROTOCOL_v0.1_DRAFT.md`
7. `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md`
8. `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`
9. `RESTRICTIONS.md`
