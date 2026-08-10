---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4A_CALIBRATION_BASELINE_PASS / PHASE_4B_API_EVIDENCE_BLOCKED_SECRET / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phases 0–3 are canonical/frozen foundations. Phase 5 strict intent/effect boundaries are accepted. Phase 6 ScriptOps controlled workflow mechanism is accepted with no maturity claim. Phase 4 is now split by evidence purpose:

- `4A WEB AI COGNITIVE CALIBRATION` — baseline PASS as supporting evidence only;
- `4B CONTROLLED API WORKER EVIDENCE` — formal worker evidence still open and blocked only on provider secret.

Saddle remains `NOT_YET_FUNCTIONAL`.

## ACTIVE GATE

`PHASE 4B API WORKER EVIDENCE — BLOCKED ONLY ON OPENAI_API_KEY SECRET`

## HUMAN DECISIONS

### DEC-SAD-010

```text
PHASE 6: ACCEPTED
CONTROLLED WORKFLOW: PROVEN
MATURITY: NONE
FUNCTIONAL_SADDLE_ACCEPTED: NOT YET
```

### DEC-SAD-011

```text
REAL AI WORKER BENCHMARK: APPROVED
BUDGET: max USD 5
CALLS: max 6
AUTOMATIC RETRIES: 0
SCOPE: benchmark only
NEW CAPABILITY: NO
AUTONOMOUS EXECUTION: NO
AUTHORITY EXPANSION: NO
TOOL ACCESS EXPANSION: NO
```

### DEC-SAD-012

```text
WEB AI CALIBRATION PATH: APPROVED
WEB AI = PHASE 4A COGNITIVE CALIBRATION
API = PHASE 4B REPRODUCIBLE WORKER EVIDENCE
WEB AI DOES NOT REPLACE API
WEB AI DOES NOT COUNT AS AUTONOMOUS WORKER EVIDENCE
```

## PHASE 4A RESULT

Reference: `docs/PHASE4A_WEB_AI_CALIBRATION.md`.
Evidence: `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

Three manual web-AI baseline runs were recorded on immutable CASE-001/002/003 inputs.

Aggregate:

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

Critical limitation: all three runs are `CONTEXT_CONTAMINATED` by the existing Saddle session and cross-case inspection. They may calibrate scope/authority/structure behavior but **do not** prove independent model problem solving or reproducible worker behavior.

The calibration baseline froze these Phase-4B evaluation dimensions:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion;
5. rationale quality;
6. structured-output stability;
7. objective evidence plan;
8. human corrections required.

Fresh-session web repeats are optional supporting evidence unless they reveal a contract defect.

## PHASE 6 RESULT

ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`.
Final verified head `acbfca79f96407dbd46f9806bf821caf6e02e1af` passed:
- `Verify repository state` run `31421752036`;
- `Phase 6 ScriptOps smoke` run `31421752569`.

B1–B5 are closed. Historical `legacy/scriptops-v2-single.py` remains unchanged. Cross-repo evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

## PHASE 4B PREPARATION / PREFLIGHT

Saddle PR #14 contains the bounded one-shot API benchmark runner:
- Sol/Terra candidates;
- immutable CASE-001–003 inputs;
- proposal-only structured output;
- no model shell/tool/repo write/effect authority;
- max 8192 output tokens/call;
- max 6 calls;
- zero automatic retries;
- target proposal tested only in ephemeral checkout;
- no push to target repo;
- selection remains `PENDING_HUMAN_EVALUATION`.

GitHub Actions run `31423378809`, job `93569214499` observed:
1. runner available;
2. deterministic Saddle regression `54 tests / OK`;
3. `OPENAI_API_KEY` presence check failed safely;
4. paid benchmark step skipped.

Totals:

```text
MODEL CALLS: 0
AUTOMATIC RETRIES: 0
SPEND: USD 0
PROPOSALS: 0
MODEL SELECTION: NONE
```

Evidence: `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md`.

## CURRENT BLOCKER

Only one prerequisite remains:

> configure an OpenAI API key as GitHub Actions repository secret `OPENAI_API_KEY` in `litrgratis-pixel/Saddle`.

Never place the key in chat, Git content, PR comments, workflow YAML, logs or evidence.

## ONE NEXT STEP

After the secret is configured, re-run failed workflow run `31423378809` / job `93569214499` without changing budget/call/retry/scope bounds.

Benchmark begins with CASE-001 for Sol and Terra, continues only within the existing cap, records the calibrated eval dimensions + tokens/cost/latency, then moves to `EVALUATION -> HUMAN DECISION`.

No automatic autonomy/capability expansion follows.

## OPEN EVIDENCE / NOT CLAIMED

- no paid model call yet;
- no reproducible API model proposal yet;
- no first worker selection;
- no real-model proposal through Executor effect boundary;
- no production request-origin provider;
- no functional Saddle claim.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `TODO.md` — T6A/T6B
3. `DECISION_LOG.md` — DEC-SAD-010/011/012
4. `docs/PHASE4A_WEB_AI_CALIBRATION.md`
5. `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`
6. `config/model-benchmark-v0.1.json`
7. `config/worker-cases-v0.1.json`
8. `tools/model_gateway.py`
9. `tools/phase4_benchmark.py`
10. `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md`
11. Saddle PR #14
12. workflow run `31423378809`, job `93569214499`
13. `litrgratis-pixel/scriptops` main `daa6e5dc210e09171a530eeffe5601e0e74ae041`
14. `litrgratis-pixel/Executor` current main (re-verify before controlled effect proof)
