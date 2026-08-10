# Saddle

Status: `PHASE 4 / FIRST REAL AI WORKER / NOT YET FUNCTIONAL`

Saddle is a durable control/coupling layer between **human intent** and **arbitrarily capable AI**.

## Core laws

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

> **Do not constrain intelligence unnecessarily. Constrain unauthorized effects.**

GitHub is durable project memory. Completion lock remains active until the first full functional acceptance.

## Read order

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md`
4. `TODO.md`
5. `RESTRICTIONS.md`
6. `SESSION_HANDOFF.md`
7. `DECISION_LOG.md`
8. `ECOSYSTEM_MAP.md`
9. `SOURCE_REGISTRY.md`

## Completed foundations

### Phase 0 — durable memory
Repository-only cold start passed.

### Phase 1 — reconciliation
Executor/COS/ScriptOps/pilot material classified and responsibility boundary frozen.

### Phase 2 — Protocol v0.1
Frozen provider-independent:

`IntentEnvelope → EffectProposal → EffectReceipt → StateDelta`.

Schemas: `protocol/v0.1/`.
Protocol evidence: 14 tests PASS.

### Phase 3 — audit/eval foundation
Plain JSON/JSONL + stdlib harness:

- fail-closed eval records and aggregation;
- state/handoff continuity audit;
- lane registry for cold-start, Reconstructor, Executor, pilot CASE-001–003 and later ScriptOps;
- measured fields for model/prompt/result/violations/tokens/cost/latency/retries/human corrections/evidence.

Phase-3 tests: 12 PASS; combined Phase-2+3 regression: 26 PASS.

## Current gate — Phase 4

Build the first **real** model-generated worker path:

```text
pinned task/source/tests
→ thin ModelGateway
→ real AI proposal
→ bounded validation
→ Executor effect path
→ tests + eval evidence
```

Before model selection, verify current official information and benchmark at least two sensible candidates on the same immutable CASE-001–003 inputs.

No dynamic routing platform, multi-agent system, unrestricted worker shell/write/network, or provider framework.

## Functional acceptance

Saddle is still **NOT YET FUNCTIONAL**. Functional acceptance requires the full human-intent → real AI → authority → bounded effect → evidence → durable StateDelta → zero-history resume loop plus required human acceptance.
