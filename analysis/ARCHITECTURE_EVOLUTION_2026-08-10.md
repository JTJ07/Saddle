# ARCHITECTURE EVOLUTION — SESSION LINEAGE 2026-08-10

Status: `ANALYSIS / DECISION LINEAGE / NOT A PROTOCOL SPEC`

Purpose: preserve the reasoning sequence that moved the project from an Executor-centric trust-boundary question to the current Saddle-level responsibility model.

This file exists so a future agent does not flatten multiple generations of analysis into one contradictory snapshot.

---

## Stage A — Executor-centric authority research

The original authority research in Executor progressed through increasingly precise questions:

1. Can Executor perform a bounded effect?
2. Is that effect permitted?
3. Is the contract valid and exact?
4. Did a human really approve the exact contract?
5. Where does trustworthy evidence of the original human request begin?

The PR #51–#57 stack progressively separated:

- human action from verified human authority;
- authentication from authorization;
- AI interpretation from user intent;
- intent authority from resource/action authority;
- decision receipt from verified authority evidence;
- evidence references from trust selection;
- event identity from event-content identity;
- user provenance from independently verified request-origin evidence.

This research was valuable and remains reusable.

---

## Stage B — A1 vs strengthened A2 under Executor-centric framing

The initial product question was framed as whether Executor itself should remain the human front door.

### A1 — externalized governed request intake

```text
USER
 ↓
EXTERNAL TRUST DOMAIN
 ↓
VERIFIED REQUEST
 ↓
EXECUTOR
```

Advantages identified:

- simpler trust topology;
- origin event + identity + decision event can live in one governed domain;
- clean fit before existing Executor formation kernel.

Product cost identified:

- Executor ceases to be the true governed request front door;
- risk of becoming mainly an approval/runtime engine behind Teams/Docusign/Ping/etc.

### Naive A2 — rejected

```text
user types request
→ later authentication
→ Executor locally associates identity with request
```

Rejected because authentication or later local binding does not prove the principal directly originated/attested the exact immutable request.

### Strengthened A2 — survives the attack

Original Executor-centric shape:

```text
USER
 ↓
EXECUTOR FRONT DOOR
captures exact raw request A / H(A)
 ↓
EXTERNAL TRUST DOMAIN
records direct transaction-specific principal action bound to H(A)
 ↓
verified request origin
 ↓
Executor formation / critique
 ↓
EXTERNAL TRUST DOMAIN
records later exact ACCEPT event
 ↓
Executor verifies identity and exact bindings
```

Important surviving invariant:

```text
USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE
```

Another key conclusion:

A2 cannot be bolted on only after formation reaches `AWAITING_VERIFIED_HUMAN_AUTHORIZATION`; verified origin must exist before the governed formation relies on it.

The initial audit recommendation therefore preferred strengthened A2 for Executor as the target product architecture, with A1 a valid enterprise variant and provider selection deferred.

---

## Stage C — Saddle appears as the higher-level product boundary

Once Saddle was defined as the coupling layer between human intent and arbitrary intelligence/effects, a new architecture observation became unavoidable:

The earlier question `Should Executor own the human front door?` was being asked one layer too low.

Current Saddle-level product model:

```text
HUMAN
 ↓
SADDLE
 ↓
INTELLIGENCE
 ↓
EXECUTOR
 ↓
WORLD
```

This does not invalidate the Executor trust research.

It relocates ownership of the human-intent boundary.

The key correction was:

```text
FRONT DOOR OWNER = SADDLE, NOT EXECUTOR
```

at the global Saddle product level.

---

## Stage D — A1/A2 reinterpretation at the Saddle boundary

The useful security/trust logic survives.

### Default / strengthened-A2-like Saddle path

```text
HUMAN
 ↓
SADDLE FRONT DOOR
captures exact raw intent
 ↓
EXTERNAL ORIGIN ATTESTATION
binds direct human action to exact request/intent identity
 ↓
VERIFIED INTENT
 ↓
INTELLIGENCE
 ↓
EFFECT PROPOSAL
 ↓
EXECUTOR
```

The external trust domain supplies trustworthy event facts; it does not become semantic owner of the user's goal.

### Delegated / enterprise A1-like path

```text
HUMAN
 ↓
CORPORATE / EXTERNAL TRUST DOMAIN
 ↓
SADDLE
 ↓
INTELLIGENCE
 ↓
EXECUTOR
```

This is not a competitor to Executor. It is a possible upstream governed intake arrangement for Saddle.

Therefore the new working interpretation is:

```text
strengthened A2 principle = retained as default Saddle intent-boundary pattern
naive A2                 = rejected
A1                       = valid delegated/enterprise intake variant
provider                 = not selected
```

---

## Stage E — wording correction: Saddle must not own meaning

A temporary phrase emerged during discussion:

```text
SADDLE AUTHORIZES MEANING
```

This was explicitly corrected and rejected as too strong.

Reason:

If Saddle can authorize the meaning of a human's request, the system can silently promote its own interpretation into the user's intent — reproducing the same category error previously discovered in Executor.

Preferred ownership model:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

Human remains semantic authority.

Saddle preserves exact origin/content/context/decision lineage and binds later artifacts to that human-owned intent.

---

## Stage F — no-layer-substitution principle

The user then proposed a unifying invariant:

```text
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Examples:

- AI cannot substitute for human goal ownership.
- Saddle cannot substitute its interpretation for human intent.
- Executor cannot substitute consequence authority for intent ownership.
- Verifier cannot substitute observation for permission.
- Receipt cannot substitute for authority.
- Proposal cannot substitute for canon.

This principle is intended to prevent responsibilities from drifting upward or downward merely because a component technically has enough information or capability to do so.

---

## Stage G — current responsibility map

| Concern | Primary owner | Must not silently become |
|---|---|---|
| Human intent / what matters | Human | AI/Saddle-generated semantic canon |
| Intent preservation / provenance / context / decision lineage | Saddle | independent goal owner |
| Solution search / reasoning / alternatives | Intelligence | authority source |
| Consequential effect authority / policy / scope / bounded execution | Executor | human-intent interpreter |
| What actually happened | Verifier / evidence path | authority source |

Compact verbal checksum:

> Human decides what matters. Saddle protects that meaning. Intelligence discovers how. Executor controls what happens. Verifier proves what happened.

---

## Stage H — consequence for Executor interface

A likely design target is to minimize the semantic context Executor needs.

Conceptual input may eventually resemble:

```text
EffectProposal
+ EffectAuthority
+ scope
+ constraints
+ evidence requirements
+ intent_ref
```

The `intent_ref` preserves traceability without requiring Executor to ingest all conversation history, motivation or business semantics.

This is not yet a frozen protocol or schema.

The design test is:

Executor should primarily answer:

> Is this exact effect permitted, in scope, and executable under the supplied authority/constraints?

not:

> Why does the human want it?

---

## Stage I — consequence for roadmap

Do NOT respond to the architecture insight by immediately creating a large new implementation stack.

The user explicitly agreed that the correct next placement is Phase 1 reconciliation.

Recommended ordering:

```text
Phase 1
→ reconcile ownership and map Executor #51–#57 findings
→ record superseded assumptions vs reusable trust invariants
→ finish component/source map

then Phase 2/T4
→ freeze minimal provider-independent contracts
```

Likely later semantic documents/areas:

- `SADDLE_VERIFIED_INTENT_BOUNDARY`
- `EXECUTOR_EFFECT_AUTHORITY_BOUNDARY`

But those should begin as minimal semantics/contracts/tests, not as new frameworks/products.

No provider should be selected before these boundaries are sufficiently defined.

---

## Stage J — what is superseded vs retained

### Superseded at global Saddle level

```text
USER → EXECUTOR
```

as the assumed universal product front door.

Also rejected:

```text
SADDLE AUTHORIZES MEANING
```

### Retained

- human owns goal/intent;
- exact raw request/intent preservation;
- AI interpretation != human intent;
- intent authority != effect/action authority;
- user provenance != verified origin evidence;
- exact transaction-specific binding;
- anti-replay / freshness / trust-domain discipline;
- strengthened-A2 trust pattern;
- A1 as a consciously delegated intake variant;
- deterministic trust/effect controls around flexible AI reasoning.

### Still open

- exact provider/technology;
- exact verified-intent schema;
- exact effect-authority schema/interface;
- exact external attestation ceremony;
- exact minimum information Executor needs beyond `intent_ref`;
- canonicalization/merge strategy for Executor #51–#57.

---

## Final architecture checksum

```text
                 HUMAN
                   │
             owns intent
                   │
                   ▼
                SADDLE
      preserves / binds / remembers
                   │
                   ▼
             INTELLIGENCE
       reasons / explores / proposes
                   │
                   ▼
              EXECUTOR
    governs consequences / executes
                   │
                   ▼
                WORLD
                   │
                   ▼
              VERIFIER
         establishes evidence/facts
                   │
                   └────→ durable Saddle state
```

Core anti-drift rule:

```text
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

This lineage should be used during Phase-1 reconciliation to prevent older Executor-centric language from accidentally overriding the later Saddle-level product boundary.
