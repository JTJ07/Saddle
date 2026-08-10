# Phase 4C — Final Merge Verification

Date: 2026-08-10
Status: `MERGED / FINAL HEAD VERIFIED / SYNTHETIC INTEGRATION ONLY`

## Canonical merge

```text
Saddle PR: #16
final PR head: 171c274224939b711d92d767a5390176ee8a37c0
merge commit: 5b7ef758891522ca09787318e1e98fc7cdd25f32
```

## Final-head workflow proof

```text
workflow: Phase 4C synthetic integration proof
run: 31430644901
job: 93592960972
conclusion: SUCCESS
```

All final-head steps passed:
- checkout + Python setup;
- deterministic Saddle regression;
- explicit Phase-4B pause invariant (`workflow_dispatch`, no PR auto-trigger);
- exact Executor commit acquisition;
- exact CASE-001 fixture acquisition;
- immutable sandbox image resolution;
- full synthetic Saddle → exact authority → real Executor → evidence → Protocol bundle;
- evidence artifact upload;
- sandbox cleanup.

## Final artifact

```text
artifact: phase4c-synthetic-integration-evidence
artifact ID: 9078956705
size: 1175 bytes
ZIP digest: sha256:328059102d155bf826f8f616ef28d04d05724f1e155a3900c2941e1f0d98e4cb
```

Extracted `summary.json` confirms:

```text
happy_path:
  PASS
  authority: ALLOW / EXACT_EFFECT_AUTHORITY_MATCH
  executor_status: ACTION_COMPLETED_REVIEW_REQUIRED

intent_scope_drift:
  BLOCK / PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE

authority_mismatch:
  BLOCK / AUTHORITY_EFFECT_ID_MISMATCH
          AUTHORITY_EFFECT_HASH_MISMATCH

authority_replay:
  BLOCK / EFFECT_AUTHORITY_REPLAYED

protocol_bundle: PASS
worker_evidence: false
model_performance_claim: false
maturity_claim: NONE
functional_saddle_accepted: false
```

Final content-addressed identities from this run:

```text
VerifiedIntentBinding:
verified-intent:sha256:c59cc2b3a6f6b9d8d13d84377d538d780c2ff554a2ebccec1583d6dc92df6840

EffectAuthority:
effect-authority:sha256:ac38d88b9741d7badf9e008cc7358769382b50b350221fef38045325418eb990

EffectReceipt:
receipt:sha256:fbcf2acc8a8d950c6c1534c32200838a2f9e40a7055151f9b947b07e728d9f71

StateDelta:
state-delta:sha256:0450d8fe6d2019768b23f92011c0cd50b9347382499ffc83854a9b4aa14757ce
```

## Evidence boundary

This final verification upgrades only confidence in the Phase-4C system-integration proof. It does not change its evidence class.

It is NOT:
- API worker evidence;
- model performance evidence;
- production trust-provider evidence;
- maturity evidence;
- `FUNCTIONAL_SADDLE_ACCEPTED`.

## Next gate

Phase 4B remains the next measurement gate and must be explicitly dispatched only after `OPENAI_API_KEY` is present in approved GitHub Actions secret storage. Its budget, call, retry, capability and authority bounds remain unchanged.
