# Saddle

Status: `PHASE 1 / ECOSYSTEM RECONCILIATION / NOT YET FUNCTIONAL`

Saddle is a durable control layer between **human intent** and **arbitrarily capable AI**.

Its job is not to prescribe how intelligence should think. Its job is to preserve the human goal, provide the right context, bind consequential effects to authority, observe what actually happened, and keep enough durable state that work can resume after any session loss.

## Prime memory law

> Any AI session may end without warning and its conversational memory may be lost forever.

Therefore:

1. GitHub is the durable memory of Saddle.
2. A session is never the only owner of a decision, plan, blocker, result, or next step.
3. Before a session is considered complete, durable state must be written to the repository.
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
4. `RESTRICTIONS.md`
5. `SESSION_HANDOFF.md`
6. `DECISION_LOG.md`
7. `ECOSYSTEM_MAP.md`
8. `SOURCE_REGISTRY.md`
9. `FUTURE_IDEAS.md` only when recording or checking a parked idea

Then read only the source repositories and documents required by the active gate.

## Product thesis

Saddle should behave like a universal saddle or coupling layer. The underlying capability can be a model, coding agent, swarm, future AI system, or something not yet invented. Saddle should not force that intelligence into today's prompt/agent/workflow conventions.

The durable separation is:

```text
HUMAN INTENT
    ↓
SADDLE
intent / context / authority / feedback / evidence
    ↓
ARBITRARY INTELLIGENCE
    ↓
EFFECT PROPOSAL
    ↓
EXECUTION ADAPTERS / EXECUTOR / TOOLS
    ↓
REAL EFFECT
    ↓
EVIDENCE + STATE DELTA
    ↺
```

Core rule:

> **Do not constrain intelligence unnecessarily. Constrain unauthorized effects.**

## Existing ecosystem we reuse

Saddle is not a rewrite of the existing `litrgratis-pixel` repositories.

- `COS` → canonical high-level state and project memory.
- `creative-os-project-reconstructor` → recovery of project meaning/state from messy historical material.
- `scriptops` → first strong domain candidate for a real human↔AI↔canon workflow.
- `Executor` → controlled effect engine: policy, sandbox, authorization boundaries, execution, evidence.
- `executor-pilot-target` → deterministic laboratory for AI-worker and Executor evaluation.
- Ginseng work in COS PR #18 → reusable decision-intelligence semantics (`FACT / DECISION / HYPOTHESIS`, decision lineage, impact reasoning), not yet a runtime requirement.

See `ECOSYSTEM_MAP.md` and `docs/ECOSYSTEM_AUDIT_2026-08-10.md`.

## Functional Saddle definition

Saddle is **not functional** merely because schemas, prompts, documents, or components exist.

The first functional acceptance requires a fresh-session run proving this chain:

```text
human request
→ durable intent identity
→ correct project/context recovery
→ AI independently proposes a useful solution
→ consequential effect is checked against authority
→ effect is executed in a bounded environment
→ observable evidence is produced
→ result is reviewable by the human
→ canonical state/handoff is updated
→ a brand-new session can resume without chat history
```

Until this passes, the status remains `NOT YET FUNCTIONAL`.
