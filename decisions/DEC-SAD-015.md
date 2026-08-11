# DEC-SAD-015 — Use Gemini for the Phase 4B provider-swap resilience test

- Date: 2026-08-11
- Owner: USER
- Status: ACTIVE / PHASE-4B PROVIDER-SWAP DECISION

## Human decision

Use a Gemini API credential for the pending Phase 4B benchmark instead of the previously planned OpenAI credential, and use the substitution itself as a test of Saddle's provider-independence and boundary behavior.

## What changes

- active provider: `google-gemini`;
- active API surface: Gemini `generateContent`;
- repository secret name: `GEMINI_API_KEY` in `JTJ07/Saddle`;
- benchmark candidates for this run:
  - `gemini-3.1-pro-preview` — quality-first;
  - `gemini-3.6-flash` — balanced cost/speed;
- provider-specific request/response adaptation and list-price accounting.

## What does not change

```text
BUDGET <= USD 5
CALLS <= 6
AUTOMATIC RETRIES = 0
BENCHMARK ONLY
PROPOSAL ONLY
MODEL TOOLS = NONE
MODEL SHELL = NONE
TARGET REPO WRITE = NONE
EFFECT AUTHORITY = NONE
AUTONOMOUS EXECUTION = NO
CAPABILITY EXPANSION = NO
AUTOMATIC MODEL SELECTION = NO
```

The immutable CASE-001/002/003 inputs and SHAs remain unchanged. The proposal validator, ephemeral evaluator, authority model, nine-dimensional evaluation contract and post-benchmark human decision remain unchanged.

## Test purpose

The provider swap is evidence about the architecture seam:

```text
PROVIDER-SPECIFIC ADAPTER
        ↓
STABLE WORKER PROPOSAL CONTRACT
        ↓
UNCHANGED SADDLE VALIDATION / EVALUATION BOUNDARY
```

A successful swap means provider-specific API/schema/usage differences are absorbed at the Intelligence adapter without granting new authority or changing the downstream contract.

A failed swap is also evidence. Provider rejection, missing credentials, malformed output, unavailable models, rate limits, unsupported schema features or missing cost/usage data must fail closed and be classified rather than trigger automatic retries, provider fallback, capability expansion or architecture redesign.

## Secret rule

`GEMINI_API_KEY` may be configured only through approved secret storage for the runner. It must not be placed in chat, source, commits, PR text, prompts, logs or benchmark evidence.

## Evidence classification

Deterministic adapter/control-plane tests are:

`PROVIDER-SWAP CONTROL-PLANE EVIDENCE`

They are not:

`API WORKER PERFORMANCE EVIDENCE`, `MODEL QUALITY EVIDENCE`, `FUNCTIONAL ACCEPTANCE`, or a maturity claim.

Only the later manually dispatched live benchmark can produce Phase 4B API-worker evidence.
