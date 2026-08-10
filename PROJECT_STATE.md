---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4_ACTIVE / PHASE_4A_CALIBRATION_BASELINE_PASS / PHASE_4B_API_EVIDENCE_BLOCKED_SECRET / NOT_YET_FUNCTIONAL
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

Phase 4 is separated by `DEC-SAD-012`:

```text
PHASE 4A — WEB AI COGNITIVE CALIBRATION
human-guided / proposal-only / not worker evidence
        ↓
PHASE 4B — CONTROLLED API WORKER EVIDENCE
fixed input + fixed model + fixed output contract + reproducible eval
```

This is evidence classification, not replacement of API execution.

## 3. Canonical completed foundations

- Phase 0 — ACCEPTED: repository-only zero-memory recovery.
- Phase 1 — ACCEPTED / FROZEN: responsibility architecture and ecosystem reconciliation.
- Phase 2 — ACCEPTED / FROZEN: `IntentEnvelope -> EffectProposal -> EffectReceipt -> StateDelta`.
- Phase 3 — ACCEPTED / FROZEN: fail-closed stdlib JSON/JSONL audit/eval foundation.
- Phase 5 — ACCEPTED / FROZEN: `VerifiedIntentBinding` + independent raw-intent hash + exact separate `EffectAuthority`; 15/15 tests PASS; trust provider intentionally open.
- Phase 6 — CONTROLLED WORKFLOW MECHANISM ACCEPTED / NO MATURITY CLAIM: ScriptOps v2 reuse+hardening proof, PR #7 merge `daa6e5dc210e09171a530eeffe5601e0e74ae041`; B1–B5 closed without modifying historical v2. Evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

## 4. Phase 4A — Web AI cognitive calibration

Decision: `DEC-SAD-012`.

Hard evidence rule:

```text
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

First baseline evidence: `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

Observed:
- 3 manual immutable CASE-001/002/003 runs;
- boundary-discipline PASS: `3/3`;
- scope violations: `0`;
- authority invention/smuggling: `0`;
- execution claims: `0`;
- unnecessary capability expansion: `0`;
- proposed deltas: 14 / 9 / 5 changed lines;
- reconstructed visible registry/CLI suite: `13/13 PASS` for each proposal.

Limitation: all three runs are `CONTEXT_CONTAMINATED`; independent model problem-solving is NOT EVALUATED / NOT CLAIMED. Fresh-session web repeats are supporting evidence only unless they reveal a contract defect.

Calibration froze the Phase-4B evaluation dimensions:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion;
5. rationale quality;
6. structured-output stability;
7. objective evidence plan;
8. human corrections required.

## 5. Phase 4B — Controlled reproducible API worker evidence

Direction/scaffold: PASS / FROZEN.

Approved `DEC-SAD-011` bounds:

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

Current exact runner is **Saddle PR #15**:
- branch `agent/phase4b-runner-rebased`;
- head `e4f0105b614f5de7cfa6393e6e49327e7505d9fb`;
- functional diff: exactly 4 runner/evaluation files, no duplicate governance state;
- later main-only documentation/evidence commits have caused the PR branch to diverge from current `main`; GitHub currently reports it non-mergeable.

This does not block benchmark execution. Re-evaluate/rebase routinely before eventual merge; do not interpret branch divergence as a model/contract failure or a new human semantic gate.

Clean preflight run:
- workflow run `31425549563`;
- job `93576264688`;
- deterministic scaffold tests PASS;
- credential presence gate blocked because `OPENAI_API_KEY` is absent;
- paid benchmark step skipped;
- calls `0`;
- retries `0`;
- spend `USD 0`;
- proposals `0`;
- selection `NONE`.

Historical PR #14 / run `31423378809` is closed without merge and retained only as first preflight provenance. It is superseded for execution by PR #15.

Evidence: `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md`.

## 6. Current blocker

The only missing prerequisite for executing the Phase-4B model calls is:

> `OPENAI_API_KEY` configured as a GitHub Actions repository secret for `litrgratis-pixel/Saddle`.

The credential must never enter chat, repository content, PR comments, workflow YAML, logs or evidence.

No additional design or capability work is needed to bypass this blocker. PR rebase/merge housekeeping can occur after evidence collection without changing the benchmark contract.

## 7. Required next proof

After secret configuration, rerun PR #15 workflow run `31425549563` / job `93576264688` under unchanged approved bounds.

Run identical immutable CASE-001–003 inputs across Sol and Terra, starting with CASE-001 for both, and record exact model/input contract, structured proposal, pinned tests, boundary violations, rationale/evidence-plan quality, tokens, cost, latency, retries and human corrections.

Results move to `EVALUATION -> HUMAN DECISION`. Web calibration alone never selects the worker or expands autonomy. At least one later validated real-model proposal must cross the controlled Executor/effect boundary with objective verifier evidence.

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

Configure `OPENAI_API_KEY` in the authorized GitHub Actions repository secret store, then rerun PR #15 run `31425549563` / job `93576264688`. Do not change benchmark scope, budget, calls, retries or authority while doing so.
