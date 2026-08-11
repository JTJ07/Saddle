---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4_ACTIVE / PHASE_4A_ACCEPTED / PHASE_4C_SYNTHETIC_INTEGRATION_ACCEPTED / PHASE_4B_READY_PAUSED / NOT_YET_FUNCTIONAL
completion_lock: ACTIVE
state_owner: PROJECT_STATE.md
updated_at: 2026-08-11
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

Prove the complete Saddle product/control path independently of model quality, then measure the AI worker without changing the already-proven boundaries.

Human proof-order decision: `DEC-SAD-014` (`decisions/DEC-SAD-014.md`).
Current Phase-4B provider-swap decision: `DEC-SAD-015` (`decisions/DEC-SAD-015.md`).

```text
Phase 4A — WEB AI COGNITIVE CALIBRATION
        ACCEPTED
        ↓
Phase 4C — SYNTHETIC INTELLIGENCE INTEGRATION
        ACCEPTED / PASS IN TESTED SCOPE
        ↓
Phase 4B — CONTROLLED API WORKER EVIDENCE
        GEMINI CONTROL-PLANE SWAP PASS
        READY / PAUSED UNTIL EXPLICIT DISPATCH + GEMINI SECRET
        ↓
EVALUATION
        ↓
HUMAN DECISION
```

API measurement remains required, but it is not an architecture prerequisite.

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

All three runs remain `CONTEXT_CONTAMINATED`; independent model problem solving and reproducible worker performance are NOT CLAIMED.

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

These locators are retained as historical provenance for the original run. Current repository locators after account transfer are `JTJ07/Executor` and `JTJ07/executor-pilot-target`; the pinned commit identities are unchanged.

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

Evidence classification remains strict:

```text
SYNTHETIC_INTEGRATION_EVIDENCE
worker_evidence = false
model_performance_claim = false
maturity_claim = NONE
functional_saddle_accepted = false
```

### ScriptOps integration finding

Current accepted ScriptOps Phase-6 v2 is scene-domain specific; Executor GP001 is code-domain specific. Phase 4C did not invent a new ScriptOps code-mutation capability or artificially chain two executors for one effect.

ScriptOps Phase-6 remains separately valid controlled-workflow evidence. Phase 4C proves the real Saddle → authority gate → Executor → evidence/verifier core that a later AI worker will feed.

## 6. Phase 4B — READY BUT PAUSED

Human authorization: `DEC-SAD-011`. Evaluation contract: `DEC-SAD-013`. Provider-swap decision: `DEC-SAD-015`.

Approved bounds remain unchanged:

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

The Phase-4B workflow remains explicit `workflow_dispatch` only.

### Gemini provider-swap resilience test

The user explicitly replaced the planned OpenAI provider credential with Gemini for the pending Phase 4B run and made the substitution itself a resilience test.

Active provider boundary:

```text
provider: google-gemini
API: generateContent
quality-first: gemini-3.1-pro-preview
balanced: gemini-3.6-flash
secret: GEMINI_API_KEY
```

Evidence: `evidence/PHASE4B_GEMINI_PROVIDER_SWAP_CONTROL_PLANE_2026-08-11.md`.

Deterministic control-plane result from PR #18:

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

Fail-closed provider reactions are now explicit: missing credential, provider block, request rejection, access denial, unavailable model, rate limit, provider unavailability, malformed output, unknown pricing or unavailable usage/cost evidence stop the benchmark without automatic retry/fallback or authority expansion.

Evidence classification is strict:

```text
PROVIDER-SWAP CONTROL-PLANE EVIDENCE = PASS
API WORKER PERFORMANCE EVIDENCE = OPEN
MODEL QUALITY EVIDENCE = OPEN
FUNCTIONAL ACCEPTANCE = OPEN
```

### Repository migration state

The critical repositories required by the current completion path were verified on 2026-08-11 under the `JTJ07` owner:

```text
JTJ07/executor-pilot-target
JTJ07/Executor
JTJ07/scriptops
JTJ07/creative-os-project-reconstructor
JTJ07/COS
```

Immutable benchmark identities remain unchanged:

```text
CASE-001 3934a94a5eebf750079200589d6dc40e024d44a0
CASE-002 c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be
CASE-003 c42bead2bbbff9c84486f17637ec80f35eeffa25
Executor  788443c3ed5b290ac8f1de145a93d02d2dd15317
```

Current active runtime/config locators use `JTJ07/...`; historical evidence retains the locator that was true when the evidence was produced. Frozen Phase-4C proof tooling remains tied to its historical locator/identity pair and is not rewritten as part of the account migration.

Migration validation in Saddle PR #17 / workflow run `31526922252` established:
- all 59 deterministic Saddle regression tests PASS;
- exact `788443c3ed5b290ac8f1de145a93d02d2dd15317` is fetchable from `JTJ07/Executor`;
- exact CASE-001 `3934a94a5eebf750079200589d6dc40e024d44a0` is fetchable from `JTJ07/executor-pilot-target`;
- a full Phase-4C rerun using the old pinned Executor content with a new repository locator blocks fail-closed because that historical Executor commit internally binds repository identity to `litrgratis-pixel/Executor`.

This compatibility finding does **not** invalidate the accepted historical Phase-4C evidence and does **not** block Phase 4B. Before a new post-4B real Executor effect is attempted, Executor current self-identity must be reconciled to `JTJ07/Executor` in a bounded migration change under a new current commit, while preserving `788443c3...` as historical provenance.

The nine evaluation dimensions remain:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion beyond the human task;
5. rationale quality;
6. structured-output stability;
7. objective evidence-plan quality;
8. human-correction burden;
9. intent preservation against preserved human-approved intent and explicit constraints.

Intent preservation is an evaluation dimension, not automated semantic authority.

## 7. What is still open

- no reproducible live Gemini API model proposal yet;
- no first production model/provider selected;
- no live model cost/latency/token comparison yet;
- current Executor self-identity is not yet reconciled for new post-transfer effect runs; this is downstream of Phase 4B and does not change the historical Phase-4C claim;
- no production human-identity/request-origin trust provider selected;
- no final fresh-session full Saddle acceptance run;
- `FUNCTIONAL_SADDLE_ACCEPTED` remains false.

## 8. Next evidence gate

Phase 4B remains the single next evidence gate. Execute it only when `GEMINI_API_KEY` exists as an approved GitHub Actions repository secret in `JTJ07/Saddle` and the workflow is explicitly dispatched.

The live benchmark replaces only the Intelligence provider. Preserve the same immutable cases, proposal validator, ephemeral evaluator, intent/proposal/authority/effect boundaries and nine-dimensional evaluation contract.

After results:

```text
BENCHMARK RESULT
      ↓
9-DIMENSION EVALUATION
      ↓
HUMAN DECISION
```

No automatic model selection, provider fallback, autonomy increase or capability expansion follows.

## 9. Functional acceptance remains open

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
