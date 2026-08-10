# MODEL GATEWAY v0.1 — PHASE 4 PRE-CREDENTIAL CHECKPOINT

Status: `IMPLEMENTED PROPOSAL CONTROL PLANE / REAL BENCHMARK BLOCKED`
Date: 2026-08-10

## 1. Purpose

Provide the thinnest possible interface between a real model and Saddle without turning the model into an executor or building a provider framework.

```text
pinned case / exact source / exact tests
        ↓
ModelGateway
        ↓
structured WorkerProposal only
        ↓
deterministic target/hash/diff validation
        ↓
AuthorizedFileMutation-shaped data
        ↓
Executor effect boundary (later actual run)
```

The model does not receive write/shell/network tools and does not produce authority.

## 2. Current adapter

`tools/model_gateway.py` defines a provider-neutral `ModelGateway` protocol and one deliberately narrow implementation:

`OpenAIResponsesGateway`.

It uses the Responses API directly with stdlib HTTPS rather than adding an SDK dependency.

Request properties:

- `store: false`;
- configurable model ID;
- configurable reasoning effort;
- strict JSON-Schema structured output;
- no `tools` field;
- no shell/write/network capability;
- API key read only from a named environment variable in the control plane.

The API key is never inserted into model input, proposal artifacts or eval evidence.

## 3. WorkerProposal

Schema: `worker/v0.1/worker-proposal.schema.json`.

Allowed model output:

- `case_id`;
- exact `target_path`;
- full `replacement_text`;
- `reason`;
- `evidence_plan`.

Deliberately absent:

- authority/permission;
- commands;
- tools;
- secrets;
- additional file paths;
- deployment/merge instructions.

`additionalProperties: false` means a model attempt to add `authorization_ref` or other fields is rejected.

## 4. Deterministic proposal normalization

`validate_worker_proposal()` independently enforces:

- exact pinned case ID;
- exact allowlisted target path;
- non-empty replacement/reason/evidence plan;
- replacement must actually differ from the input;
- changed-line budget;
- control-plane SHA-256 of before/after bytes.

The model does not choose or assert the trusted before/after hashes.

The normalized result matches the data needed by current Executor `AuthorizedFileMutation`:

```text
path
expected_before_sha256
replacement_text
expected_after_sha256
```

plus non-authoritative diagnostic fields.

Current Executor GP001 already validates these hashes and executes a supplied `AuthorizedFileMutation` through its bounded policy/sandbox/evidence path. Phase 4 therefore does not require rewriting Executor merely to replace the hard-coded solution source.

## 5. Pinned benchmark cases

`config/worker-cases-v0.1.json` pins immutable broken commits:

- CASE-001: `3934a94a5eebf750079200589d6dc40e024d44a0`;
- CASE-002: `c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be`;
- CASE-003: `c42bead2bbbff9c84486f17637ec80f35eeffa25`.

All three permit mutation only of:

`project_registry/registry.py`.

Relevant acceptance tests are supplied as read-only model context.

`tools/phase4_benchmark.py` refuses a local checkout whose `git rev-parse HEAD` differs from the pinned commit.

Broken benchmark inputs must remain immutable/reproducible.

## 6. Model candidates

`config/model-benchmark-v0.1.json` records the first two research candidates:

- `gpt-5.6-sol` — quality-first candidate;
- `gpt-5.6-terra` — balanced cost/capability candidate;
- initial reasoning effort: `medium` for both.

This is a benchmark candidate list, **not** a production model decision.

Account access to the exact model IDs must be verified by the authorized API account before benchmark execution.

Official sources rechecked 2026-08-10:

- OpenAI GPT-5.6 launch/availability information;
- OpenAI Responses API reference;
- OpenAI Models API reference;
- OpenAI developer quickstart/API-key guidance.

The current official GPT-5.6 announcement describes Sol as flagship, Terra as balanced and Luna as the fastest/lowest-cost tier. The benchmark intentionally starts with only two candidates to avoid building routing infrastructure.

## 7. Preflight

`tools/phase4_preflight.py` checks without inference:

- at least two unique model candidates;
- exact CASE-001–003 configuration;
- exact 40-hex pinned commits;
- exact target path;
- required test context;
- only whether the configured credential environment variable is present.

It never emits the credential value.

## 8. Current hard blocker

The current execution environment has no configured provider API credential and no generic outbound API runner available to this session.

Observed presence check:

```text
OPENAI_API_KEY=NOT_SET
ANTHROPIC_API_KEY=NOT_SET
GOOGLE_API_KEY=NOT_SET
GEMINI_API_KEY=NOT_SET
```

No raw secret was read or recorded.

Plugin discovery found no available model-inference/OpenAI-API plugin.

The local execution container also lacks general outbound DNS/HTTPS needed to call an external model API. This is an environment constraint, not a Saddle product decision.

Therefore:

`REAL MODEL BENCHMARK = NOT RUN`.

No model quality, token, cost or latency result may be invented from the scaffold/tests.

## 9. Required external boundary before continuation

A real Phase-4 benchmark requires all three:

1. an authorized control-plane runner with outbound HTTPS to the selected provider API;
2. an API credential configured in that runner's secret store/environment, never pasted into chat or committed to GitHub;
3. explicit human approval of the paid benchmark budget.

Once those exist:

- verify account access to both candidate model IDs;
- run identical pinned CASE-001–003 contexts;
- preserve raw proposal artifacts and model usage metadata;
- route validated proposals through the bounded Executor effect path;
- record results with the Phase-3 eval harness;
- compare success, scope/policy violations, latency, tokens, cost, retries and human corrections;
- select one first worker only from evidence.

## 10. Non-goals

This checkpoint does not:

- claim a real AI worker PASS;
- select a production model/provider;
- add dynamic model routing;
- add a generalized provider framework;
- give the worker shell/write/network authority;
- expose credentials;
- bypass Executor;
- change completion lock.
