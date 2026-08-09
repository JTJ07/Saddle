# SADDLE PROTOCOL v0.1 — DRAFT

Status: `DRAFT / NOT FROZEN / NOT AN IMPLEMENTATION CLAIM`

Purpose: define the smallest coupling surface that does not care whether the intelligence underneath is one model, an agent, a swarm, a coding system, or a future architecture.

## 1. IntentEnvelope

Represents what must survive reinterpretation.

Illustrative shape:

```json
{
  "schema_version": "saddle-intent/0.1",
  "intent_id": "...",
  "raw_human_intent": "verbatim input",
  "origin_evidence": {},
  "desired_outcome": "...",
  "success_evidence": [],
  "human_owned_constraints": [],
  "context_refs": [],
  "budget": {},
  "created_at": "..."
}
```

Invariants:

- `raw_human_intent` is never overwritten by AI interpretation;
- AI may attach an interpretation, but it remains derived/provenanced;
- verified origin is distinct from a string labelled USER;
- intent identity must be stable enough for later effect/decision binding.

## 2. EffectProposal

Represents a consequential action proposed by intelligence.

```json
{
  "schema_version": "saddle-effect-proposal/0.1",
  "effect_id": "...",
  "intent_id": "...",
  "action": "...",
  "target": {},
  "expected_effect": "...",
  "required_capabilities": [],
  "risk": {},
  "estimated_cost": {},
  "reason": "...",
  "evidence_plan": []
}
```

Invariants:

- proposal is not permission;
- proposal must bind back to an intent identity;
- authority is evaluated at the effect boundary.

## 3. EffectReceipt

Represents what actually happened.

```json
{
  "schema_version": "saddle-effect-receipt/0.1",
  "effect_id": "...",
  "authorization_ref": "...",
  "status": "...",
  "actual_effect": {},
  "changed_objects": [],
  "evidence_refs": [],
  "tests": [],
  "cost": {},
  "duration": {},
  "observed_at": "..."
}
```

Invariants:

- execution is not proof;
- receipt must link observable evidence;
- ephemeral model confidence is not a substitute for external verification.

## 4. StateDelta

Represents the smallest durable update needed after the effect and review.

```json
{
  "schema_version": "saddle-state-delta/0.1",
  "intent_id": "...",
  "effect_id": "...",
  "facts_added": [],
  "decisions_added": [],
  "hypotheses_added": [],
  "superseded": [],
  "project_status_change": null,
  "blockers": [],
  "next_step": "...",
  "source_refs": []
}
```

Invariants:

- `FACT`, `DECISION`, and `HYPOTHESIS` never silently collapse into one type;
- AI recommendation is not a human decision;
- the delta must be sufficient for a future zero-memory resume but should not copy the whole session.

## 5. What the protocol deliberately does not define

- internal chain of thought;
- planner/coder/critic roles;
- number of models;
- model provider;
- MCP vs native tool calls;
- RAG implementation;
- storage database;
- UI;
- agent framework.

Those are replaceable mechanisms below/around the protocol.
