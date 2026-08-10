# PHASE 4B LIVE AI BENCHMARK — PREFLIGHT

Date: 2026-08-10
Status: `BLOCKED BEFORE PAID CALL / SECRET NOT CONFIGURED / USD 0 SPENT`
Evidence class: `API_RUNNER_PREFLIGHT / NOT WORKER EVIDENCE`

## Human authorization

Recorded as `DEC-SAD-011`:

```text
BENCHMARK: APPROVED
MAX BUDGET: USD 5
MAX MODEL CALLS: 6
AUTOMATIC RETRIES: 0
SCOPE: BENCHMARK ONLY
NEW CAPABILITY: NO
AUTONOMOUS EXECUTION: NO
AUTHORITY EXPANSION: NO
TOOL ACCESS EXPANSION: NO
```

`DEC-SAD-012` additionally distinguishes:

```text
PHASE 4A = WEB AI COGNITIVE CALIBRATION
PHASE 4B = CONTROLLED REPRODUCIBLE API WORKER EVIDENCE
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

## Provider/model re-verification

Immediately before the first attempted Phase-4B run, official OpenAI documentation was checked again and still listed:

- `gpt-5.6-sol` — flagship API model;
- `gpt-5.6-terra` — balanced-cost API model.

Public availability does not prove account-level access. Account-level access remains a runtime fact.

## Historical preflight — PR #14

Saddle PR #14 originally opened the one-shot GitHub Actions workflow:

- workflow: `Phase 4 live AI benchmark`;
- run ID: `31423378809`;
- job ID: `93569214499`;
- runner: GitHub-hosted Ubuntu 24.04 / Python 3.11;
- repository token permission: contents read only.

Before checking the provider secret, the workflow ran the complete Saddle deterministic suite:

```text
Ran 54 tests
OK
```

Credential gate result:

```text
BLOCKED: OPENAI_API_KEY repository secret is not configured for this runner.
```

The paid benchmark step was skipped.

After `DEC-SAD-012` and subsequent canonical state updates moved `main`, PR #14 became non-mergeable. It was closed without merge and explicitly retained as historical provenance. It must not be deleted or treated as the current runner.

## Current clean preflight — PR #15

A fresh runner branch was created from current `main`:

```text
branch: agent/phase4b-runner-rebased
PR: #15
head: e4f0105b614f5de7cfa6393e6e49327e7505d9fb
changed files: 4
```

Only runner/evaluation files are changed:
- `.github/workflows/phase4-live-ai-benchmark.yml`;
- `tools/model_gateway.py`;
- `tools/phase4_benchmark.py`;
- `tools/phase4_live_benchmark.py`.

No governance/state duplicate is carried by PR #15.

PR #15 is `mergeable: true` and is the active exact Phase-4B runner artifact.

Its preflight:

- workflow run ID: `31425549563`;
- job ID: `93576264688`;
- deterministic scaffold tests: `PASS`;
- credential presence gate: `FAIL / SECRET ABSENT`;
- paid benchmark step: `SKIPPED`.

Therefore, across the current clean preflight:

```text
MODEL CALLS ATTEMPTED: 0
AUTOMATIC RETRIES: 0
API BENCHMARK SPEND: USD 0
MODEL PROPOSALS: 0
MODEL SELECTION: NONE
CAPABILITY EXPANSION: NONE
AUTHORITY EXPANSION: NONE
```

## Runner boundary proved by preflight

The current runner is prepared to enforce:
- fixed immutable CASE-001/002/003 inputs;
- Sol and Terra compared beginning with CASE-001 for both;
- strict proposal-only structured output;
- max `8192` output tokens/call;
- max `6` calls;
- `0` automatic retries;
- USD `5` hard cap;
- no model shell/tools/repository write/effect authority;
- proposal application only in ephemeral target checkout;
- pinned target tests + full tests;
- no target-repository push;
- selection remains `PENDING_HUMAN_EVALUATION`.

## Exact remaining blocker

The only missing prerequisite for the approved Phase-4B benchmark is:

> configure an OpenAI API credential as the GitHub Actions repository secret named `OPENAI_API_KEY` for `litrgratis-pixel/Saddle`.

The credential must never be placed in chat, repository files, PR comments, workflow YAML, logs or benchmark evidence.

After the secret is configured, re-run PR #15 workflow run `31425549563` / job `93576264688` under unchanged approved bounds.

## Evidence boundary

Neither preflight is REAL AI WORKER EVIDENCE. Together they prove:
- human budget/scope authorization exists;
- a reproducible read-only CI runner exists;
- deterministic Saddle regression executes before model use;
- missing credential stops the path before paid/model execution;
- the current runner is cleanly rebased on the 4A/4B canon.

They do not prove:
- any real API model proposal;
- independent worker problem solving;
- model cost/latency/token measurements;
- model selection;
- Executor effect execution;
- `FUNCTIONAL_SADDLE_ACCEPTED`.
