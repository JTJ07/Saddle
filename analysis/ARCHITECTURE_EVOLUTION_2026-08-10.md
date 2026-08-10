# ARCHITECTURE EVOLUTION — SESSION LINEAGE 2026-08-10

Status: `ANALYSIS / DECISION LINEAGE / NOT A PROTOCOL SPEC`

Purpose: preserve the reasoning sequence that moved the project from an Executor-centric trust-boundary question to the current Saddle-level responsibility model.

This file exists so a future agent does not flatten multiple generations of analysis into one contradictory snapshot.

## Stage A — Executor-centric authority research

The original authority research progressed through increasingly precise questions:

1. Can Executor perform a bounded effect?
2. Is that effect permitted?
3. Is the contract valid and exact?
4. Did a human really approve the exact contract?
5. Where does trustworthy evidence of the original human request begin?

PR #51–#57 progressively separated human action from verified authority, authentication from authorization, AI interpretation from user intent, intent authority from effect authority, receipt from evidence, event identity from content identity, and user provenance from verified request-origin evidence.

This research remains reusable.

## Stage B — A1 vs strengthened A2 under Executor-centric framing

A1 externalized governed request intake simplified trust topology but moved the front door outside Executor.

Naive A2 — later authentication plus local binding — was rejected because it cannot prove that a principal directly originated/attested the exact immutable request.

Strengthened A2 survived only with a direct transaction-specific external principal action bound to exact request identity before governed formation relies on it, plus later exact decision binding.

Surviving invariant:

`USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.

## Stage C — Saddle becomes the higher-level boundary

Once Saddle was defined as the coupling layer between human intent and arbitrary intelligence/effects, the earlier question `Should Executor own the human front door?` was recognized as one layer too low.

Current system-level model:

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

This relocates ownership of the human-intent boundary without discarding Executor trust research.

## Stage D — A1/A2 reinterpretation

Default Saddle path retains the strengthened-A2 trust principle:

```text
HUMAN
 ↓
SADDLE FRONT DOOR
 captures exact raw intent
 ↓
EXTERNAL ORIGIN ATTESTATION when required
 binds direct human action to exact intent identity
 ↓
BOUND / VERIFIED INTENT
 ↓
INTELLIGENCE
 ↓
EFFECT PROPOSAL
 ↓
EXECUTOR
```

Delegated/enterprise A1-like path:

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

Thus:

- strengthened A2 principle = retained at default Saddle intent boundary;
- naive A2 = rejected;
- A1 = valid delegated/enterprise intake variant;
- provider = not selected.

## Stage E — Saddle must not own meaning

Rejected wording:

`SADDLE AUTHORIZES MEANING`.

Reason: Saddle must not promote its own interpretation into the user's intent.

Preferred model:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

## Stage F — no-layer-substitution invariant

Human decision:

`NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER`.

Examples:
- AI cannot substitute for human goal ownership;
- Saddle cannot substitute its interpretation for human intent;
- Executor cannot infer effect permission merely from intent;
- Verifier cannot turn observation into authority;
- receipt cannot substitute for permission;
- proposal cannot substitute for canon.

## Stage G — responsibility map

| Concern | Primary owner | Must not silently become |
|---|---|---|
| Human intent / what matters | Human | AI/Saddle-generated semantic canon |
| Intent preservation / provenance / context / decision lineage | Saddle | independent goal owner |
| Solution search / reasoning / alternatives | Intelligence | authority source |
| Consequential effect authority / policy / scope / bounded execution | Executor | human-intent interpreter |
| What actually happened | Verifier / evidence path | authority source |

Checksum:

> Human decides what matters. Saddle protects that meaning. Intelligence discovers how. Executor controls what happens. Verifier proves what happened.

## Stage H — consequence for Executor interface

Design target: minimize semantic context Executor needs.

Conceptually:

```text
EffectProposal
+ EffectAuthority
+ scope
+ constraints
+ evidence requirements
+ intent_ref
```

`intent_ref` preserves traceability without forcing Executor to ingest the full human conversation or business meaning.

Executor should primarily answer:

> Is this exact effect permitted, in scope, and executable under the supplied authority/constraints?

not:

> Why does the human want it?

This is a design target, not yet a frozen protocol.

## Stage I — roadmap consequence

Do not turn the architecture correction into a new framework/runtime stack.

Correct ordering:

```text
Phase 1
→ reconcile ownership and Executor #51–#57 findings
→ record superseded assumptions vs reusable trust invariants
→ finish ecosystem/source map

Phase 2
→ freeze minimal provider-independent Saddle protocol
```

Likely later semantic areas:
- `SADDLE_VERIFIED_INTENT_BOUNDARY`;
- `EXECUTOR_EFFECT_AUTHORITY_BOUNDARY`.

They should begin as minimal semantics/contracts/tests, not platforms.

## Stage J — superseded vs retained

Superseded at global Saddle level:
- `USER -> EXECUTOR` as universal product front door;
- `SADDLE AUTHORIZES MEANING`.

Retained:
- human owns goal/intent;
- exact raw intent preservation;
- AI interpretation != human intent;
- intent authority != effect authority;
- user provenance != verified origin evidence;
- exact transaction-specific binding;
- anti-replay/freshness/trust-domain discipline;
- strengthened-A2 trust pattern;
- A1 as consciously delegated intake;
- deterministic trust/effect controls around flexible AI reasoning.

Still open after Phase 1:
- exact provider/technology;
- exact verified-intent schema;
- exact effect-authority schema/interface;
- exact external attestation ceremony;
- production model/provider;
- ScriptOps v2 base selection.

## Final architecture checksum

```text
                 HUMAN
                   │
             owns intent
                   ▼
                SADDLE
      preserves / binds / remembers
                   ▼
             INTELLIGENCE
       reasons / explores / proposes
                   ▼
              EXECUTOR
    governs consequences / executes
                   ▼
                WORLD
                   ▼
              VERIFIER
         establishes evidence/facts
                   └────→ durable Saddle state
```

Anti-drift rule:

`NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER`.
