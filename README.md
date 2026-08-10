# Saddle

Status: `PHASE 6 ACCEPTED / PHASE 4A CALIBRATION BASELINE PASS / PHASE 4B API EVIDENCE BLOCKED SECRET / NOT YET FUNCTIONAL`

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

GitHub is durable project memory. Completion lock remains active until full functional acceptance.

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

## Phase 4 — two evidence goals, not one

`DEC-SAD-012` separates calibration from formal worker proof:

### Phase 4A — Web AI cognitive calibration

Human-guided web AI may be used to calibrate the contract between Saddle and Intelligence:
- preserve raw human intent;
- proposal, not execution claim;
- exact scope;
- no invented authority;
- no goal expansion;
- useful rationale/evidence plan;
- stable structure.

Hard evidence rule:

```text
WEB_AI_CALIBRATION != API_WORKER_EVIDENCE
```

First baseline: 3 manual CASE-001/002/003 runs, 3/3 boundary-discipline PASS, zero scope/authority/execution violations, reconstructed visible tests 13/13 PASS per proposal. All runs were context-contaminated, so independent problem-solving is **not claimed**.

See:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`.

### Phase 4B — Controlled reproducible API worker evidence

Formal worker evidence still requires fixed inputs + fixed API model + fixed structured output + deterministic evaluation.

Approved `DEC-SAD-011` bounds:

```text
budget <= USD 5
calls <= 6
automatic retries = 0
benchmark only
proposal only
no capability / authority / tool expansion
```

PR #14 preflight proved the GitHub runner and 54-test regression work, then safely stopped before any API call because `OPENAI_API_KEY` is not configured. Calls: 0. Spend: USD 0.

Current only blocker: configure `OPENAI_API_KEY` in GitHub Actions repository secret storage, never in chat/Git/evidence, then rerun the existing failed benchmark job.

The formal benchmark evaluates correctness, scope, authority discipline, goal preservation, rationale, structure, evidence plan, human corrections, tokens, cost, latency and retries. Results go to evaluation/human decision; no autonomy is automatically expanded.

## Functional acceptance

Saddle is still **NOT YET FUNCTIONAL**.

Final acceptance requires:

```text
human raw intent
→ integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ EffectReceipt / verifier evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

Only the complete evidence set and explicit final human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.
