# Saddle

Status: `PHASE 3 / AUDIT + EVAL FOUNDATION / NOT YET FUNCTIONAL`

Saddle is a durable control/coupling layer between **human intent** and **arbitrarily capable AI**.

Its job is not to prescribe how intelligence should think. It preserves and binds human-owned intent, supplies durable context, keeps consequential effects behind authority boundaries, records evidence/state, and lets a fresh session resume from GitHub alone.

## Prime memory law

> Any AI session may end without warning and its conversational memory may be lost forever.

Therefore GitHub is durable memory. A session is never the only owner of a decision, plan, blocker, result or next step.

## Completion lock

Until first functional end-to-end acceptance:

- do not develop new product directions;
- do not broaden scope;
- do not add frameworks because they are interesting;
- park every non-required new idea in `FUTURE_IDEAS.md`;
- finish the current gated path first.

## Read order for every new session

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md`
4. `TODO.md`
5. `RESTRICTIONS.md`
6. `SESSION_HANDOFF.md`
7. `DECISION_LOG.md`
8. `ECOSYSTEM_MAP.md`
9. `SOURCE_REGISTRY.md`
10. `FUTURE_IDEAS.md` only when needed for parking/reactivation checks

## Responsibility law

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

Core capability rule:

> **Do not constrain intelligence unnecessarily. Constrain unauthorized effects.**

## Frozen Saddle Protocol v0.1

Phase 2 established a provider/model/agent-independent four-object contract:

```text
IntentEnvelope
→ EffectProposal
→ EffectReceipt
→ StateDelta
```

Normative description: `docs/SADDLE_PROTOCOL_v0.1.md`.

Schemas: `protocol/v0.1/`.

Deterministic utilities/tests:
- `tools/protocol_v01.py`
- `tests/test_protocol_v01.py`

Phase-2 evidence: compileall PASS, 14 tests OK. This proves protocol mechanics only, not a functional Saddle.

## Current gate

Phase 3 builds the smallest stdlib Python + JSON/JSONL audit/eval foundation required to measure later work without adding a full observability platform.

Target lanes:
- Saddle/COS cold-start;
- Reconstructor regression;
- Executor policy/security;
- executor-pilot-target CASE-001–003;
- later ScriptOps smoke.

## Functional Saddle definition

Saddle is **not functional** merely because schemas, documents or components exist.

Functional acceptance still requires:

```text
human request
→ durable intent
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded execution
→ observable evidence
→ required human review
→ durable StateDelta/handoff
→ brand-new zero-history session resumes correctly
```

Until that passes with required human acceptance, status remains `NOT YET FUNCTIONAL`.
