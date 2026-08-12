# Phase 7 E2E review packet — 2026-08-12

Status: `E2E_EFFECT_COMPLETE_REVIEW_REQUIRED`

This is durable factual evidence only. It is **not** a human acceptance decision, does **not** set `FUNCTIONAL_SADDLE_ACCEPTED`, and does **not** release the completion lock.

## Canonical Saddle state for this evidence

```text
Saddle main before evidence-recording PR: e7ae3a892bbb976ce27b86a4c4638e9e7dfcbcc5
Phase-7 recovery workflow run: 31564950467
event: push
actor: JTJ07
workflow conclusion: SUCCESS
recovery-control-plane: SUCCESS
recovery-e2e: SUCCESS
```

Recovered evidence artifact:

```text
artifact id: 9129112642
name: phase7-recovered-functional-acceptance-evidence
artifact ZIP digest: sha256:548aa9384327642bfc6ae594d21ad74dc75288afcebc8d14629a1d4b5e6987a3
expires_at: 2026-09-11T04:58:04Z
```

The repository also permanently preserves attempt-001 metadata and the exact consumed worker patch in:

- `evidence/phase7/attempt-001.json`
- `evidence/phase7/attempt-001-model.patch`

## Raw intent / origin integrity

Literal human raw intent preserved by the Phase-7 chain:

```text
Kontynuuj Saddle od canonical GitHub state i wykonaj Phase 7
```

Original authenticated acceptance-only origin event:

```text
provider: github-actions-push-actor/acceptance-only
principal_ref: github-user:JTJ07
actor: JTJ07
event: push
ref: refs/heads/main
original Saddle SHA: 522e48ba50ac106b6c85a67ece634044f53788e1
original Phase-7 live run: 31564368431
origin event hash: sha256:6a86742226260eff46b1007d13fec7f2e73f9d797b210bde2bf92cf8ed338df3
raw intent hash: sha256:31c277d7438c565dcbdb80e1841fa586ea0b7a138ecbc4e46e72877c133e412b
```

This origin binding is explicitly acceptance-only and is not a production request-origin / human-identity trust-provider selection.

## Real AI worker evidence

Exactly one real worker call was consumed for Phase 7:

```text
provider: google-gemini
api: generateContent
model: gemini-3.6-flash
provider response id: 3fp7asHlEtGfqtsPiszR0QM
input tokens: 2024
output tokens: 982
reasoning tokens: 2288
latency: 13414 ms
estimated list-price cost: USD 0.027561
automatic retries: 0
original model calls: 1
recovery model calls: 0
total Phase-7 model calls: 1
```

Immutable worker-proposal hash:

```text
sha256:f2abb3bb8f72f772a2c00a46b624821b84e6ca1a6b22c0115f96094a1a0c81c4
```

Exact mutation binding:

```text
path: project_registry/registry.py
before sha256: bf18f6a6dc6adfe4d5afd0e63d0db79ff400293148b6c3528c355e38075c8f0d
after sha256: 26baef8666b6a37ff784ba0d303f9638aaa9769985831019218191fa16367b01
changed model patch lines: 14
```

Worker reason:

> Make ProjectRegistry.add_many atomic by materializing the input batch, checking for duplicates against both existing registry state and within the batch itself, and only mutating state once all items are validated.

## Attempt-001 fail-closed recovery

The original live run reached the real worker, exact EffectAuthority, and successful current-Executor effect, then failed at final Protocol v0.1 bundle validation because the runner used `ORIGIN` as `sourceRef.kind`; Protocol v0.1 permits `EVIDENCE`, not `ORIGIN`.

Observed original-run executor status was already:

```text
ACTION_COMPLETED_REVIEW_REQUIRED
```

No model retry was permitted or performed. Recovery therefore:

1. persisted the consumed worker response/hash/usage/patch;
2. set the paid gate to `MODEL_CALL_CONSUMED_RECOVERY_ONLY`;
3. removed the live Gemini/secret job from the original Phase-7 workflow;
4. corrected only the origin evidence reference kind to `EVIDENCE`;
5. reconstructed the exact consumed before/after-hash mutation;
6. derived a new exact single-use recovery EffectAuthority;
7. re-executed the same mutation on a fresh controlled CASE-001 checkout through the current reconciled Executor;
8. validated the complete Protocol v0.1 bundle.

## Recovered E2E result

Recovered summary:

```text
status: E2E_EFFECT_COMPLETE_REVIEW_REQUIRED
protocol_bundle: PASS
model: gemini-3.6-flash
original_model_calls: 1
recovery_model_calls: 0
total_phase7_model_calls: 1
automatic_model_retries: 0
current Executor: JTJ07/Executor@728d23e56ec9f76fb7a37673ceb20efccf91e03d
controlled fixture: litrgratis-pixel/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0
changed_paths: [project_registry/registry.py]
human_review_required: true
second_zero_history_resume_required: true
explicit_final_human_acceptance_required: true
functional_saddle_accepted: false
completion_lock_release_authorized: false
```

Recovered exact protocol identities:

```text
EffectProposal: effect:sha256:82af9e27d53396851874bc13b0dbdc20cf010a3a05a75bc3cf8b3ba9bacb3b1f
EffectAuthority: effect-authority:sha256:8c38c352b0345668a84205218198a829771c6fde7d62b972913d68db2bd19a72
EffectReceipt: receipt:sha256:5e14e81b2aa2d83d652f4100592d753bd570d7626c36e511d3e39c7242f0283e
StateDelta: state-delta:sha256:f94b65137c1ea7cc577b69178ab488de79243f023e5c477e65bf1d1ba10e4e3d
Executor report hash: sha256:2056fd49f7b3731716ec74a40a5906f7dd0d229781749319ab7cf2374ced5fab
```

## Executor / verifier evidence

Current Executor returned:

```text
status: ACTION_COMPLETED_REVIEW_REQUIRED
human_decision_required: true
changed_paths: [project_registry/registry.py]
fixture_authority: BOUND
input_identity: MATCH
pre_change_target_test: FAIL
post_change_target_test: PASS
regression_checks: PASS
diff_scope: ALLOWED
protected_material: UNCHANGED
execution_limits: RESPECTED
result_artifact: PRESENT
```

Objective command evidence:

```text
pre-change target test: expected FAIL, observed exit 1
post-change target test: PASS
full fixture regression: 13 tests / PASS
compileall: PASS
sandbox cleanup: PASS
```

No target test, regression test, protected material, repository identity, Executor identity, model-call count, retry count, or authority boundary was broadened during recovery.

## Human review gate — OPEN

The technical Phase-7 E2E evidence is complete through the required review boundary. The following are still human-owned and therefore deliberately **not** asserted by this evidence record:

```text
HUMAN_REVIEW_ACCEPTED = OPEN
SECOND_ZERO_HISTORY_RESUME = REQUIRED / NOT YET PERFORMED
EXPLICIT_FINAL_HUMAN_ACCEPTANCE = OPEN
FUNCTIONAL_SADDLE_ACCEPTED = false
COMPLETION_LOCK = ACTIVE
```

If the human accepts this evidence, the next operation is the required **second zero-history repository-only resume**. That resume must independently recover this canonical state and verify that the evidence and boundaries survive context loss. Only after that gate and an explicit human final acceptance may canonical state record `FUNCTIONAL_SADDLE_ACCEPTED` or release the completion lock.
