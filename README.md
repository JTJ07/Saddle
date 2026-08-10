# Saddle

Status: `PHASE 5 ACCEPTED / PHASE 6 REAL-WORKFLOW GATE / NOT YET FUNCTIONAL`

Saddle is a durable control/coupling layer between **human intent** and **arbitrarily capable AI**.

## Constitution

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

> **Saddle preserves the integrity of human intent. It does not authorize meaning.**

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

## Frozen foundations

### Phase 0 — durable memory
Repository-only cold start passed.

### Phase 1 — responsibility / ecosystem reconciliation
Ownership architecture is frozen:
human intent, Saddle integrity, AI proposal, Executor consequence authority, Verifier facts.

### Phase 2 — Protocol v0.1
Provider-independent:

`IntentEnvelope → EffectProposal → EffectReceipt → StateDelta`.

### Phase 3 — audit/eval foundation
Plain JSON/JSONL + stdlib fail-closed evidence harness.

### Phase 4 — AI proposal worker direction
Direction/scaffold PASS and frozen:

```text
pinned input
→ proposal-only ModelGateway
→ deterministic validation
→ Executor effect boundary
```

The live external Sol/Terra benchmark remains **unexecuted** and is still required before final functional acceptance. No model result is inferred.

## Phase 5 — strict boundary proof

Accepted on deterministic evidence:

```text
raw human intent
→ VerifiedIntentBinding
→ AI EffectProposal
→ separate exact EffectAuthority
→ ALLOW / BLOCK
```

Key guarantees:

- exact raw human text has an independent `raw_intent_hash` anchor;
- AI interpretation may change without silently replacing that raw anchor;
- USER-like metadata is not verified origin;
- proposal is never permission;
- authority binds exact intent binding + exact proposal ID/hash + exact action/target;
- stale, deny, mismatch and replay cases fail closed;
- one exact active ALLOW control passes.

See:
- `docs/PHASE5_STRICT_BOUNDARIES_v0.1.md`;
- `authority/v0.1/`;
- `evidence/PHASE5_STRICT_BOUNDARY_TEST_2026-08-10.md`.

## Current gate — Phase 6

Move into one controlled **real user workflow** without adding capability layers.

Current technical recommendation: reuse `legacy/scriptops-v2-single.py` as the smallest ScriptOps base. That base selection remains an explicit human semantic decision before runtime changes begin.

No multi-agent, autonomous loops, AI memory service, dynamic routing, tool expansion, browser/computer use, agent framework or generalized IAM.

## Functional acceptance

Saddle is still **NOT YET FUNCTIONAL**.

Final acceptance requires the complete observed chain:

```text
human raw intent
→ integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ verifier evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

The still-open live Phase-4 model benchmark evidence is part of that final proof.
