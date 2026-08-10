# DEC-SAD-014 — Prove synthetic system integration before API worker measurement

Date: 2026-08-10
Owner: USER
Status: `ACTIVE / PROOF-ORDER DECISION`

## Human verdict

```text
ARCHITECTURE: PASS
OWNERSHIP MODEL: PASS
PHASE 4A: PASS
PHASE 4B: READY BUT PAUSED
PHASE 6: PASS
NEXT: PRODUCT / SYSTEM INTEGRATION
```

## Decision

The API benchmark is not an architecture blocker. It measures one later question: whether a selected AI worker produces sufficiently useful proposals under the already frozen Saddle/Executor boundaries.

Before buying that measurement, prove the provider-independent product/system composition with deterministic synthetic intelligence.

Accepted evidence order:

```text
Phase 4A — cognitive calibration / ACCEPTED
        ↓
Phase 4C — Synthetic Intelligence Integration
        ↓
Phase 4B — controlled reproducible API worker benchmark
        ↓
evaluation
        ↓
human decision
```

## Phase 4C scope

Use a deterministic proposal generator only to validate the complete responsibility/effect path:

```text
IntentEnvelope
→ VerifiedIntentBinding
→ synthetic WorkerProposal
→ EffectProposal
→ exact EffectAuthority
→ existing Executor bounded execution
→ objective evidence
→ EffectReceipt
→ StateDelta
→ verifier
```

Synthetic intelligence:
- is proposal-only;
- has no shell or tools;
- has no repository-write authority;
- has no effect authority;
- cannot make product/canonical decisions.

## Required attacks

1. exact happy path must execute one bounded effect and return review-required evidence;
2. explicit proposal scope drift must BLOCK before execution;
3. authority for a different exact proposal must BLOCK;
4. replay of a consumed exact authority must BLOCK.

Scope-drift checks must use preserved explicit intent constraints/action/target bindings. Saddle may not replace this with semantic similarity or a claim that it knows what the human "really meant".

## Evidence classes

```text
SYNTHETIC_INTEGRATION_EVIDENCE != API_WORKER_EVIDENCE
SYNTHETIC_INTEGRATION_EVIDENCE != MODEL_PERFORMANCE_EVIDENCE
```

A Phase-4C PASS cannot select a model, increase autonomy, establish maturity, or produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## ScriptOps composition consequence

The accepted ScriptOps Phase-6 v2 substrate is currently scene-domain specific, while the existing Executor GP001 effect is code-domain specific.

Do not invent a new ScriptOps code-mutation capability or artificially chain two executors merely to satisfy a diagram. Keep the accepted ScriptOps controlled-workflow proof as separate evidence and use Phase 4C to prove the real Saddle → effect-authority → Executor → evidence core.

A future integration may compose ScriptOps with another effect domain only after an explicit need and authority/capability decision.

## Phase 4B consequence

Phase 4B stays intact and required. During Phase 4C it is `READY BUT PAUSED`; its benchmark contract, budget (`<= USD 5`), calls (`<= 6`), retries (`0`) and proposal-only authority boundary are unchanged.

The benchmark workflow should not auto-run merely because an unrelated PR opens. While paused, execution requires an explicit workflow dispatch after the provider secret is available.

## Non-goals

No new capability, model/provider selection, agent framework, autonomous loop, tool expansion, authority expansion, trust-provider selection, ScriptOps rewrite, Executor rewrite, or functional-acceptance claim.
