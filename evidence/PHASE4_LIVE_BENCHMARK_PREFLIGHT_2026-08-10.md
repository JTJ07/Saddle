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

Immediately before the first attempted Phase-4B run, official OpenAI documentation was checked again and still listed `gpt-5.6-sol` and `gpt-5.6-terra` as API models. Public availability does not prove account-level access.

## Historical preflight — PR #14

PR #14 produced run `31423378809` / job `93569214499`:
- GitHub-hosted runner available;
- repository token contents read-only;
- full deterministic Saddle suite: `54 tests / OK`;
- `OPENAI_API_KEY` absent;
- paid benchmark skipped;
- calls `0`, retries `0`, spend `USD 0`, proposals `0`.

After the 4A/4B canon moved `main`, PR #14 became non-mergeable. It was closed without merge and retained only as historical provenance.

## Current runner preflight — PR #15

Current exact runner:

```text
branch: agent/phase4b-runner-rebased
PR: #15
head: e4f0105b614f5de7cfa6393e6e49327e7505d9fb
functional diff: exactly 4 runner/evaluation files
```

Only these files differ:
- `.github/workflows/phase4-live-ai-benchmark.yml`;
- `tools/model_gateway.py`;
- `tools/phase4_benchmark.py`;
- `tools/phase4_live_benchmark.py`.

No duplicate governance/state is carried by PR #15.

Preflight run `31425549563` / job `93576264688`:
- deterministic scaffold tests PASS;
- credential gate: `SECRET ABSENT`;
- paid benchmark: `SKIPPED`;
- calls `0`;
- retries `0`;
- spend `USD 0`;
- proposals `0`;
- selection `NONE`.

At initial post-preflight inspection GitHub reported the PR mergeable. Subsequent direct main-only documentation/evidence commits caused the branch to diverge from current `main`; a later PR snapshot reports `mergeable: false`.

Do **not** infer a code-contract failure from that status. The functional PR diff remains only the four runner/evaluation files, and benchmark execution does not require merge. Re-evaluate/rebase routinely before eventual merge after evidence collection. This is not a new human semantic blocker.

## Runner boundary proved by preflight

The runner is prepared to enforce:
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

## Exact remaining external blocker

The only missing prerequisite for executing the approved Phase-4B model calls is:

> configure `OPENAI_API_KEY` as a GitHub Actions repository secret for `litrgratis-pixel/Saddle`.

Never place the credential in chat, repository files, PR comments, workflow YAML, logs or evidence.

After configuration, rerun PR #15 workflow run `31425549563` / job `93576264688` under unchanged approved bounds. Rebase/merge housekeeping may be completed after evidence collection without changing the benchmark contract.

## Evidence boundary

Neither preflight is REAL AI WORKER EVIDENCE. They prove only authorization, runner availability, deterministic pre-model regression and correct fail-closed behavior when the secret is absent.

They do not prove a real API proposal, independent worker solving, model cost/latency/tokens, model selection, Executor effect execution or `FUNCTIONAL_SADDLE_ACCEPTED`.
