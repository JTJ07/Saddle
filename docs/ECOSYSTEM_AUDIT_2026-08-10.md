# ECOSYSTEM AUDIT — 2026-08-10

## Executive finding

The accessible `litrgratis-pixel` package is already close to a modular Saddle architecture. The highest-value move is not another agent framework; it is reconciling existing state and connecting proven pieces through a minimal intent/effect/evidence protocol.

## What can be used now

### COS
Use its durable-state and continuity principles, not as an AI brain.

### Reconstructor
Use as a universal context-recovery method for unknown/historical projects.

### Executor
Use as the controlled effect engine. Its security/evidence work is the strongest technical asset in the package.

### executor-pilot-target
Use as deterministic AI-worker lab.

### ScriptOps
Use preserved v2 as an RC1 recovery base and potential first real domain. Do not rewrite from zero without evidence.

### Ginseng semantics
Reuse `FACT / DECISION / HYPOTHESIS`, lineage and impact semantics from COS PR #18 without activating a full graph runtime.

## What must be finished

### 1. Durable Saddle memory
A new canonical Saddle repo plus zero-memory cold-start proof.

### 2. Cross-repo reconciliation
Existing documents and drafts contain state drift. Saddle must classify canonical vs draft vs experiment vs history.

### 3. Minimal provider-independent protocol
`IntentEnvelope`, `EffectProposal`, `EffectReceipt`, `StateDelta`.

### 4. Eval foundation
One small harness that aggregates existing component tests/evals and measures AI worker outcomes.

### 5. Real AI proposal generation
Executor GP001 currently validates a real bounded execution path but the repair itself is hard-coded in `tools/run_gp001_real_e2e.py` (`OLD_BLOCK` → `NEW_BLOCK`). The next leverage point is to have a real AI produce the proposal while Executor retains effect control.

### 6. Human/intent authority bridge
Executor main stops intentionally at `AWAITING_VERIFIED_HUMAN_AUTHORIZATION`. PRs #51–#57 contain the active design attack/research for this boundary. The important fact is that a user-labelled input is not independently verified request-origin evidence.

### 7. Real-domain result
A controlled benchmark is necessary but insufficient. A real workflow must prove user value. ScriptOps RC1 is a strong candidate because it naturally combines intent, context, AI candidate generation, validation, human decision, Git and canon.

## ScriptOps audit result

No later RC1 implementation repository was visible among the accessible GitHub repositories.

The preserved v2 is significant, not disposable. It already contains much of the RC1 mechanism: CLI, Git cleanliness, task/context machinery, prompt bundling, token budgets, validation, hashing, staging and approval/decision mechanics.

Likely RC1 deltas if no missing external artifact exists:

- formalize generic RC1 task flow;
- HANDSHAKE v2;
- strengthen validation beyond placeholders;
- impact report;
- approve/reject/revision with mandatory `why`;
- clarify commit semantics;
- full smoke test.

## Executor trust work

Main observed: `788443c...` (merged PR #50 formation boundary).

Active unmerged stack #51–#57 develops:

- verified human authority model;
- decision receipt/evidence model;
- implementation contract;
- external trust boundary;
- technology comparison;
- provider-class research;
- A1 vs strengthened A2 architecture attack.

No provider and no final A1/A2 decision are canonical yet.

## What must be attached/integrated to accelerate work

### Required now
- canonical Saddle repo;
- existing GitHub repos as read/referenced components;
- plain generated ecosystem audit;
- unified eval records;
- one thin model API adapter for first benchmark.

### Helpful after current gates
- CodeQL/default code scanning where appropriate;
- Dependabot for GitHub Actions/supply-chain references;
- OpenTelemetry-compatible trace fields or plain structured evidence;
- MCP only when a real external integration benefits from it.

### Not justified now
- multi-agent runtime;
- graph/vector platforms;
- browser automation;
- generalized routing framework;
- broad observability platform;
- self-hosted LLM stack;
- dashboard;
- autonomous merge/deploy.

## Architecture target

```text
HUMAN
  ↓
SADDLE INTENT
  ↓
ARBITRARY AI CAPABILITY
  ↓
EFFECT PROPOSAL
  ↓
EXECUTOR / OTHER EFFECT ADAPTER
  ↓
REAL EFFECT
  ↓
EVIDENCE
  ↓
STATE DELTA → COS / local truth / decision lineage
```

This architecture deliberately avoids making today's agent/model topology permanent.
