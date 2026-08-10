# SADDLE PROTOCOL v0.1 — FROZEN CONTRACT

Status: `PHASE 2 CONTRACT / PROVIDER-INDEPENDENT`

Purpose: define the smallest durable coupling surface between human-owned intent, arbitrary intelligence, governed consequential effects and durable evidence/state.

This protocol does **not** define the intelligence's internal reasoning method, number of models/agents, provider, UI, database, MCP topology or orchestration framework.

## 1. Responsibility boundary

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Consequences:

- `raw_human_intent` cannot be replaced by an AI interpretation;
- verified request origin is distinct from a local label such as `USER`;
- `EffectProposal` cannot carry executable authority;
- execution receipt cannot manufacture prior authority;
- `DECISION` records in `StateDelta` require a human decision owner;
- a project status change must bind to a human decision record;
- evidence establishes facts but does not grant permission.

## 2. Protocol objects

### IntentEnvelope
Schema: `protocol/v0.1/intent-envelope.schema.json`

Preserves the exact human input, origin status/evidence, desired outcome, success evidence, human-owned constraints, context refs and optional budget limits.

An optional `derived_interpretation` is explicitly separate and provenance-bearing. It never overwrites `raw_human_intent`.

### EffectProposal
Schema: `protocol/v0.1/effect-proposal.schema.json`

Represents what intelligence proposes to do: action, target, expected effect, capabilities, risk, cost estimate, reason and evidence plan.

There is deliberately no `authorization_ref` field. `additionalProperties: false` makes an attempt to smuggle effect authority into the proposal invalid.

### EffectReceipt
Schema: `protocol/v0.1/effect-receipt.schema.json`

Represents the observed execution result. It includes the exact `effect_id`, an `EFFECT_PERMISSION` authority reference, actual effect, changed objects, evidence refs, test results, duration and optional cost.

A valid receipt must bind active effect authority to both the exact `EffectProposal.effect_id` and its `content_hash`.

Statuses are execution statuses only:

- `SUCCEEDED`
- `FAILED`
- `BLOCKED`

They are not human acceptance or product-level PASS.

### StateDelta
Schema: `protocol/v0.1/state-delta.schema.json`

Represents the smallest durable state update after the effect/review boundary.

It keeps separate arrays for:

- `facts_added`
- `decisions_added`
- `hypotheses_added`

A `decision` record requires `decision_owner_kind = HUMAN`. A project status change requires a `decision_ref` that resolves to a human decision added in the same delta in the v0.1 bundle validator.

## 3. Identity and canonical hashing

Each top-level object has an object-specific ID and a `content_hash`.

Identity procedure:

1. copy the object;
2. remove its object-ID field and `content_hash`;
3. canonicalize the remaining JSON according to the Saddle v0.1 JCS profile below;
4. compute SHA-256 over the canonical UTF-8 bytes;
5. set `content_hash = "sha256:<lowercase hex>"`;
6. set object ID to `<type>:<content_hash>`, e.g. `intent:sha256:...`.

Any later content mutation makes the stored ID/hash invalid.

### Saddle v0.1 JCS profile

Canonicalization follows RFC 8785 JSON Canonicalization Scheme for the data types allowed by v0.1:

- object keys sorted recursively by UTF-16 code units;
- array order preserved;
- no insignificant whitespace;
- strings preserved as supplied; no Unicode normalization;
- duplicate object property names rejected at parsing;
- invalid Unicode rejected;
- floating-point JSON numbers are forbidden by the v0.1 protocol utilities;
- integers must be within `[-9007199254740991, 9007199254740991]`.

The float restriction is a deliberate protocol simplification, not a statement that RFC 8785 forbids floats. Exact monetary values use integer minor units; durations use integer milliseconds; higher-precision decimals should be strings until a later protocol version explicitly defines their semantics.

Implementation: `tools/protocol_v01.py`.

## 4. Provenance and authority references

`protocol/v0.1/common.schema.json` defines provider-independent refs.

A `sourceRef` can refer to a repository, commit, PR, issue, file, URL, evidence artifact, intent/effect/receipt/delta or another identified source.

An `authorityRef` records:

- opaque authority ID;
- authority kind;
- status;
- exact bound object type / object ID / content hash;
- source evidence refs;
- issuance/optional expiry timestamps;
- optional opaque provider reference.

The protocol intentionally does not choose an identity or authority provider.

## 5. Bundle invariants

`validate_bundle()` deterministically enforces:

```text
EffectProposal.intent_id == IntentEnvelope.intent_id
EffectReceipt.effect_id == EffectProposal.effect_id
EffectReceipt.authorization_ref binds exact EffectProposal ID + content_hash
StateDelta.intent_id == IntentEnvelope.intent_id
StateDelta.effect_id == EffectProposal.effect_id
```

For a project status change, v0.1 requires a human-owned decision in the same `StateDelta` and a matching `decision_ref`.

This is intentionally conservative. Later versions may support references to separately persisted decision objects, but v0.1 does not need that extra indirection for the first functional slice.

## 6. Verification boundary

Schema validity is necessary but not sufficient.

The protocol utilities distinguish:

1. schema/shape validation;
2. content identity/hash validation;
3. cross-object semantic binding validation.

External facts still require actual evidence/verifier mechanisms in later gates. A valid `sourceRef` does not prove that the referenced source is trustworthy. A syntactically valid `authorityRef` does not create authority by itself; the actual adapter/verifier belongs to the later verified-intent/effect-authority gate.

## 7. No hidden architecture commitment

Protocol v0.1 deliberately does not choose:

- OpenAI/Anthropic/Google/other provider;
- single-agent vs future multi-agent architecture;
- prompt language;
- internal chain-of-thought or planner/coder/critic roles;
- MCP vs native tools;
- vector/graph/database storage;
- browser automation;
- GUI/dashboard;
- trust/identity provider;
- ScriptOps implementation base.

The four objects should remain usable if all of those mechanisms change.

## 8. Deterministic evidence for Phase 2

Required commands:

```text
python -m compileall -q tools tests
python -m unittest discover -s tests -v
```

The tests cover:

- schema registry/version resolution;
- valid four-object bundle;
- stable canonicalization under object-property reorder;
- UTF-16 key ordering;
- preserved array order;
- rejection of floats and duplicate JSON keys;
- raw-intent mutation invalidating identity;
- verified origin requiring evidence;
- authority smuggling into `EffectProposal` failing closed;
- receipt authority exact-effect binding;
- AI-owned `DECISION` rejection;
- status change without matching human decision rejection;
- unknown properties failing closed.

A passing test set freezes the protocol mechanics only. It does **not** claim a functional Saddle, real authority provider or real AI worker.

## 9. Standards basis

The schemas use JSON Schema Draft 2020-12. Canonical identity uses a restricted v0.1 profile of RFC 8785 JCS. The restriction to safe integers/no floats is a Saddle v0.1 interoperability choice layered on top of JCS.
