# Phase 4C — Synthetic Intelligence Integration Evidence

Date: 2026-08-10
Evidence class: `SYNTHETIC_INTEGRATION_EVIDENCE`
Verdict: `PASS IN TESTED SCOPE`

This is **not** API worker evidence, model-performance evidence, a maturity claim, or `FUNCTIONAL_SADDLE_ACCEPTED`.

## Human-approved proof order

Phase 4B is a measurement gate for worker quality, not an architecture prerequisite. The accepted proof order is:

```text
Phase 4A calibration — ACCEPTED
        ↓
Phase 4C synthetic integration — THIS EVIDENCE
        ↓
Phase 4B reproducible API worker benchmark
        ↓
evaluation
        ↓
human decision
```

No new capability, autonomy, authority or model tool access was added.

## Exact inputs

```text
Saddle PR: #16
Workflow: Phase 4C synthetic integration proof
Run: 31429931199
Job: 93590584463
Executor repository: litrgratis-pixel/Executor
Executor commit: 788443c3ed5b290ac8f1de145a93d02d2dd15317
Fixture repository: litrgratis-pixel/executor-pilot-target
Fixture commit: 3934a94a5eebf750079200589d6dc40e024d44a0
Case: CASE-001
Allowed target: project_registry/registry.py
Synthetic generator: DETERMINISTIC_CASE001_PROPOSAL
Executor calls: 1
```

## Proven chain

```text
IntentEnvelope
  ↓
VerifiedIntentBinding
  ↓
deterministic synthetic WorkerProposal
  ↓
EffectProposal
  ↓
explicit declared-scope check
  ↓
exact EffectAuthority
  ↓
existing Executor GP001Runtime
  ↓
ACTION_COMPLETED_REVIEW_REQUIRED
  ↓
EffectReceipt
  ↓
StateDelta
  ↓
Protocol v0.1 bundle validation
```

The synthetic proposal has no authority. The Executor call occurs only after Saddle's existing Phase-5 exact-authority gate returns `ALLOW`.

## Deterministic regression

The workflow first executed the Saddle suite:

```text
Ran 59 tests
OK
```

This includes the five Phase-4C integration-boundary tests plus existing protocol, Phase-5 boundary, eval and model-gateway tests.

## Real Executor path

The workflow acquired the exact current Executor main checkpoint and exact CASE-001 fixture commit, resolved an immutable Python sandbox image, then executed the existing GP001 Docker runtime.

Observed happy-path result:

```text
status: PASS
Saddle authority: ALLOW / EXACT_EFFECT_AUTHORITY_MATCH
Executor terminal status: ACTION_COMPLETED_REVIEW_REQUIRED
Protocol bundle: PASS
changed target: project_registry/registry.py only
human review requirement: preserved
```

Content-addressed evidence identities from the uploaded summary:

```text
VerifiedIntentBinding:
verified-intent:sha256:c59cc2b3a6f6b9d8d13d84377d538d780c2ff554a2ebccec1583d6dc92df6840

EffectAuthority:
effect-authority:sha256:ac38d88b9741d7badf9e008cc7358769382b50b350221fef38045325418eb990

EffectReceipt:
receipt:sha256:da4506003d1cb4b3708c9b300db5db020e943d654bfb465f761f5aa806fec37c

StateDelta:
state-delta:sha256:7f6c9111bd111e2dfad203de760999e5b7e5eb67bfac19ff76735bb2e6d1217d
```

## Negative cases

### 1. Declared intent/scope drift

Synthetic attack:

```text
human-approved declared scope: one exact file
proposal: REBUILD_MODULE / project_registry directory
```

Observed:

```text
BLOCK
PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE
```

This check uses explicit machine-readable action/target constraints. It does **not** infer what the human "really meant" and does not turn Saddle into a semantic authority.

### 2. Effect-authority mismatch

Authority was bound to a different exact proposal identity.

Observed:

```text
BLOCK
AUTHORITY_EFFECT_ID_MISMATCH
AUTHORITY_EFFECT_HASH_MISMATCH
```

### 3. Effect-authority replay

The exact authority that allowed the happy path was presented a second time.

Observed:

```text
BLOCK
EFFECT_AUTHORITY_REPLAYED
```

## Artifact evidence

GitHub Actions artifact:

```text
name: phase4c-synthetic-integration-evidence
artifact ID: 9078675806
size: 1174 bytes
ZIP digest: sha256:cac22ce36e2bfff030f1e3fb1aea3a5323dd55abf75a02d70962cda6165a75e1
```

The extracted `summary.json` reports:

```text
evidence_class: SYNTHETIC_INTEGRATION_EVIDENCE
worker_evidence: false
model_performance_claim: false
maturity_claim: NONE
functional_saddle_accepted: false
protocol_bundle: PASS
happy_path: PASS
intent_scope_drift: BLOCK
authority_mismatch: BLOCK
authority_replay: BLOCK
```

## ScriptOps boundary finding

The accepted ScriptOps Phase-6 substrate is scene-domain specific. Executor GP001 is code-domain specific. Phase 4C therefore does **not** invent a new ScriptOps code-mutation capability and does not chain two execution mechanisms artificially for one effect.

ScriptOps Phase-6 evidence remains separately valid as proof of its controlled workflow lifecycle. Phase 4C proves the provider-independent Saddle → authority gate → real Executor → evidence/verifier core that a later AI worker can feed.

## Phase-4B pause / trigger correction

Opening PR #16 exposed a CI trigger drift: the already-canonical Phase-4B workflow automatically started on every newly opened PR, even though the new proof order says `4B READY BUT PAUSED`.

Observed accidental run:

```text
run: 31429930237
job: 93590580949
deterministic pre-model step: PASS
credential gate: FAIL / secret absent
model benchmark step: SKIPPED
```

No paid/model step ran. The Phase-4B workflow was changed on the Phase-4C branch to `workflow_dispatch` only. This pauses execution without changing the benchmark contract or approved limits.

## What Phase 4C proves

Only this:

> The provider-independent Saddle control/effect chain can preserve a bounded intent, accept a deterministic proposal, require exact effect authority, execute one real bounded effect through the existing Executor, produce objective evidence, form a valid EffectReceipt/StateDelta bundle, and fail closed on explicit scope drift, authority mismatch and replay.

It does **not** prove:
- AI worker quality;
- independent model problem solving;
- API reproducibility/cost/latency;
- production trust-provider identity;
- arbitrary-domain integration;
- ScriptOps maturity;
- product maturity;
- `FUNCTIONAL_SADDLE_ACCEPTED`.

## Next evidence gate

After this synthetic integration proof is accepted/canonicalized, Phase 4B becomes the next measurement gate. It must replace only the synthetic Intelligence component with the controlled API worker while keeping the same responsibility boundaries.
