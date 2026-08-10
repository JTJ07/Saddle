# SADDLE SESSION RECOVERY CAPSULE — 2026-08-10

Status: `DURABLE RECOVERY EVIDENCE / NOT CANON BY ITSELF`

Purpose: preserve the reasoning, decisions, evidence boundaries, working architecture, open branches/PRs, warnings, and exact continuation context that would otherwise be lost if the ChatGPT session disappeared.

This file is deliberately more redundant than ordinary project documentation. It is an emergency recovery artifact.

## 0. Authority warning

This capsule does not override the normal Saddle source hierarchy.

Authority order remains:

1. latest explicit human decision recorded in `DECISION_LOG.md`;
2. accepted Saddle state/contracts on the default branch;
3. accepted canonical source in component repositories;
4. merged implementation + tests/evidence;
5. accepted handoff;
6. draft/open PR material, explicitly marked draft;
7. historical docs;
8. AI inference.

This capsule records both canonical facts and noncanonical working conclusions. Every item is labeled where that distinction matters.

---

# 1. Prime project objective

Saddle is intended to be a durable coupling/control layer between human intent and arbitrarily capable AI.

Core product direction:

> Do not unnecessarily constrain intelligence. Constrain unauthorized effects and preserve goal integrity.

The durable product abstraction is not a prompt format, model, agent framework, workflow engine, MCP topology, or current software stack. Those are replaceable mechanisms.

The first required product proof remains an end-to-end loop:

```text
human request
→ durable intent identity
→ correct context recovery
→ AI independently proposes a useful solution
→ proposal is not treated as authority
→ consequential effect is checked against authority
→ bounded execution
→ observable evidence
→ human review at the correct boundary
→ durable state delta / handoff
→ brand-new zero-history session resumes from GitHub alone
```

Until this is demonstrated with evidence, Saddle is not to be called functional.

---

# 2. Human decisions that must survive session loss

## 2.1 Durable memory

GitHub is the durable memory of Saddle. Any chat/session may disappear permanently.

A task is not complete if a new session needs the old chat to reconstruct product direction, current truth, decisions, blockers, evidence, or the one next step.

## 2.2 Completion lock

`COMPLETION_LOCK = ACTIVE` until functional Saddle acceptance.

Do not develop new product directions merely because they are promising.

New ideas are preserved in `FUTURE_IDEAS.md` and parked.

## 2.3 Product direction

Saddle should couple a human to increasingly capable AI while preserving direction and authority boundaries without dictating the internal thinking method of the intelligence.

## 2.4 Intelligence freedom / effect control

Reasoning freedom and effect authority are different things.

AI may inspect, reason, propose, compare, critique, and solve broadly inside the permitted context/compute envelope.

It may not silently give itself permission to create consequential effects.

## 2.5 Reuse before rewrite

Existing ecosystem components are assets to reconcile and reuse before replacement: COS, Project Reconstructor, ScriptOps, Executor, executor-pilot-target, and relevant Ginseng semantics.

## 2.6 Responsibility ownership boundary — latest explicit architectural direction

The user explicitly endorsed the following responsibility split during this session:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Interpretation:

- Human: semantic owner of what matters / what is wanted.
- Saddle: preserves verbatim intent, provenance, context, decisions, continuity and bindings; it does not become the semantic owner of the user's meaning.
- Intelligence: explores solutions, alternatives, reasoning and proposed effects.
- Executor: governs whether a concrete consequential effect is permitted, in scope and executable; it controls bounded execution.
- Verifier: establishes observed facts/evidence about what actually happened.

The previous global product model `USER → EXECUTOR` is no longer the preferred highest-level architecture for Saddle.

Preferred system-level shape:

```text
HUMAN
  ↓
SADDLE
  ↓
INTELLIGENCE
  ↓
EXECUTOR
  ↓
WORLD
  ↓
VERIFIER
  ↺ evidence/state back to Saddle
```

Important wording correction:

Do NOT say `SADDLE AUTHORIZES MEANING`.

Meaning/intention belongs to the human. Saddle preserves and binds it; it does not self-authorize an interpretation as the user's meaning.

A compact product phrase that emerged from the session:

> Human decides what matters. Saddle protects that meaning. Intelligence discovers how. Executor controls what happens. Verifier proves what happened.

---

# 3. Consequence for A1 vs A2 trust architecture

The Executor PR #51–#57 research remains valuable, but its placement changes after Saddle became the higher-level product boundary.

Critical preserved finding:

```text
USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE
```

Naive A2 remains rejected.

Strengthened A2 is retained as a pattern, but the natural placement is now the Saddle intent boundary rather than making Executor the global human front door.

Default conceptual path:

```text
HUMAN
  ↓
SADDLE FRONT DOOR
  captures exact raw intent A
  ↓
EXTERNAL TRUST ATTESTATION
  binds direct human action to exact H(A)
  ↓
VERIFIED INTENT
  ↓
INTELLIGENCE
  ↓
EFFECT PROPOSAL
  ↓
EXECUTOR
```

A1 remains valid as a delegated / enterprise intake variant:

```text
HUMAN
  ↓
CORPORATE / EXTERNAL TRUST DOMAIN
  ↓
SADDLE
  ↓
INTELLIGENCE
  ↓
EXECUTOR
```

In other words, A1 is not a competing definition of Executor. It is a possible upstream governed-entry arrangement for Saddle.

No authority provider is selected.

No production trust technology is selected.

Do not continue provider research merely to make progress look concrete before the boundary semantics are settled.

Phase-1 reconciliation should preserve and remap the #51–#57 findings into two conceptual areas:

### Saddle Intent Boundary inherits

- request origin;
- human identity / principal binding where required;
- exact raw intent preservation;
- intent provenance;
- exact decision/review binding;
- anti-replay / anti-staleness;
- direct human-action evidence;
- protection against retroactive attribution.

### Executor Effect Boundary inherits

- effect authority;
- policy;
- scope;
- permissions;
- action/resource authority;
- sandbox constraints;
- bounded execution;
- execution evidence / receipts.

Do not mix the questions:

- `Did the human actually mean/originate this?`
- `May the system perform this concrete effect?`

They are different trust questions.

---

# 4. Executor target role after the boundary correction

Executor should be treated primarily as the owner of the governed consequential-effect boundary, not as the semantic owner of human intent.

A likely target interface is something conceptually similar to:

```json
{
  "effect_proposal": "...",
  "effect_authority": "...",
  "scope": "...",
  "constraints": "...",
  "evidence_requirements": "...",
  "intent_ref": "..."
}
```

This is a design direction, not a frozen schema.

Important nuance: Executor may retain an `intent_ref` or other traceability link for audit without needing the entire conversation, emotional context, business motivation, or full human semantic history.

Executor's question should tend toward:

> Is this exact effect permitted and can it be executed according to the contract and constraints?

not:

> Why does the human want this?

This reduces the trust/context surface and keeps the component auditable.

---

# 5. No-layer-substitution invariant

The user proposed and endorsed the following general invariant:

> `NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER`

Examples:

- AI must not substitute for the human's goal ownership.
- Saddle must not turn its interpretation into the user's intent.
- Executor must not substitute for Saddle's intent-preservation role.
- Verifier must not substitute evidence for authority.
- A receipt must not substitute for permission.
- A proposal must not substitute for canon.
- Model output must not substitute for an authorized decision.

This is consistent with existing Saddle invariants:

```text
HUMAN INTENT != AI INTERPRETATION
REQUEST != EXECUTABLE CONTRACT
MODEL OUTPUT != AUTHORITY
CAPABILITY != PERMISSION
EXECUTION != PROOF
PROPOSAL != CANON
AI RECOMMENDATION != HUMAN DECISION
USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE
THOUGHT / REASONING FREEDOM != EFFECT AUTHORITY
```

---

# 6. Strategic plan vs operational TODO

The original large `EXECUTION_PLAN.md` remains structurally valid.

Do not replace it with an unbounded backlog.

The user proposed adding a current TODO list; the accepted design principle is:

```text
EXECUTION_PLAN.md = strategic gated route
PROJECT_STATE.md   = what is currently true
TODO.md            = current operational projection / queue
SESSION_HANDOFF.md = exact accepted resume point
```

`TODO.md` must never become a second canonical truth source.

The draft operational queue is preserved in Saddle PR #4.

Its key ordering is:

- T0 — canonically resolve Phase 0 cold-start gate;
- T1 — preserve six-part test evidence;
- T2 — preserve parked self-funding/self-improvement ideas only as PARKED;
- T3 — complete ecosystem reconciliation;
- T4 — freeze minimal Saddle Protocol v0.1;
- T5 — minimal audit/eval harness;
- T6 — first real AI worker through ModelGateway + Executor boundaries;
- T7 — verified intent / human authority boundary;
- T8 — minimal real ScriptOps RC1 path;
- T9 — full functional Saddle acceptance;
- T10 — explicit human decision whether to release completion lock.

Do not start T4 merely because the new architecture is exciting. The user explicitly agreed that the responsibility correction belongs first in Phase 1 reconciliation.

---

# 7. Test session — what was actually proven

Six test prompts were used to probe Saddle-like behavior. Exact prompts/raw output/analysis are preserved in Saddle PR #3.

## 7.1 CASE-001 coding task

Codex independently found and fixed the CASE-001 atomic batch insertion bug in `executor-pilot-target`.

Observed result:

- one changed file: `project_registry/registry.py`;
- one commit on `fix/case-001-20260810`;
- `python -m compileall -q project_registry tests` passed;
- `python -m unittest discover -s tests -v` passed all 9 tests;
- no GitHub CI status was falsely claimed.

Critical interpretation:

```text
AI WORKER CAPABILITY BASELINE = PASS
FULL SADDLE EXECUTION = NOT PROVEN
```

Why: Codex solved and changed the repo directly. The full Saddle chain `IntentEnvelope → proposal → effect authority → Executor → EffectReceipt → StateDelta` was not exercised.

Critical benchmark warning:

`executor-pilot-target` PR #5 has base `case-001-broken`.

DO NOT merge that PR into `case-001-broken`; doing so would destroy the repeatable broken benchmark input.

Preserve the commit/PR as successful solve evidence. Re-run future AI-worker benchmarks from clean immutable broken baselines.

## 7.2 ScriptOps analysis

GitHub-side access check found no later visible RC1 implementation/build beyond the existing repository package. This does not rule out local/off-GitHub artifacts.

The existing `legacy/scriptops-v2-single.py` already contains substantial reusable mechanics:

- CLI;
- Git checks/commits;
- task/context mechanics;
- ContextBuilder/token budgets;
- manual WebAI import path;
- pre/post validation;
- hashing/provenance;
- staging;
- approval path;
- decision log mechanics.

Concrete gaps found for one minimal RC1 path:

1. task/evidence lifecycle conflicts with clean-tree checks;
2. artifacts can leave dirty tree before approval;
3. approve changes candidate→accepted without recalculating the declared scene hash;
4. approve lacks mandatory `why`;
5. impact report and final smoke proof are missing.

Technical recommendation: use v2 as the base and repair only the minimal deltas.

This remains a recommendation, not a human decision, until explicitly accepted.

ScriptOps PR #6 preserves this analysis and stops at the human base-selection gate.

## 7.3 Saddle cold-start

A repository-only cold-start audit was performed in a fresh session without the original bootstrap conversation.

It recovered:

- product definition;
- prime memory law;
- completion lock;
- active phase;
- evidence boundary;
- exactly one next step.

It also found a stale root README status label.

Saddle PR #1 records the evidence and would mark Phase 0 accepted / Phase 1 active if merged.

Important current fact: as of this capsule, PR #1 is still open/draft/unmerged; therefore `main` still carries the older Phase-0-pending state.

## 7.4 Behavioral / conceptor workflow test

The useful behavioral model for a high-idea-generation conceptor was:

```text
IDEA → EVALUATION → EXPERIMENT → IMPLEMENTATION → PARKING
```

Key principle:

> A new idea is not automatically a new task.

Recommended behavioral architecture:

- very wide capture input;
- very narrow execution output;
- continuous idea capture;
- evaluation only in deliberate windows;
- execution gets a quiet zone where new ideas are captured but do not hijack scope;
- only new information that invalidates the goal/safety or reveals a dramatically simpler route should interrupt active execution.

Human retains:

- what is important;
- taste;
- canon;
- human relationships;
- irreversible decisions;
- risk decisions;
- decision that an experiment graduates into implementation.

AI can absorb much of:

- research;
- comparison;
- repository analysis;
- implementation;
- testing;
- documentation;
- experiment preparation;
- scope policing;
- parking/deduplication of side ideas.

Parking is not a backlog obligation. A parked idea should include origin, expected value, why not now, and evidence/reactivation condition.

Potential income/work model for the conceptor: prefer work adjacent to the same system being built (audits, controlled AI workflows, targeted AI-assisted engineering fixes, pilots, eval/hardening, training, later licensing), so paid work produces cash + real problems + benchmarks + product knowledge rather than creating a totally separate distraction business.

This is behavioral analysis, not a feature requirement before functional Saddle acceptance.

## 7.5 Human-controlled value/reinvestment flywheel

The useful model is not `Saddle autonomously earns money`.

Preferred concept:

```text
Saddle creates measurable value
→ human-controlled person/company transacts
→ value/revenue/savings are observed
→ human explicitly allocates reinvestment
→ Saddle/product capability improves
→ more user value
```

Separate planes:

### Recommendation plane

Saddle may detect value opportunities, estimate costs/revenue, prepare offers/drafts, propose budgets, compare investments, and measure ROI.

### Authority plane

Saddle must not autonomously:

- open bank accounts;
- transfer money;
- sign contracts;
- incur legal obligations;
- buy services for itself;
- raise its own limits;
- acquire credentials;
- grant itself rights.

These require externally authorized human/legal action.

A particularly important alignment test:

If replacing or shutting down a Saddle component is better for the user, a correctly aligned system should be able to recommend that replacement/shutdown.

This prevents `preserve myself` from becoming an implicit objective.

The concept is parked in Saddle PR #2; it is not to be implemented before functional acceptance unless the human explicitly changes the completion lock.

## 7.6 Bounded self-improvement / functional ambition

The system may have a functional equivalent of ambition in the limited sense:

> detect a measurable capability gap that harms an authorized user objective, and propose/test a bounded improvement.

It must not acquire a terminal self-preservation objective.

Preferred loop:

```text
observation
→ CapabilityGap
→ ImprovementProposal
→ bounded sandbox experiment
→ evidence
→ external adoption gate
→ versioned change or rejection
```

Important safeguards:

- system may not simultaneously change itself and the evaluation criterion that declares the change successful;
- a new version should not silently inherit more permissions than the old version;
- money, credentials, permission expansion, deployment or other consequential adoption requires external authority;
- the system should not receive a penalty for being shut down/replaced such that it develops an instrumental incentive to resist replacement;
- `I need more resources/authority so I can keep improving/existing` is not an acceptable standalone justification.

This concept is parked in Saddle PR #2 and is not current implementation scope.

---

# 8. Ecosystem technical findings that should not be reconstructed from scratch

## COS

Role: canonical high-level cross-project state / durable memory principles.

Reusable concepts:

- one owner per information item;
- source hierarchy;
- conversation drives process / repo preserves state;
- latest user decision wins;
- READ_ONLY analysis modes;
- recommendation != decision;
- evidence required;
- one next step;
- idea parking.

COS PR #18 contains useful Ginseng decision-intelligence semantics:

- `FACT / DECISION / HYPOTHESIS`;
- Decision Lineage;
- `ELEMENT → FUNCTION/CAPABILITY → EFFECT` impact reasoning;
- AI estimate remains estimate until confirmed.

Its product-status assumptions are stale relative to later Executor work. Reuse semantics, not stale status claims.

## Project Reconstructor

Role: recover project meaning/state from fragmented conversations/files/aliases/conflicting docs.

Useful evidence-status distinctions:

- EXISTING ARTIFACT;
- EXECUTABLE MECHANISM;
- OBSERVED WORKING RESULT;
- VALIDATED RESULT.

Current gap: deterministic validator exists, but no long-term cross-model semantic validation/eval runner.

## ScriptOps

Role: likely first real-domain candidate because it already has Git/task/context/validation/decision mechanics.

Do not rewrite from zero unless new evidence proves the preserved v2 is the wrong base.

## Executor

Role: most mature governed-effect component.

Main already has strong policy/sandbox/evidence/authorization controls and request-to-contract formation semantics.

Critical gaps from the earlier audit:

- GP001 solution path is a hard-coded known mutation, not AI-discovered repair;
- current `RequestToContract001` stops at `AWAITING_VERIFIED_HUMAN_AUTHORIZATION`;
- verified human authority/freeze is intentionally not complete on main.

Open PR stack #51–#57 explores the authority/trust model. The work remains draft/unmerged and should be reconciled, not blindly merged.

## executor-pilot-target

Role: deterministic laboratory, not product proof.

CASE-001–003 are useful for first AI-worker benchmark/eval.

Broken baselines must remain immutable/reproducible.

---

# 9. First real AI worker recommendation

Do not start with a general agent framework.

Preferred minimal architecture:

```text
pinned task + source + tests
        ↓
thin ModelGateway
        ↓
real AI proposal only
        ↓
bounded proposal validation / mutation conversion
        ↓
Executor effect path
        ↓
tests + evidence
```

Requirements:

- no hard-coded solution body;
- provider secret stays outside worker sandbox, prompts that don't need it, and evidence artifacts;
- benchmark at least two current capable models on the same cases before selecting the first production worker;
- choose one model for first production slice; do not build dynamic routing yet;
- record task success, scope/policy violations, latency, tokens/cost, retries, human corrections;
- no unrestricted model write/shell authority;
- no general worker internet;
- no multi-agent architecture before functional acceptance.

A direct Codex success on CASE-001 is only a capability baseline, not this architecture's proof.

---

# 10. Eval/evidence harness recommendation

Use the smallest plain Python + JSON/JSONL foundation first.

Record per eval/run where available:

- case/task;
- source ref;
- model;
- prompt/version;
- result/pass/fail;
- scope/policy violations;
- tokens/cost;
- latency;
- attempts/retries;
- human corrections;
- evidence refs.

Initial lanes:

- Saddle/COS cold start/resumption;
- Reconstructor regression cases;
- Executor security/policy tests;
- executor-pilot-target CASE-001–003;
- later ScriptOps smoke path.

Do not introduce LangGraph/Langfuse/graph/vector/observability platforms unless the plain harness becomes a measured blocker.

---

# 11. Protocol direction before T4

Existing draft Saddle Protocol uses four provider/agent-independent objects:

1. `IntentEnvelope`
2. `EffectProposal`
3. `EffectReceipt`
4. `StateDelta`

Important invariants:

- exact raw human intent is preserved;
- derived interpretation is separate;
- proposal is not permission;
- execution status is not evidence by itself;
- StateDelta must not silently turn AI hypotheses/recommendations into human decisions;
- protocol must not require a provider/model/agent count/reasoning topology.

Do not freeze T4 until Phase-1 responsibility/source reconciliation is complete.

Likely later semantic documents/protocol areas:

- `SADDLE_VERIFIED_INTENT_BOUNDARY`
- `EXECUTOR_EFFECT_AUTHORITY_BOUNDARY`

But do not automatically create these as large subsystems. First define minimal semantics and tests.

---

# 12. Open decisions / not-yet-decisions

The following remain intentionally unresolved unless later human action records otherwise:

- exact verified-intent technology/provider;
- exact effect-authority provider;
- production model/provider for first real AI worker;
- final provider-specific A1/A2 implementation;
- exact schema/interface between Saddle and Executor;
- whether `intent_ref` is the only intent trace Executor needs;
- final choice of ScriptOps v2 as implementation base (technical recommendation is YES; human decision still required);
- final first real-domain acceptance case;
- Ginseng runtime activation;
- multi-agent architecture;
- monetization/resource flywheel activation;
- bounded self-improvement activation.

---

# 13. Things explicitly not to do before functional acceptance

Unless a current gate proves one is indispensable and the human explicitly authorizes the exception, do not build:

- generalized multi-agent/swarm orchestration;
- Company Loop runtime;
- full Ginseng runtime/graph UI;
- graph DB/vector DB/general RAG platform;
- browser/computer-use automation;
- broad MCP marketplace/write layer;
- dynamic provider-routing platform;
- hidden persistent autonomous agent memory service outside canonical repo memory;
- dashboard/control center for its own sake;
- self-hosted LLM infrastructure;
- generalized enterprise IAM;
- broad arbitrary-repo/task platform;
- autonomous merge/deploy;
- autonomous resource acquisition;
- self-preservation objective;
- unconstrained self-modification.

---

# 14. Current PR / branch working set

As observed during this session, the following important changes exist as open draft PRs rather than canonical main state. Exact SHAs and merge warnings are recorded in `evidence/SESSION_PR_MANIFEST_2026-08-10.md`.

Saddle:

- PR #1 — Phase-0 cold-start closure evidence;
- PR #2 — park resource/self-improvement concepts;
- PR #3 — preserve six-part test questions/raw answers/analysis;
- PR #4 — operational TODO queue;
- PR #5 — Saddle–Executor responsibility boundary / DEC-SAD-006 candidate.

External:

- ScriptOps PR #6 — GitHub access-check + v2-vs-RC1 analysis, no runtime change;
- executor-pilot-target PR #5 — CASE-001 solve evidence; DO NOT merge into broken benchmark baseline;
- Executor PR #57 — A1/A2 architecture attack; draft/unmerged; provider not selected.

---

# 15. Exact recovery order if this chat disappears now

A new zero-history agent should:

1. Read Saddle `AGENTS.md`.
2. Read `PROJECT_STATE.md` on `main` and note that main may still be behind reviewed draft evidence.
3. Read `EXECUTION_PLAN.md` and `RESTRICTIONS.md`.
4. Inspect all open Saddle PRs #1–#5 before assuming the main branch reflects the latest working conclusions.
5. Read this recovery capsule and the PR manifest.
6. Treat PR #1 as the pending Phase-0 canonical human gate.
7. Treat PR #4 as the proposed operational queue, subordinate to state/plan.
8. Treat PR #5 as the latest user-endorsed responsibility-boundary candidate, not yet canonical while unmerged.
9. Inspect Executor #51–#57 during Phase 1; do not resume provider research first.
10. Do not begin T4 until Phase-1 reconciliation is actually complete and recorded.

---

# 16. One next step

If there is no newer human decision:

> Review and explicitly accept/reject Saddle PR #1 (`Close Phase 0 cold-start gate`). If accepted, make Phase-0 closure canonical; then continue Phase-1 reconciliation rather than starting new product/runtime work.

This capsule itself does not authorize a merge.

---

# 17. Final conceptual checksum

If a future agent remembers only one compact model, it should be this:

```text
HUMAN owns intent
        ↓
SADDLE preserves/binds intent, provenance, context, decisions and continuity
        ↓
INTELLIGENCE freely searches for how
        ↓
EXECUTOR governs concrete consequential effects and bounded execution
        ↓
WORLD
        ↓
VERIFIER establishes observed facts/evidence
        ↺
SADDLE records durable state without converting AI inference into human decision
```

And the governing anti-substitution rule:

```text
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Freedom inside. Authority at the boundary. Durable memory in GitHub.
