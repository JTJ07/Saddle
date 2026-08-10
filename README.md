# Saddle

Status: `PHASE 2 / PROTOCOL FREEZE / NOT YET FUNCTIONAL`

Saddle is a durable control/coupling layer between **human intent** and **arbitrarily capable AI**.

Its job is not to prescribe how intelligence should think. Its job is to preserve and bind the human-owned intent, provide the right durable context, keep consequential effects behind authority boundaries, observe what actually happened, and preserve enough state that work can resume after any session loss.

## Prime memory law

> Any AI session may end without warning and its conversational memory may be lost forever.

Therefore:

1. GitHub is the durable memory of Saddle.
2. A session is never the only owner of a decision, plan, blocker, result, or next step.
3. Before material work is considered complete, durable state must be written to the repository.
4. A fresh agent with no chat history must be able to resume by reading this repository only.

## Current completion lock

Until Saddle passes its first functional end-to-end acceptance test:

- **do not develop new product ideas**;
- **do not broaden scope**;
- **do not install new frameworks because they are interesting**;
- **do not build multi-agent orchestration, dashboards, graph platforms, vector databases, browser automation, or general MCP marketplaces**;
- every new idea is recorded in `FUTURE_IDEAS.md` and immediately parked.

The current goal is **completion, not expansion**.

## Read order for every new session or agent

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md`
4. `TODO.md` — current operational projection
5. `RESTRICTIONS.md`
6. `SESSION_HANDOFF.md`
7. `DECISION_LOG.md`
8. `ECOSYSTEM_MAP.md`
9. `SOURCE_REGISTRY.md`
10. `FUTURE_IDEAS.md` only when recording/checking a parked idea

`EXECUTION_PLAN.md` is the strategic gated path. `TODO.md` never overrides a higher-authority decision or state.

Then read only the sources required by the active gate.

## Responsibility law

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

Across layers:

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

This means, among other things:

- AI interpretation is not human intent;
- Saddle does not authorize the meaning of a human request;
- intent does not itself authorize an effect;
- Executor does not become the semantic owner of human goals;
- evidence/receipt does not create missing authority.

## Product thesis

Saddle should behave like a universal saddle/coupling layer. The underlying capability can be a model, coding agent, future AI system or something not yet invented. Saddle should not force that intelligence into today's prompt/agent/workflow conventions.

```text
HUMAN
  ↓
SADDLE
intent / provenance / context / decisions / state
  ↓
ARBITRARY INTELLIGENCE
reasoning / planning / alternatives / proposals
  ↓
EFFECT PROPOSAL
  ↓
EXECUTOR / EFFECT ADAPTER
policy / authority / scope / bounded execution
  ↓
REAL EFFECT
  ↓
VERIFIER / EVIDENCE
  ↓
STATE DELTA → SADDLE
```

Core rule:

> **Do not constrain intelligence unnecessarily. Constrain unauthorized effects.**

## Existing ecosystem we reuse

Saddle is not a rewrite of the existing repositories.

- `COS` → reusable project/portfolio memory patterns and Ginseng decision-intelligence semantics.
- `creative-os-project-reconstructor` → recovery of project meaning/state from fragmented history.
- `scriptops` → strongest first real-domain candidate; GitHub-side access check is complete, v2 reuse is recommended but not yet human-selected as runtime base.
- `Executor` → governed consequential-effect engine: policy, scope, authorization, sandbox, execution, evidence.
- `executor-pilot-target` → immutable/repeatable technical lab for AI-worker and Executor evaluation.

See `ECOSYSTEM_MAP.md` and `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.

## Functional Saddle definition

Saddle is **not functional** merely because schemas, prompts, documents or components exist.

The first functional acceptance requires a fresh-session run proving:

```text
human request
→ durable intent identity
→ correct context recovery
→ AI independently proposes a useful solution
→ proposal is not authority
→ exact consequential effect is checked against authority
→ bounded execution
→ observable evidence
→ required human review/acceptance
→ durable StateDelta/handoff
→ a brand-new session resumes without chat history
```

Until this passes, status remains `NOT YET FUNCTIONAL`.
