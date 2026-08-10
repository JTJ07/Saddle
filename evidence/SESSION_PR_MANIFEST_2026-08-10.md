# SESSION PR MANIFEST — 2026-08-10

Status: `OBSERVED GITHUB STATE / RECOVERY EVIDENCE`

Purpose: preserve the exact draft/open working set that contains knowledge newer than Saddle `main` or needed for Phase-1 reconciliation.

This is an observed snapshot, not a permanent pin. Re-check GitHub before taking action.

## A. Saddle open draft PRs

### Saddle PR #1 — Close Phase 0 cold-start gate

- URL: https://github.com/litrgratis-pixel/Saddle/pull/1
- state: OPEN
- draft: YES
- merged: NO
- base: `main`
- base SHA: `7622b7dd6d2fc8b541e1aaf0b1581642af01aaeb`
- head: `agent/phase0-cold-start-audit`
- head SHA: `e6c7026e88944024664a0462157db05c649baf5d`
- role: repository-only cold-start evidence + stale README status correction + branch state `PHASE_0_ACCEPTED / PHASE_1_ACTIVE / NOT_YET_FUNCTIONAL`.
- human gate: review/accept or reject Phase-0 closure evidence.

### Saddle PR #2 — Park resource and bounded self-improvement concepts

- URL: https://github.com/litrgratis-pixel/Saddle/pull/2
- state: OPEN
- draft: YES
- merged: NO
- base: `main`
- head: `agent/park-resource-self-improvement`
- head SHA: `53ed3f6d5dd033cc8f4c07cb1d47254a199d213f`
- role: preserves only as `PARKED`:
  - human-controlled value/reinvestment flywheel;
  - bounded self-improvement loop.
- warning: merge as parking knowledge only; do not activate implementation under current completion lock.

### Saddle PR #3 — Preserve six-part Saddle test session

- URL: https://github.com/litrgratis-pixel/Saddle/pull/3
- state: OPEN
- draft: YES
- merged: NO
- base: `main`
- head: `agent/preserve-test-session-20260810`
- head SHA: `8425181311d4144132c11f435ad76130d3295f16`
- role: exact test questions/prompts, raw agent output, separate analysis, evidence index.
- important distinction: `TEST INPUT → RAW OUTPUT → VERIFIED ANALYSIS → HUMAN DECISION/CANON`.
- critical warning retained there: executor-pilot-target PR #5 is solve evidence, not a normal merge target into the broken benchmark branch.

### Saddle PR #4 — Add operational completion TODO

- URL: https://github.com/litrgratis-pixel/Saddle/pull/4
- state: OPEN
- draft: YES
- merged: NO
- base: `main`
- head: `agent/add-operational-todo`
- head SHA: `fc1f1f64b5a6e155f46f2ba5fd3635568c36a24e`
- role: adds `TODO.md` as operational queue and places it in read order.
- governance order in the proposal:
  1. human decisions / `DECISION_LOG.md`;
  2. `PROJECT_STATE.md`;
  3. `EXECUTION_PLAN.md`;
  4. `TODO.md`;
  5. handoff/drafts.
- warning: TODO is not a second source of product truth.

### Saddle PR #5 — Record Saddle–Executor responsibility boundary

- URL: https://github.com/litrgratis-pixel/Saddle/pull/5
- state: OPEN
- draft: YES
- merged: NO
- base: `main`
- head: `agent/phase1-responsibility-boundary`
- head SHA: `662ae5524191f8c0c25bfae9eace47ed9bb5a0e8`
- role: records user-endorsed Phase-1 responsibility ownership and `DEC-SAD-006` candidate.
- key direction:
  - HUMAN OWNS INTENT
  - SADDLE PRESERVES AND BINDS INTENT
  - INTELLIGENCE PROPOSES HOW
  - EXECUTOR GOVERNS CONSEQUENCES
  - VERIFIER ESTABLISHES FACTS
  - NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
- A1/A2 reinterpretation:
  - global `USER → EXECUTOR` front door is superseded as the Saddle-level model;
  - strengthened-A2 principle retained at Saddle intent boundary;
  - naive A2 rejected;
  - A1 valid delegated/enterprise variant;
  - provider not selected.

## B. ScriptOps working PR

### ScriptOps PR #6 — Close GitHub access check and compare v2 with RC1

- URL: https://github.com/litrgratis-pixel/scriptops/pull/6
- state: OPEN
- draft: YES
- merged: NO
- base: `main`
- base SHA: `90a5ba9863961c4b79472db84297cfb403cc5158`
- head: `agent/rc1-v2-gap-analysis`
- head SHA: `0be9212c5c42275e90553f530e6bd9c788fea8a3`
- role:
  - closes GitHub-side access check while preserving uncertainty for local/off-GitHub artifacts;
  - compares preserved v2 with RC1;
  - identifies concrete lifecycle/hash/why/impact/smoke gaps;
  - no runtime change.
- technical recommendation: use `legacy/scriptops-v2-single.py` as minimal one-case base.
- human gate: base selection remains a human decision.

## C. executor-pilot-target working PR

### executor-pilot-target PR #5 — Fix CASE-001 atomic batch insertion

- URL: https://github.com/litrgratis-pixel/executor-pilot-target/pull/5
- state: OPEN
- draft: YES
- merged: NO
- base: `case-001-broken`
- base SHA: `3934a94a5eebf750079200589d6dc40e024d44a0`
- head: `fix/case-001-20260810`
- head SHA: `313ebc9789a4518d91b8dea440b1aeba5629cb89`
- changed files: 1 (`project_registry/registry.py`)
- observed test evidence in PR body: compileall PASS; 9 unittest tests PASS.
- interpretation: `AI WORKER CAPABILITY BASELINE`, not full Saddle execution proof.

### CRITICAL DO-NOT-MERGE-TO-BASE WARNING

The PR base is `case-001-broken`.

Do not merge the successful repair into that broken benchmark baseline. Preserve the broken baseline so CASE-001 can be replayed from a clean identical start.

The repair commit/PR is evidence of a successful solve.

## D. Executor authority/trust stack — open drafts

All of PR #51–#57 are observed OPEN / DRAFT / UNMERGED as of this snapshot.

### #51 — Define verified human authority model

- URL: https://github.com/litrgratis-pixel/Executor/pull/51
- head SHA: `9cb10dd0a0c9bb209146a9790aa4766a327e63c7`
- base: `main`
- important rules include:
  - HUMAN ACTION != VERIFIED HUMAN AUTHORITY
  - AUTHENTICATION != AUTHORIZATION
  - AI INTERPRETATION != USER INTENT
  - AUTHORIZATION MUST BIND TO EXACT CONTRACT IDENTITY
  - INTENT AUTHORITY != RESOURCE / ACTION AUTHORITY
- direction accepted in Executor history; not merged; provider not selected.

### #52 — Design minimal human decision receipt

- URL: https://github.com/litrgratis-pixel/Executor/pull/52
- head SHA: `c351e9cc3faedf035130cb6d8e938c60283cceb4`
- key distinctions:
  - HUMAN DECISION RECEIPT != VERIFIED AUTHORITY EVIDENCE
  - EVIDENCE REF != TRUST SELECTOR
  - authority dimension separation.

### #53 — Define minimal verified human authority implementation contract

- URL: https://github.com/litrgratis-pixel/Executor/pull/53
- head SHA: `f3caba12f3ff601e57bafa47a24d0b8c41cf3c99`
- non-executable contract only; implementation not started.
- includes explicit first-slice identity/binding requirements.

### #54 — Design technology-agnostic external trust boundary

- URL: https://github.com/litrgratis-pixel/Executor/pull/54
- head SHA: `8de10de45fe6110db29366dc380994ce64e09fc4`
- core rule:
  - `EXECUTOR VERIFIES AUTHORITY != EXECUTOR OWNS IDENTITY AUTHORITY`
- no concrete identity provider selected.

### #55 — Compare trust technologies against fixed requirements

- URL: https://github.com/litrgratis-pixel/Executor/pull/55
- head SHA: `1b71ffaf4c2b7abacb128f5417a4e976d819a3f4`
- core rule:
  - `THE TRUST CONTRACT MUST SELECT THE TECHNOLOGY; THE TECHNOLOGY MUST NOT REDEFINE THE TRUST CONTRACT`
- identifies F-22 retroactive request-origin attribution and F-23 review/signing-surface substitution.

### #56 — Evaluate Pattern A technologies

- URL: https://github.com/litrgratis-pixel/Executor/pull/56
- head SHA: `1eece349f08f8eb827abc195f516bf801c2b4f60`
- finding:
  - `APPROVAL PLATFORM != COMPLETE REQUEST-INTENT AUTHORITY DOMAIN`
- A1/A2 left open; provider not selected.

### #57 — Attack A1 vs A2 trust architecture placement

- URL: https://github.com/litrgratis-pixel/Executor/pull/57
- head SHA: `9038c546db03311547e1adeaeed9b4d3d9e9b74d`
- key question in original Executor-centric framing:
  - `WHERE DOES THE TRUSTED REQUEST-ORIGIN EVENT BEGIN?`
- important finding:
  - `USER provenance != VERIFIED REQUEST-ORIGIN EVIDENCE`
- original adversarial result:
  - A1 survives and simplifies trust topology but moves product front door outside Executor;
  - naive A2 rejected;
  - strengthened A2 survives if exact request receives direct external origin attestation before governed formation and same trust domain later binds decision.
- IMPORTANT SADDLE REINTERPRETATION: the surviving trust findings are retained, but global front-door ownership moves up to Saddle. Do not treat the older `USER → EXECUTOR` product boundary as the current Saddle-level decision.

## E. Older Executor draft debt that Phase 1 should classify rather than blindly revive

Observed open drafts also include older implementation/evidence experiments such as #19, #20, #21, #22, #29, #34, #36, #38.

Especially:

- #36 — temporary CI-only helper; PR body explicitly says `Never merge`.
- #38 — temporary CI-only red-test materialization; PR body explicitly says `Never merge`.
- #29 — draft/rework pinned pilot runtime candidate with missing exact external CI/evidence gate in its historical state.
- #34 — governance-only Executor Product Contract freeze candidate.

These are Phase-1 archaeology/classification inputs, not automatic merge candidates.

## F. Recovery rule

Before any new implementation, a zero-history agent must inspect this manifest plus the live PR state and classify material as:

- canonical;
- active draft design;
- reusable semantics/evidence;
- experimental;
- superseded;
- temporary/never-merge.

Open PR existence is not canonical acceptance.
