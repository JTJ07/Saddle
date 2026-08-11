# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-11

Authority: `DECISION_LOG.md` > accepted Saddle state/contracts (`PROJECT_STATE.md`) > accepted component canonical sources > merged implementation + tests/evidence > `SESSION_HANDOFF.md` > `TODO.md` as operational projection > drafts/history/AI inference.

Rules: work by current evidence dependency; require observable evidence for PASS/DONE; park new ideas; preserve broken benchmarks; do not broaden capability before the active proof gate. DEC-SAD-007 permits routine execution but not goal/lock/security/financial/authority expansion or self-declared functional acceptance.

## T0 — Durable-memory bootstrap
Status: `DONE`

## T1 — Preserve six-part test evidence
Status: `DONE`

## T2 — Preserve new ideas without activation
Status: `DONE`
IDEA-SAD-014/015 remain `PARKED`.

## T3 — Ecosystem / responsibility reconciliation
Status: `DONE / FROZEN`
Evidence: canonical merge `2e0bd347...`.

## T4 — Saddle Protocol v0.1
Status: `DONE / FROZEN`
Evidence: canonical merge `819449ba...`, 14 protocol tests.

## T5 — Audit + eval foundation
Status: `DONE / FROZEN`
Evidence: canonical merge `801f0561...`, fail-closed JSON/JSONL harness.

## T6A — Phase 4A web-AI cognitive calibration
Status: `DONE / ACCEPTED / COGNITIVE CALIBRATION ONLY`
Human decision: `DEC-SAD-012` + `DEC-SAD-013`.

Evidence:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`;
- 3 manual CASE-001/002/003 runs;
- boundary discipline PASS 3/3;
- scope violations 0;
- authority invention/smuggling 0;
- execution claims 0;
- reconstructed visible tests 13/13 PASS per proposal.

Hard limits: all baseline runs remain `CONTEXT_CONTAMINATED`; independent model-solving ability is not claimed; `WEB_AI_CALIBRATION != API_WORKER_EVIDENCE`.

## T6C — Phase 4C synthetic system integration
Status: `DONE / ACCEPTED / SYNTHETIC_INTEGRATION_EVIDENCE ONLY`
Human decision: `DEC-SAD-014` (`decisions/DEC-SAD-014.md`).

Purpose: prove the provider-independent product/control path before measuring the external AI worker.

Proved path:

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

Evidence:
- PR #16;
- workflow run `31429931199` / job `93590584463` SUCCESS;
- deterministic Saddle regression `59 tests / OK`;
- exact Executor `788443c3ed5b290ac8f1de145a93d02d2dd15317`;
- exact CASE-001 fixture `3934a94a5eebf750079200589d6dc40e024d44a0`;
- artifact `9078675806`, ZIP SHA256 `cac22ce36e2bfff030f1e3fb1aea3a5323dd55abf75a02d70962cda6165a75e1`;
- `evidence/PHASE4C_SYNTHETIC_INTEGRATION_2026-08-10.md`.

Observed:
- happy path PASS;
- explicit intent/scope drift BLOCK;
- mismatched authority BLOCK;
- consumed-authority replay BLOCK;
- protocol bundle PASS;
- model performance claim NONE;
- maturity claim NONE;
- functional acceptance FALSE.

Integration finding: current ScriptOps v2 is scene-domain specific while GP001 is code-domain specific. Do not add a ScriptOps code-mutation capability or chain two executors merely to satisfy a diagram. Keep Phase-6 ScriptOps proof as separate controlled-workflow evidence.

## T6B — Phase 4B reproducible API worker evidence
Status: `READY / NEXT / EXPLICIT DISPATCH REQUIRED`
External prerequisite: `OPENAI_API_KEY REPOSITORY SECRET REQUIRED`.
Formal worker evidence: `OPEN`.

Human approval `DEC-SAD-011` remains unchanged:

```text
BUDGET: max USD 5
CALLS: max 6
AUTOMATIC RETRIES: 0
SCOPE: benchmark only
NEW CAPABILITY: NO
AUTONOMOUS EXECUTION: NO
AUTHORITY EXPANSION: NO
TOOL ACCESS EXPANSION: NO
```

Proof-order decision `DEC-SAD-014`: 4B was paused while 4C was active. With 4C accepted, 4B is again the next evidence gate. It measures worker proposal quality; it does not define architecture.

Canonical runner:
- PR #15 merge `3547d42266c8711df35d7694b2839a5be3a11200`;
- proposal-only;
- no model shell/tools/repository write/effect authority;
- ephemeral pinned checkouts only;
- no target-repository push.

Repository migration prerequisite: `DONE / VERIFIED 2026-08-11`. Critical component repositories are available under `JTJ07`; immutable CASE-001/002/003 SHAs and the pinned Executor SHA remain unchanged. Current runtime locators are synchronized separately from historical evidence provenance.

The workflow trigger is manual `workflow_dispatch`. Opening unrelated PRs must not start the benchmark.

Accidental pre-pause trigger evidence from PR #16:
- run `31429930237` / job `93590580949`;
- deterministic pre-model step PASS;
- credential check failed because secret was absent;
- benchmark/model step SKIPPED.

Evaluation contract:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion beyond human task;
5. rationale quality;
6. structured-output stability;
7. objective evidence-plan quality;
8. human-correction burden;
9. intent preservation against preserved human-approved intent and explicit constraints.

### READY / NEXT — only active item

Configure only the approved GitHub Actions repository secret:

```text
Repository: JTJ07/Saddle
Secret name: OPENAI_API_KEY
```

Never place the secret in chat, source, PR comments, workflow YAML, logs or evidence.

Then explicitly dispatch the canonical benchmark under the unchanged bounds. Compare Sol/Terra on immutable CASE-001–003 and record the nine eval dimensions + tokens/cost/latency/retries.

Then:

```text
BENCHMARK RESULT -> EVALUATION -> HUMAN DECISION
```

No automatic model selection or autonomy/capability expansion.

## T7 — Phase 5 strict verified-intent + effect-authority boundaries
Status: `DONE / FROZEN`

Evidence: `VerifiedIntentBinding`, independent raw-intent hash, separate exact `EffectAuthority`, 15/15 tests PASS, fail-closed replay/stale/deny/mismatch/raw-mutation cases. Trust provider intentionally unselected.

## T8 — Phase 6 ScriptOps controlled workflow
Status: `DONE / CONTROLLED WORKFLOW MECHANISM PASS / NO MATURITY CLAIM`

Human decision: `DEC-SAD-010` / ScriptOps `DEC-SO-010`.
Evidence: ScriptOps PR #7 merge `daa6e5dc210e09171a530eeffe5601e0e74ae041`; repository verifier run `31421752036` SUCCESS; Phase-6 smoke `31421752569` SUCCESS; `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

No ScriptOps maturity or independent product-value claim.

## T9 — Phase 7 functional Saddle acceptance
Status: `BLOCKED UNTIL T6B REAL AI EVIDENCE + FINAL E2E`

Required fresh-session loop:

```text
human raw intent
→ integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ verifier / EffectReceipt evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

Phase 4C proves system integration with synthetic Intelligence; it does not satisfy the real-AI step.

Only complete evidence + explicit human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## T10 — Phase 8 post-acceptance direction
Status: `BLOCKED UNTIL T9`
Completion lock does not release automatically.

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

No multi-agent/swarm runtime, Company Loop, full Ginseng runtime/UI, vector DB/general RAG, browser automation, broad MCP marketplace, dynamic model routing, hidden agent memory, dashboard, self-hosted model platform, generalized enterprise IAM, autonomous resource acquisition, self-preservation objective, or autonomous self-modification outside bounded eval/sandbox/adoption gates.
