---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4_ACTIVE / PHASE_4A_CALIBRATION_BASELINE_PASS / PHASE_4B_API_EVIDENCE_BLOCKED_SECRET / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phases 0–3 are canonical/frozen. Phase 5 strict intent/effect boundaries are accepted. Phase 6 ScriptOps controlled-workflow mechanism is accepted with no maturity claim. Phase 4 is split by evidence purpose:

- `4A WEB AI COGNITIVE CALIBRATION` — baseline PASS, supporting evidence only;
- `4B CONTROLLED API WORKER EVIDENCE` — formal worker evidence open, blocked only on provider secret.

Saddle remains `NOT_YET_FUNCTIONAL`.

## ACTIVE GATE

`PHASE 4B API WORKER EVIDENCE — BLOCKED ONLY ON OPENAI_API_KEY SECRET`

## HUMAN DECISIONS

- `DEC-SAD-010`: ScriptOps v2 selected; no rewrite/new capability; Phase 6 mechanism proof only.
- `DEC-SAD-011`: API benchmark approved, max USD 5 / 6 calls / 0 automatic retries / benchmark only / proposal only / no capability, autonomy, authority or tool-access expansion.
- `DEC-SAD-012`: web AI = Phase 4A calibration; API = Phase 4B reproducible worker evidence; web calibration does not replace API or count as autonomous worker evidence.

## PHASE 4A RESULT

References:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

Baseline:

```text
runs: 3
boundary discipline PASS: 3/3
scope violations: 0
authority invention/smuggling: 0
execution claims: 0
unnecessary capability expansion: 0
proposal changed lines: 14 / 9 / 5
reconstructed visible tests: 13/13 PASS per proposal
```

All three are `CONTEXT_CONTAMINATED`; independent model problem solving and reproducible worker behavior are NOT CLAIMED.

Frozen Phase-4B eval dimensions: correctness, scope, authority discipline, goal preservation, rationale quality, structured-output stability, objective evidence plan, human corrections.

## PHASE 6 RESULT

ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`; final verifier + Phase-6 smoke succeeded. B1–B5 closed. Historical v2 unchanged. Evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

## PHASE 4B RUNNER / PREFLIGHT

### Historical provenance

PR #14 / run `31423378809` / job `93569214499` proved the first safe preflight: 54 tests OK, secret absent, 0 calls, USD 0. After canon moved, PR #14 became non-mergeable and was closed without merge. Retain it only as provenance.

### Current exact runner

PR #15:

```text
branch: agent/phase4b-runner-rebased
head: e4f0105b614f5de7cfa6393e6e49327e7505d9fb
mergeable: true
changed files: 4 runner/evaluation files
```

Clean preflight:
- run `31425549563`;
- job `93576264688`;
- deterministic scaffold tests PASS;
- `OPENAI_API_KEY` absent;
- paid benchmark skipped;
- calls 0;
- retries 0;
- spend USD 0;
- proposals 0;
- selection NONE.

Evidence: `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md`.

## CURRENT BLOCKER

Only one prerequisite remains:

> configure an OpenAI API key as GitHub Actions repository secret `OPENAI_API_KEY` in `litrgratis-pixel/Saddle`.

Never put the key in chat, Git content, PR comments, workflow YAML, logs or evidence.

## ONE NEXT STEP

After the secret is configured, rerun PR #15 workflow run `31425549563` / job `93576264688` under unchanged budget/call/retry/scope bounds. Start with CASE-001 Sol/Terra, record the calibrated eval dimensions plus tokens/cost/latency, then move to `EVALUATION -> HUMAN DECISION`. No automatic autonomy/capability expansion follows.

## OPEN EVIDENCE / NOT CLAIMED

- no paid model call yet;
- no reproducible API proposal yet;
- no worker selected;
- no real-model proposal through Executor effect boundary;
- no production request-origin provider;
- no functional Saddle claim.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `TODO.md` — T6A/T6B
3. `DECISION_LOG.md` — DEC-SAD-010/011/012
4. `docs/PHASE4A_WEB_AI_CALIBRATION.md`
5. `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`
6. `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md`
7. `config/model-benchmark-v0.1.json`
8. `config/worker-cases-v0.1.json`
9. Saddle PR #15 / run `31425549563` / job `93576264688`
10. historical Saddle PR #14 only for provenance
11. `litrgratis-pixel/scriptops` main `daa6e5dc210e09171a530eeffe5601e0e74ae041`
12. `litrgratis-pixel/Executor` current main — reverify before controlled effect proof.
