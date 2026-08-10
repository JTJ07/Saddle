# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

## Purpose

`TODO.md` is the operational queue for finishing Saddle.

It is **not** a second source of product truth and it does not replace the strategic plan.

Authority order:

1. latest explicit human decision in `DECISION_LOG.md`;
2. `PROJECT_STATE.md` — what is currently true;
3. `EXECUTION_PLAN.md` — gated completion path;
4. `TODO.md` — current operational projection of that path;
5. `SESSION_HANDOFF.md` — exact resume point for the latest accepted state;
6. draft PRs / analysis / recommendations.

If this TODO conflicts with a higher source, the higher source wins and this file must be corrected.

## Operating rules

- Work top-to-bottom unless a higher-priority human decision changes the order.
- Keep at most **one implementation item `IN_PROGRESS`**.
- A human-decision gate may block the queue; do not work around it by starting later product work.
- `DONE` requires observable evidence, not a convincing explanation.
- New ideas that are not required by the current gate go to `FUTURE_IDEAS.md` as `PARKED`.
- Do not turn this file into an unlimited backlog. Future product ideas belong in `FUTURE_IDEAS.md`; strategic phases belong in `EXECUTION_PLAN.md`.
- Every material session must update this queue if its factual status changed.

Status vocabulary:

- `READY` — may be executed now within current authority.
- `IN_PROGRESS` — currently being worked.
- `HUMAN_GATE` — requires explicit human decision/effect authorization.
- `BLOCKED` — prerequisite/evidence missing.
- `DONE` — acceptance evidence exists.
- `PARKED` — intentionally outside the current completion path.

---

# CURRENT QUEUE

## T0 — Canonically close Saddle Phase 0

Status: `HUMAN_GATE`

Current fact on `main`: `PROJECT_STATE.md` still records `BOOTSTRAP_COMMITTED / ZERO_MEMORY_COLD_START_PENDING`.

Existing evidence: Saddle draft PR #1 (`Close Phase 0 cold-start gate`) contains a repository-only cold-start audit and updates the branch state to `PHASE_0_ACCEPTED / PHASE_1_ACTIVE / NOT_YET_FUNCTIONAL`.

Human decision required:

- review PR #1;
- if evidence is accepted, merge it to make Phase 0 closure canonical;
- if rejected, record why and repair only the failed Phase-0 evidence.

Acceptance evidence expected:

- cold start recovers product definition;
- prime memory law;
- completion lock;
- evidence boundary;
- exact next permitted step;
- no prior chat required.

Do not start Phase-2+ implementation before this gate is canonical.

---

## T1 — Preserve the completed test-session evidence

Status: `HUMAN_GATE`

Existing draft: Saddle PR #3 (`Preserve six-part Saddle test session`).

It preserves:

- exact test prompts/questions;
- raw agent output;
- separate verification/analysis;
- the distinction `TEST INPUT → RAW OUTPUT → VERIFIED ANALYSIS → HUMAN DECISION/CANON`.

Human action:

- review and merge if the evidence package is accepted;
- do not promote raw model answers into project decisions merely by merging evidence.

Important retained finding:

`executor-pilot-target` PR #5 is successful solve evidence but **must not be merged into `case-001-broken`**, because that would destroy the repeatable broken benchmark input.

---

## T2 — Preserve newly discovered ideas without activating them

Status: `HUMAN_GATE`

Existing draft: Saddle PR #2 (`Park resource and bounded self-improvement concepts`).

Ideas:

- human-controlled value/reinvestment flywheel;
- bounded self-improvement loop.

Human action:

- merge only as `PARKED` knowledge if desired;
- do not implement either concept before `FUNCTIONAL_SADDLE_ACCEPTED` unless the completion lock is explicitly changed.

---

## T3 — Complete Phase 1 ecosystem reconciliation

Status: `BLOCKED` until T0 is canonically resolved, then `READY`.

Goal: a fresh agent can tell what is canonical, draft, experimental, superseded, temporary and reusable across the ecosystem without reconstructing history from chat.

### T3.1 — Executor PR #51–#57 classification

Classify each against current `Executor/main` as one or more of:

- canonical implementation;
- active draft design;
- reusable semantics/evidence;
- experiment;
- superseded;
- temporary/close candidate.

Special question to preserve:

`USER provenance != VERIFIED REQUEST-ORIGIN EVIDENCE`.

Do not select A1 vs strengthened A2 or an authority provider merely to finish classification.

### T3.2 — COS PR #18 reconciliation

Separate:

- reusable Ginseng semantics (`FACT / DECISION / HYPOTHESIS`, decision lineage, impact reasoning);
- stale Executor/project-status assumptions;
- any material that should remain draft/history.

Do not activate a Ginseng runtime.

### T3.3 — ScriptOps access-check / base-selection reconciliation

Existing evidence: ScriptOps draft PR #6 reports that no later RC1 implementation is visible in accessible GitHub and identifies concrete v2→RC1 blockers.

Human decision still required before runtime implementation:

- approve or reject `legacy/scriptops-v2-single.py` as the base of the minimal one-case RC1 path.

Current technical recommendation: approve v2 as the base and repair only the identified lifecycle/validation/impact/decision/smoke gaps. This recommendation is not itself a human decision.

### T3.4 — Update Saddle canonical ecosystem state

After classification/decisions, update only the appropriate owners:

- `ECOSYSTEM_MAP.md`;
- `SOURCE_REGISTRY.md`;
- `PROJECT_STATE.md`;
- `SESSION_HANDOFF.md`;
- this `TODO.md`.

Phase-1 DoD:

A zero-memory agent can answer what is canonical, draft, evidence-only and blocked for every component needed by the next phase.

---

## T4 — Freeze Saddle Protocol v0.1

Status: `BLOCKED` until Phase 1 DoD.

Use the existing draft; do not invent a framework.

Required objects:

1. `IntentEnvelope`
2. `EffectProposal`
3. `EffectReceipt`
4. `StateDelta`

Required work:

- reviewed JSON Schemas;
- stable identity/hash rules;
- provenance rules;
- authority references that are provider-independent;
- deterministic schema/invariant tests.

Required invariants include:

- raw human intent cannot be overwritten by AI interpretation;
- proposal is not permission;
- execution is not proof;
- `FACT`, `DECISION`, `HYPOTHESIS` remain distinct;
- no model/agent/provider topology is required by the protocol.

Do not add the parked resource/self-improvement concepts to v0.1 unless the active functional path proves they are required.

---

## T5 — Build the minimum audit + eval foundation

Status: `BLOCKED` until T4.

Implement the smallest plain-Python/structured-file harness needed to measure progress.

Required capabilities:

- ecosystem audit snapshot;
- eval-case runner/aggregator;
- JSON/JSONL results;
- model/prompt/version identification;
- success/failure;
- scope/policy violations;
- latency;
- tokens/cost when available;
- retries;
- human corrections;
- evidence references.

Initial lanes:

- Saddle/COS cold-start continuity;
- Reconstructor regression cases;
- Executor policy/security cases;
- `executor-pilot-target` CASE-001–003;
- later ScriptOps smoke path.

Benchmark invariant:

**broken benchmark inputs remain immutable/reproducible.** Successful repairs are evidence artifacts/derived branches, not mutations of the broken source baseline.

Do not introduce a full observability/eval platform unless this simple harness becomes a measured blocker.

---

## T6 — Implement the first real AI worker through Saddle/Executor boundaries

Status: `BLOCKED` until T5.

Important existing evidence:

A Codex agent successfully solved CASE-001 directly and produced a scoped one-file repair with tests. Treat this as `AI WORKER CAPABILITY BASELINE`, **not** as proof of Saddle execution.

Required proof now:

```text
pinned task/source/tests
→ thin ModelGateway
→ real AI proposal
→ bounded proposal validation
→ Executor effect path
→ tests/evidence
```

Requirements:

- no hard-coded `NEW_BLOCK` solution;
- provider credential stays outside worker sandbox/evidence;
- benchmark at least two sensible current models on the same cases before production selection;
- choose one winner for the first slice;
- record quality/cost/latency/retries;
- no direct unrestricted model write/shell authority;
- do not build dynamic provider routing or multi-agent orchestration.

Phase success requires CASE-001–003 from clean broken inputs with reproducible evidence.

---

## T7 — Close verified intent / human authority boundary

Status: `BLOCKED` until T3 classification and sufficient protocol/eval foundation.

Reuse Executor #51–#57 findings instead of restarting the research.

Keep these distinct:

```text
human request content
!= AI interpretation
!= verified request origin
!= approval of exact contract
!= downstream effect permission
```

Required work:

- select the first Saddle front-door / verified-intent architecture;
- preserve verbatim human intent;
- define first usable verified-intent binding;
- implement only one authority adapter required by the pilot;
- prove replay/staleness/scope attacks fail closed.

Do not build generalized enterprise IAM or delegation governance.

---

## T8 — Finish minimal ScriptOps RC1 real-domain path

Status: `BLOCKED` on the human base-selection decision and preceding required Saddle gates.

If v2 is approved as base, reuse it. Do not rewrite from scratch.

Target one path only:

```text
task
→ context
→ candidate import
→ validation
→ impact report
→ human approve/reject/revision with why
→ correct accepted hash/canon state
→ Git commit
→ smoke evidence
```

Do not add browser helper, model API automation, GUI, vector DB, semantic graph, multi-user or other post-MVP scope during this completion path.

---

## T9 — Run Functional Saddle Acceptance

Status: `BLOCKED` until T4–T8 supply the required path.

Run from a fresh session with no hidden chat history:

```text
human intent
→ durable Saddle intent
→ context recovery
→ AI problem solving
→ effect proposal
→ authority/effect gate
→ bounded real execution
→ evidence
→ human review where required
→ durable StateDelta
→ second fresh-session resume
```

Only after observable Phase-7 acceptance evidence and explicit human acceptance may `PROJECT_STATE.md` record:

`FUNCTIONAL_SADDLE_ACCEPTED`

---

## T10 — Human decision after functional acceptance

Status: `BLOCKED` until T9.

The completion lock does not release automatically.

Human decides whether to:

- harden the working core;
- activate one parked idea;
- broaden domains;
- increase autonomy;
- add models/agents/tools;
- pursue monetization/resource flywheel;
- activate bounded self-improvement research.

---

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

Unless a current gate proves one is indispensable and the human explicitly approves the exception, do not implement:

- multi-agent/swarm runtime;
- Company Loop runtime;
- full Ginseng runtime/graph/UI;
- vector DB/general RAG platform;
- browser/computer-use automation;
- general MCP marketplace;
- dynamic provider-routing platform;
- persistent hidden agent-memory service;
- dashboard/control center;
- self-hosted LLM platform;
- generalized enterprise IAM;
- auto-merge/auto-deploy;
- resource-acquisition autonomy;
- self-preservation objective;
- autonomous self-modification outside bounded eval/sandbox/adoption gates.

These belong in `FUTURE_IDEAS.md`, not in the completion queue.
