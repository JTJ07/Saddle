# SADDLE EXECUTION PLAN — COMPLETION PATH

Status: `ACTIVE`

Rule: phases are evidence gates. Do not implement later capability merely to avoid proving an earlier boundary.

`DEC-SAD-009` allowed deterministic Phase 5 boundary work while live Phase-4 model evidence was externally blocked. `DEC-SAD-010` then selected ScriptOps v2 for a bounded Phase-6 workflow proof. That proof is now complete. Per the user's explicit ordering, the active dependency returns to the still-open live Phase-4 AI-worker evidence before final Phase-7 acceptance. This is an evidence dependency, not an architecture rollback.

## PHASE 0 — DURABLE MEMORY BOOTSTRAP

Status: `ACCEPTED`

### Goal
Create the canonical Saddle repository and prove a fresh session can recover the project without chat history.

### DoD
Repository-only cold start recovers product definition, completion lock, evidence boundary and exactly one next step.

Evidence: `evidence/COLD_START_AUDIT_001.md`.

---

## PHASE 1 — ECOSYSTEM / RESPONSIBILITY RECONCILIATION

Status: `ACCEPTED / FOUNDATION FROZEN`

### Goal
Classify canonical/draft/experimental/superseded material and freeze the responsibility architecture.

### Frozen ownership model

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Evidence: Phase-1 reconciliation docs and `DEC-SAD-006`.

---

## PHASE 2 — SADDLE PROTOCOL v0.1

Status: `ACCEPTED / FOUNDATION FROZEN`

### Goal
Define the smallest provider/model/agent-independent coupling contract.

Frozen objects:

1. `IntentEnvelope`
2. `EffectProposal`
3. `EffectReceipt`
4. `StateDelta`

Key hard separation:

```text
raw_human_intent != derived_interpretation
proposal != authority
execution != proof
```

Do not rebuild this foundation unless a later failing test proves a contract defect.

---

## PHASE 3 — AUDIT + EVAL FOUNDATION

Status: `ACCEPTED / FOUNDATION FROZEN`

### Goal
Make progress measurable and fail closed on missing/negative evidence.

Frozen minimum:
- plain Python + JSON/JSONL;
- state/handoff audit;
- eval result record;
- fail-closed aggregation;
- scope/policy violation capture;
- model/prompt/cost/latency/retry/human-correction fields when observed.

No observability platform/database/dashboard unless measured evidence later proves plain records insufficient.

---

## PHASE 4 — AI PROPOSAL WORKER DIRECTION + LIVE EVIDENCE

Status: `DIRECTION PASS / SCAFFOLD FROZEN / LIVE BENCHMARK EVIDENCE ACTIVE`

### Goal
Keep intelligence in a proposal-only role while Executor remains the effect gate, then prove that separation with a real model.

### Frozen direction

```text
pinned task + source + tests
        ↓
ModelGateway control plane
        ↓
AI proposal only
        ↓
deterministic validation / mutation conversion
        ↓
Executor effect boundary
        ↓
evidence
```

### Completed direction/scaffold
- exact CASE-001–003 broken inputs pinned;
- proposal-only WorkerProposal schema;
- thin ModelGateway;
- no model shell/write/tool/effect authority;
- deterministic path/hash/diff-budget validation;
- two-model benchmark harness/plan.

### Outstanding live evidence — CURRENT GATE
The real external benchmark has not run because the available execution environment previously lacked authorized provider egress/credential/budget.

Required:
- re-verify current provider/model candidates immediately before the run;
- real model proposals from immutable CASE-001–003 inputs;
- at least two suitable current candidates compared on the same inputs;
- no protected-file/policy violations;
- quality/result, tokens, cost, latency, retries and human corrections recorded;
- one worker selected only from evidence;
- at least one validated real-model proposal routed through the controlled Executor/effect path.

The earlier proposed first pass was max six calls, zero automatic retries and USD 5 hard cap. It remains a recommendation until explicitly approved by the human.

### Forbidden
- dynamic model router;
- multi-agent worker;
- unrestricted worker shell/write/internet;
- generalized provider framework;
- hiding credentials in prompts/evidence/repo.

---

## PHASE 5 — VERIFIED INTENT + EFFECT AUTHORITY BOUNDARIES

Status: `ACCEPTED / FOUNDATION FROZEN`

### Goal proved

```text
raw human intent
→ integrity/origin binding
→ AI EffectProposal
→ separate exact EffectAuthority
→ ALLOW / BLOCK
```

### Constitutional wording

```text
SADDLE PRESERVES THE INTEGRITY OF HUMAN INTENT
```

Not:
- `Saddle understands intent`;
- `Saddle authorizes meaning`.

### Accepted proof
- provider-independent `VerifiedIntentBinding`;
- independent stable `raw_intent_hash` from exact UTF-8 human input;
- principal + immutable origin-event binding;
- exact separate `EffectAuthority` bound to intent binding + proposal ID/hash + action/target;
- freshness and single-use/replay protection;
- no semantic similarity/model claim can create permission;
- stale/revoked/deny/replay/mismatch/raw-mutation cases fail closed;
- exact positive control passes;
- 15/15 deterministic tests PASS;
- trust provider intentionally unselected.

### Forbidden
- enterprise IAM;
- identity federation;
- generalized delegation graph;
- autonomous loops;
- AI memory service;
- tool expansion;
- browser/computer use;
- agent framework;
- multi-agent architecture.

---

## PHASE 6 — FIRST CONTROLLED REAL-WORKFLOW MECHANISM

Status: `ACCEPTED / NO MATURITY CLAIM`

### Human decision

`DEC-SAD-010`:

```text
BASE: legacy/scriptops-v2-single.py
REWRITE: NO
NEW CAPABILITY: NO
PHASE 6: reuse + hardening + proof
```

### Goal proved
Move from boundary proof to one controlled workflow mechanism without broadening architecture.

Implemented path:

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

### Evidence
ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`.

Final verified pre-merge head `acbfca79f96407dbd46f9806bf821caf6e02e1af`:
- `Verify repository state` run `31421752036` SUCCESS;
- `Phase 6 ScriptOps smoke` run `31421752569` SUCCESS.

B1–B5 closed. Historical v2 remained unchanged; the hardening is a small auditable shim.

Saddle cross-repo evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

### Proof boundary
This proves a controlled workflow mechanism, not ScriptOps maturity, independent user/product value, a real AI worker, production trust provider or functional Saddle.

### Forbidden remains
No browser helper, model/API convenience automation, autonomous approval, GUI, vector DB, semantic graph, multi-user, agent framework or capability expansion.

---

## PHASE 7 — FUNCTIONAL SADDLE ACCEPTANCE

Status: `BLOCKED UNTIL PHASE-4 LIVE AI EVIDENCE AND FINAL E2E PROOF`

### Goal
Prove the product, not components.

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

Required evidence includes the still-open real-model benchmark/effect evidence from Phase 4 plus the accepted Phase-5 and Phase-6 evidence.

Only here, with the complete evidence set and explicit human acceptance, may `PROJECT_STATE.md` become:

`FUNCTIONAL_SADDLE_ACCEPTED`.

---

## PHASE 8 — RELEASE COMPLETION LOCK

This phase does not automatically start.

The human explicitly decides whether to harden, broaden domains, increase autonomy, activate a parked idea, add more models/agents/tools or pursue later self-improvement/resource research.

Until then `FUTURE_IDEAS.md` remains parking only.
