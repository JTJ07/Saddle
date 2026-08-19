# DELEGATING SADDLE WORK TO OPENAI CODEX — HISTORICAL COMPLETION-PHASE GUIDE

Status: `HISTORICAL / SUPERSEDED FOR CURRENT OPERATIONS BY ROOT AGENTS.md`

This document preserves the operating guidance used during Saddle's gated completion phases. It is retained for provenance, not as current startup authority.

Current agent authority and read order are defined by root `AGENTS.md`, current `PROJECT_STATE.md`, `SESSION_HANDOFF.md`, `RESTRICTIONS.md`, and the accepted Human decisions.

## What remains valid historically

The completion-phase guide established useful boundaries that remain compatible with current governance:

- Human owns product goal, normative decisions, high-risk authority and final acceptance;
- coding agents may perform bounded operational engineering inside delegated scope;
- repository state is durable authority; chat memory must not be required;
- agents may inspect, implement minimum deltas, test, debug, prepare branches/PRs and update durable evidence;
- agents must stop on genuine Human authority/semantic boundaries;
- coding agents must not become the hidden product-roadmap owner.

## What is superseded

The old guide assumed:

```text
completion lock ACTIVE
active completion phase/gate exists
advance the first incomplete gate
first work order = Phase 0
```

Those assumptions are no longer current.

Current accepted state is:

```text
FUNCTIONAL_SADDLE_ACCEPTED = true
COMPLETION_LOCK = RELEASED
ACTIVE COMPLETION GATE = NONE
ACTIVE PRODUCT ROADMAP = NONE
```

Therefore a current agent must **not** restart Phase 0 or infer a new product-development queue from this file.

## Current post-acceptance rule

Post-acceptance work is allowed only within an explicit delegated evaluation, maintenance or repository-reconciliation scope. Released completion lock does not itself authorize new capability, autonomy, provider, security weakening, deployment, release, spending or roadmap activation.

Use root `AGENTS.md` for current instructions.
