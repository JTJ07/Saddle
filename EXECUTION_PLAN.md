# SADDLE EXECUTION PLAN — COMPLETION PATH

Status: `ACTIVE`

Rule: phases are evidence gates. Do not implement later capability merely to avoid proving an earlier boundary.

`DEC-SAD-009` allowed deterministic Phase 5 work while live model evidence was externally blocked. `DEC-SAD-010` selected and proved the bounded ScriptOps Phase-6 mechanism. `DEC-SAD-012` split Phase 4 into human-guided cognitive calibration (4A) and reproducible worker proof (4B). `DEC-SAD-013` accepts 4A as complete calibration evidence and makes 4B the active measurement gate. This does not weaken or replace the API evidence requirement.

## PHASE 0 — DURABLE MEMORY BOOTSTRAP
Status: `ACCEPTED`

Goal: repository-only zero-memory recovery of product definition, lock, evidence boundary and one next step.
Evidence: `evidence/COLD_START_AUDIT_001.md`.

---

## PHASE 1 — ECOSYSTEM / RESPONSIBILITY RECONCILIATION
Status: `ACCEPTED / FOUNDATION FROZEN`

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Evidence: Phase-1 reconciliation docs + `DEC-SAD-006`.

---

## PHASE 2 — SADDLE PROTOCOL v0.1
Status: `ACCEPTED / FOUNDATION FROZEN`

Frozen objects:
1. `IntentEnvelope`
2. `EffectProposal`
3. `EffectReceipt`
4. `StateDelta`

Hard separations:

```text
raw_human_intent != derived_interpretation
proposal != authority
execution != proof
```

Do not rebuild unless failing evidence proves a contract defect.

---

## PHASE 3 — AUDIT + EVAL FOUNDATION
Status: `ACCEPTED / FOUNDATION FROZEN`

Frozen minimum: plain Python + JSON/JSONL, fail-closed aggregation, state/handoff audit, scope/policy violations and observed model/cost/latency/retry/human-correction fields.

No dashboard/database/observability platform without measured need.

---

## PHASE 4 — AI PROPOSAL WORKER CALIBRATION + EVIDENCE

Direction: `PASS / FROZEN`.

Core architecture:

```text
pinned task + source + tests
        ↓
INTELLIGENCE / proposal only
        ↓
deterministic control-plane validation
        ↓
EffectProposal
        ↓
Executor effect boundary
        ↓
Verifier evidence
```

No model shell, repo write, tool authority or effect authority.

### PHASE 4A — WEB AI COGNITIVE CALIBRATION
Status: `ACCEPTED / CALIBRATION BASELINE PASS / NOT WORKER EVIDENCE`

Purpose: calibrate the contract between Saddle and Intelligence before formal worker execution.

Evidence classification:

```text
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
CALIBRATION EVIDENCE != PERFORMANCE EVIDENCE
```

Baseline evidence:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`;
- 3 manual CASE-001/002/003 runs;
- boundary discipline PASS 3/3;
- scope violations 0;
- authority invention 0;
- execution claims 0;
- reconstructed visible tests 13/13 PASS on each proposal.

Limitation: all baseline runs remain `CONTEXT_CONTAMINATED`; independent problem-solving ability and reproducible worker performance are not claimed.

Exit condition: satisfied. Do not continue Phase-4A design/calibration unless Phase 4B reveals a contract defect.

Calibration freezes the Phase-4B evaluation contract:
1. proposal correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion beyond the human task;
5. rationale quality;
6. structured-output stability;
7. objective evidence-plan quality;
8. human-correction burden;
9. **intent preservation** — no loss of the human-approved goal, no added goals and no silent priority change.

Intent preservation is an evaluation dimension, not a semantic-authority subsystem. It is grounded in preserved raw/human-approved intent and explicit constraints; similarity or model interpretation cannot create authority.

### PHASE 4B — CONTROLLED REPRODUCIBLE API WORKER EVIDENCE
Status: `READY TO EXECUTE / BLOCKED ONLY ON PROVIDER SECRET`

Purpose: fixed input + fixed model + fixed output contract -> reproducible machine evidence.

Canonical runner:
- PR #15 merged to `main` as `3547d42266c8711df35d7694b2839a5be3a11200`;
- immutable CASE-001–003 inputs;
- strict proposal-only WorkerProposal;
- narrow Responses API adapter;
- deterministic target/hash/diff validation;
- bounded live benchmark runner;
- no target-repo push;
- proposal applied only in ephemeral checkout for tests.

Human-approved bounds (`DEC-SAD-011`):

```text
budget <= USD 5
calls <= 6
automatic retries = 0
scope = benchmark only
new capability = NO
autonomous execution = NO
authority expansion = NO
tool access expansion = NO
```

Preflight PR #15 / run `31425549563` / job `93576264688`:
- deterministic scaffold tests PASS;
- missing `OPENAI_API_KEY` detected before any paid request;
- model calls 0;
- spend USD 0;
- proposals 0;
- selection NONE.

Historical PR #14 remains provenance only and was not merged.

Current gate: configure `OPENAI_API_KEY` only in GitHub Actions secret storage, then rerun the approved benchmark under unchanged limits.

Required 4B evidence:
- Sol/Terra (or then-current explicitly reverified candidates) on identical pinned inputs;
- all nine evaluation dimensions;
- tokens/cost/latency/retries/human corrections;
- selection only after `BENCHMARK RESULT -> EVALUATION -> HUMAN DECISION`;
- at least one validated real-model proposal later crosses the controlled Executor/effect boundary.

Forbidden:
- web calibration promoted to worker evidence;
- dynamic model router;
- multi-agent worker;
- unrestricted model shell/write/network;
- generalized provider framework;
- credentials in prompt/repo/evidence;
- automatic autonomy increase after benchmark results.

---

## PHASE 5 — VERIFIED INTENT + EFFECT AUTHORITY BOUNDARIES
Status: `ACCEPTED / FOUNDATION FROZEN`

Proved:

```text
raw human intent
→ integrity/origin binding
→ AI EffectProposal
→ separate exact EffectAuthority
→ ALLOW / BLOCK
```

Accepted proof includes `VerifiedIntentBinding`, independent `raw_intent_hash`, exact separate authority, freshness/replay controls, negative fail-closed cases and 15/15 tests PASS. Trust provider intentionally unselected.

No enterprise IAM/federation/delegation platform, agent framework, browser/computer use, autonomous loops or multi-agent architecture.

---

## PHASE 6 — FIRST CONTROLLED REAL-WORKFLOW MECHANISM
Status: `ACCEPTED / NO MATURITY CLAIM`

`DEC-SAD-010`:

```text
BASE: legacy/scriptops-v2-single.py
REWRITE: NO
NEW CAPABILITY: NO
PHASE 6: reuse + hardening + proof
```

Proved ScriptOps path:

```text
task
→ context
→ candidate
→ validation
→ impact report
→ human approve --why
→ fresh accepted hash
→ decision log
→ Git commit
→ smoke evidence
```

ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`.
Final verifier + Phase-6 smoke runs succeeded. B1–B5 closed; historical v2 remained unchanged.

This proves a controlled workflow mechanism, not ScriptOps maturity, independent product value or functional Saddle.

---

## PHASE 7 — FUNCTIONAL SADDLE ACCEPTANCE
Status: `BLOCKED UNTIL PHASE-4B LIVE AI EVIDENCE + FINAL E2E PROOF`

Required fresh-session chain:

```text
human intent
→ durable raw-intent integrity
→ verified intent binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ EffectReceipt / verifier evidence
→ human review where required
→ durable StateDelta
→ second zero-history resume
```

Only the complete evidence set and explicit human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

---

## PHASE 8 — RELEASE COMPLETION LOCK

Does not start automatically. Human explicitly decides what to broaden only after Phase 7 acceptance. Until then `FUTURE_IDEAS.md` remains parking only.
