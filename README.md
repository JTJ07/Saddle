# Saddle

Status: `FUNCTIONAL_SADDLE_ACCEPTED / PHASE 7 ACCEPTED / COMPLETION LOCK RELEASED`

Saddle is a durable control/coupling layer between **human intent** and **arbitrarily capable AI**.

## Constitution

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

> **Saddle preserves the integrity of human intent. It does not authorize meaning.**

> **Do not constrain intelligence unnecessarily. Constrain unauthorized effects.**

GitHub is durable project memory. The original completion lock was released by explicit human decision `DEC-SAD-018` after the complete Phase-7 acceptance chain passed.

## Read order

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `EXECUTION_PLAN.md`
4. `TODO.md`
5. `RESTRICTIONS.md`
6. `SESSION_HANDOFF.md`
7. `DECISION_LOG.md`
8. `ECOSYSTEM_MAP.md`
9. `SOURCE_REGISTRY.md`

## Accepted foundations

- **Phase 0** — repository-only durable-memory cold start.
- **Phase 1** — responsibility/ecosystem reconciliation.
- **Phase 2** — Protocol v0.1: `IntentEnvelope -> EffectProposal -> EffectReceipt -> StateDelta`.
- **Phase 3** — fail-closed JSON/JSONL audit/eval foundation.
- **Phase 5** — verified-intent + exact effect-authority boundaries; 15/15 deterministic tests PASS.
- **Phase 6** — bounded ScriptOps controlled-workflow mechanism PASS, no maturity claim.

## Phase 4 — calibration, integration, and worker evidence

`DEC-SAD-012` separates calibration from formal worker proof.

### Phase 4A — Web AI cognitive calibration

Human-guided web AI calibrated the contract between Saddle and Intelligence. The first baseline used 3 manual CASE-001/002/003 runs with 3/3 boundary-discipline PASS, zero scope/authority/execution violations, and reconstructed visible tests 13/13 PASS per proposal. All runs remain context-contaminated, so independent problem-solving is not claimed from Phase 4A.

```text
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

See `docs/PHASE4A_WEB_AI_CALIBRATION.md` and `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

### Phase 4B — Controlled reproducible API worker evidence

The bounded Gemini benchmark completed with 6/6 canonical evaluator PASS, 0 automatic retries, and no execution authority or target-repository write. The human selected `google-gemini / gemini-3.6-flash` in `DEC-SAD-016`. Model selection did not expand autonomy or authority.

### Phase 4C — Provider-independent integration proof

The provider-independent `IntentEnvelope -> VerifiedIntentBinding -> EffectProposal -> exact EffectAuthority -> Executor -> EffectReceipt -> StateDelta` chain passed its bounded synthetic integration proof before the live worker measurement.

## Functional acceptance

Saddle is **FUNCTIONAL_SADDLE_ACCEPTED** in the defined tested completion scope.

Accepted chain:

```text
human raw intent
→ integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ EffectReceipt / verifier evidence
→ StateDelta
→ required human review — ACCEPTED / DEC-SAD-017
→ second zero-history resume — PASS
→ explicit final human acceptance — ACCEPTED / DEC-SAD-018
→ FUNCTIONAL_SADDLE_ACCEPTED
→ completion lock RELEASED
```

Primary evidence:
- `evidence/PHASE7_E2E_REVIEW_PACKET_2026-08-12.md`;
- `evidence/PHASE7_SECOND_ZERO_HISTORY_RESUME_2026-08-13.md`;
- `decisions/DEC-SAD-017.md`;
- `decisions/DEC-SAD-018.md`.

Functional acceptance is not a blanket maturity or arbitrary-environment production-readiness claim. The production human-identity/request-origin trust provider remains intentionally unselected, and no parked post-acceptance direction is activated automatically by lock release.
