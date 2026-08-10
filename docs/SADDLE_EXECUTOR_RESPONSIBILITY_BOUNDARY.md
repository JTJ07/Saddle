# SADDLE ↔ EXECUTOR RESPONSIBILITY BOUNDARY

Status: `PHASE 1 DECISION CANDIDATE / USER-ENDORSED / NOT CANONICAL UNTIL MERGED`
Date: 2026-08-10
Scope: ownership of intent, reasoning, consequential effects, and factual verification

## 1. Purpose

This document records the architectural clarification that emerged while reconciling the Executor trust-boundary research with Saddle.

It does not implement a provider, authority adapter, verified-intent protocol, Executor runtime change, or Phase-2 schema.

It exists to prevent a lower-level component from accidentally becoming the owner of a higher-level responsibility.

## 2. Core ownership model

```text
HUMAN
  owns intent
    ↓
SADDLE
  preserves and binds intent
  provenance / context / decisions / continuity
    ↓
INTELLIGENCE
  explores possibilities
  reasons / proposes / critiques / plans
    ↓
EXECUTOR
  governs consequences
  policy / authority / scope / bounded execution
    ↓
WORLD
    ↓
VERIFIER
  establishes facts from evidence
    ↺
SADDLE durable state
```

Canonical wording candidate:

> **HUMAN OWNS INTENT.**
>
> **SADDLE PRESERVES AND BINDS INTENT.**
>
> **INTELLIGENCE PROPOSES HOW.**
>
> **EXECUTOR GOVERNS CONSEQUENCES.**
>
> **VERIFIER ESTABLISHES FACTS.**

Plain-language form:

> Human decides what matters. Saddle protects that meaning. Intelligence discovers how. Executor controls what happens. Verifier proves what happened.

## 3. Saddle is not the semantic owner of human intent

Rejected wording:

```text
SADDLE AUTHORIZES MEANING
```

Reason:

Saddle must not promote its own interpretation into ownership of what the human meant.

Saddle may:

- preserve the verbatim request;
- preserve provenance and request-origin evidence;
- bind interpretations and decisions back to the original request;
- maintain context and decision lineage;
- detect ambiguity or drift;
- request human clarification or confirmation at the correct boundary.

Saddle may not silently convert:

```text
AI INTERPRETATION -> HUMAN INTENT
```

The human remains the highest-order owner of intent.

## 4. New cross-layer invariant

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

Examples:

- AI does not substitute for the human as owner of intent.
- Saddle does not substitute its interpretation for human meaning.
- Executor does not infer effect permission merely from intent.
- Verifier does not create authority by proving that an action occurred.
- An execution receipt does not substitute for prior authority.
- An external trust provider can prove identity/events without becoming the semantic owner of the user's goal.

This complements existing invariants:

```text
HUMAN INTENT != AI INTERPRETATION
REQUEST != EXECUTABLE CONTRACT
MODEL OUTPUT != AUTHORITY
CAPABILITY != PERMISSION
EXECUTION != PROOF
PROPOSAL != CANON
AI RECOMMENDATION != HUMAN DECISION
USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE
THOUGHT / REASONING FREEDOM != EFFECT AUTHORITY
```

## 5. Product front door correction

Historical Executor research treated this as the product-level shape:

```text
USER -> EXECUTOR -> CONTRACT -> WORLD
```

For Saddle-level architecture that is no longer the global product boundary.

Adopted direction candidate:

```text
USER -> SADDLE -> INTELLIGENCE -> EXECUTOR -> WORLD
```

Therefore:

> **SADDLE OWNS THE HUMAN-INTENT INTERACTION BOUNDARY BY DEFAULT.**
>
> **EXECUTOR OWNS THE GOVERNED CONSEQUENTIAL-EFFECT BOUNDARY.**

This does not mean Saddle owns the human goal. The human owns the goal; Saddle owns the responsibility to preserve and bind it faithfully through the system.

## 6. Reinterpretation of Executor PR #51–#57

The research remains valuable. It is not discarded.

Its findings are redistributed across two architectural boundaries.

### 6.1 Saddle intent boundary inherits

- request-origin evidence;
- human/principal identity evidence;
- exact raw-request binding;
- anti-replay / anti-staleness requirements for intent events;
- exact review binding where a human confirms meaning;
- direct-human-action evidence;
- the invariant `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`;
- protection against retroactive request-origin attribution;
- protection against review/signing-surface substitution.

Primary question:

> Did the system preserve and bind the actual human-originated intent without substituting an AI or later system interpretation?

### 6.2 Executor effect boundary inherits

- effect authority;
- policy;
- scope;
- permissions;
- freeze/binding requirements for an executable effect contract;
- sandbox and tool restrictions;
- bounded execution;
- execution evidence and receipts;
- fail-closed behavior when authority is absent, stale, mismatched or replayed.

Primary question:

> Is this exact consequential effect authorized, in scope, and executable under the governing constraints?

## 7. A1 / A2 reinterpretation

The old A1/A2 question was framed around Executor front-door ownership.

At the Saddle level the better question is:

> **WHERE DOES VERIFIED HUMAN INTENT ENTER THE SYSTEM?**

### Default Saddle pattern — strengthened A2 concept retained

```text
HUMAN
  ↓
SADDLE FRONT DOOR
  captures exact raw intent
  ↔ external transaction-specific trust attestation when required
  ↓
VERIFIED / BOUND INTENT
  ↓
INTELLIGENCE
  ↓
EFFECT PROPOSAL
  ↓
EXECUTOR
```

The key strengthened-A2 lesson remains:

ordinary login, local `USER` provenance, or later authentication is not sufficient proof that a specific principal directly originated the exact governed request.

### Enterprise/delegated intake — A1 remains valid

```text
HUMAN
  ↓
AUTHORIZED CORPORATE / EXTERNAL TRUST DOMAIN
  ↓
SADDLE
  ↓
INTELLIGENCE
  ↓
EXECUTOR
```

A1 is therefore treated as a valid explicitly delegated intake pattern, not the default product front door and not a competing Executor product architecture.

### Explicit status

```text
NAIVE A2: REJECTED
STRENGTHENED A2 PRINCIPLE: RETAINED AT SADDLE INTENT BOUNDARY
A1: VALID DELEGATED / ENTERPRISE VARIANT
PROVIDER: NOT SELECTED
IMPLEMENTATION: NOT STARTED
```

## 8. Executor minimal-context design target

This is a design target, not yet a frozen protocol.

Executor should preferably not need the full human conversation, emotional context, business narrative or reasoning trace merely to authorize and execute a consequential effect.

A future minimal input may conceptually resemble:

```json
{
  "effect_proposal": "...",
  "effect_authority": "...",
  "scope": "...",
  "constraints": "...",
  "evidence_requirements": "...",
  "intent_ref": "..."
}
```

`intent_ref` preserves audit linkage without requiring Executor to become the semantic owner of the human goal.

This shape is illustrative only. Phase 2 must define the actual provider-independent contract and tests.

## 9. Phase-1 consequence

Before freezing Saddle Protocol v0.1, Phase 1 reconciliation should record that:

1. `USER -> EXECUTOR` is not the global Saddle front-door model;
2. `USER -> SADDLE -> INTELLIGENCE -> EXECUTOR` is the current responsibility model;
3. Executor #51–#57 findings are reused by the appropriate intent/effect boundaries rather than discarded;
4. strengthened A2 is retained as a Saddle intent-boundary pattern;
5. A1 is retained as an explicit delegated/enterprise intake variant;
6. no provider is selected by this clarification;
7. no new runtime subsystem is authorized by this clarification.

## 10. Follow-on design questions — not yet implementation

After Phase 1 reconciliation, later work may define:

- `SADDLE_VERIFIED_INTENT_BOUNDARY` — how exact human-originated intent is preserved, proven and bound;
- `EXECUTOR_EFFECT_AUTHORITY_BOUNDARY` — how Executor receives and verifies authority for an exact consequential effect.

These should begin as protocol semantics and tests, not as new large platforms.

## 11. Compact architecture law

```text
HUMAN owns WHAT matters.
SADDLE preserves WHAT the human means.
INTELLIGENCE is free to discover HOW.
EXECUTOR governs WHAT may happen.
VERIFIER establishes WHAT actually happened.
```

And across all layers:

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**
