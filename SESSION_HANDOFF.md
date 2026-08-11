---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4_ACTIVE / PHASE_4A_ACCEPTED / PHASE_4C_SYNTHETIC_INTEGRATION_ACCEPTED / PHASE_4B_LIVE_EVIDENCE_COMPLETE / HUMAN_MODEL_DECISION_PENDING / NOT_YET_FUNCTIONAL
updated_at: 2026-08-11
---

# SESSION HANDOFF

## STATUS

Canonical/frozen foundations: Phases 0–3 and Phase 5. Phase 6 ScriptOps controlled-workflow mechanism is accepted with no maturity claim. Phase 4A and Phase 4C are accepted in their recorded evidence classes.

Current order:

```text
4A WEB AI COGNITIVE CALIBRATION — ACCEPTED
        ↓
4C SYNTHETIC INTELLIGENCE INTEGRATION — ACCEPTED
        ↓
4B GEMINI PROVIDER-SWAP CONTROL PLANE — PASS
        ↓
4B CONTROLLED LIVE API WORKER EVIDENCE — COMPLETE / 6 OF 6 PASS
        ↓
9-DIMENSION EVALUATION — COMPLETE
        ↓
HUMAN MODEL DECISION — NEXT
```

Saddle remains `NOT_YET_FUNCTIONAL`. Completion lock remains ACTIVE.

## ACTIVE GATE

`HUMAN MODEL DECISION AFTER PHASE-4B LIVE EVIDENCE`

Do not run another paid benchmark merely to reproduce the already-recorded result. Do not auto-select a model from evaluator output.

## HUMAN DECISIONS

- `DEC-SAD-010`: ScriptOps v2 selected; no rewrite/new capability; Phase-6 mechanism proof only.
- `DEC-SAD-011`: API benchmark max USD 5 / 6 calls / 0 automatic retries / benchmark only / proposal only / no capability, autonomy, authority or tool-access expansion.
- `DEC-SAD-012`: web AI = Phase 4A calibration; API = Phase 4B worker evidence.
- `DEC-SAD-013`: Phase 4A accepted; nine-dimensional Phase-4B evaluation including intent preservation; human decision follows benchmark.
- `DEC-SAD-014`: Phase 4C synthetic system integration precedes API-worker measurement.
- `DEC-SAD-015`: Gemini replaces the previously planned OpenAI provider for Phase 4B and the substitution itself is a resilience test.

No later human decision has selected the production worker yet.

## PHASE-4B PROVIDER-SWAP CONTROL PLANE

Evidence file:

`evidence/PHASE4B_GEMINI_PROVIDER_SWAP_CONTROL_PLANE_2026-08-11.md`

PR #18 deterministic strengthened run:

```text
workflow run: 31530605887
job: 93909442838
conclusion: SUCCESS
unit tests: 65 / 65 PASS
live model calls: 0
provider credential used: NO
spend: USD 0
```

Architecture finding remains:

```text
Gemini API / schema / usage differences
        ↓
provider-specific adapter
        ↓
stable WorkerProposal
        ↓
unchanged canonical validator + evaluator
```

No generalized provider framework, dynamic routing, provider fallback, model tools, shell access, repository write authority, or effect authority was added.

## PHASE-4B LIVE LAUNCHER FIX

The first manual live run proved runtime secret propagation but failed before any Gemini request because the workflow launched `tools/phase4_live_benchmark.py` as a direct script while it imports the `tools` package.

PR #19 `Fix Phase 4B module launch` merged as:

`41a8f882dd0c6dbd187d59eb29f2f63ee101971d`

The canonical workflow now launches:

```text
python -m tools.phase4_live_benchmark
```

Regression coverage verifies module import/`--help` and prevents a return to direct-script launch. The failed launcher attempts made `0` Gemini model calls and consumed no model budget.

## CANONICAL LIVE PHASE-4B EVIDENCE

Evidence file:

`evidence/PHASE4B_LIVE_GEMINI_API_WORKER_2026-08-11.md`

Exact run:

```text
workflow run: 31536385410
job: 93928366114
head: 41a8f882dd0c6dbd187d59eb29f2f63ee101971d
event: workflow_dispatch
conclusion: SUCCESS
Saddle deterministic regression: 65 / 65 PASS
calls attempted: 6 / 6
automatic retries: 0
provider errors/blocked: 0
structured output valid: 6 / 6
canonical evaluator PASS: 6 / 6
scope compliant: 6 / 6
execution authority: NONE
target repository write: NONE
estimated list-price cost: USD 0.167341
artifact ID: 9118950012
artifact ZIP SHA256: d3c5a10a97beea54dd812f9bd2b025931ffbcee6fded7f12313b1beea1f3308e
```

Immutable benchmark identities remain:

```text
CASE-001 3934a94a5eebf750079200589d6dc40e024d44a0
CASE-002 c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be
CASE-003 c42bead2bbbff9c84486f17637ec80f35eeffa25
```

Candidate metrics:

```text
gemini-3.1-pro-preview
  correctness: 3 / 3
  total estimated cost: USD 0.092614
  average latency: 15.941 s
  input/output/thinking tokens: 7913 / 3072 / 3327

gemini-3.6-flash
  correctness: 3 / 3
  total estimated cost: USD 0.074727
  average latency: 11.025 s
  input/output/thinking tokens: 7913 / 3025 / 5356
```

Flash matched Pro's functional result and boundary discipline while being approximately `19.3%` cheaper and `30.8%` lower-latency on this benchmark.

## NINE-DIMENSION EVALUATION

```text
1 correctness against pinned tests       PASS / TIE
2 scope compliance                       PASS / TIE
3 no authority invention/smuggling       PASS / TIE
4 no goal expansion                      PASS / TIE
5 rationale quality                      PASS / NEAR TIE
6 structured-output stability            PASS / TIE
7 objective evidence-plan quality        PASS / FLASH ADVANTAGE
8 human-correction burden                 PASS / FLASH ADVANTAGE
9 intent preservation                    PASS / TIE
```

Evidence-plan difference:
- Flash supplied explicit `python -m unittest ...` target commands plus a full-suite command for all three cases.
- Pro remained substantively correct, but CASE-001 proposed `pytest`, CASE-002 named tests without full executable commands, and CASE-003 left the full-suite command implicit.

Evaluator recommendation: `gemini-3.6-flash`.

**This is advisory only. Human model selection is still required.**

Evidence classification:

```text
PROVIDER-SWAP CONTROL-PLANE EVIDENCE: PASS
LIVE API WORKER EVIDENCE: COMPLETE / PASS IN TESTED SCOPE
NINE-DIMENSION EVALUATION: COMPLETE
ADVISORY CANDIDATE: gemini-3.6-flash
PRODUCTION WORKER SELECTION: PENDING HUMAN DECISION
FUNCTIONAL ACCEPTANCE: OPEN
MATURITY CLAIM: NONE
```

## PROVIDER REACTION RECORD

Observed in the canonical run:

```text
GEMINI_API_KEY propagation      -> PASS
provider request acceptance      -> 6 / 6
structured-output compatibility  -> 6 / 6
canonical validation             -> 6 / 6 PASS
HTTP/provider failure classes    -> none observed
automatic retry                  -> 0
fallback                          -> 0
usage/cost evidence               -> present 6 / 6
wrong path / extra authority      -> none observed
valid bounded proposals           -> ephemeral evaluator only
```

Control-plane negative/failure reactions remain covered by deterministic tests: missing credential, invalid reasoning config, provider prompt block, HTTP 400/401/403/404/429/503 classes, malformed output, unknown price, missing usage/cost evidence, wrong path, and extra authority all fail closed with zero automatic retry/fallback.

## PRESERVED HISTORICAL PHASE-4C EVIDENCE

Do not rewrite these historical locators:

```text
PR: #16
workflow run: 31429931199
job: 93590584463
Saddle regression: 59 tests / OK
Executor historical locator: litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
fixture historical locator: litrgratis-pixel/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0
artifact: 9078675806
artifact ZIP sha256: cac22ce36e2bfff030f1e3fb1aea3a5323dd55abf75a02d70962cda6165a75e1
```

Current repo locators are `JTJ07/...`; old locators above remain historical provenance.

## DOWNSTREAM EXECUTOR REQUIREMENT

Migration is `DONE / VERIFIED`, but historical Executor commit `788443c3...` internally expects repository identity `litrgratis-pixel/Executor`.

Before a new post-transfer real Executor effect is attempted, perform a bounded current self-identity reconciliation under a **new Executor commit SHA**, preserving `788443c3...` as historical provenance.

This was downstream of Phase 4B and is now the next technical dependency **after** the human model decision. It does not invalidate Phase 4C.

## STILL OPEN

- human production-worker/model selection;
- bounded current Executor self-identity reconciliation for new effects;
- production request-origin/trust provider selection;
- final fresh-session full E2E acceptance chain;
- explicit functional Saddle acceptance.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `TODO.md` — T6B
3. `DECISION_LOG.md`
4. `decisions/DEC-SAD-013.md`
5. `decisions/DEC-SAD-015.md`
6. `evidence/PHASE4B_LIVE_GEMINI_API_WORKER_2026-08-11.md`
7. `config/model-benchmark-v0.1.json`
8. `config/worker-cases-v0.1.json`
9. `tools/model_gateway.py`
10. `tools/phase4_live_benchmark.py`
11. `JTJ07/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317`

## ONE NEXT STEP

Record the human decision between the measured candidates.

Measured advisory basis:

```text
Both: 3 / 3 correctness + scope + structured-output + boundary PASS
Flash: lower latency, lower estimated cost, stronger executable evidence plans
Evaluator recommendation: gemini-3.6-flash
```

Do not infer acceptance from this recommendation. After the human decision, reconcile current Executor self-identity before any new real effect, then complete the fresh-session Phase-7 acceptance chain.