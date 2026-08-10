# SADDLE ECOSYSTEM MAP

Observed / reconciled: 2026-08-10

## System view

```text
HUMAN
  owns intent
    ↓
SADDLE
  preserves/binds intent, context, provenance, decisions, durable state
    ↓
ARBITRARY INTELLIGENCE
  reasons / explores / proposes HOW
    ↓
EFFECT PROPOSAL
    ↓
EXECUTOR
  governs consequence authority / scope / policy / bounded execution
    ↓
WORLD
    ↓
VERIFIER / EVIDENCE
  establishes what actually happened
    ↺
SADDLE durable StateDelta
```

Cross-layer invariant:

`NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER`.

Default product front door is Saddle, not Executor. Explicit enterprise/delegated intake may place an authorized trust domain before Saddle.

## Component responsibilities

### Saddle
Owns Saddle-specific durable project state, intent binding, authority references, protocol, completion plan and evidence lineage.

### COS
Role: reusable high-level project/portfolio memory patterns and session-resumption discipline.

Observed main: `3220310267c3d0ba2184daaf3f2adad259a9cb20`.

Reuse now:
- Git-backed memory;
- `START_HERE`/single entry pattern;
- source hierarchy;
- truthful statuses;
- one-next-step discipline;
- idea parking.

COS PR #18 classification:
`REUSABLE GINSENG SEMANTICS + STALE/SUPERSEDED GLOBAL STATUS/PLACEMENT`.

Reuse from PR #18:
- Ginseng = Decision Intelligence Layer;
- `FACT / DECISION / HYPOTHESIS` separation;
- Decision Lineage;
- AI cannot confirm its own hypothesis/relation;
- relation source/proposer/confidence/status;
- `ELEMENT -> FUNCTION/CAPABILITY -> EFFECT` impact reasoning.

Do not import as current global truth:
- old `ACTIVE_PRIORITY: EXECUTOR P1 / PR #32`;
- old Executor-specific gate ordering;
- `User -> Ginseng -> Creative OS -> ... -> Executor` as the current Saddle product map;
- `Creative OS owns canon` if interpreted as global ownership over Saddle's own canonical repository.

Ginseng runtime/UI remains parked.

### creative-os-project-reconstructor
Role: context-recovery adapter for fragmented project histories.

Observed main: `defc7b029097284f94136fec54b75c313ac12f68`.

Reuse:
- evidence/status separation;
- source recovery;
- deterministic validator;
- regression cases;
- reconstruction methodology.

Gap to be handled in T5: larger automated semantic/cross-model eval coverage.

### ScriptOps
Role: strongest first real-domain candidate.

Current main after reconciled access-check merge: `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`.

Canonical facts now include:
- no separate later RC1 implementation/build was found in accessible GitHub;
- local/off-GitHub artifacts remain unknown;
- preserved v2 already contains CLI/Git/context/validation/hash/staging/decision mechanics;
- one-slice blockers are concrete: clean-tree lifecycle, approval dirty-tree, stale accepted hash, missing mandatory `why`, missing impact/smoke proof.

Technical recommendation: use `legacy/scriptops-v2-single.py` as the minimal RC1 base.

Status: `RECOMMENDATION, NOT YET HUMAN BASE-SELECTION DECISION`.

### Executor
Role: canonical governed consequential-effect boundary.

Observed main: `788443c3ed5b290ac8f1de145a93d02d2dd15317`.

Canonical main provides:
- request-to-contract phase-1 formation boundary;
- separation of verbatim user request from model interpretation;
- policy/task/project/source checks;
- action-authorization machinery;
- hardened networkless execution sandbox;
- evidence/replay-oriented controls;
- controlled GP001 path.

Current gaps:
- GP001 proposal is hard-coded, not produced by a real AI worker;
- verified human authority/freeze is intentionally absent from main.

Executor PR #51–#57 classification:
- #51: active draft design + reusable human-authority semantics;
- #52: active draft design + reusable receipt/evidence-trust semantics;
- #53: draft non-executable implementation contract + reusable requirements;
- #54: active draft technology-agnostic trust-boundary semantics;
- #55: research/evidence + reusable technology-selection principle;
- #56: research/evidence, provider unselected;
- #57: reusable adversarial trust semantics + partially superseded product placement.

Critical retained findings:
- `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`;
- naive A2 rejected;
- later authentication cannot retroactively establish request origin;
- exact transaction-specific binding and anti-replay/freshness matter;
- trust technology must satisfy the contract, not redefine it.

Saddle reinterpretation:
- strengthened-A2 principle belongs at the Saddle intent boundary by default;
- A1 is a valid delegated/enterprise intake variant;
- Executor does not own the global human front door.

Older Executor drafts:
- #36/#38 = temporary NEVER-MERGE helpers;
- #29 = historical rework/experimental implementation evidence;
- #34 = governance draft/historical product-boundary input;
- #19–#22 and similar = experimental/evidence only, not current completion path.

### executor-pilot-target
Role: immutable/repeatable technical lab for AI-worker + Executor evals.

Observed main: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`.

Cases:
- CASE-001 atomic batch insertion;
- CASE-002 reopen authorization;
- CASE-003 deterministic canonical output.

Direct Codex CASE-001 solve at `313ebc9789a4518d91b8dea440b1aeba5629cb89` is `AI_WORKER_CAPABILITY` evidence, not full Saddle execution proof.

Critical benchmark rule:
Do not merge the repair into `case-001-broken`; keep broken inputs reproducible.

## Integration principle

Do not merge these repositories into a monolith for conceptual neatness.

Saddle references/integrates them through narrow contracts. Component repositories remain authoritative for their own merged implementations; Saddle owns the cross-component product state, responsibility map and completion path.

Detailed Phase-1 classification: `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.
