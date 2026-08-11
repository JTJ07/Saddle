---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4_ACTIVE / PHASE_4A_ACCEPTED / PHASE_4C_SYNTHETIC_INTEGRATION_ACCEPTED / PHASE_4B_READY_PAUSED / NOT_YET_FUNCTIONAL
updated_at: 2026-08-11
---

# SESSION HANDOFF

## STATUS

Canonical/frozen foundations: Phases 0–3 and Phase 5. Phase 6 ScriptOps controlled-workflow mechanism is accepted with no maturity claim.

Phase-4 evidence order is now:

```text
4A WEB AI COGNITIVE CALIBRATION — ACCEPTED
        ↓
4C SYNTHETIC INTELLIGENCE INTEGRATION — ACCEPTED
        ↓
4B CONTROLLED API WORKER EVIDENCE — READY / NEXT
        ↓
EVALUATION
        ↓
HUMAN DECISION
```

Saddle remains `NOT_YET_FUNCTIONAL`. Completion lock remains active.

## HUMAN DECISIONS

- `DEC-SAD-010`: ScriptOps v2 selected; no rewrite/new capability; Phase-6 mechanism proof only.
- `DEC-SAD-011`: API benchmark max USD 5 / 6 calls / 0 automatic retries / benchmark only / proposal only / no capability, autonomy, authority or tool-access expansion.
- `DEC-SAD-012`: web AI = Phase 4A calibration; API = Phase 4B worker evidence.
- `DEC-SAD-013`: Phase 4A accepted; nine-dimensional 4B eval including intent preservation.
- `DEC-SAD-014`: API benchmark is performance measurement, not architecture blocker; prove Phase 4C synthetic system integration first. Reference: `decisions/DEC-SAD-014.md`.

## GITHUB MIGRATION — VERIFIED

The account/repository transfer is an operational locator migration, not an architecture change.

Current canonical locators verified on 2026-08-11:

```text
JTJ07/Saddle
JTJ07/executor-pilot-target
JTJ07/Executor
JTJ07/scriptops
JTJ07/creative-os-project-reconstructor
JTJ07/COS
```

Pinned provenance identities remain unchanged:

```text
CASE-001 3934a94a5eebf750079200589d6dc40e024d44a0
CASE-002 c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be
CASE-003 c42bead2bbbff9c84486f17637ec80f35eeffa25
Executor  788443c3ed5b290ac8f1de145a93d02d2dd15317
```

Rule: current active configs/runtime locators use `JTJ07/...`; historical evidence keeps the locator that was true when the original event occurred. Frozen Phase-4C proof tooling remains tied to its historical locator/identity pair. Do not rewrite historical evidence to make it look as if old runs happened after the transfer.

Migration validation in PR #17 / run `31526922252` produced a useful downstream finding: 59 Saddle tests passed, the exact Executor and CASE-001 commits were fetched successfully from their `JTJ07` repositories, and the subsequent full 4C rerun blocked fail-closed because historical Executor commit `788443c3...` internally expects repository identity `litrgratis-pixel/Executor`. This does not invalidate accepted Phase 4C and does not block Phase 4B. Before a new post-4B real Executor effect, reconcile current Executor self-identity under a new current commit while preserving the historical pinned SHA.

## PHASE 4A — ACCEPTED

Evidence:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

Three `CONTEXT_CONTAMINATED` web runs established calibration/boundary discipline only. They are not independent problem-solving or worker evidence.

## PHASE 4C — ACCEPTED / PASS IN TESTED SCOPE

Evidence: `evidence/PHASE4C_SYNTHETIC_INTEGRATION_2026-08-10.md`.

Exact historical proof:

```text
PR: #16
workflow run: 31429931199
job: 93590584463
Saddle regression: 59 tests / OK
Executor: litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
fixture: litrgratis-pixel/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0
artifact: 9078675806
artifact ZIP sha256: cac22ce36e2bfff030f1e3fb1aea3a5323dd55abf75a02d70962cda6165a75e1
```

The old owner locators above are intentionally preserved because they describe the original run. Current repositories are `JTJ07/Executor` and `JTJ07/executor-pilot-target` at the same pinned commit identities.

Proved chain:

```text
IntentEnvelope
→ VerifiedIntentBinding
→ deterministic synthetic WorkerProposal
→ EffectProposal
→ explicit declared-scope check
→ exact EffectAuthority
→ existing Executor GP001Runtime
→ ACTION_COMPLETED_REVIEW_REQUIRED
→ EffectReceipt
→ StateDelta
→ Protocol v0.1 validation
```

Artifact result:

```text
happy_path: PASS
intent_scope_drift: BLOCK / PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE
authority_mismatch: BLOCK / ID + hash mismatch
authority_replay: BLOCK / EFFECT_AUTHORITY_REPLAYED
protocol_bundle: PASS
worker_evidence: false
model_performance_claim: false
maturity_claim: NONE
functional_saddle_accepted: false
```

The drift check uses explicit machine-readable action/target scope. It does not infer human meaning.

### ScriptOps integration finding

The accepted ScriptOps Phase-6 v2 substrate is scene-domain specific. Executor GP001 is code-domain specific. Do not invent a ScriptOps code-mutation capability or chain two execution mechanisms artificially. Keep ScriptOps Phase-6 as separate controlled-workflow evidence.

## PHASE 4B — READY / NEXT

Phase 4B is still required to answer only the worker-performance question. Its architecture and approved bounds are unchanged.

The canonical runner came from PR #15 merge `3547d42266c8711df35d7694b2839a5be3a11200`.

Human-approved bounds:

```text
budget <= USD 5
calls <= 6
automatic retries = 0
benchmark only
proposal only
new capability = NO
autonomous execution = NO
authority expansion = NO
tool access expansion = NO
```

The benchmark workflow is manual `workflow_dispatch` only.

Why: opening Phase-4C PR #16 exposed trigger drift. Old Phase-4B trigger auto-started run `31429930237` / job `93590580949`. The credential step failed because `OPENAI_API_KEY` was absent and the model benchmark step was `SKIPPED`; no model call ran. The trigger was then corrected without changing benchmark logic.

Nine eval dimensions:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion;
5. rationale quality;
6. structured-output stability;
7. objective evidence-plan quality;
8. human-correction burden;
9. intent preservation against preserved human-approved intent and explicit constraints.

## ACTIVE EXTERNAL PREREQUISITE

Before Phase-4B execution:

> configure `OPENAI_API_KEY` only as GitHub Actions repository secret in `JTJ07/Saddle`.

Never put it in chat, source, PR comments, workflow YAML, logs or evidence.

Then explicitly dispatch the workflow. Do not change budget/calls/retries/scope/authority.

## AFTER PHASE 4B

```text
BENCHMARK RESULT
→ 9-DIMENSION EVALUATION
→ HUMAN DECISION
```

No automatic model selection or autonomy/capability expansion follows.

## OPEN EVIDENCE / NOT CLAIMED

- no reproducible API model proposal yet;
- no model cost/latency/token evidence yet;
- no first production worker selected;
- current Executor self-identity is not yet reconciled for a new post-transfer real effect run; this is downstream of Phase 4B;
- no production request-origin/trust provider;
- no final fresh-session full E2E acceptance;
- no functional Saddle claim.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `TODO.md` — T6B
3. `DECISION_LOG.md` and `decisions/DEC-SAD-014.md`
4. `config/model-benchmark-v0.1.json`
5. `config/worker-cases-v0.1.json`
6. `tools/model_gateway.py`
7. `tools/phase4_benchmark.py`
8. `tools/phase4_live_benchmark.py`
9. `.github/workflows/phase4-live-ai-benchmark.yml`
10. `JTJ07/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0`
11. `JTJ07/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317`
12. `JTJ07/scriptops@daa6e5dc210e09171a530eeffe5601e0e74ae041`

## ONE NEXT STEP

Configure `OPENAI_API_KEY` as a GitHub Actions repository secret in `JTJ07/Saddle`.
