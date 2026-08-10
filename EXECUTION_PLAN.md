# SADDLE EXECUTION PLAN — COMPLETION PATH

Status: `ACTIVE`

Rule: phases are gates. Do not implement a later capability merely to avoid proving an earlier boundary.

Explicit roadmap decision `DEC-SAD-009` permits deterministic Phase 5 boundary work while the live external Phase-4 model benchmark remains blocked. This does **not** waive the real-model evidence required before final functional acceptance.

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

## PHASE 4 — AI PROPOSAL WORKER DIRECTION

Status: `DIRECTION PASS / SCAFFOLD FROZEN / LIVE BENCHMARK EVIDENCE OPEN`

### Goal
Keep intelligence in a proposal-only role while Executor remains the effect gate.

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
- two-model benchmark plan.

### Outstanding evidence
The real Sol/Terra benchmark has not run because the available environment lacks authorized provider egress/credential/budget.

This evidence remains mandatory before final functional acceptance:
- real model proposals from immutable inputs;
- at least two candidates compared;
- no protected-file/policy violations;
- quality/cost/latency/retries recorded;
- one worker selected only from evidence;
- validated proposal routed through the controlled effect path.

`DEC-SAD-009` explicitly allows Phase 5 to proceed without pretending this evidence exists.

### Forbidden
- dynamic model router;
- multi-agent worker;
- unrestricted worker shell/write/internet;
- generalized provider framework.

---

## PHASE 5 — VERIFIED INTENT + EFFECT AUTHORITY BOUNDARIES

Status: `ACTIVE / STRICT SCOPE`

### Goal
Prove the minimal deterministic boundary:

```text
raw human intent
→ integrity/origin binding
→ AI EffectProposal
→ separate exact EffectAuthority
→ ALLOW / BLOCK
```

Not: implement full authority/IAM.

### Constitutional wording

```text
SADDLE PRESERVES THE INTEGRITY OF HUMAN INTENT
```

Not:
- `Saddle understands intent`;
- `Saddle authorizes meaning`.

### Phase 5A — Verified Intent Boundary

Prove only:

> this exact raw human input is bound to this principal/source event under this immutable binding.

Minimum:
- `intent_id` + envelope hash;
- stable `raw_intent_hash` from exact UTF-8 human input;
- principal reference;
- immutable origin event reference + hash;
- freshness/status;
- content-addressed binding identity.

Trust-provider selection remains intentionally open.

### Phase 5B — Effect Authority Boundary

Prove only:

> this exact `EffectProposal` is explicitly ALLOW or DENY under this exact verified-intent binding.

Minimum:
- separate authority object;
- exact proposal ID + hash;
- exact action + target;
- exact verified-intent binding ID + hash;
- evidence requirements;
- issuer reference;
- freshness;
- single-use/replay protection.

### Negative tests — primary acceptance evidence

Must fail closed for:
1. AI interpretation expands the human goal but no exact authority exists;
2. raw intent changes after origin binding;
3. USER-like metadata exists without verified origin;
4. authority belongs to another proposal;
5. proposal mutates after authority;
6. action or target changes after authority;
7. binding/authority is stale, expired or revoked;
8. authority is replayed;
9. authority explicitly denies;
10. proposal references a different intent.

Positive control: only exact active binding + exact active `ALLOW` authority for the exact proposal may return `ALLOW`.

### Method

```text
MODEL
↓
ATTACK
↓
INVARIANT
↓
IMPLEMENTATION
↓
TEST
```

### DoD
- provider-independent `VerifiedIntentBinding` and `EffectAuthority` contracts exist;
- raw intent has an interpretation-independent integrity anchor;
- no semantic similarity/model claim can create permission;
- negative tests fail closed;
- one exact positive-control path passes;
- trust provider remains unselected;
- no capability expansion occurs.

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

## PHASE 6 — FIRST REAL USER WORKFLOW

Status: `BLOCKED UNTIL PHASE 5 ACCEPTED`

### Goal
Move from boundary proof to one controlled real-world workflow without broadening the architecture.

Preferred existing candidate: ScriptOps, subject to the still-open human base-selection decision.

If ScriptOps v2 is selected, repair only the smallest path:

```text
task
→ context
→ candidate
→ validation
→ impact
→ human approve/reject/revision with why
→ accepted hash
→ Git commit
→ smoke evidence
```

Do not add browser helper, direct autonomous model approval, GUI, vector DB, graph platform or multi-user scope.

---

## PHASE 7 — FUNCTIONAL SADDLE ACCEPTANCE

Status: `BLOCKED UNTIL REQUIRED PHASE 4–6 EVIDENCE`

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
→ verifier evidence
→ human review where required
→ durable StateDelta
→ second zero-history resume
```

Required evidence includes the still-open real-model benchmark evidence from Phase 4.

Only here, with required evidence and explicit human acceptance, may `PROJECT_STATE.md` become:

`FUNCTIONAL_SADDLE_ACCEPTED`.

---

## PHASE 8 — RELEASE COMPLETION LOCK

This phase does not automatically start.

The human explicitly decides whether to harden, broaden domains, increase autonomy, activate a parked idea, add more models/agents/tools or pursue later self-improvement/resource research.

Until then `FUTURE_IDEAS.md` remains parking only.
