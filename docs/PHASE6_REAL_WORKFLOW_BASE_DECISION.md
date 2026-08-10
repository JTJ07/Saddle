# PHASE 6 — REAL WORKFLOW BASE DECISION

Status: `HUMAN SEMANTIC DECISION REQUIRED / NO RUNTIME CHANGE`

## Decision to make

Should `legacy/scriptops-v2-single.py` become the implementation base for Saddle Phase 6's first controlled real-user workflow?

Recommended decision:

```text
YES — REUSE SCRIPTOPS V2 AS THE BASE
```

This remains a recommendation until explicitly selected by the human owner.

## Why this is a human decision

The choice determines which existing product artifact becomes the canonical implementation base for the first real workflow. Earlier ScriptOps governance explicitly reserved that promotion to the user.

Saddle must not convert the technical recommendation into a user decision merely because the evidence is strong.

## Facts currently established on ScriptOps main

Source: `litrgratis-pixel/scriptops` main after the 2026-08-10 access-check reconciliation.

1. ScriptOps' current target is one smallest RC1 loop:

```text
task
→ context bundle
→ WebAI candidate import
→ validation
→ impact report
→ human decision
→ decision log
→ Git commit
```

2. No later RC1/Codex build is visible in the accessible GitHub package. Local/off-GitHub artifacts remain explicitly unknown.

3. `legacy/scriptops-v2-single.py` is an executable partial mechanism and already contains most mechanics needed for one path:

- CLI;
- Git state/commit mechanics;
- task/context mechanics;
- validation;
- staging;
- approval path;
- decision log foundation.

4. The current v2 happy path has five concrete blockers:

- B1 — task creation dirties the tree while pre-check expects clean state;
- B2 — task/context/WebAI artifacts can keep the tree dirty before approval;
- B3 — approval changes candidate→accepted without recalculating the accepted scene hash;
- B4 — approval does not require `why`;
- B5 — impact report + final full smoke proof are missing.

5. Current ScriptOps state explicitly recommends v2 reuse and explicitly forbids runtime work before the base-selection decision.

## If YES

Implementation scope is frozen to the smallest delta that closes B1–B5 for one real workflow:

```text
task
→ context
→ candidate
→ validation
→ impact report
→ human approve/reject/revision with mandatory why
→ correct accepted hash
→ Git commit
→ smoke evidence
```

### Allowed

- repair existing v2 lifecycle/Git handling;
- minimal impact report;
- mandatory `why` at human decision;
- correct accepted-hash recalculation;
- one deterministic smoke path;
- tests/evidence/state/handoff needed to prove that one loop.

### Forbidden

- rewrite ScriptOps from zero;
- browser helper;
- direct autonomous model approval;
- model API automation merely for convenience;
- GUI/dashboard;
- vector DB;
- semantic graph platform;
- multi-user scope;
- agent framework;
- multi-agent system;
- new product features.

## If NO

Do not start a rewrite automatically.

The next required input would be one of:

1. another existing implementation artifact selected by the human; or
2. explicit evidence that no reusable base is acceptable, followed by a new human decision authorizing a different implementation base.

A `NO` does not authorize architecture expansion.

## Why YES is recommended

The recommendation is based on reuse-before-rewrite and the current evidence:

- the target RC1 loop is already known;
- v2 is executable rather than specification-only;
- most required mechanics already exist;
- the known gap is bounded to five concrete lifecycle/integrity/evidence problems;
- the missing work can be tested as one small real loop;
- this is the shortest known path from boundary proof to controlled user-value proof.

## Relationship to Saddle Phase 5

Phase 5 established:

```text
raw intent integrity
→ verified binding
→ proposal
→ exact authority
→ ALLOW / BLOCK
```

Phase 6 should now test whether those responsibility boundaries remain useful around a **real workflow** rather than inventing more architecture.

## Relationship to open Phase-4 live-model evidence

Selecting ScriptOps v2 does not waive the still-open live model benchmark.

The final `FUNCTIONAL_SADDLE_ACCEPTED` proof still requires real-model evidence plus the real-workflow/effect/evidence/resume chain.

## Minimal human response

To accept the recommendation, the semantic decision can be as small as:

```text
TAK — używamy legacy/scriptops-v2-single.py jako bazy Phase 6.
```

To reject it:

```text
NIE — nie używamy v2 jako bazy Phase 6.
```

Any later implementation must follow the chosen branch without broadening scope.
