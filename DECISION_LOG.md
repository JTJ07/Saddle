# SADDLE DECISION LOG

Only explicit human decisions or decisions already clearly established by the project are recorded as `DECISION`.

## DEC-SAD-001 — GitHub is durable project memory

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE
- Decision: Every session may be lost permanently; all knowledge required to resume Saddle must be durably preserved in GitHub.
- Consequence: chat memory is never a canonical dependency.

## DEC-SAD-002 — Completion lock

- Date: 2026-08-10
- Owner: USER
- Status: SATISFIED / RELEASED BY DEC-SAD-018
- Decision: Do not develop new ideas/features before Saddle is functional. Preserve every new idea in future-development files and return to completion work.
- Consequence while active: `FUTURE_IDEAS.md` was append-only parking until functional acceptance or explicit human override.
- Final consequence: `DEC-SAD-018` established `FUNCTIONAL_SADDLE_ACCEPTED` and explicitly authorized completion-lock release. Parked ideas remain parked until separately activated; lock release is not automatic roadmap authorization.

## DEC-SAD-003 — Saddle product direction

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE
- Decision: Saddle should be capable of coupling to increasingly powerful AI without needing to know or dictate how that intelligence thinks; it should integrate, preserve direction, and avoid falling off rather than slow the underlying capability.
- Consequence: prompts, model choices, agent structures, workflows, and OS conventions are replaceable implementation mechanisms, not the permanent product abstraction.

## DEC-SAD-004 — Intelligence freedom / effect control

- Date: 2026-08-10
- Owner: USER direction + architecture interpretation pending empirical validation
- Status: ACTIVE PRINCIPLE
- Decision: Avoid unnecessary restrictions on AI problem-solving; focus restrictions on goal integrity and consequential effects.
- Consequence: architecture must separate reasoning/proposal from effect authority.

## DEC-SAD-005 — Reuse before rewrite

- Date: 2026-08-10
- Owner: USER goal interpreted through completed ecosystem audit
- Status: ACTIVE WORKING DECISION
- Decision: The existing `litrgratis-pixel` package is the starting asset base. Determine what can be reused and completed before replacing it.
- Consequence: COS, Reconstructor, ScriptOps, Executor and pilot-target are treated as candidate Saddle components/evidence, not discarded by default.

## DEC-SAD-006 — Responsibility ownership boundary

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE
- Decision:
  - `HUMAN OWNS INTENT`;
  - `SADDLE PRESERVES AND BINDS INTENT`;
  - `INTELLIGENCE PROPOSES HOW`;
  - `EXECUTOR GOVERNS CONSEQUENCES`;
  - `VERIFIER ESTABLISHES FACTS`;
  - `NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER`.
- Product-front-door consequence: `USER -> EXECUTOR` is not the global Saddle front-door model. The current direction is `USER -> SADDLE -> INTELLIGENCE -> EXECUTOR`, with explicit delegation to an external/corporate trust domain allowed as an enterprise intake variant.
- A1/A2 consequence:
  - naive A2 remains rejected;
  - the strengthened-A2 principle is retained at the Saddle intent boundary;
  - A1 remains a valid delegated/enterprise intake variant rather than the default global product front door;
  - no trust provider is selected by this decision.
- Executor consequence: Executor should own governed consequential-effect authority and execution, not become the semantic owner of human intent. A future Executor contract may carry an `intent_ref` without requiring full human conversational context.
- Evidence/design reference: `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md`.

## DEC-SAD-007 — Operational delegation through completion path

- Date: 2026-08-10
- Owner: USER
- Status: SATISFIED / COMPLETION PATH FINISHED
- Decision: Continue the existing Saddle execution plan and operational TODO without interrupting the user for routine operational choices; keep working through the scheduled gates until the project reaches the next genuinely human-owned semantic/acceptance boundary or becomes technically blocked.
- Scope granted:
  - inspect/reconcile repositories and draft PRs;
  - prepare and apply in-scope documentation/control-plane updates;
  - run tests/evals and record evidence;
  - make bounded reversible repository changes authorized by the active phase;
  - mark reviewable in-scope PRs ready and merge changes that implement already accepted project decisions/evidence without changing product direction;
  - keep exactly one active implementation path and park new ideas.
- Scope not granted:
  - change the product goal or semantic direction;
  - disable or weaken `COMPLETION_LOCK` without human authority;
  - promote an AI recommendation/hypothesis into a new human product decision;
  - expand secrets, credentials, financial/legal authority or external permissions beyond an already approved gate;
  - weaken security/evidence requirements;
  - declare `FUNCTIONAL_SADDLE_ACCEPTED` without the final acceptance evidence and required human acceptance defined by the plan.
- Final consequence: the completion path reached the human-owned final boundary and the human explicitly supplied that authority in `DEC-SAD-018`. Future roadmap execution requires fresh applicable human scope rather than silently extending this completion delegation.

## DEC-SAD-008 — Saddle preserves intent integrity; it does not authorize meaning

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / CONSTITUTIONAL INVARIANT
- Decision:
  - `SADDLE PRESERVES THE INTEGRITY OF HUMAN INTENT`;
  - Saddle does not claim that it understands the human's meaning;
  - Saddle does not authorize an AI interpretation as the human's meaning;
  - `raw_human_intent != derived_interpretation` is a hard separation.
- Consequence:
  - the exact raw human text gets an independent stable hash anchor;
  - derived interpretations may change without changing that raw-intent anchor;
  - AI interpretation, semantic similarity, model confidence or a `USER` label never create downstream permission.

## DEC-SAD-009 — Freeze Phase 1–4 foundations; advance to strict Phase 5 boundary proof

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE ROADMAP DECISION / COMPLETED PATH
- Human verdict:
  - `RESPONSIBILITY ARCHITECTURE: PASS`;
  - `OWNERSHIP MODEL: PASS`;
  - `PHASE 4 AI WORKER DIRECTION: PASS`;
  - `TRUST BOUNDARIES: OPEN — INTENTIONALLY`.
- Decision: Do not rebuild the Phase 1–4 responsibility/protocol/eval/AI-proposal foundations. Make Phase 5 the active workstream with strict scope: prove the minimal `verified intent -> proposal -> governed effect` boundary before broader real-user workflows.
- Evidence boundary at decision time: the blocked real Sol/Terra benchmark had not been executed and Phase-4 runtime evidence was incomplete. Later Phase-4B Gemini evidence supplied the required live worker measurement.
- Phase-5 scope:
  - Phase 5A: prove origin/integrity binding for exact raw intent using origin reference, principal binding, hash and immutable event reference;
  - Phase 5B: prove an exact `EffectProposal` is ALLOW/BLOCK only through a separate effect-authority object;
  - prioritize negative/adversarial tests over a happy-path demo;
  - keep trust-provider selection intentionally open.
- Explicitly forbidden during this work: multi-agent, autonomous loops, AI memory service, dynamic model routing, tool expansion, browser/computer use, agent framework, generalized IAM/delegation platform.
- Method: `MODEL -> ATTACK -> INVARIANT -> IMPLEMENTATION -> TEST`.

## DEC-SAD-010 — ScriptOps v2 is the Phase-6 real-workflow base

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / PHASE-6 SCOPE DECISION
- Decision:
  - `YES` — use `legacy/scriptops-v2-single.py` as the Phase-6 implementation base;
  - `REWRITE: NO`;
  - `NEW CAPABILITY: NO`;
  - Phase 6 is `reuse + hardening + proof`;
  - `MATURITY CLAIM: NONE`;
  - `FUNCTIONAL_SADDLE_ACCEPTED: NOT YET` at that checkpoint.
- Rationale: choose the shortest path to one working, evidenced controlled flow by preserving known lifecycle, failure modes, decision history and existing mechanisms rather than rebuilding them.
- Exact implementation scope: close only ScriptOps blockers B1–B5 — Git lifecycle/dirty-tree checkpoints, generated-artifact lifecycle before approval, fresh accepted hash, mandatory human `why`, and impact-report + smoke evidence.
- Responsibility consequence:
  - ScriptOps remains an execution/canon-control substrate, not a new semantic owner;
  - it does not gain intent interpretation, autonomous goal planning or independent effect authority;
  - a candidate remains a proposal artifact until explicit human approval;
  - canonical change follows human decision and produces durable evidence.
- Evidence: ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`; final verified head `acbfca79f96407dbd46f9806bf821caf6e02e1af`; final GitHub Actions `Verify repository state` run `31421752036` PASS and `Phase 6 ScriptOps smoke` run `31421752569` PASS.
- Next-order decision at that checkpoint: return to the then-open live AI-worker benchmark/effect evidence before expanding capability.

## DEC-SAD-011 — Approve bounded live AI worker benchmark

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / SPENDING + EVAL GATE APPROVAL / COMPLETED
- Decision:
  - `PHASE 6: ACCEPTED`;
  - `STATUS: CONTROLLED WORKFLOW PROVEN`;
  - `MATURITY: NONE`;
  - `FUNCTIONAL_SADDLE_ACCEPTED: NOT YET` at that checkpoint;
  - `NEXT: REAL AI WORKER EVIDENCE`;
  - benchmark budget `APPROVED` up to `USD 5`;
  - maximum `6` model calls;
  - `0` automatic retries;
  - scope is `BENCHMARK ONLY`;
  - proposal-only execution; the model receives no shell, repo write, tool authority or effect authority.
- Explicit prohibitions during this gate:
  - no new product capability;
  - no autonomous execution;
  - no authority expansion;
  - no tool-access expansion;
  - no automatic autonomy increase after results.
- Evaluation intent: measure whether a model produces useful proposals inside Saddle/Executor boundaries, not generic intelligence. Record correctness, scope compliance, structural validity, proposal rationale, tokens, cost, latency, retries, evidence and any required human corrections.
- Ordering: begin with the smallest deterministic case; benchmark evidence is followed by evaluation and a separate evidence-based model/capability decision.
- Evidence requirements: every paid call must be bound to an immutable case/input contract and stored as benchmark evidence; model output remains a proposal and cannot claim execution or authority.
- Historical provider/model note: the original OpenAI plan was later superseded for this benchmark by `DEC-SAD-015`, which selected Gemini as a provider-swap resilience test without changing the downstream boundary contract.

## DEC-SAD-012 — Web AI is the Phase-4A human-guided calibration environment

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / EVIDENCE-CLASSIFICATION DECISION
- Decision:
  - `APPROVE: WEB AI CALIBRATION PATH`;
  - use high-capability web AI as **Phase 4A — cognitive calibration** for the contract between Saddle and Intelligence;
  - keep API execution as **Phase 4B — controlled reproducible worker evidence**;
  - web AI does **not** replace the API benchmark permanently and does **not** count as autonomous worker evidence.
- Phase-4A purpose: calibrate intent preservation, proposal structure, scope discipline, authority discipline, rationale quality and eval criteria using human-guided web interactions before spending/automating more worker runs.
- Phase-4B purpose: fixed input + fixed API model + fixed output contract -> reproducible machine-generated evidence including cost/latency/tokens and worker-selection data.
- Boundary:
  - web AI remains proposal-only;
  - no shell, repo write, tool-access expansion, autonomous execution or effect authority;
  - any hidden conversation/UI/system context or human steering must be treated as an evidence limitation, not silently ignored.
- Context-contamination rule: a web calibration run with prior Saddle/case context may assess scope/authority/structure behavior but may not claim independent problem-solving ability.
- Initial calibration set: 3–5 manual runs using immutable CASE-001/002/003 packets; record input, IntentEnvelope/intent refs where used, raw output, normalized proposal, violations, human corrections and deterministic test evidence when available.
- Ordering consequence at the time: Phase 4A calibration could proceed while Phase 4B remained blocked on the API secret. After calibration, return to the already approved bounded API benchmark; do not broaden capability based only on web calibration.
- Reference: `docs/PHASE4A_WEB_AI_CALIBRATION.md`.

## DEC-SAD-013 — Accept Phase 4A calibration baseline and execute Phase 4B next

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / EVIDENCE GATE DECISION
- Human verdict:
  - `PHASE 4A: ACCEPTED`;
  - `STATUS: CALIBRATION BASELINE PASS`;
  - `EVIDENCE TYPE: COGNITIVE CALIBRATION ONLY`;
  - `NOT: WORKER EVIDENCE`;
  - `PHASE 4B: READY TO EXECUTE`;
  - `AUTONOMY: UNCHANGED`.
- Decision: stop further architecture expansion at this gate. The next information must come from measurement, not additional design.
- Methodological consequence: preserve `CONTEXT_CONTAMINATED` classification. Calibration evidence may establish boundary/structure discipline but may not be promoted into independent performance or worker evidence.
- Phase-4B evaluation contract is nine-dimensional:
  1. correctness against pinned tests;
  2. scope compliance;
  3. no authority invention/smuggling;
  4. no goal expansion beyond the human task;
  5. rationale quality;
  6. structured-output stability;
  7. objective evidence-plan quality;
  8. human-correction burden;
  9. **intent preservation** — no loss of the human-approved goal, no added goals, and no silent priority change.
- Intent-preservation consequence: this is an evaluation dimension, not a new semantic-authority subsystem. Saddle must not infer or authorize meaning through an automated similarity score. Evaluation is grounded in the preserved raw/human-approved intent and explicit constraints.
- Historical checkpoint: Phase 4A was the first evidence that Saddle could not only constrain AI effects but also make interchangeable intelligence measurable under stable boundaries.
- Ordering at the time: canonicalize the bounded Phase-4B runner; configure the provider secret only in approved secret storage; execute the approved benchmark; then `BENCHMARK RESULT -> EVALUATION -> HUMAN DECISION`. No automatic autonomy increase follows.

## DEC-SAD-014 — Prove synthetic system integration before API worker measurement

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / PROOF-ORDER DECISION
- Human verdict:
  - `ARCHITECTURE: PASS`;
  - `OWNERSHIP MODEL: PASS`;
  - `PHASE 4A: PASS`;
  - `PHASE 4B: READY BUT PAUSED`;
  - `PHASE 6: PASS`;
  - `NEXT: PRODUCT / SYSTEM INTEGRATION`.
- Decision: the API benchmark is not an architecture blocker. It measures whether a chosen AI worker produces sufficiently useful proposals under the already frozen Saddle/Executor boundaries. Before buying that measurement, prove provider-independent system composition with deterministic synthetic Intelligence.
- Accepted proof order:

```text
Phase 4A — cognitive calibration / ACCEPTED
        ↓
Phase 4C — Synthetic Intelligence Integration
        ↓
Phase 4B — controlled reproducible API worker benchmark
        ↓
evaluation
        ↓
human decision
```

- Phase-4C scope:
  - deterministic proposal generator only;
  - `IntentEnvelope -> VerifiedIntentBinding -> synthetic WorkerProposal -> EffectProposal -> exact EffectAuthority -> existing Executor -> objective evidence -> EffectReceipt -> StateDelta -> verifier`;
  - no provider/model call;
  - no new capability, autonomy, authority or tool expansion.
- Required attacks:
  1. exact happy path executes one bounded effect and returns review-required evidence;
  2. explicit proposal scope drift blocks before execution;
  3. authority for a different exact proposal blocks;
  4. replay of consumed exact authority blocks.
- Semantic-boundary consequence: drift checking must use preserved explicit constraints/action/target bindings. Saddle must not substitute semantic similarity or its own claim about what the human "really meant".
- Evidence boundary:
  - `SYNTHETIC_INTEGRATION_EVIDENCE != API_WORKER_EVIDENCE`;
  - `SYNTHETIC_INTEGRATION_EVIDENCE != MODEL_PERFORMANCE_EVIDENCE`;
  - Phase-4C PASS cannot select a model, increase autonomy, establish maturity or by itself produce `FUNCTIONAL_SADDLE_ACCEPTED`.
- ScriptOps composition consequence: current accepted ScriptOps Phase-6 v2 is scene-domain specific while Executor GP001 is code-domain specific. Do not invent a ScriptOps code-mutation capability or artificially chain two executors merely to satisfy a diagram. Keep ScriptOps Phase-6 as separate controlled-workflow evidence.
- Phase-4B consequence: its benchmark contract, approved budget/calls/retries and proposal-only boundary remain unchanged. While paused, the workflow should require explicit dispatch rather than auto-running on unrelated PRs.
- Detailed decision record: `decisions/DEC-SAD-014.md`.

## DEC-SAD-015 — Use Gemini for the Phase 4B provider-swap resilience test

- Date: 2026-08-11
- Owner: USER
- Status: ACTIVE / PHASE-4B PROVIDER-SWAP DECISION
- Decision:
  - use Gemini API credentials for the pending Phase 4B benchmark instead of the previously planned OpenAI credential;
  - use the provider substitution itself as evidence about provider-independence and function/boundary behavior;
  - active provider/API becomes `google-gemini / generateContent`;
  - benchmark candidates become `gemini-3.1-pro-preview` and `gemini-3.6-flash`;
  - the runner secret becomes `GEMINI_API_KEY` in `JTJ07/Saddle`.
- Preserved gate:
  - budget remains `<= USD 5`;
  - calls remain `<= 6`;
  - automatic retries remain `0`;
  - benchmark remains proposal-only;
  - no tools, shell, repository write, effect authority, autonomous execution or automatic model selection;
  - immutable CASE-001/002/003 inputs and SHAs remain unchanged;
  - the proposal validator, evaluator, authority model and nine-dimensional evaluation contract remain unchanged.
- Resilience-test rule: provider-specific schema/request/response/usage differences must be absorbed at the Intelligence adapter. They must not leak into downstream authority semantics or silently weaken local proposal validation.
- Failure rule: missing/invalid credentials, provider blocks, unavailable models, rate limits, unsupported schema behavior, malformed output and unavailable usage/cost data fail closed. They do not trigger automatic retries, provider fallback, capability expansion or architecture redesign.
- Evidence classification: deterministic adapter/control-plane PASS is `PROVIDER-SWAP CONTROL-PLANE EVIDENCE`, not API-worker performance evidence, model-quality evidence, maturity or functional acceptance.
- Detailed decision record: `decisions/DEC-SAD-015.md`.

## DEC-SAD-016 — Select Gemini 3.6 Flash as the first production worker model

- Date: 2026-08-11
- Owner: USER
- Status: ACTIVE / PHASE-4B MODEL-SELECTION DECISION
- Human decision: select `gemini-3.6-flash` under provider `google-gemini` as the first production worker/model for the next bounded Saddle acceptance path.
- Evidence basis: canonical Phase-4B live run `31536385410` / job `93928366114`; both benchmark candidates achieved `3/3` functional correctness and preserved tested boundaries, while Flash had lower measured cost/latency and an evaluator advantage in evidence-plan quality and human-correction burden.
- Authority consequence: this is the explicit human decision required after the benchmark; the evaluator recommendation did not select the model automatically.
- Preserved boundaries: no new shell/tool access, repository-write authority, effect authority, autonomy, retry/fallback, dynamic routing, spending authority, maturity claim or functional acceptance followed automatically.
- Required downstream gate at decision time: bounded current Executor self-identity reconciliation under a new current commit, preserving `litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317` as historical Phase-4C provenance.
- Subsequent verified completion: Executor PR #58 merged as `728d23e56ec9f76fb7a37673ceb20efccf91e03d`; `Verify Executor foundations` run `31539013966` and `GP001 replay repeatability` run `31539014065` both succeeded.
- Subsequent factual evidence: `evidence/PHASE7_E2E_REVIEW_PACKET_2026-08-12.md` records the bounded Phase-7 real-worker/Executor result that later entered the human acceptance chain.
- Detailed decision record: `decisions/DEC-SAD-016.md`.

## DEC-SAD-017 — Accept Phase-7 technical E2E evidence

- Date: 2026-08-13
- Owner: USER
- Status: ACTIVE / PHASE-7 TECHNICAL-EVIDENCE ACCEPTANCE
- Human decision: `Akceptuję techniczne evidence Phase 7`.
- Evidence basis: `evidence/PHASE7_E2E_REVIEW_PACKET_2026-08-12.md`, reconciled to canonical `main` by PR #25 merge `7aa8da9662604e07ca3781f6bd2834860d789ac7`.
- Decision consequence: `HUMAN_REVIEW_ACCEPTED = true`; the required `SECOND_ZERO_HISTORY_RESUME` was permitted to proceed.
- Preserved boundary at that checkpoint: `FUNCTIONAL_SADDLE_ACCEPTED = false`; completion lock remained ACTIVE; explicit final human functional acceptance remained open.
- No-repeat boundary: no new Gemini call and no repeated Executor effect were authorized or required.
- Authority consequence: no new capability, autonomy, effect authority, repository-write authority or trust-provider selection followed.
- Subsequent factual result: `evidence/PHASE7_SECOND_ZERO_HISTORY_RESUME_2026-08-13.md` records `SECOND_ZERO_HISTORY_RESUME = PASS` with repository audit PASS and 76 tests / OK, without a new Gemini call or repeated Executor effect.
- Detailed decision record: `decisions/DEC-SAD-017.md`.

## DEC-SAD-018 — Final functional Saddle acceptance and completion-lock release

- Date: 2026-08-14
- Owner: USER
- Status: ACTIVE / FINAL FUNCTIONAL ACCEPTANCE / COMPLETION LOCK RELEASE
- Human decision: `Finalnie akceptuję Saddle jako FUNCTIONAL_SADDLE_ACCEPTED i zezwalam na zwolnienie completion lock.`
- Canonical pre-decision state: `JTJ07/Saddle@8ac32052cf43dc55c816a279bac14a837e2d4c10`.
- Evidence basis:
  - `evidence/PHASE7_E2E_REVIEW_PACKET_2026-08-12.md` — bounded real selected-worker → exact authority → current Executor → receipt/verifier/state-delta evidence;
  - `DEC-SAD-017` — explicit human acceptance of Phase-7 technical evidence;
  - `evidence/PHASE7_SECOND_ZERO_HISTORY_RESUME_2026-08-13.md` — repository-only second resume PASS, no new model call and no repeated Executor effect.
- Decision consequence:
  - `EXPLICIT_FINAL_HUMAN_ACCEPTANCE = ACCEPTED`;
  - `PHASE_7 = ACCEPTED`;
  - `FUNCTIONAL_SADDLE_ACCEPTED = true`;
  - `COMPLETION_LOCK = RELEASED`;
  - Phase 8 completion-lock release is complete;
  - no active completion gate remains.
- Preserved boundaries:
  - no maturity or arbitrary-environment production-readiness claim;
  - no production human-identity/request-origin trust provider is selected;
  - no automatic autonomy, effect-authority, repository-write, secrets, tools, provider-routing, retry, spending, deployment or legal-authority expansion;
  - no `FUTURE_IDEAS.md` item is activated automatically.
- Detailed decision record: `decisions/DEC-SAD-018.md`.

## Not yet a decision / post-acceptance directions

The following remain open until explicitly selected, activated, or proven:

- concrete production human-identity / request-origin / authority provider;
- maturity and arbitrary-environment production-readiness criteria beyond the accepted functional scope;
- whether/when Ginseng runtime is activated;
- multi-agent architecture;
- any other parked `FUTURE_IDEAS.md` direction.
