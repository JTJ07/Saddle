---
project: Saddle
status: PHASE_4_ACTIVE / EXTERNAL_MODEL_RUN_BLOCKED / NOT_YET_FUNCTIONAL
updated_at: 2026-08-10
---

# SESSION HANDOFF

## STATUS

Phases 0–3 are canonical. Phase 4 has a proposal-only ModelGateway scaffold and exact benchmark pins, but no real model call has occurred. Saddle remains `NOT YET FUNCTIONAL`.

## ACTIVE GATE

`PHASE 4 — FIRST REAL AI WORKER`

## WHAT CHANGED

- pinned CASE-001–003 to exact broken commits;
- added strict proposal-only worker schema;
- added provider-neutral `ModelGateway` protocol plus narrow OpenAI Responses adapter;
- added exact-path/diff-budget/before-after-hash proposal validation;
- added non-secret Phase-4 preflight;
- added pinned-checkout proposal runner;
- researched current official Sol/Terra API availability/pricing;
- bounded first-pass proposal to six calls / zero automatic retries / recommended USD 5 hard cap;
- confirmed current Executor accepts the normalized `AuthorizedFileMutation` shape, so CASE-001 does not require an Executor rewrite merely to replace the hard-coded solution source.

## EVIDENCE

- `docs/MODEL_GATEWAY_v0.1.md`;
- `evidence/PHASE4_PRE_CREDENTIAL_CHECKPOINT_2026-08-10.md`;
- `worker/v0.1/worker-proposal.schema.json`;
- `config/worker-cases-v0.1.json`;
- `config/model-benchmark-v0.1.json`;
- `tools/model_gateway.py`;
- `tools/phase4_preflight.py`;
- `tools/phase4_benchmark.py`;
- Phase-4 local scaffold slice: 13 tests PASS.

Actual preflight:
`BLOCKED / PROVIDER_CREDENTIAL_NOT_CONFIGURED`.

## BOUNDARIES PRESERVED

- no real provider call;
- no model selected;
- no secret read or recorded;
- no tools/shell/write/network authority granted to model;
- no fake token/cost/latency/quality result;
- completion lock remains ACTIVE.

## BLOCKERS

All three are required:

1. authorized external control-plane runner with outbound provider HTTPS;
2. `OPENAI_API_KEY` configured in that runner's secret store/environment, never chat/GitHub/evidence;
3. explicit human approval of paid first-pass budget.

Recommended first pass: max 6 calls, no retries, USD 5.00 hard cap.

## ONE NEXT STEP

Enable an authorized external model-runner environment, configure its API secret securely, approve the first-pass budget, then run Sol vs Terra on pinned CASE-001–003 and record results through the Phase-3 eval harness before any worker-model selection.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `TODO.md` — T6
3. `docs/MODEL_GATEWAY_v0.1.md`
4. `evidence/PHASE4_PRE_CREDENTIAL_CHECKPOINT_2026-08-10.md`
5. `config/model-benchmark-v0.1.json`
6. `config/worker-cases-v0.1.json`
7. `tools/model_gateway.py`
8. `tools/phase4_preflight.py`
9. `tools/phase4_benchmark.py`
10. `litrgratis-pixel/Executor` main `788443c...`
