---
project: Saddle
status: PHASE_1_ACCEPTED / PHASE_2_ACTIVE / NOT_YET_FUNCTIONAL
completion_lock: ACTIVE
state_owner: PROJECT_STATE.md
updated_at: 2026-08-10
---

# PROJECT_STATE — Saddle

## 1. Current product definition

Saddle is the durable control/coupling layer between human intent and arbitrary AI capability.

It preserves and binds the human-owned intent, supplies durable context and decision lineage, keeps consequential effects behind authority boundaries, records evidence/state, and avoids unnecessarily prescribing how the underlying intelligence solves the problem.

Core rules:

> **Maximize usable AI capability; constrain unauthorized effects, not intelligence itself.**

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

Current responsibility model:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

## 2. Current objective

Finish the smallest end-to-end Saddle that proves:

```text
human intent
→ durable/bound intent
→ correct context recovery
→ real AI proposal
→ effect authority boundary
→ bounded execution
→ objective evidence
→ durable StateDelta
→ fresh-session resume
```

The project remains in completion mode. New product development is frozen.

## 3. Current ecosystem checkpoints

Observed / reconciled on 2026-08-10:

- Saddle: Phase-0 closure merge `b950660c84c6dcad1a093a7aba5ad2d70d472ee4` plus current Phase-1 sync branch;
- COS main: `3220310267c3d0ba2184daaf3f2adad259a9cb20`;
- creative-os-project-reconstructor main: `defc7b029097284f94136fec54b75c313ac12f68`;
- ScriptOps main after access-check reconciliation: `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`;
- Executor main: `788443c3ed5b290ac8f1de145a93d02d2dd15317`;
- executor-pilot-target main: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`.

These are observed refs, not permanent implementation pins unless a later protocol explicitly pins one.

## 4. Reconciled component roles

### COS
Reuse memory/source-hierarchy/session-handoff patterns.

COS PR #18 classification:
`REUSABLE GINSENG SEMANTICS + STALE/SUPERSEDED GLOBAL STATUS/PLACEMENT`.

Reuse:
- `FACT / DECISION / HYPOTHESIS`;
- Decision Lineage;
- source/proposer/confidence/status on important relations;
- AI cannot confirm its own hypothesis/relation;
- `ELEMENT -> FUNCTION/CAPABILITY -> EFFECT` reasoning.

Do not activate Ginseng runtime/UI under completion lock.

### Project Reconstructor
Reuse as context-recovery adapter and regression source. Automated cross-model/large-set eval belongs in T5.

### ScriptOps
GitHub-side access check is now canonical. No separate later RC1 build was found in accessible GitHub; local/off-GitHub artifacts remain unknown.

Preserved v2 already has most needed mechanics. Known minimal one-slice gaps:
- clean-tree lifecycle conflict;
- dirty-tree before approval;
- stale accepted hash;
- missing mandatory `why`;
- missing impact report/smoke proof.

Technical recommendation: reuse v2. This remains a recommendation until human base selection.

### Executor
Canonical effect-control implementation remains `Executor/main` at `788443c...`.

Current main strengths:
- request-to-contract formation boundary;
- user-request vs model-interpretation separation;
- policy/source/task/project checks;
- action authorization machinery;
- hardened sandbox;
- evidence/replay controls;
- GP001 controlled path.

Current main gaps:
- GP001 proposal is hard-coded rather than real-AI-generated;
- verified human authority/freeze not implemented.

Executor #51–#57 classification is recorded in `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.

Critical retained trust findings:
- `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`;
- naive A2 rejected;
- exact transaction-specific origin binding, anti-replay/freshness and explicit trust-domain rules;
- approval/authentication do not automatically prove exact request origination.

Global placement correction:
`USER -> EXECUTOR` is superseded as Saddle's front door. Strengthened-A2 principle is retained at the Saddle intent boundary; A1 is a valid delegated/enterprise intake variant.

### executor-pilot-target
Repeatable technical lab for CASE-001–003.

Direct Codex CASE-001 solve demonstrates `AI_WORKER_CAPABILITY`, not full Saddle execution.

Do not merge the repair into `case-001-broken`; broken benchmark inputs remain reproducible.

## 5. Phase results

### Phase 0 — ACCEPTED

Evidence: `evidence/COLD_START_AUDIT_001.md` and merged PR #1.

A zero-history session recovered product definition, memory law, completion lock, evidence boundary and one next step from GitHub alone.

### Phase 1 — ACCEPTED ON THIS CANONICAL SYNC

Evidence:
- `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`;
- `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md`;
- updated `ECOSYSTEM_MAP.md`;
- updated `SOURCE_REGISTRY.md`;
- ScriptOps access-check/gap analysis merged;
- `DEC-SAD-006` responsibility boundary;
- preserved test/evidence package and parked ideas.

Phase-1 DoD result:
a fresh agent can distinguish canonical implementation, active draft research, reusable semantics, superseded placement, experimental evidence and never-merge helpers for the components needed by the next phase.

## 6. Current active gate

`PHASE 2 — FREEZE SADDLE PROTOCOL v0.1`

Required provider/model/agent-independent objects:

1. `IntentEnvelope`;
2. `EffectProposal`;
3. `EffectReceipt`;
4. `StateDelta`.

Required work:
- JSON Schemas;
- deterministic canonical serialization/hash identity;
- provenance/source references;
- provider-independent authority references;
- schema and invariant tests.

Do not select a provider/model/agent framework merely to complete this gate.

## 7. Functional acceptance definition

`FUNCTIONAL_SADDLE_ACCEPTED` requires observable proof that:

1. a human supplies a natural request;
2. verbatim intent is durably preserved with stable identity;
3. project/context recovery needs no hidden chat memory;
4. real AI independently proposes a useful solution;
5. proposal is not authority;
6. exact consequential effect is checked against scope/permission;
7. effect executes in a bounded environment;
8. objective evidence verifies the actual result;
9. required human review/acceptance occurs at the correct boundary;
10. canonical state/handoff is updated;
11. another zero-history session resumes correctly.

## 8. Current blocker

No Phase-1 reconciliation blocker remains on this change set.

The current blocker is absence of a frozen/tested Saddle Protocol v0.1 contract.

## 9. One next step

Implement and deterministically test the four Phase-2 protocol schemas (`IntentEnvelope`, `EffectProposal`, `EffectReceipt`, `StateDelta`) without coupling them to a model provider, agent framework, trust provider or UI.
