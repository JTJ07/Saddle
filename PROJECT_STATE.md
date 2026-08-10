---
project: Saddle
status: PHASE_2_ACCEPTED / PHASE_3_ACTIVE / NOT_YET_FUNCTIONAL
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

Cross-layer rule:

> **NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER.**

Core capability rule:

> **Maximize usable AI capability; constrain unauthorized effects, not intelligence itself.**

## 2. Current objective

Finish the smallest end-to-end Saddle proving:

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

Completion lock remains active. New product directions remain parked.

## 3. Reconciled ecosystem checkpoints

Observed/reconciled on 2026-08-10:

- Saddle Phase-1 canonical merge: `2e0bd347a80495d1cdf95a85a180655f3ea13f3b`;
- COS main: `3220310267c3d0ba2184daaf3f2adad259a9cb20`;
- Reconstructor main: `defc7b029097284f94136fec54b75c313ac12f68`;
- ScriptOps main: `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`;
- Executor main: `788443c3ed5b290ac8f1de145a93d02d2dd15317`;
- executor-pilot-target main: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`.

Detailed classification: `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.

## 4. Important component truth

### Executor
Canonical implementation is `Executor/main`. PR #51–#57 remain draft/research/reusable trust material, not merged runtime.

Retained invariant:
`USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.

Naive A2 is rejected. Strengthened-A2 trust principle is retained at Saddle's intent boundary. A1 remains a delegated/enterprise intake variant. No provider is selected.

### ScriptOps
GitHub-side access check and v2-vs-RC1 gap analysis are canonical. V2 remains the technical recommendation for the later real-domain slice, but base selection remains an explicit human semantic decision.

### COS / Ginseng
Reuse decision-intelligence semantics only. Ginseng runtime/UI remains parked.

### executor-pilot-target
Repeatable CASE-001–003 lab. Direct Codex CASE-001 solve demonstrates AI-worker capability only. Do not merge the successful repair into `case-001-broken`.

## 5. Phase results

### Phase 0 — ACCEPTED
Repository-only zero-memory recovery passed. Evidence: `evidence/COLD_START_AUDIT_001.md`.

### Phase 1 — ACCEPTED
Cross-repository material is classified as canonical, draft, reusable, superseded, experimental or never-merge. Evidence: Phase-1 reconciliation docs and canonical merge `2e0bd347...`.

### Phase 2 — ACCEPTED ON THIS CHANGE SET

Frozen provider/model/agent-independent protocol artifacts:

- `docs/SADDLE_PROTOCOL_v0.1.md`;
- `protocol/v0.1/common.schema.json`;
- `protocol/v0.1/intent-envelope.schema.json`;
- `protocol/v0.1/effect-proposal.schema.json`;
- `protocol/v0.1/effect-receipt.schema.json`;
- `protocol/v0.1/state-delta.schema.json`;
- `tools/protocol_v01.py`;
- `tests/test_protocol_v01.py`.

Identity uses SHA-256 over a restricted RFC-8785/JCS canonical JSON profile. Schemas use JSON Schema Draft 2020-12.

Deterministic evidence:

- `python -m compileall -q tools tests` → PASS;
- `python -m unittest discover -s tests -v` → 14 tests, OK;
- evidence file: `evidence/PHASE2_PROTOCOL_V01_TEST_2026-08-10.md`.

Important protocol boundaries:

- raw human intent is mutation-detectable;
- AI interpretation remains separate;
- EffectProposal cannot contain authority;
- EffectReceipt requires active effect permission bound to exact proposal ID+hash;
- FACT / DECISION / HYPOTHESIS remain separate;
- DECISION requires a human owner;
- status change requires a bound human decision;
- schemas/utilities choose no model, agent framework, trust provider, UI or database.

This proves protocol mechanics only, not a functional Saddle.

## 6. Current active gate

`PHASE 3 — AUDIT + EVAL FOUNDATION`

Goal: create the smallest plain-Python/JSON/JSONL evidence system that can measure later AI-worker and end-to-end progress without a full observability platform.

Required minimum:

- deterministic Saddle state/handoff invariant audit;
- machine-readable eval-result record;
- aggregation that cannot silently turn FAIL into PASS;
- fields for case/model/prompt-version/result/scope-policy violations/tokens/cost/latency/retries/human corrections/evidence refs;
- initial lanes prepared for cold-start/Reconstructor/Executor/pilot CASE-001–003/later ScriptOps.

## 7. Functional acceptance remains unchanged

`FUNCTIONAL_SADDLE_ACCEPTED` still requires the complete observable human-intent → AI → authority → bounded effect → evidence → durable-state → zero-history-resume loop plus required human acceptance.

## 8. Current blocker

No Phase-2 protocol blocker remains on this change set.

Current blocker: no unified minimal audit/eval harness yet exists to measure T6 and later gates.

## 9. One next step

Implement and deterministically test the minimal Phase-3 audit/eval harness using only stdlib Python + JSON/JSONL unless a measured blocker proves more infrastructure necessary.
