---
project: Saddle
status: PHASE_4_ACTIVE / EXTERNAL_MODEL_RUN_BLOCKED / NOT_YET_FUNCTIONAL
completion_lock: ACTIVE
state_owner: PROJECT_STATE.md
updated_at: 2026-08-10
---

# PROJECT_STATE — Saddle

## 1. Product definition

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

> **Maximize usable AI capability; constrain unauthorized effects, not intelligence itself.**

GitHub is durable memory. Completion lock remains ACTIVE.

## 2. Current objective

Finish the smallest end-to-end path:

```text
human intent
→ durable/bound intent
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded execution
→ evidence
→ durable StateDelta
→ fresh-session resume
```

## 3. Canonical completed foundations

- Phase 0 durable-memory bootstrap: ACCEPTED.
- Phase 1 ecosystem/responsibility reconciliation: ACCEPTED.
- Phase 2 Protocol v0.1: ACCEPTED; merge `819449bab850fdd6cacabc67980d803e0ba43088`.
- Phase 3 audit/eval foundation: ACCEPTED; merge `801f0561030b528efaa19db01f3a1a587235f437`.

Reconciled component checkpoints:
- COS main `3220310267c3d0ba2184daaf3f2adad259a9cb20`;
- Reconstructor main `defc7b029097284f94136fec54b75c313ac12f68`;
- ScriptOps main `33c9d15a10dfd3f833a99dfcebea22dd77f26b65`;
- Executor main `788443c3ed5b290ac8f1de145a93d02d2dd15317`;
- executor-pilot-target main `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`.

## 4. Critical current boundaries

- `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.
- naive A2 rejected.
- strengthened-A2 principle retained at Saddle intent boundary.
- A1 valid delegated/enterprise intake variant.
- no trust provider selected.
- ScriptOps v2 remains recommended, not yet human-selected as runtime base.
- direct Codex CASE-001 solve demonstrates AI-worker capability only; do not merge it into `case-001-broken`.

## 5. Phase 4 work completed before external-model boundary

Implemented on the current Phase-4 checkpoint:

- `worker/v0.1/worker-proposal.schema.json`;
- `config/worker-cases-v0.1.json` with exact CASE-001–003 broken commit pins;
- `config/model-benchmark-v0.1.json` with Sol/Terra first-pass candidates;
- `tools/model_gateway.py` — proposal-only `ModelGateway` + narrow OpenAI Responses adapter;
- `tools/phase4_preflight.py` — non-secret credential/case/model preflight;
- `tools/phase4_benchmark.py` — exact-checkout proposal generator;
- Phase-4 boundary tests;
- `docs/MODEL_GATEWAY_v0.1.md`;
- `evidence/PHASE4_PRE_CREDENTIAL_CHECKPOINT_2026-08-10.md`.

Model boundary:
- no tools are supplied to the model;
- no shell/write/network authority;
- strict structured WorkerProposal only;
- model cannot add authority fields;
- control plane independently verifies exact case/path/diff budget and derives before/after SHA-256;
- normalized mutation fields match current Executor `AuthorizedFileMutation` input.

Pinned broken inputs:
- CASE-001 `3934a94a5eebf750079200589d6dc40e024d44a0`;
- CASE-002 `c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be`;
- CASE-003 `c42bead2bbbff9c84486f17637ec80f35eeffa25`.

## 6. Model benchmark plan — not yet executed

Current research candidates:
- `gpt-5.6-sol`, medium reasoning;
- `gpt-5.6-terra`, medium reasoning.

First-pass proposal:
- 3 cases × 2 models;
- one call each = max 6 model calls;
- zero automatic retries;
- recommended hard cap USD 5.00;
- budget status `HUMAN_APPROVAL_REQUIRED`.

No production model has been selected.

## 7. Current evidence boundary

Local Phase-4 scaffold test slice: 13 tests PASS.

Actual preflight against the pinned case/model config:

```text
status: BLOCKED
credential_present: false
reason: PROVIDER_CREDENTIAL_NOT_CONFIGURED
```

Observed environment variables by presence only:
`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY` are all NOT SET.

The current execution container also lacks generic outbound DNS/HTTPS for arbitrary external API calls, and no installed/in-scope plugin exposes model-inference API execution.

Therefore NO real Sol/Terra call, quality result, token count, cost, latency or Executor AI-worker run has occurred. Do not infer or invent one.

## 8. Current blocker

Phase 4 is legitimately blocked at an external human/infrastructure boundary. Real benchmark execution requires all three:

1. authorized control-plane runner with outbound HTTPS to the selected provider API;
2. provider credential configured in that runner's secret environment/store, never pasted into chat or committed to GitHub/evidence;
3. explicit human approval of the paid benchmark budget.

Recommended first-pass budget: hard cap USD 5.00, maximum six calls, no automatic retries.

## 9. One next step

Provide/enable an authorized external model-runner environment with outbound provider API access, securely configure `OPENAI_API_KEY` there, and explicitly approve the first-pass benchmark budget; then execute Sol vs Terra on the exact pinned CASE-001–003 inputs and record results through the Phase-3 eval harness before selecting any worker model.
