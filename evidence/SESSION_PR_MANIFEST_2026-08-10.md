# SESSION PR MANIFEST — 2026-08-10

Status: `OBSERVED GITHUB STATE / RECOVERY EVIDENCE`

Purpose: preserve exact working refs that carried knowledge during the Saddle bootstrap/test/reconciliation session. This is a historical snapshot, not permanent canonical status; always re-check live GitHub before acting.

## Saddle

### PR #1 — Close Phase 0 cold-start gate
- head: `agent/phase0-cold-start-audit`
- head SHA: `e6c7026e88944024664a0462157db05c649baf5d`
- result: MERGED on 2026-08-10
- squash merge: `b950660c84c6dcad1a093a7aba5ad2d70d472ee4`
- role: canonical Phase-0 cold-start evidence/state transition.

### PR #2 — Park resource and bounded self-improvement concepts
- original head: `agent/park-resource-self-improvement`
- head SHA: `53ed3f6d5dd033cc8f4c07cb1d47254a199d213f`
- role: IDEA-SAD-014 and IDEA-SAD-015 parking only.
- canonical-sync note: contents were copied onto `agent/phase1-canonical-sync`; do not interpret them as activated features.

### PR #3 — Preserve six-part Saddle test session
- original head: `agent/preserve-test-session-20260810`
- head SHA: `8425181311d4144132c11f435ad76130d3295f16`
- role: exact questions, raw output, analysis, evidence index.
- canonical-sync note: evidence package was copied onto `agent/phase1-canonical-sync`.

### PR #4 — Add operational completion TODO
- original head: `agent/add-operational-todo`
- head SHA: `fc1f1f64b5a6e155f46f2ba5fd3635568c36a24e`
- role: operational TODO concept.
- canonical-sync note: TODO was rebuilt against post-Phase-0 state so T0/T1/T2/T3 statuses are current.

### PR #5 — Record Saddle–Executor responsibility boundary
- original head: `agent/phase1-responsibility-boundary`
- head SHA: `662ae5524191f8c0c25bfae9eace47ed9bb5a0e8`
- role: user-endorsed responsibility split and A1/A2 reinterpretation.
- canonical-sync note: DEC-SAD-006 and responsibility document were copied/reconciled onto the fresh sync branch.

### PR #6 — Preserve full session recovery capsule
- original head: `agent/session-recovery-capsule-20260810`
- head SHA: `69610d483f3afbfea8d172278666f0c471b8bc5e`
- role: emergency recovery capsule, historical PR manifest and architecture lineage.
- canonical-sync note: durable recovery knowledge is being folded into current main-bound state; the original branch remains historical evidence.

### Current Phase-1 canonical sync
- branch: `agent/phase1-canonical-sync`
- base: Phase-0 accepted main `b950660c84c6dcad1a093a7aba5ad2d70d472ee4`
- role: consolidate accepted evidence/parking/TODO/responsibility/reconciliation against the current main, avoiding stale-base conflicts from PR #2–#6.

## ScriptOps

### PR #6 — Close GitHub access check and compare v2 with RC1
- head: `agent/rc1-v2-gap-analysis`
- head SHA: `0be9212c5c42275e90553f530e6bd9c788fea8a3`
- result: MERGED on 2026-08-10
- squash merge: `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`
- role: canonicalizes accessible-GitHub access check and v2-vs-RC1 gap analysis.
- does NOT select v2 as runtime base.

## executor-pilot-target

### PR #5 — Fix CASE-001 atomic batch insertion
- base: `case-001-broken`
- base SHA: `3934a94a5eebf750079200589d6dc40e024d44a0`
- head: `fix/case-001-20260810`
- head SHA: `313ebc9789a4518d91b8dea440b1aeba5629cb89`
- changed path: `project_registry/registry.py` only.
- evidence recorded by PR: compileall PASS; 9 unit tests PASS.
- interpretation: `AI_WORKER_CAPABILITY` baseline, not full Saddle execution.

CRITICAL: do not merge this PR into `case-001-broken`; preserve the broken benchmark input for replay.

## Executor authority/trust stack

All of #51–#57 were observed open/draft/unmerged during reconciliation. Current canonical implementation is Executor/main `788443c3ed5b290ac8f1de145a93d02d2dd15317`.

- #51 head `9cb10dd0a0c9bb209146a9790aa4766a327e63c7` — verified human authority model; reusable semantics, not runtime.
- #52 head `c351e9cc3faedf035130cb6d8e938c60283cceb4` — human decision receipt/evidence trust design.
- #53 head `f3caba12f3ff601e57bafa47a24d0b8c41cf3c99` — non-executable authority implementation contract.
- #54 head `8de10de45fe6110db29366dc380994ce64e09fc4` — technology-agnostic external trust boundary.
- #55 head `1b71ffaf4c2b7abacb128f5417a4e976d819a3f4` — trust technology comparison; contract must select technology, not vice versa.
- #56 head `1eece349f08f8eb827abc195f516bf801c2b4f60` — Pattern A evaluation; approval platform != complete request-intent authority domain.
- #57 head `9038c546db03311547e1adeaeed9b4d3d9e9b74d` — A1/A2 adversarial review.

Retained from #57:
- `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`;
- naive A2 rejected;
- exact external request-origin binding before governed formation;
- front-door ownership must be explicit.

Superseded at global Saddle level:
- `USER -> EXECUTOR` as default front door.

Current interpretation:
- strengthened-A2 principle at Saddle intent boundary;
- A1 valid delegated/enterprise intake variant;
- provider unselected.

## Older Executor draft debt

Observed relevant classes:
- #36 / #38 — temporary CI helpers; PR bodies explicitly say NEVER MERGE;
- #29 — historical rework/experimental runtime evidence;
- #34 — governance draft / historical boundary input;
- #19–#22 — experimental replay/evidence/atomic-consumption work, evidence only unless a current blocker requires it.

## COS

### PR #18
- head: `agent/ecosystem-control-package-v1-1`
- head SHA: `22060901523431aa86536372440e6ca0a82a8518`
- status observed: open/draft/unmerged.
- reuse: Ginseng Decision Intelligence semantics, FACT/DECISION/HYPOTHESIS, Decision Lineage, relation authority, element→function/capability→effect, AI cannot self-confirm relations.
- stale/superseded globally: old Executor P1/PR32 priority/gate status and old global `User -> Ginseng -> Creative OS -> ...` placement.
- do not activate Ginseng runtime/UI under completion lock.

## Recovery rule

Open PR existence is not canonical acceptance. Before acting, classify each live source as canonical implementation, active draft, reusable semantics/evidence, experimental, superseded or temporary/never-merge.
