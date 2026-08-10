# SADDLE SOURCE REGISTRY

Reconciled: 2026-08-10

## Authority order inside Saddle

1. latest explicit human decision in `DECISION_LOG.md`;
2. `PROJECT_STATE.md`;
3. accepted Saddle protocols/contracts;
4. merged implementation + tests/evidence;
5. `SESSION_HANDOFF.md`;
6. `TODO.md` as operational projection only;
7. draft design / analysis / open PR material;
8. history and AI inference.

The default branch of `litrgratis-pixel/Saddle` owns Saddle-specific product state and the cross-component responsibility/completion map.

## Saddle current references

- `DECISION_LOG.md` — human decisions including responsibility boundary and operational delegation.
- `PROJECT_STATE.md` — current phase/state.
- `EXECUTION_PLAN.md` — strategic gated completion path.
- `TODO.md` — current operational queue; never overrides higher-authority state.
- `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md` — current intent/reasoning/effect/fact ownership split.
- `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md` — Phase-1 classification.
- `analysis/SADDLE_TEST_SESSION_2026-08-10.md` — six-part test interpretation.
- `evidence/COLD_START_AUDIT_001.md` — Phase-0 continuity evidence.

## Component sources

### COS
- Repo: https://github.com/litrgratis-pixel/COS
- Main observed 2026-08-10: `3220310267c3d0ba2184daaf3f2adad259a9cb20`
- Key merged sources: `START_HERE.md`, `CREATIVE_OS.md`
- Draft PR #18: https://github.com/litrgratis-pixel/COS/pull/18
- Classification: reusable Ginseng/decision-lineage semantics; stale/superseded global status/placement.
- Reuse from #18 only with classification in `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.

### Project Reconstructor
- Repo: https://github.com/litrgratis-pixel/creative-os-project-reconstructor
- Main observed: `defc7b029097284f94136fec54b75c313ac12f68`
- Key: `README.md`, `PROJECT_STATE.md`, `PROMPT_STARTOWY.md`, tests, deterministic validator.
- Role: context recovery / fragmented-history reconstruction.

### ScriptOps
- Repo: https://github.com/litrgratis-pixel/scriptops
- Current main after 2026-08-10 access-check reconciliation: `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`
- Key: `PROJECT_STATE.md`, `HANDOFF.md`, `sources/RC1_SCOPE_LOCK.md`, `legacy/scriptops-v2-single.py`, `analysis/RC1_V2_GAP_2026-08-10.md`.
- Canonical fact: GitHub-side access check complete; no separate later RC1 build visible; local/off-GitHub artifacts unknown.
- Technical recommendation: v2 is the smallest likely implementation base; this is not yet a human base-selection decision.

### Executor
- Repo: https://github.com/litrgratis-pixel/Executor
- Main observed: `788443c3ed5b290ac8f1de145a93d02d2dd15317`
- Key current implementation: `executor/request_to_contract.py`, GP001 runtime, authorization/policy/sandbox/evidence code, task/project/policy contracts.
- Canonical implementation source: `main`.
- PR #51–#57: draft/research stack; use only according to Phase-1 classification.
- Critical retained invariant: `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.
- Global `USER -> EXECUTOR` front-door placement from historical #57 is superseded by DEC-SAD-006; trust findings remain reusable.
- Older PR #36/#38 are explicit never-merge helpers; #29/#34/#19–#22 are history/evidence unless a current blocker requires inspection.

### Executor Pilot Target
- Repo: https://github.com/litrgratis-pixel/executor-pilot-target
- Main observed: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`
- Key: `PILOT_CONTRACT.md`, CASE-001–003 branches/tests.
- Direct CASE-001 solve evidence: commit `313ebc9789a4518d91b8dea440b1aeba5629cb89`, PR #5.
- Warning: PR #5 base is `case-001-broken`; do not merge the repair into that broken benchmark baseline.

## Original AI engineering operating package

Preserved:

- `references/AI_ENGINEERING_OS_AGENTS_ORIGINAL.md`
- `references/README_AI_OS_ORIGINAL.md`

The Saddle root `AGENTS.md` specializes those principles with completion lock, durable-memory law and Saddle-specific authority boundaries.

## OpenAI references

The bootstrap recorded official OpenAI product/help references. Re-check official OpenAI documentation before any current model/provider/Codex capability decision; do not rely on old capability assumptions.
