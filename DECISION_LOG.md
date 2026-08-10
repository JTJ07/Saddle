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

## Not yet a decision

The following remain open until explicitly selected or proven:

- concrete human-identity / request-origin / authority provider;
- first production model/provider based on real benchmark evidence;
- whether ScriptOps RC1 is the final first real-domain acceptance case;
- whether/when Ginseng runtime is activated;
- multi-agent architecture.
