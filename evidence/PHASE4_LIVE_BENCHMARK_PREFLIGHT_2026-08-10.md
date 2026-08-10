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

`DEC-SAD-012` + `DEC-SAD-013` distinguish and close the calibration gate:

```text
PHASE 4A = ACCEPTED WEB AI COGNITIVE CALIBRATION
PHASE 4B = CONTROLLED REPRODUCIBLE API WORKER EVIDENCE
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

## Historical preflight — PR #14

PR #14 produced run `31423378809` / job `93569214499`:
- GitHub-hosted runner available;
- repository token contents read-only;
- full deterministic Saddle suite: `54 tests / OK`;
- `OPENAI_API_KEY` absent;
- paid benchmark skipped;
- calls `0`, retries `0`, spend `USD 0`, proposals `0`.

PR #14 was closed without merge and retained only as historical provenance.

## Canonical runner preflight — PR #15

PR #15 contained exactly four runner/evaluation files:
- `.github/workflows/phase4-live-ai-benchmark.yml`;
- `tools/model_gateway.py`;
- `tools/phase4_benchmark.py`;
- `tools/phase4_live_benchmark.py`.

Preflight run `31425549563` / job `93576264688`:
- deterministic scaffold tests PASS;
- credential gate: `SECRET ABSENT`;
- paid benchmark: `SKIPPED`;
- calls `0`;
- retries `0`;
- spend `USD 0`;
- proposals `0`;
- selection `NONE`.

PR #15 was subsequently merged to `main` as:

`3547d42266c8711df35d7694b2839a5be3a11200`

Therefore runner merge/rebase housekeeping is CLOSED. The current benchmark code is canonical on `main`.

## Runner boundary proved by preflight

The runner enforces:
- immutable CASE-001/002/003 inputs;
- Sol/Terra comparison beginning with CASE-001 for both;
- strict proposal-only structured output;
- max `8192` output tokens/call;
- max `6` calls;
- `0` automatic retries;
- USD `5` hard cap;
- no model shell/tools/repository write/effect authority;
- proposal application only in ephemeral checkout;
- pinned target tests + full tests;
- no target-repository push;
- selection remains `PENDING_HUMAN_EVALUATION`.

The Phase-4B evaluation contract now contains nine dimensions, including intent preservation against the preserved human-approved intent. Intent preservation is an evaluation criterion, not an automated semantic-authority mechanism.

## Exact remaining external blocker

The only missing prerequisite for executing the approved Phase-4B model calls is:

> configure `OPENAI_API_KEY` as a GitHub Actions repository secret for `litrgratis-pixel/Saddle`.

Never place the credential in chat, repository files, PR comments, workflow YAML, logs or evidence.

After configuration, rerun the approved benchmark workflow under unchanged bounds.

## Evidence boundary

This preflight is not REAL AI WORKER EVIDENCE. It proves authorization, canonical runner availability, deterministic pre-model regression and correct fail-closed behavior when the secret is absent.

It does not prove a real API proposal, independent worker solving, model cost/latency/tokens, model selection, Executor effect execution or `FUNCTIONAL_SADDLE_ACCEPTED`.
