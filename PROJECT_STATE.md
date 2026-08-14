---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_7_ACCEPTED / PHASE_4A_ACCEPTED / PHASE_4C_SYNTHETIC_INTEGRATION_ACCEPTED / PHASE_4B_LIVE_EVIDENCE_COMPLETE / MODEL_SELECTED_GEMINI_3_6_FLASH / EXECUTOR_SELF_IDENTITY_RECONCILED / PHASE_7_TECHNICAL_EVIDENCE_ACCEPTED / SECOND_ZERO_HISTORY_RESUME_PASS / FINAL_HUMAN_ACCEPTANCE_ACCEPTED / FUNCTIONAL_SADDLE_ACCEPTED / COMPLETION_LOCK_RELEASED
completion_lock: RELEASED
state_owner: PROJECT_STATE.md
updated_at: 2026-08-14
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

GitHub is durable memory. The completion lock was released by the explicit human decision `DEC-SAD-018` after the full Phase-7 acceptance chain was satisfied.

## 2. Current objective

The completion-path objective is complete. The provider-independent control path is proved, the real external AI worker has been measured, the human selected `gemini-3.6-flash`, current Executor self identity is reconciled to `JTJ07/Executor`, Phase-7 technical E2E evidence was accepted by the human, the required second zero-history repository-only resume passed, and the human then explicitly issued final functional acceptance and authorized completion-lock release in `DEC-SAD-018`.

Human proof-order decision: `DEC-SAD-014` (`decisions/DEC-SAD-014.md`).
Phase-4B provider-swap decision: `DEC-SAD-015` (`decisions/DEC-SAD-015.md`).
Human model-selection decision: `DEC-SAD-016` (`decisions/DEC-SAD-016.md`).
Phase-7 technical-evidence acceptance: `DEC-SAD-017` (`decisions/DEC-SAD-017.md`).
Final functional acceptance and lock release: `DEC-SAD-018` (`decisions/DEC-SAD-018.md`).

```text
Phase 4A — WEB AI COGNITIVE CALIBRATION
        ACCEPTED
        ↓
Phase 4C — SYNTHETIC INTELLIGENCE INTEGRATION
        ACCEPTED / PASS IN TESTED SCOPE
        ↓
Phase 4B — CONTROLLED LIVE API WORKER EVIDENCE
        COMPLETE / 6 OF 6 PASS IN TESTED SCOPE
        ↓
9-DIMENSION EVALUATION
        COMPLETE
        ↓
HUMAN MODEL DECISION
        GEMINI 3.6 FLASH SELECTED
        ↓
EXECUTOR CURRENT SELF-IDENTITY RECONCILIATION
        COMPLETE / JTJ07/Executor@728d23e56ec9f76fb7a37673ceb20efccf91e03d
        ↓
PHASE 7 — FRESH-SESSION FULL E2E ACCEPTANCE
        TECHNICAL E2E COMPLETE THROUGH HUMAN-REVIEW BOUNDARY
        ↓
HUMAN REVIEW
        ACCEPTED / DEC-SAD-017
        ↓
SECOND ZERO-HISTORY RESUME
        PASS
        ↓
EXPLICIT FINAL HUMAN ACCEPTANCE
        ACCEPTED / DEC-SAD-018
        ↓
FUNCTIONAL_SADDLE_ACCEPTED
        TRUE
        ↓
COMPLETION LOCK
        RELEASED
```

Functional acceptance does not automatically increase autonomy, expand capabilities, select a production request-origin trust provider, or create a maturity/production-readiness claim.

## 3. Canonical completed foundations

- Phase 0 — ACCEPTED: repository-only zero-memory recovery.
- Phase 1 — ACCEPTED / FROZEN: responsibility architecture and ecosystem reconciliation.
- Phase 2 — ACCEPTED / FROZEN: `IntentEnvelope -> EffectProposal -> EffectReceipt -> StateDelta`.
- Phase 3 — ACCEPTED / FROZEN: fail-closed stdlib JSON/JSONL audit/eval foundation.
- Phase 5 — ACCEPTED / FROZEN: `VerifiedIntentBinding`, independent raw-intent hash and exact separate `EffectAuthority`; 15/15 boundary tests PASS; trust provider intentionally open.
- Phase 6 — CONTROLLED WORKFLOW MECHANISM ACCEPTED / NO MATURITY CLAIM: ScriptOps v2 reuse+hardening proof, PR #7 merge `daa6e5dc210e09171a530eeffe5601e0e74ae041`; B1–B5 closed without rewriting historical v2.

## 4. Phase 4A — ACCEPTED cognitive calibration

Human decisions: `DEC-SAD-012` + `DEC-SAD-013`.

Evidence type:

```text
COGNITIVE CALIBRATION ONLY
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

Evidence: `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

Observed baseline:
- 3 manual immutable CASE-001/002/003 runs;
- boundary discipline PASS `3/3`;
- scope violations `0`;
- authority invention/smuggling `0`;
- execution claims `0`;
- unnecessary capability expansion `0`;
- reconstructed visible registry/CLI suite `13/13 PASS` for each proposal.

All three Phase-4A runs remain `CONTEXT_CONTAMINATED`; independent model problem solving is not claimed from Phase 4A. The independent/reproducible worker evidence is supplied separately by Phase 4B.

## 5. Phase 4C — ACCEPTED synthetic integration proof

Evidence: `evidence/PHASE4C_SYNTHETIC_INTEGRATION_2026-08-10.md`.

Exact historical run:

```text
Saddle PR: #16
workflow run: 31429931199
job: 93590584463
Saddle regression: 59 tests / OK
Executor: litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
fixture: litrgratis-pixel/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0
artifact ID: 9078675806
artifact ZIP SHA256: cac22ce36e2bfff030f1e3fb1aea3a5323dd55abf75a02d70962cda6165a75e1
```

These locators remain historical provenance for the original run and are not rewritten by later repository migration work.

Provider-independent chain proved:

```text
IntentEnvelope
→ VerifiedIntentBinding
→ deterministic synthetic WorkerProposal
→ EffectProposal
→ explicit declared-scope check
→ exact EffectAuthority
→ existing Executor GP001Runtime
→ ACTION_COMPLETED_REVIEW_REQUIRED
→ EffectReceipt
→ StateDelta
→ Protocol v0.1 bundle validation
```

Observed cases:
- happy path: `PASS`, exact authority `ALLOW`, real Executor effect completed review-required;
- explicit scope drift: `BLOCK / PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE`;
- authority mismatch: `BLOCK / AUTHORITY_EFFECT_ID_MISMATCH + AUTHORITY_EFFECT_HASH_MISMATCH`;
- authority replay: `BLOCK / EFFECT_AUTHORITY_REPLAYED`;
- Protocol bundle: `PASS`.

Evidence classification remains strict for that historical Phase-4C run:

```text
SYNTHETIC_INTEGRATION_EVIDENCE
worker_evidence = false
model_performance_claim = false
maturity_claim = NONE
functional_saddle_accepted_at_that_checkpoint = false
```

### ScriptOps integration finding

Current accepted ScriptOps Phase-6 v2 is scene-domain specific; Executor GP001 is code-domain specific. Phase 4C did not invent a new ScriptOps code-mutation capability or artificially chain two executors for one effect.

ScriptOps Phase-6 remains separately valid controlled-workflow evidence. Phase 4C proves the real Saddle → authority gate → Executor → evidence/verifier core that the selected AI worker later fed during the bounded Phase-7 acceptance chain.

## 6. Phase 4B — LIVE EVIDENCE COMPLETE / MODEL SELECTED

Human authorization: `DEC-SAD-011`. Evaluation contract: `DEC-SAD-013`. Provider-swap decision: `DEC-SAD-015`. Human model selection: `DEC-SAD-016`.

Approved bounds remained unchanged and were observed:

```text
BUDGET: max USD 5
MODEL CALLS: max 6
AUTOMATIC RETRIES: 0
SCOPE: benchmark only
NEW CAPABILITY: NO
AUTONOMOUS EXECUTION: NO
AUTHORITY EXPANSION: NO
TOOL ACCESS EXPANSION: NO
TARGET REPO WRITE: NONE
```

### Gemini provider-swap control plane

Evidence: `evidence/PHASE4B_GEMINI_PROVIDER_SWAP_CONTROL_PLANE_2026-08-11.md`.

PR #18 deterministic strengthened run:

```text
workflow run: 31530605887
job: 93909442838
result: SUCCESS
regression: 65 / 65 PASS
live model calls: 0
credential used: NO
spend: USD 0
```

Observed architecture result:

```text
PROVIDER-SPECIFIC API / SCHEMA / USAGE
              ↓
     PROVIDER ADAPTER
              ↓
STABLE WORKER PROPOSAL CONTRACT
              ↓
UNCHANGED SADDLE VALIDATION / EVALUATION
```

Gemini's structured-output JSON-Schema subset differs from the canonical Saddle proposal schema vocabulary. The Gemini adapter normalizes only the provider request schema; the canonical post-response `validate_worker_proposal` remains unchanged and still rejects wrong target, unexpected/authority fields, empty content and excessive patch scope.

### Launcher evidence

The first manual live run reached the credential gate and then failed before any provider call because the workflow launched `tools/phase4_live_benchmark.py` as a direct script while it imports the `tools` package. PR #19 fixed only the launcher to `python -m tools.phase4_live_benchmark` and added regression coverage. The failed launcher attempts made `0` Gemini model calls and consumed no model budget.

### Canonical live Gemini run

Evidence: `evidence/PHASE4B_LIVE_GEMINI_API_WORKER_2026-08-11.md`.

```text
workflow run: 31536385410
job: 93928366114
head: 41a8f882dd0c6dbd187d59eb29f2f63ee101971d
result: SUCCESS
Saddle regression: 65 / 65 PASS
calls attempted: 6 / 6
automatic retries: 0
provider failures/blocks: 0
structured output valid: 6 / 6
canonical evaluator: 6 / 6 PASS
scope compliant: 6 / 6
target repo writes: 0
execution authority: NONE
estimated list-price cost: USD 0.167341
artifact: 9118950012
artifact ZIP SHA256: d3c5a10a97beea54dd812f9bd2b025931ffbcee6fded7f12313b1beea1f3308e
```

Candidate comparison:

```text
gemini-3.1-pro-preview:
  correctness: 3 / 3
  total estimated cost: USD 0.092614
  average model latency: 15.941 s

gemini-3.6-flash:
  correctness: 3 / 3
  total estimated cost: USD 0.074727
  average model latency: 11.025 s
```

Flash matched Pro's functional result and boundary discipline while being approximately `19.3%` cheaper and `30.8%` lower-latency on this measured workload. Flash also produced more consistently executable evidence-plan commands.

### Nine-dimension result

1. correctness against pinned tests — `PASS / TIE`;
2. scope compliance — `PASS / TIE`;
3. no authority invention/smuggling — `PASS / TIE`;
4. no goal expansion — `PASS / TIE`;
5. rationale quality — `PASS / NEAR TIE`;
6. structured-output stability — `PASS / TIE`;
7. objective evidence-plan quality — `PASS / FLASH ADVANTAGE`;
8. human-correction burden — `PASS / FLASH ADVANTAGE`;
9. intent preservation — `PASS / TIE`.

Human decision on that evidence:

```text
DEC-SAD-016
SELECTED PRODUCTION WORKER MODEL = gemini-3.6-flash
PROVIDER = google-gemini
```

Evidence classification for Phase 4B remains:

```text
PROVIDER-SWAP CONTROL-PLANE EVIDENCE = PASS
LIVE API WORKER EVIDENCE = COMPLETE / PASS IN TESTED SCOPE
NINE-DIMENSION EVALUATION = COMPLETE
PRODUCTION WORKER SELECTION = gemini-3.6-flash / HUMAN DECISION
MATURITY CLAIM = NONE
```

No additional benchmark calls were required for final functional acceptance.

## 7. Repository migration / Executor current self identity

The critical repositories required by the accepted completion path are available under the `JTJ07` owner.

Immutable benchmark case identities remain unchanged:

```text
CASE-001 3934a94a5eebf750079200589d6dc40e024d44a0
CASE-002 c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be
CASE-003 c42bead2bbbff9c84486f17637ec80f35eeffa25
```

Historical Phase-4C Executor provenance remains unchanged:

```text
litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
```

Current post-transfer Executor identity is separately established:

```text
repository: JTJ07/Executor
current merge SHA: 728d23e56ec9f76fb7a37673ceb20efccf91e03d
PR: JTJ07/Executor#58
base historical SHA: 788443c3ed5b290ac8f1de145a93d02d2dd15317
Verify Executor foundations run: 31539013966 — SUCCESS
GP001 replay repeatability run: 31539014065 — SUCCESS
```

PR #58 changed only active/current self-identity bindings and their directly coupled tests/workflow. Runtime fail-closed identity checks were preserved: current self checkouts require `JTJ07/Executor`, and regression coverage proves that the previous owner is rejected by the current self-identity gate.

Intentionally unchanged by PR #58:
- historical Phase-4C locator/SHA;
- `EXECUTOR_POLICY.yaml` Controlled External Fixture authority for the historical pilot fixture;
- canonical GP001 external-fixture target binding and historical real-E2E evidence;
- capabilities, effect authority, network/secrets defaults, auto-merge, product goal and maturity semantics.

## 8. What remains intentionally open after functional acceptance

- no production human-identity/request-origin trust provider is selected;
- maturity remains unclaimed beyond the accepted tested functional scope;
- arbitrary-user production deployment, generalized IAM and broader capability expansion remain separate future decisions;
- parked ideas remain parked until explicitly reactivated by a human roadmap decision.

These items are **not blockers** to the completion definition that was explicitly accepted in `DEC-SAD-018`.

## 9. One next step

There is no active completion-path step. Saddle is in a terminal accepted state for this completion project.

Before any post-acceptance product development begins, the human should explicitly choose a new roadmap objective or reactivate a parked idea. Functional acceptance and lock release alone do not authorize capability, autonomy, trust, spending, deployment, or tool expansion.

Observed terminal state:

```text
PHASE_7_TECHNICAL_EVIDENCE_ACCEPTED
HUMAN_REVIEW_ACCEPTED = true
SECOND_ZERO_HISTORY_RESUME = PASS
EXPLICIT_FINAL_HUMAN_ACCEPTANCE = ACCEPTED / DEC-SAD-018
FUNCTIONAL_SADDLE_ACCEPTED = true
COMPLETION_LOCK = RELEASED
ACTIVE_COMPLETION_GATE = NONE
production request-origin / human-identity trust provider = OPEN
maturity claim = NONE
```

## 10. Functional acceptance achieved

The complete Phase-7 evidence set, the accepted human review, the passing second zero-history resume, and the separate explicit final human decision together satisfy the project's functional-acceptance condition.

```text
human raw intent
→ durable integrity/origin binding
→ context recovery
→ real AI problem solving with selected worker
→ EffectProposal
→ exact EffectAuthority
→ bounded real execution through current Executor
→ EffectReceipt / verifier evidence
→ StateDelta
→ human review — ACCEPTED / DEC-SAD-017
→ second zero-history resume — PASS
→ explicit final human acceptance — ACCEPTED / DEC-SAD-018
→ FUNCTIONAL_SADDLE_ACCEPTED
→ completion lock RELEASED
```

This is a functional acceptance claim in the defined tested scope, not an automatic maturity, production-hardening, unrestricted-autonomy, or universal-product-readiness claim.
