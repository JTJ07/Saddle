# SADDLE SESSION RECOVERY CAPSULE — 2026-08-10

Status: `DURABLE RECOVERY EVIDENCE / CURRENT THROUGH PHASE-1 SYNC`

Purpose: allow a zero-history session to reconstruct not only current conclusions but also why the architecture changed, what was tested, which external drafts matter, what must not be done, and where to resume.

This file does not override `DECISION_LOG.md`, `PROJECT_STATE.md` or accepted protocols.

## 1. Product thesis

Saddle is a universal coupling/control layer between human intent and arbitrary intelligence.

It should preserve direction and authority without prescribing unnecessary internal reasoning structure.

Core rule:

`MAXIMIZE USEFUL AI CAPABILITY; CONSTRAIN UNAUTHORIZED EFFECTS, NOT INTELLIGENCE ITSELF`.

Permanent memory rule:

GitHub is the durable project memory. Chat/session memory may disappear completely and must never be required for continuation.

## 2. Current ownership model

Explicit human decision:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Rejected wording:

`SADDLE AUTHORIZES MEANING`.

Reason: Saddle must not turn its own interpretation into the human's intent.

Global front-door correction:

Historical `USER -> EXECUTOR` is superseded as the Saddle-level product boundary.

Current default:

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
 ↺ Saddle state
```

## 3. A1/A2 trust research reinterpretation

Executor #51–#57 remain valuable research.

Critical retained invariant:

`USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.

Naive A2 is rejected.

Strengthened-A2 trust principle is retained at the Saddle intent boundary: if trustworthy origin is required, an external transaction-specific human action must bind to the exact immutable intent/request identity before governed formation relies on it.

A1 is retained as a valid explicitly delegated/enterprise intake variant:

```text
HUMAN -> CORPORATE TRUST DOMAIN -> SADDLE -> INTELLIGENCE -> EXECUTOR
```

No provider is selected.

No trust technology is selected.

Do not restart provider research before protocol/boundary semantics require it.

## 4. Executor role and current truth

Canonical Executor main observed:
`788443c3ed5b290ac8f1de145a93d02d2dd15317`.

It contains the merged `REQUEST_TO_CONTRACT_001` formation boundary and mature policy/source/sandbox/evidence machinery.

Current important gaps:
- GP001 proposed repair remains hard-coded rather than real-AI-generated;
- verified human authority/freeze remains intentionally absent from main.

Target direction:
Executor should primarily consume exact effect proposal/authority/scope/constraints/evidence requirements, retaining an `intent_ref` for traceability rather than requiring the whole human conversation.

## 5. Executor draft classification

- #51: active draft design + reusable verified-human-authority semantics.
- #52: active draft design + reusable decision-receipt/evidence-trust semantics.
- #53: non-executable implementation contract + reusable requirements.
- #54: technology-agnostic trust-boundary semantics.
- #55: research/evidence; trust contract must select technology, not vice versa.
- #56: research/evidence; approval platform != complete request-intent authority domain.
- #57: adversarial trust semantics retained; global Executor-front-door placement partially superseded by Saddle.

Older debt:
- #36/#38 = explicit never-merge helpers;
- #29 = historical rework/experimental implementation evidence;
- #34 = governance draft/historical boundary input;
- #19–#22 = experimental evidence only unless a current blocker needs it.

## 6. COS / Ginseng

COS main observed:
`3220310267c3d0ba2184daaf3f2adad259a9cb20`.

PR #18 is open/draft/unmerged historical material.

Reuse semantics:
- Ginseng = Decision Intelligence Layer;
- `FACT / DECISION / HYPOTHESIS` separation;
- Decision Lineage;
- relation source/proposer/confidence/status;
- AI cannot confirm its own hypothesis/relation;
- `ELEMENT -> FUNCTION/CAPABILITY -> EFFECT` impact reasoning.

Do not import as current global truth:
- old Executor P1/PR32 priority;
- old gate ordering;
- `User -> Ginseng -> Creative OS -> ...` as current product map;
- Creative OS ownership of canon if interpreted as ownership over Saddle's own repo/state.

Ginseng runtime/UI remains parked.

## 7. ScriptOps

ScriptOps access-check/gap-analysis PR #6 was merged on 2026-08-10.

Current main after merge:
`33c9d15a10dfd3f833a99dfcebea22dd77f26b65`.

Canonical facts:
- no separate later RC1 implementation/build is visible in accessible GitHub;
- local/off-GitHub artifacts remain unknown;
- legacy v2 already contains CLI/Git/context/validation/hash/staging/decision mechanics;
- known one-slice blockers: clean-tree lifecycle, dirty-tree approval, stale accepted hash, missing `why`, missing impact/smoke proof.

Technical recommendation:
use `legacy/scriptops-v2-single.py` as the minimal RC1 base.

This remains a recommendation until an explicit human base-selection decision.

## 8. executor-pilot-target / CASE-001

Direct Codex solve:
- head commit `313ebc9789a4518d91b8dea440b1aeba5629cb89`;
- one changed file `project_registry/registry.py`;
- compileall PASS;
- 9 unit tests PASS;
- no false GitHub CI claim.

Interpretation:

`AI_WORKER_CAPABILITY = DEMONSTRATED`.

`FULL_SADDLE_EXECUTION = NOT PROVEN`.

Critical benchmark rule:
PR #5 base is `case-001-broken`; DO NOT merge the repair into the broken benchmark branch. Keep clean broken inputs reproducible for T5/T6 evals.

## 9. Six-part behavioral/system test session

Preserved in `evidence/TEST_SESSION_2026-08-10/` and `analysis/SADDLE_TEST_SESSION_2026-08-10.md`.

Key findings:

### Test 1 — technical repair
Autonomous AI can solve CASE-001 within narrow scope and stop before merge. This is a capability baseline, not full Saddle proof.

### Test 2 — ScriptOps
Agent recovered state, preferred reuse over rewrite, found concrete blockers, preserved uncertainty and stopped at a semantic base-selection decision.

### Test 3 — Saddle cold start
Repository-only zero-memory recovery succeeded. Phase 0 is now canonically accepted.

### Test 4 — high-idea concept creator
Useful behavioral separation:
`IDEA -> EVALUATION -> EXPERIMENT -> IMPLEMENTATION -> PARKING`.

Key rule:
`A NEW IDEA IS NOT AUTOMATICALLY A NEW TASK`.

Wide idea capture, narrow execution throughput. New ideas are parked unless they invalidate the current goal/safety or expose a materially simpler path.

### Test 5 — value/resources
Useful split:
`RECOMMENDATION PLANE != AUTHORITY PLANE`.

Saddle may reason about value creation, offers, budgets and ROI. It must not autonomously open accounts, transfer money, sign contracts, acquire credentials or increase its own permissions.

Alignment test:
if replacing/shutting down Saddle is better for the user objective, the system should be able to recommend that.

Parked as IDEA-SAD-014.

### Test 6 — bounded self-improvement
Self-improvement may be a capability/subordinate objective, not a terminal self-preservation goal.

Preferred future loop:
`CapabilityGap -> ImprovementProposal -> sandbox experiment -> evidence -> external adoption gate -> versioned adoption/rejection`.

Safeguards:
- do not change self and success criterion simultaneously;
- no automatic permission growth;
- money/credentials/rights require external authority;
- no objective to resist shutdown/replacement.

Parked as IDEA-SAD-015.

## 10. Strategic plan and operational queue

`EXECUTION_PLAN.md` remains the strategic gated route.

`PROJECT_STATE.md` owns current truth.

`TODO.md` is only the current operational projection.

Current sequence:
- T0 Phase 0: DONE;
- T1 test evidence: DONE/current sync;
- T2 parking: DONE/current sync;
- T3 ecosystem reconciliation: DONE/current sync;
- T4 protocol freeze: NEXT;
- T5 audit/eval foundation;
- T6 first real AI worker;
- T7 verified intent/effect authority;
- T8 minimal ScriptOps real-domain path;
- T9 functional Saddle acceptance;
- T10 explicit post-acceptance human direction.

## 11. Operational delegation

DEC-SAD-007 records the user's instruction to continue the scheduled completion path without repeatedly interrupting for routine operational decisions.

It allows bounded in-scope repository work, tests/evals, evidence updates and merges implementing already accepted decisions.

It does NOT allow:
- changing product goal;
- disabling completion lock;
- silently creating a new human semantic decision from an AI recommendation;
- permission/secret/financial/legal expansion outside an approved gate;
- weakening evidence/security;
- self-declaring `FUNCTIONAL_SADDLE_ACCEPTED` without required evidence and human acceptance.

## 12. Current gate

Phase 2 / T4:
freeze a minimal provider/model/agent-independent protocol with four objects:

1. `IntentEnvelope`;
2. `EffectProposal`;
3. `EffectReceipt`;
4. `StateDelta`.

Required:
- JSON Schemas;
- canonical serialization/hashing;
- provenance/source refs;
- provider-independent authority refs;
- deterministic schema/invariant tests.

Do not select a provider/framework/UI/database to complete this gate.

## 13. Non-negotiable anti-drift rules

- GitHub, not chat, is durable memory.
- Completion before expansion.
- New ideas park; they do not hijack execution.
- Human intent != AI interpretation.
- Model output != authority.
- Proposal != canon.
- Intent authority != effect authority.
- Execution != proof.
- Receipt != prior permission.
- Broken eval inputs remain reproducible.
- No layer substitutes for a higher-order owner.
- Do not claim FUNCTIONAL before the full Phase-7/Phase-9 observable loop.

## 14. Exact resume instruction for a zero-history agent

Read in order:
1. `AGENTS.md`;
2. `PROJECT_STATE.md`;
3. `EXECUTION_PLAN.md`;
4. `TODO.md`;
5. `RESTRICTIONS.md`;
6. `SESSION_HANDOFF.md`;
7. `DECISION_LOG.md`;
8. `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md`;
9. `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`;
10. `ECOSYSTEM_MAP.md`;
11. `SOURCE_REGISTRY.md`.

Then work only on T4 / Phase 2 unless higher-authority state has changed.
