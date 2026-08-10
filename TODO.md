# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

## Authority
1. `DECISION_LOG.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md`
4. `TODO.md`
5. `SESSION_HANDOFF.md`
6. draft analysis/PR material

Rules: work top-to-bottom; one implementation item at a time; `DONE` needs evidence; park new ideas; keep broken eval inputs reproducible; DEC-SAD-007 permits routine scheduled execution but not goal/lock/security/authority expansion or self-declared functional acceptance.

## T0 — Durable-memory bootstrap
Status: `DONE`
Evidence: cold-start audit + merged `b950660c...`.

## T1 — Preserve six-part test evidence
Status: `DONE`

## T2 — Preserve new ideas without activation
Status: `DONE`
IDEA-SAD-014/015 remain `PARKED`.

## T3 — Ecosystem reconciliation
Status: `DONE`
Evidence: Phase-1 reconciliation + merged `2e0bd347...`.

## T4 — Freeze Saddle Protocol v0.1
Status: `DONE`
Evidence: frozen schemas/validator + 14 tests + merged `819449ba...`.

## T5 — Minimal audit + eval foundation
Status: `DONE ON CURRENT PHASE-3 CHANGE SET`

Artifacts:
- `eval/v0.1/eval-result.schema.json`;
- `config/eval-lanes.json`;
- `tools/eval_harness.py`;
- `tests/test_eval_harness.py`;
- `docs/EVAL_FOUNDATION_v0.1.md`;
- smoke record/summary and Phase-3 evidence.

Evidence:
- 12/12 Phase-3 tests PASS;
- combined Phase-2+3 regression 26/26 PASS;
- empty result set => BLOCKED;
- scope/policy violation => effective FAIL;
- FAIL cannot be hidden by PASS;
- synthetic scope-violation CLI smoke => overall FAIL / exit code 1.

No dashboard/database/observability framework added.

## T6 — First real AI worker through Saddle/Executor
Status: `READY / NEXT`

Required path:

```text
pinned task/source/tests
→ thin ModelGateway
→ real model-generated proposal
→ bounded proposal validation
→ Executor effect path
→ tests + eval evidence
```

Immediate work:
1. verify current official model/API candidates;
2. define only the ModelGateway interface needed for CASE-001–003;
3. determine authorized credential path with secret isolated from worker/evidence;
4. benchmark at least two current candidates on identical cases;
5. choose one first worker only after results;
6. keep CASE inputs immutable;
7. no unrestricted write/shell/internet, no dynamic routing, no multi-agent.

## T7 — Verified intent / effect authority boundary
Status: `BLOCKED UNTIL REQUIRED T6 FOUNDATION`

Keep request content, AI interpretation, verified request origin, human decision and downstream effect authority distinct. Reuse Executor #51–#57 under Saddle ownership model. One minimal authority adapter only; no generalized IAM.

## T8 — Minimal ScriptOps real-domain path
Status: `HUMAN SEMANTIC GATE + BLOCKED ON PRECEDING SADDLE GATES`

Open decision: select/reject `legacy/scriptops-v2-single.py` as implementation base. Current technical recommendation: `YES — reuse v2`.

If selected, repair only: task → context → candidate → validation → impact → human approve/reject/revision with why → accepted hash → Git commit → smoke evidence.

## T9 — Functional Saddle acceptance
Status: `BLOCKED UNTIL T6–T8`

Fresh-session proof: human intent → IntentEnvelope → context recovery → real AI → EffectProposal → authority/effect gate → bounded execution → EffectReceipt/evidence → required human review → StateDelta → second zero-history resume.

Only required evidence + human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## T10 — Post-acceptance human direction
Status: `BLOCKED UNTIL T9`
Completion lock does not release automatically.

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

No multi-agent/swarm runtime, Company Loop, full Ginseng runtime/UI, vector DB/general RAG, browser automation, broad MCP marketplace, dynamic model routing, hidden agent memory, dashboard, self-hosted model platform, generalized enterprise IAM, autonomous resource acquisition, self-preservation objective, or autonomous self-modification outside bounded eval/sandbox/adoption gates.
