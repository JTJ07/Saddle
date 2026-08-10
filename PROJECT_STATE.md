---
project: Saddle
status: PHASE_5_ACCEPTED / PHASE_6_ACTIVE / HUMAN_BASE_DECISION_REQUIRED / NOT_YET_FUNCTIONAL
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

Move from boundary definition into controlled proof of value without capability expansion.

Final target remains:

```text
human raw intent
→ durable integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded execution
→ verifier evidence
→ durable StateDelta
→ zero-history resume
```

## 3. Human verdict / roadmap decision

Recorded in `DEC-SAD-008` and `DEC-SAD-009`:

- `RESPONSIBILITY ARCHITECTURE: PASS`;
- `OWNERSHIP MODEL: PASS`;
- `PHASE 4 AI WORKER DIRECTION: PASS`;
- `TRUST BOUNDARIES: OPEN — INTENTIONALLY`;
- Phase 1–4 foundations are frozen against unnecessary redesign;
- Phase 5 strict boundary proof was authorized as the next active work.

Important evidence distinction:

`PHASE 4 AI WORKER DIRECTION: PASS` does not mean the live Sol/Terra benchmark ran. It remains unexecuted evidence required before final functional acceptance.

## 4. Canonical completed foundations

### Phase 0 — ACCEPTED
Repository-only zero-memory recovery.

### Phase 1 — ACCEPTED / FROZEN
Responsibility architecture and cross-repository reconciliation.

### Phase 2 — ACCEPTED / FROZEN
Provider-independent Protocol v0.1:
`IntentEnvelope -> EffectProposal -> EffectReceipt -> StateDelta`.

### Phase 3 — ACCEPTED / FROZEN
Fail-closed stdlib JSON/JSONL audit/eval foundation.

### Phase 4 — DIRECTION PASS / SCAFFOLD FROZEN / LIVE EVIDENCE OPEN
Proposal-only ModelGateway direction, immutable CASE-001–003 pins and bounded validation exist.

Still unexecuted:
- real external model calls;
- two-model measured comparison;
- real-model proposal routed through Executor;
- observed model cost/latency/token evidence.

Do not infer these results.

## 5. Phase 5 — ACCEPTED ON THIS CHANGE SET

### Phase 5A — Verified Intent Boundary

Added `VerifiedIntentBinding`:

- binds exact `intent_id` + envelope content hash;
- adds independent `raw_intent_hash` derived from exact UTF-8 `raw_human_intent`;
- binds a `principal_ref`;
- binds immutable origin-event reference + hash + observation time;
- has content-addressed identity, freshness and status.

Critical result:

`raw_intent_hash` is independent of `derived_interpretation`.

AI can revise its interpretation without silently rewriting the preserved human statement.

### Phase 5B — Effect Authority Boundary

Added separate `EffectAuthority`:

- exact verified-intent binding ID + hash;
- exact EffectProposal ID + hash;
- exact action + target;
- evidence requirements;
- explicit `ALLOW` / `DENY`;
- issuer reference;
- expiry;
- single-use replay protection.

Core rule:

```text
EffectProposal != EffectAuthority
```

Semantic similarity, AI confidence, derived interpretation or USER-like metadata never create permission.

### Implementation

- `authority/v0.1/verified-intent-binding.schema.json`;
- `authority/v0.1/effect-authority.schema.json`;
- `tools/phase5_boundaries.py`;
- `tests/test_phase5_boundaries.py`;
- `docs/PHASE5_STRICT_BOUNDARIES_v0.1.md`;
- `evidence/PHASE5_STRICT_BOUNDARY_TEST_2026-08-10.md`.

### Test evidence

Local deterministic Phase-5 slice:

```text
python -m compileall -q tools tests
PASS

python -m unittest discover -s tests -p 'test_phase5_boundaries.py' -v
Ran 15 tests
OK
```

Primary negative cases block:
- proposal without separate authority;
- goal-expanding AI interpretation without authority;
- raw-intent mutation;
- unverified USER-like origin;
- authority for another effect;
- proposal mutation after authority;
- action/target mismatch;
- stale binding/authority;
- explicit deny;
- replay;
- wrong intent binding.

Positive control: exact active binding + exact active one-use `ALLOW` authority for the exact proposal returns `ALLOW`.

## 6. Trust boundary remains intentionally open

Phase 5 does not select or claim a production identity/request-origin provider.

The boundary proves structure, integrity, exact binding, freshness and fail-closed behavior around a supplied trusted-origin event. Real-world authenticity of that event remains a later adapter/provider concern.

No enterprise IAM, federation, delegation graph or generalized authority platform was introduced.

## 7. Functional acceptance remains open

Saddle is still `NOT_YET_FUNCTIONAL`.

Final acceptance still requires:
- live real-model benchmark evidence from Phase 4;
- one controlled real user workflow;
- real bounded Executor/effect execution;
- verifier evidence;
- required human review;
- durable StateDelta;
- second zero-history resume;
- explicit final human acceptance.

## 8. Current blocker / Phase 6 gate

Phase 5 has no remaining strict-boundary blocker on this change set.

Phase 6 is active, but its first real workflow requires an explicit base selection. The existing technical recommendation remains ScriptOps using `legacy/scriptops-v2-single.py`, while earlier governance explicitly reserves that base selection as a human semantic decision.

No runtime implementation should begin until that base is explicitly selected or rejected.

## 9. One next step

Human selects or rejects `legacy/scriptops-v2-single.py` as the Phase-6 real-workflow implementation base. Current technical recommendation: **select/reuse v2**. If selected, repair only the minimal task -> context -> candidate -> validation -> impact -> human decision with why -> accepted hash -> Git commit -> smoke-evidence path.
