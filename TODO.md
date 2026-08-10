# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

## Authority

This file is an operational projection, not a second source of truth.

Authority order:

1. `DECISION_LOG.md` — explicit human decisions;
2. `PROJECT_STATE.md` — current canonical truth;
3. `EXECUTION_PLAN.md` — strategic gated path;
4. `TODO.md` — current operational queue;
5. `SESSION_HANDOFF.md` — exact resume point;
6. draft analysis/PR material.

If this file conflicts with a higher source, correct this file.

## Operating rules

- Work top-to-bottom.
- Keep at most one implementation item `IN_PROGRESS`.
- `DONE` requires evidence.
- New ideas go to `FUTURE_IDEAS.md` as `PARKED`.
- Broken eval inputs remain reproducible; successful derived repairs do not overwrite them.
- Under DEC-SAD-007, routine scheduled work proceeds without repeated user interruption.
- DEC-SAD-007 does not authorize goal changes, completion-lock removal, hidden permission expansion, weakened evidence/security, or self-declared functional acceptance.

---

## T0 — Durable-memory bootstrap / Phase 0

Status: `DONE`

Evidence:
- `evidence/COLD_START_AUDIT_001.md`;
- merged Saddle PR #1;
- canonical merge commit `b950660c84c6dcad1a093a7aba5ad2d70d472ee4`.

Result:
repository-only zero-memory recovery works; Saddle remains `NOT YET FUNCTIONAL`.

---

## T1 — Preserve six-part test evidence

Status: `DONE IN PHASE-1 CANONICAL SYNC`

Artifacts:
- `evidence/TEST_SESSION_2026-08-10/QUESTIONS.md`;
- `evidence/TEST_SESSION_2026-08-10/ANSWERS_RAW.md`;
- `analysis/SADDLE_TEST_SESSION_2026-08-10.md`;
- evidence index.

Key result:
`AI_WORKER_CAPABILITY` was demonstrated on CASE-001, but `FULL_SADDLE_EXECUTION` remains unproven.

Critical benchmark rule:
do not merge executor-pilot-target PR #5 into `case-001-broken`.

---

## T2 — Preserve new ideas without activating them

Status: `DONE IN PHASE-1 CANONICAL SYNC`

Parked:
- IDEA-SAD-014 human-controlled value/reinvestment flywheel;
- IDEA-SAD-015 bounded self-improvement loop.

Both remain `PARKED` under completion lock.

---

## T3 — Phase 1 ecosystem reconciliation

Status: `DONE IN PHASE-1 CANONICAL SYNC`

Evidence:
- `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`;
- `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md`;
- updated `ECOSYSTEM_MAP.md`;
- updated `SOURCE_REGISTRY.md`;
- ScriptOps PR #6 merged as knowledge reconciliation at `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`.

Canonical classification summary:
- Executor/main is canonical effect-control implementation;
- Executor #51–#57 are draft/research/reusable trust semantics, not current runtime;
- #57 retains trust findings but its global `USER -> EXECUTOR` front-door placement is superseded by Saddle;
- COS #18 supplies reusable Ginseng/decision-lineage semantics but stale global status/placement;
- ScriptOps GitHub access-check is closed; v2 remains recommended but not yet human-selected as runtime base;
- executor-pilot-target is the repeatable lab; broken baselines remain immutable.

---

## T4 — Freeze Saddle Protocol v0.1

Status: `READY / NEXT`

Goal:
provider/model/agent-independent coupling contract.

Required objects:
1. `IntentEnvelope`;
2. `EffectProposal`;
3. `EffectReceipt`;
4. `StateDelta`.

Required work:
- reviewed JSON Schemas;
- canonical serialization/hash/identity rules;
- provenance/source rules;
- provider-independent authority references;
- deterministic schema/invariant tests;
- preserve DEC-SAD-006 responsibility boundary.

Required invariants:
- human intent cannot be replaced by AI interpretation;
- proposal is not permission;
- execution is not proof;
- `FACT / DECISION / HYPOTHESIS` remain distinct;
- `NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER`;
- protocol must not depend on a particular model/provider/agent topology.

Do not build a provider framework, UI, graph DB or agent orchestration.

---

## T5 — Minimal audit + eval foundation

Status: `BLOCKED UNTIL T4`

Build the smallest plain-Python / JSON/JSONL harness needed for:
- schema/state invariant checks;
- ecosystem audit snapshot;
- eval result aggregation;
- model/prompt/version identification;
- success/failure and scope/policy violations;
- cost/tokens/latency/retries/human corrections when available;
- evidence refs.

Initial lanes:
- Saddle/COS cold-start;
- Reconstructor regression;
- Executor policy/security;
- executor-pilot-target CASE-001–003;
- later ScriptOps smoke.

No full observability platform unless measured necessary.

---

## T6 — First real AI worker through Saddle/Executor

Status: `BLOCKED UNTIL T5`

Required path:

```text
pinned task/source/tests
→ thin ModelGateway
→ real AI proposal
→ bounded validation/mutation conversion
→ Executor effect path
→ tests + evidence
```

Requirements:
- no hard-coded CASE solution;
- provider credential outside worker/evidence;
- compare at least two current capable model candidates before selecting one;
- record quality/cost/latency/retries;
- no unrestricted worker write/shell/internet;
- no multi-agent or dynamic routing platform.

CASE-001–003 must start from clean broken baselines.

---

## T7 — Verified intent / human authority boundary

Status: `BLOCKED UNTIL REQUIRED T4–T6 FOUNDATION`

Use Executor #51–#57 research without reviving its old global front-door assumption.

Keep distinct:

```text
human request content
!= AI interpretation
!= verified request origin
!= human confirmation/decision
!= downstream effect authority
```

Target semantics:
- Saddle preserves/binds exact human intent;
- strengthened-A2 trust principle is default Saddle intent-boundary pattern;
- A1 remains valid delegated/enterprise intake;
- Executor consumes/verifies exact effect authority;
- one minimal authority adapter only for the pilot;
- replay/staleness/scope attacks fail closed.

No generalized enterprise IAM/delegation platform.

---

## T8 — Minimal ScriptOps real-domain path

Status: `HUMAN SEMANTIC GATE + BLOCKED ON PRECEDING SADDLE GATES`

Open decision:
select or reject `legacy/scriptops-v2-single.py` as the implementation base.

Current technical recommendation: `YES — reuse v2`.

If selected, repair only the smallest one-case path:

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

Do not add browser helper, direct model automation, GUI, vector DB, semantic graph platform or multi-user scope.

---

## T9 — Functional Saddle acceptance

Status: `BLOCKED UNTIL T4–T8`

Fresh-session proof:

```text
human intent
→ durable intent
→ context recovery
→ AI problem solving
→ EffectProposal
→ authority/effect gate
→ bounded real execution
→ EffectReceipt/evidence
→ human review at required boundary
→ StateDelta
→ second zero-history session resumes
```

Only here, with required evidence and human acceptance, may state become:

`FUNCTIONAL_SADDLE_ACCEPTED`.

---

## T10 — Post-acceptance human direction

Status: `BLOCKED UNTIL T9`

Completion lock does not release automatically.

Human decides whether to harden, broaden domains, increase autonomy, activate a parked idea, add models/tools, pursue the value/reinvestment flywheel or bounded self-improvement research.

---

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

Do not implement without a proven active-gate blocker plus explicit authorized exception:
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
