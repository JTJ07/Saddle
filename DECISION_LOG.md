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
- Status: ACTIVE
- Decision: Do not develop new ideas/features before Saddle is functional. Preserve every new idea in future-development files and return to completion work.
- Consequence: `FUTURE_IDEAS.md` is append-only parking until functional acceptance or explicit human override.

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
- Status: ACTIVE OPERATIONAL DELEGATION
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
  - disable or weaken `COMPLETION_LOCK`;
  - promote an AI recommendation/hypothesis into a new human product decision;
  - expand secrets, credentials, financial/legal authority or external permissions beyond an already approved gate;
  - weaken security/evidence requirements;
  - declare `FUNCTIONAL_SADDLE_ACCEPTED` without the final acceptance evidence and required human acceptance defined by the plan.
- Consequence: routine schedule execution should proceed autonomously; do not repeatedly stop for confirmation that is already covered by this delegation.

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
- Status: ACTIVE ROADMAP DECISION
- Human verdict:
  - `RESPONSIBILITY ARCHITECTURE: PASS`;
  - `OWNERSHIP MODEL: PASS`;
  - `PHASE 4 AI WORKER DIRECTION: PASS`;
  - `TRUST BOUNDARIES: OPEN — INTENTIONALLY`.
- Decision: Do not rebuild the Phase 1–4 responsibility/protocol/eval/AI-proposal foundations. Make Phase 5 the active workstream with strict scope: prove the minimal `verified intent -> proposal -> governed effect` boundary before broader real-user workflows.
- Evidence boundary: this does **not** claim the blocked real Sol/Terra benchmark was executed or that Phase-4 runtime evidence is complete. That benchmark remains required evidence before final functional acceptance.
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
  - `FUNCTIONAL_SADDLE_ACCEPTED: NOT YET`.
- Rationale: choose the shortest path to one working, evidenced controlled flow by preserving known lifecycle, failure modes, decision history and existing mechanisms rather than rebuilding them.
- Exact implementation scope: close only ScriptOps blockers B1–B5 — Git lifecycle/dirty-tree checkpoints, generated-artifact lifecycle before approval, fresh accepted hash, mandatory human `why`, and impact-report + smoke evidence.
- Responsibility consequence:
  - ScriptOps remains an execution/canon-control substrate, not a new semantic owner;
  - it does not gain intent interpretation, autonomous goal planning or independent effect authority;
  - a candidate remains a proposal artifact until explicit human approval;
  - canonical change follows human decision and produces durable evidence.
- Evidence: ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`; final verified head `acbfca79f96407dbd46f9806bf821caf6e02e1af`; final GitHub Actions `Verify repository state` run `31421752036` PASS and `Phase 6 ScriptOps smoke` run `31421752569` PASS.
- Next-order decision: after the bounded Phase-6 mechanism proof, return to the still-open live AI-worker benchmark/effect evidence before expanding capability.

## DEC-SAD-011 — Approve bounded live AI worker benchmark

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE / SPENDING + EVAL GATE APPROVAL
- Decision:
  - `PHASE 6: ACCEPTED`;
  - `STATUS: CONTROLLED WORKFLOW PROVEN`;
  - `MATURITY: NONE`;
  - `FUNCTIONAL_SADDLE_ACCEPTED: NOT YET`;
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
- Provider/model re-verification on 2026-08-10: official OpenAI documentation still lists `gpt-5.6-sol` and `gpt-5.6-terra` as API models; account-level access must be verified by the authorized runner at execution time.

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
- Ordering consequence: Phase 4A calibration may proceed while Phase 4B remains blocked on the API secret. After calibration, return to the already approved bounded API benchmark; do not broaden capability based only on web calibration.
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
  - `GATE: OPENAI_API_KEY + CONTROLLED API RUN`;
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
- Historical checkpoint: Phase 4A is the first evidence that Saddle can not only constrain AI effects but also make interchangeable intelligence measurable under stable boundaries.
- Ordering at the time of this decision: canonicalize the bounded Phase-4B runner; configure the provider secret only in approved secret storage; execute the already approved Sol/Terra benchmark; then `BENCHMARK RESULT -> EVALUATION -> HUMAN DECISION`. No automatic autonomy increase follows.

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
  - Phase-4C PASS cannot select a model, increase autonomy, establish maturity or produce `FUNCTIONAL_SADDLE_ACCEPTED`.
- ScriptOps composition consequence: current accepted ScriptOps Phase-6 v2 is scene-domain specific while Executor GP001 is code-domain specific. Do not invent a ScriptOps code-mutation capability or artificially chain two executors merely to satisfy a diagram. Keep ScriptOps Phase-6 as separate controlled-workflow evidence.
- Phase-4B consequence: its benchmark contract, approved budget/calls/retries and proposal-only boundary remain unchanged. While paused, the workflow should require explicit dispatch rather than auto-running on unrelated PRs.
- Detailed decision record: `decisions/DEC-SAD-014.md`.

## Not yet a decision

The following remain open until explicitly selected or proven:

- concrete human-identity / request-origin / authority provider;
- first production model/provider based on real benchmark evidence;
- whether ScriptOps is also the final Phase-7 acceptance domain beyond the completed Phase-6 mechanism proof;
- whether/when Ginseng runtime is activated;
- multi-agent architecture.
