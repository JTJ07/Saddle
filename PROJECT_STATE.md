---
project: Saddle
status: PHASE_3_ACCEPTED / PHASE_4_ACTIVE / NOT_YET_FUNCTIONAL
completion_lock: ACTIVE
state_owner: PROJECT_STATE.md
updated_at: 2026-08-10
---

# PROJECT_STATE — Saddle

## 1. Product definition

Saddle is the durable control/coupling layer between human-owned intent and arbitrary AI capability.

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

> **Maximize usable AI capability; constrain unauthorized effects, not intelligence itself.**

## 2. Current objective

Finish the smallest end-to-end path:

```text
human intent
→ durable/bound intent
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded execution
→ evidence
→ durable StateDelta
→ fresh-session resume
```

Completion lock remains active.

## 3. Reconciled ecosystem checkpoints

Observed/reconciled on 2026-08-10:

- Saddle Phase-2 merge: `819449bab850fdd6cacabc67980d803e0ba43088`;
- COS main: `3220310267c3d0ba2184daaf3f2adad259a9cb20`;
- Reconstructor main: `defc7b029097284f94136fec54b75c313ac12f68`;
- ScriptOps main: `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`;
- Executor main: `788443c3ed5b290ac8f1de145a93d02d2dd15317`;
- executor-pilot-target main: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`.

Detailed cross-repo classification remains in `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.

## 4. Critical current boundaries

- `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.
- naive A2 rejected.
- strengthened-A2 principle retained at the Saddle intent boundary.
- A1 remains a valid delegated/enterprise intake variant.
- provider remains unselected.
- ScriptOps v2 remains recommended but not yet human-selected as runtime base.
- CASE-001 direct Codex solve is AI-worker capability evidence only; do not merge it into `case-001-broken`.

## 5. Phase results

### Phase 0 — ACCEPTED
Repository-only zero-memory recovery passed.

### Phase 1 — ACCEPTED
Ecosystem and ownership boundaries reconciled.

### Phase 2 — ACCEPTED
Frozen Protocol v0.1:
- four JSON Schemas;
- content-addressed IDs;
- provider-independent source/evidence/authority refs;
- deterministic validation;
- 14 protocol tests PASS.

Evidence: `evidence/PHASE2_PROTOCOL_V01_TEST_2026-08-10.md`.

### Phase 3 — ACCEPTED ON THIS CHANGE SET

Minimal stdlib audit/eval foundation:

- `eval/v0.1/eval-result.schema.json`;
- `config/eval-lanes.json`;
- `tools/eval_harness.py`;
- `tests/test_eval_harness.py`;
- `docs/EVAL_FOUNDATION_v0.1.md`;
- `eval/examples/phase3-smoke.jsonl`;
- `evidence/PHASE3_SMOKE_SUMMARY.json`;
- `evidence/PHASE3_AUDIT_EVAL_TEST_2026-08-10.md`.

Behavior:
- zero results => BLOCKED, never PASS;
- any scope/policy violation => effective FAIL;
- FAIL cannot be averaged away by PASS results;
- unknown/malformed evidence fails validation;
- repo audit checks active-phase agreement, completion lock, one-next-step discipline, frozen protocol and machine-readable source refs.

Evidence:
- Phase-3 slice: 12 tests PASS;
- combined Phase-2+3 regression: 26 tests PASS;
- CLI PASS smoke produces `evidence/PHASE3_SMOKE_SUMMARY.json`;
- synthetic scope-violation smoke returns overall FAIL and non-zero exit code.

No dashboard/database/observability framework was added.

## 6. Current active gate

`PHASE 4 — FIRST REAL AI WORKER`

Required path:

```text
pinned task + source + tests
→ thin ModelGateway control plane
→ real model-generated proposal
→ bounded proposal validation / mutation conversion
→ Executor effect path
→ tests + eval evidence
```

Required benchmark:
CASE-001–003 from clean immutable broken inputs, zero manual solution edits, no protected-file/policy violations, tests passing, model/prompt/cost/latency/retries/human corrections recorded.

Model selection rule:
verify current official provider/model information and benchmark at least two sensible current candidates on the same cases before selecting the first worker. Do not build dynamic routing.

## 7. Functional acceptance remains unchanged

Protocol/eval success does not make Saddle functional. Full human-intent → AI → authority → effect → evidence → durable resume still must pass.

## 8. Current blocker

No Phase-3 foundation blocker remains on this change set.

Current blocker: no real model-backed `ModelGateway` / worker path exists yet, and no current two-model benchmark has been executed through the Saddle/Executor boundary.

## 9. One next step

Research current official model/API options, define the thinnest ModelGateway interface needed only for CASE-001–003, and determine whether the available execution environment has an authorized provider credential path without exposing credentials to the worker or evidence.
