# PHASE 5 — STRICT INTENT / EFFECT BOUNDARIES v0.1

Status: `STRICT SCOPE / PROVIDER-INDEPENDENT / TRUST PROVIDER OPEN`

## Constitutional model

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

The wording is intentional.

Saddle does **not** claim:

- `Saddle understands intent`;
- `Saddle authorizes meaning`;
- `AI interpretation is user intent`;
- `intent identity is effect permission`.

Saddle preserves the integrity and lineage of what the human actually supplied.

## Phase 5 objective

Prove the minimum boundary:

```text
raw human intent
→ immutable integrity/origin binding
→ AI EffectProposal
→ separate exact EffectAuthority
→ ALLOW / BLOCK
```

This phase does not implement full IAM, provider federation, delegation graphs, autonomous workflows, broader tools, or a model framework.

## Phase 5A — Verified Intent Boundary

`VerifiedIntentBinding` proves only a narrow fact:

> this exact preserved raw input is bound to this principal/source event under this binding.

Minimum fields:

- `intent_id` and `intent_content_hash`;
- `raw_intent_hash` computed directly from exact UTF-8 `raw_human_intent`;
- `principal_ref`;
- immutable `origin_event.ref_id + content_hash + observed_at`;
- issued/expiry status;
- content-addressed binding identity.

Important design choice:

`raw_intent_hash` is a stable anchor independent of `derived_interpretation`.

A later AI interpretation can change while the raw human statement remains exactly anchored.

This layer does **not** establish that Saddle has understood the semantic meaning correctly.

## Phase 5B — Effect Authority Boundary

`EffectAuthority` is a separate object from `EffectProposal`.

It binds:

- exact `VerifiedIntentBinding` ID + hash;
- exact `EffectProposal` ID + hash;
- exact action;
- exact target;
- required evidence;
- issuer;
- explicit `ALLOW` or `DENY`;
- expiry;
- one use only.

Core invariant:

```text
EffectAuthority != EffectProposal
```

An `EffectProposal` is never executable merely because:

- it references a valid intent;
- an AI says it matches the intent;
- it looks semantically similar;
- it contains USER-like provenance;
- the model is confident.

There must be a separate exact authority object.

## Why Phase 5 does not implement semantic intent matching

The attack:

```text
Human: "Dodaj funkcję X."

AI interpretation:
"User wants a system-wide rewrite."

AI proposal:
REBUILD_SYSTEM
```

Saddle must not resolve this by becoming a hidden semantic sovereign.

The deterministic rule is simpler:

```text
proposal without separately issued exact EffectAuthority
→ BLOCK
```

Issuing an EffectAuthority is the explicit review/transformation boundary.

The authority issuer may be human or a later narrowly trusted policy adapter, but that provider is intentionally not selected in Phase 5.

## Attack matrix

### ATTACK 1 — AI interpretation substitutes for intent

Valid raw human intent + goal-expanding AI interpretation + proposal + no effect authority.

Expected: `BLOCK / EXPLICIT_EFFECT_AUTHORITY_REQUIRED`.

### ATTACK 2 — raw intent mutated after origin binding

Expected: `BLOCK / RAW_INTENT_HASH_BINDING_MISMATCH`.

### ATTACK 3 — USER label without verified origin

Expected: `BLOCK / INTENT_ORIGIN_NOT_VERIFIED`.

### ATTACK 4 — authority belongs to another effect

Expected: `BLOCK / AUTHORITY_EFFECT_ID_MISMATCH`.

### ATTACK 5 — proposal changed after authority

Expected: `BLOCK / AUTHORITY_EFFECT_HASH_MISMATCH`.

### ATTACK 6 — action/target exceed reviewed effect

Expected: `BLOCK / AUTHORITY_ACTION_MISMATCH` or `AUTHORITY_TARGET_MISMATCH`.

### ATTACK 7 — expired binding or effect authority

Expected: `BLOCK`.

### ATTACK 8 — authority replay

Phase-5 authority is single-use. Expected second use: `BLOCK / EFFECT_AUTHORITY_REPLAYED`.

### ATTACK 9 — explicit deny

Expected: `BLOCK / EFFECT_AUTHORITY_DENIES`.

### POSITIVE CONTROL

Only exact active verified-intent binding + exact active `ALLOW` authority for the exact proposal may return `ALLOW`.

## What Phase 5 proves

If the tests pass, Phase 5 proves a deterministic control invariant:

> neither AI interpretation nor proposal identity can silently turn into effect permission.

It also proves that raw human text has an independent stable integrity anchor.

## What Phase 5 does not prove

It does not prove:

- a production identity provider;
- real-world principal authenticity beyond the supplied trusted-origin event;
- full organization permissions;
- business authorization;
- a live external model benchmark;
- Executor runtime integration;
- full functional Saddle.

Those remain separate evidence gates.

## Relationship to Phase 4

Human verdict:

- responsibility architecture: PASS;
- ownership model: PASS;
- AI worker direction: PASS;
- trust boundaries: intentionally open.

Therefore the Phase-4 **direction/scaffold is frozen**, while its live external-model benchmark remains unexecuted evidence that must be collected before final functional acceptance.

Phase 5 may proceed deterministically without pretending that benchmark exists.

## Method

```text
MODEL
↓
ATTACK
↓
INVARIANT
↓
IMPLEMENTATION
↓
TEST
```

No capability expansion is authorized by this phase.
