# PHASE 4 — PRE-CREDENTIAL / PRE-EGRESS CHECKPOINT

Date: 2026-08-10
Status: `REAL MODEL BENCHMARK BLOCKED / GATEWAY SCAFFOLD READY`
Branch: `agent/phase4-model-gateway`

## What is implemented

- `worker/v0.1/worker-proposal.schema.json` — proposal-only model output;
- `config/worker-cases-v0.1.json` — exact CASE-001–003 broken commits;
- `config/model-benchmark-v0.1.json` — two-candidate first-pass benchmark plan;
- `tools/model_gateway.py` — provider-neutral interface + narrow OpenAI Responses adapter;
- `tools/phase4_preflight.py` — non-secret preflight;
- `tools/phase4_benchmark.py` — exact-checkout proposal generator;
- ModelGateway/preflight/checkout-boundary tests.

## Exact benchmark pins

- CASE-001: `3934a94a5eebf750079200589d6dc40e024d44a0`;
- CASE-002: `c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be`;
- CASE-003: `c42bead2bbbff9c84486f17637ec80f35eeffa25`.

All three allow only `project_registry/registry.py`.

## Current candidate research

Official OpenAI sources were rechecked on 2026-08-10.

First-pass candidates:

- `gpt-5.6-sol` — quality-first / flagship;
- `gpt-5.6-terra` — balanced capability/cost;
- reasoning effort: `medium` initially for both.

Current standard API prices observed from official OpenAI pricing/model pages:

- Sol: USD 5 / 1M input tokens, USD 30 / 1M output tokens;
- Terra: USD 2.50 / 1M input tokens, USD 15 / 1M output tokens.

Candidate list is not a production model decision. Account access must be verified by the authorized API account.

First-pass proposal:

- 3 immutable cases;
- 2 models;
- 1 call per model per case;
- 6 model calls maximum;
- 0 automatic retries;
- recommended hard cap: USD 5.00;
- budget status: `HUMAN_APPROVAL_REQUIRED`.

## Credential observation

Only presence/absence was checked; no secret value was read or recorded.

```text
OPENAI_API_KEY=NOT_SET
ANTHROPIC_API_KEY=NOT_SET
GOOGLE_API_KEY=NOT_SET
GEMINI_API_KEY=NOT_SET
```

Phase-4 preflight against the real pinned case/model config produced:

```json
{
  "candidate_models": ["gpt-5.6-sol", "gpt-5.6-terra"],
  "cases": ["CASE-001", "CASE-002", "CASE-003"],
  "credential_env": "OPENAI_API_KEY",
  "credential_present": false,
  "reasons": ["PROVIDER_CREDENTIAL_NOT_CONFIGURED"],
  "status": "BLOCKED"
}
```

## Execution-environment observation

The current local execution container does not provide general outbound DNS/HTTPS for arbitrary model API calls; a direct `git ls-remote https://github.com/...` connectivity probe failed on name resolution.

No available installed/in-scope plugin provides external model inference / OpenAI Responses API execution.

Therefore a real API benchmark cannot be executed from this session's current tool runtime even if a raw key were pasted into chat. A key must **not** be pasted into chat.

## Local scaffold tests

A local isolated test replica matching the committed ModelGateway/preflight/pinned-checkout logic was executed:

```text
Ran 13 tests
OK
```

Covered:

- missing credential fails before network;
- request uses strict structured output and `store: false`;
- no tools are granted;
- secret is not present in request payload/evidence;
- exact target path enforced;
- authority-smuggling field rejected;
- before/after hashes derived by control plane;
- patch budget fails closed;
- at least two candidates required;
- exact three cases required;
- credential preflight emits boolean only;
- exact checkout commit required;
- checkout drift and unknown case fail closed.

No real provider call was executed; these tests must not be interpreted as AI-worker quality evidence.

## Existing Executor attachment point

Current `Executor/main` `AuthorizedFileMutation` already accepts:

```text
path
expected_before_sha256
replacement_text
expected_after_sha256
```

and `GP001Runtime.execute()` validates/executes such a supplied mutation through the existing bounded policy/sandbox/evidence path.

`validate_worker_proposal()` produces those exact trusted hashes from the pinned before-text + model replacement. Therefore no Executor rewrite is required merely to remove the hard-coded solution source for CASE-001.

## What is NOT proven

- no real Sol/Terra call;
- no two-model benchmark result;
- no real token/cost/latency data;
- no model selected;
- no proposal executed through Executor;
- no CASE-001–003 AI-worker PASS;
- no Phase-4 acceptance.

## Exact blocker

All three are required before real benchmark execution:

1. authorized control-plane runner with outbound HTTPS to provider API;
2. `OPENAI_API_KEY` configured in that runner's secret environment/store, never chat/GitHub/evidence;
3. explicit human approval of a paid first-pass benchmark budget (recommended hard cap USD 5.00, max six calls, no automatic retries).

Until those exist, Phase 4 must remain open and blocked rather than inventing results.
