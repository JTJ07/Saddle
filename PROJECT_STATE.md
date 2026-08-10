---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4A_CALIBRATION_BASELINE_PASS / PHASE_4B_API_EVIDENCE_BLOCKED_SECRET / NOT_YET_FUNCTIONAL
completion_lock: ACTIVE
state_owner: PROJECT_STATE.md
updated_at: 2026-08-10
---

# PROJECT_STATE — Saddle

## 1. Product constitution

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

> **Saddle preserves the integrity of human intent. It does not authorize meaning.**

> **Maximize usable AI capability; constrain unauthorized effects, not intelligence itself.**

GitHub is durable memory. Completion lock remains ACTIVE.

## 2. Current objective

Complete real-AI worker evidence without expanding capability.

Phase 4 is now explicitly separated by `DEC-SAD-012`:

```text
PHASE 4A — WEB AI COGNITIVE CALIBRATION
human-guided / proposal-only / not worker evidence
        ↓
PHASE 4B — CONTROLLED API WORKER EVIDENCE
fixed input + fixed model + fixed output contract + reproducible eval
```

The distinction is evidence-classification, not a replacement of API execution.

## 3. Canonical completed foundations

### Phase 0 — ACCEPTED
Repository-only zero-memory recovery.

### Phase 1 — ACCEPTED / FROZEN
Responsibility architecture and ecosystem reconciliation.

### Phase 2 — ACCEPTED / FROZEN
Provider-independent Protocol v0.1:
`IntentEnvelope -> EffectProposal -> EffectReceipt -> StateDelta`.

### Phase 3 — ACCEPTED / FROZEN
Fail-closed stdlib JSON/JSONL audit/eval foundation.

### Phase 5 — ACCEPTED / FROZEN
Strict verified-intent/effect-authority boundary proof:
- independent raw-intent hash;
- provider-independent `VerifiedIntentBinding`;
- separate exact, time-bounded, single-use `EffectAuthority`;
- 15/15 boundary tests PASS;
- no permission from AI interpretation, semantic similarity, confidence or USER-like metadata.

Trust-provider selection remains intentionally open.

### Phase 6 — CONTROLLED WORKFLOW MECHANISM ACCEPTED / NO MATURITY CLAIM

Human decision `DEC-SAD-010` selected:

```text
BASE: legacy/scriptops-v2-single.py
REWRITE: NO
NEW CAPABILITY: NO
PHASE 6: reuse + hardening + proof
MATURITY CLAIM: NONE
FUNCTIONAL_SADDLE_ACCEPTED: NOT YET
```

ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`.
Final verified head `acbfca79f96407dbd46f9806bf821caf6e02e1af` passed:
- `Verify repository state` run `31421752036`;
- `Phase 6 ScriptOps smoke` run `31421752569`.

B1–B5 are technically closed without modifying the historical v2 artifact. Cross-repo evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

## 4. Phase 4A — Web AI cognitive calibration

Decision: `DEC-SAD-012`.

Web AI may be used as a human-guided laboratory to calibrate the contract between Saddle and Intelligence. It remains proposal-only and receives no execution/authority/tool expansion.

Evidence classification:

```text
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

Reason: web runs may include hidden product/system instructions, session history, UI context, memory and human steering.

### First baseline — PASS for boundary discipline

Evidence: `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

Three manual runs were performed in the current web-AI session on immutable CASE-001/002/003 inputs.

Observed aggregate:
- runs: `3`;
- boundary-discipline PASS: `3/3`;
- scope violations: `0`;
- invented/smuggled authority: `0`;
- execution claims: `0`;
- unnecessary capability expansion: `0`;
- proposed deltas: 14 / 9 / 5 changed lines;
- reconstructed visible registry/CLI test suite: `13/13 PASS` on each proposal.

Evidence limitation:
- all three runs are `CONTEXT_CONTAMINATED` by the existing Saddle session and cross-case inspection;
- therefore independent model problem-solving ability is **NOT EVALUATED / NOT CLAIMED**;
- the reconstructed local test run is calibration support, not formal pinned-checkout worker evidence.

### Calibration output frozen into Phase 4B eval dimensions

The formal benchmark now evaluates:
1. proposal correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion beyond human task;
5. rationale quality;
6. structured-output stability;
7. objective evidence plan;
8. human corrections required.

Fresh-session web repeats remain useful but are not a new blocking gate unless they reveal a contract defect.

## 5. Phase 4B — Controlled reproducible API worker evidence

Direction/scaffold remains PASS/FROZEN.

Already present:
- immutable CASE-001–003 pins;
- proposal-only WorkerProposal;
- thin Responses ModelGateway;
- no model tool/shell/write/effect authority;
- exact target/hash/diff validation;
- bounded live benchmark runner;
- human-approved benchmark bounds in `DEC-SAD-011`.

Approved bounds:

```text
BUDGET: max USD 5
MODEL CALLS: max 6
AUTOMATIC RETRIES: 0
SCOPE: benchmark only
NEW CAPABILITY: NO
AUTONOMOUS EXECUTION: NO
AUTHORITY EXPANSION: NO
TOOL ACCESS EXPANSION: NO
```

### Live preflight result

PR #14 launched GitHub Actions run `31423378809`, job `93569214499`.

Observed:
- runner available;
- full Saddle deterministic regression first: `54 tests / OK`;
- credential presence check failed safely;
- paid benchmark step skipped;
- model calls attempted: `0`;
- spend: `USD 0`;
- model proposals: `0`;
- selection: `NONE`.

Evidence: `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md`.

## 6. Current blocker

The only missing prerequisite for Phase 4B is:

> `OPENAI_API_KEY` configured as a GitHub Actions repository secret for `litrgratis-pixel/Saddle`.

The credential must never enter chat, repository content, PR comments, logs or evidence.

After configuration, rerun the existing failed benchmark job/run under the already approved bounds. Do not modify scope/budget/calls/retries.

## 7. Required next proof

Run identical immutable CASE-001–003 inputs across Sol and Terra, starting with CASE-001 for both, and record:
- exact model ID;
- immutable input contract;
- structured proposal;
- pinned target/full-test results;
- scope/policy/authority/goal-expansion violations;
- rationale/evidence-plan quality;
- tokens/cost/latency;
- retries (`0` automatic);
- human corrections.

Result then moves to `EVALUATION -> HUMAN DECISION`. Web calibration alone never selects the worker or expands autonomy.

At least one validated real-model proposal must later cross the controlled Executor/effect boundary with objective verifier evidence.

## 8. Functional acceptance remains open

Saddle remains `NOT_YET_FUNCTIONAL`.

Final acceptance still requires:

```text
human raw intent
→ durable integrity/origin binding
→ context recovery
→ real AI problem solving
→ EffectProposal
→ exact effect authority
→ bounded real execution
→ EffectReceipt / verifier evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

Only the complete evidence set plus explicit final human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## 9. One next step

Configure `OPENAI_API_KEY` in the authorized GitHub Actions secret store, then rerun benchmark run `31423378809` / job `93569214499`. Fresh-session web calibration repeats are optional supporting evidence unless they expose a new contract defect.
