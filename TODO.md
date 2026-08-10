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

This file is only the operational projection. Higher-authority state wins.

## Operating rules

- Work top-to-bottom.
- Keep at most one implementation item `IN_PROGRESS`.
- `DONE` requires observable evidence.
- New ideas go to `FUTURE_IDEAS.md` as `PARKED`.
- Broken eval inputs remain reproducible.
- DEC-SAD-007 permits routine scheduled execution without repeated interruption, but not goal/lock/security/authority expansion or self-declared functional acceptance.

---

## T0 — Durable-memory bootstrap
Status: `DONE`
Evidence: `evidence/COLD_START_AUDIT_001.md`, merged PR #1 / `b950660c...`.

## T1 — Preserve six-part test evidence
Status: `DONE`
Evidence: `evidence/TEST_SESSION_2026-08-10/` + `analysis/SADDLE_TEST_SESSION_2026-08-10.md`.

## T2 — Preserve new ideas without activation
Status: `DONE`
IDEA-SAD-014 and IDEA-SAD-015 remain `PARKED`.

## T3 — Phase 1 ecosystem reconciliation
Status: `DONE`
Evidence: `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`, responsibility boundary, ecosystem/source map, canonical merge `2e0bd347...`.

---

## T4 — Freeze Saddle Protocol v0.1
Status: `DONE ON CURRENT PHASE-2 CHANGE SET`

Artifacts:
- `docs/SADDLE_PROTOCOL_v0.1.md`;
- `protocol/v0.1/common.schema.json`;
- `protocol/v0.1/intent-envelope.schema.json`;
- `protocol/v0.1/effect-proposal.schema.json`;
- `protocol/v0.1/effect-receipt.schema.json`;
- `protocol/v0.1/state-delta.schema.json`;
- `tools/protocol_v01.py`;
- `tests/test_protocol_v01.py`.

Evidence:
- compileall PASS;
- 14/14 unittest PASS;
- `evidence/PHASE2_PROTOCOL_V01_TEST_2026-08-10.md`.

Key guarantees:
- content-addressed immutable intent/effect/receipt/delta identities;
- raw human intent mutation invalidates identity;
- proposal cannot contain effect authority;
- receipt authority binds exact proposal ID+hash;
- FACT/DECISION/HYPOTHESIS separate;
- DECISION human-owned;
- project status change requires a bound human decision;
- provider/model/framework independent.

---

## T5 — Minimal audit + eval foundation
Status: `READY / NEXT`

Implement stdlib-only unless measured insufficient:

1. state/handoff invariant audit;
2. machine-readable eval result schema/record;
3. JSONL writer/reader;
4. fail-closed aggregate summary;
5. case/model/prompt/version fields;
6. result + scope/policy violations;
7. tokens/cost/latency/retries/human corrections when available;
8. evidence refs;
9. initial lane registry:
   - Saddle/COS cold-start;
   - Reconstructor regression;
   - Executor policy/security;
   - executor-pilot-target CASE-001–003;
   - later ScriptOps smoke.

Do not add Langfuse/LangGraph/database/dashboard unless plain records become a measured blocker.

---

## T6 — First real AI worker through Saddle/Executor
Status: `BLOCKED UNTIL T5`

Required path:

```text
pinned task/source/tests
→ thin ModelGateway
→ real AI proposal
→ bounded proposal validation
→ Executor effect path
→ tests + evidence
```

Requirements:
- no hard-coded solution;
- credentials outside worker/evidence;
- benchmark at least two current capable model candidates before production selection;
- record quality/cost/latency/retries;
- no unrestricted write/shell/internet;
- no multi-agent or dynamic routing platform;
- CASE-001–003 start from clean broken baselines.

---

## T7 — Verified intent / effect authority boundary
Status: `BLOCKED UNTIL REQUIRED T4–T6 FOUNDATION`

Keep distinct:

```text
human request content
!= AI interpretation
!= verified request origin
!= human confirmation/decision
!= downstream effect authority
```

Use Executor #51–#57 findings under the Saddle responsibility model:
- strengthened-A2 principle at default Saddle intent boundary;
- A1 valid delegated/enterprise intake;
- one minimal authority adapter only for the pilot;
- replay/staleness/scope attacks fail closed;
- no generalized IAM/delegation platform.

---

## T8 — Minimal ScriptOps real-domain path
Status: `HUMAN SEMANTIC GATE + BLOCKED ON PRECEDING SADDLE GATES`

Open decision: select/reject `legacy/scriptops-v2-single.py` as implementation base.
Current technical recommendation: `YES — reuse v2`.

If selected, repair only:

```text
task
→ context
→ candidate
→ validation
→ impact report
→ human approve/reject/revision with why
→ correct accepted hash
→ Git commit
→ smoke evidence
```

No browser helper, direct model automation, GUI, vector DB, graph platform or multi-user expansion.

---

## T9 — Functional Saddle acceptance
Status: `BLOCKED UNTIL T4–T8`

Required fresh-session proof:

```text
human intent
→ durable IntentEnvelope
→ context recovery
→ AI problem solving
→ EffectProposal
→ authority/effect gate
→ bounded real execution
→ EffectReceipt/evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

Only with the required evidence and human acceptance may state become `FUNCTIONAL_SADDLE_ACCEPTED`.

---

## T10 — Post-acceptance human direction
Status: `BLOCKED UNTIL T9`

Completion lock does not release automatically. Human decides whether to harden, broaden, increase autonomy, activate parked ideas, pursue value/reinvestment or bounded self-improvement.

---

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

Do not implement without a proven current-gate blocker plus authorized exception:

- multi-agent/swarm runtime;
- Company Loop runtime;
- full Ginseng runtime/graph/UI;
- vector DB/general RAG;
- browser/computer-use automation;
- broad MCP marketplace;
- dynamic provider routing;
- hidden persistent agent-memory service;
- dashboard/control center;
- self-hosted model platform;
- generalized enterprise IAM;
- autonomous resource acquisition;
- self-preservation objective;
- autonomous self-modification outside bounded eval/sandbox/adoption gates.
