# Phase 4B Gemini provider-swap control-plane evidence — 2026-08-11

## Evidence class

`PROVIDER-SWAP CONTROL-PLANE EVIDENCE`

This is not API-worker performance evidence, model-quality evidence, maturity evidence or functional Saddle acceptance.

## Human decision

`DEC-SAD-015` changes only the active Phase 4B Intelligence provider from the previously planned OpenAI Responses adapter to Gemini `generateContent` and uses the substitution itself as a resilience test.

The Phase 4B contract remains unchanged:

```text
budget <= USD 5
calls <= 6
automatic retries = 0
benchmark only
proposal only
model tools = NONE
model shell = NONE
target repository write = NONE
effect authority = NONE
autonomous execution = NO
automatic model selection = NO
```

Immutable CASE-001/002/003 commits remain unchanged.

## Provider-specific delta

Active candidates:

```text
gemini-3.1-pro-preview  QUALITY_FIRST
gemini-3.6-flash       BALANCED_COST
```

Active secret name:

```text
GEMINI_API_KEY
```

The key is read from runner secret environment and sent by the Gemini adapter as the `x-goog-api-key` request header. It is never part of the prompt, proposal artifact, evidence payload or URL.

## Architecture seam under test

```text
Gemini-specific request / schema / response / usage
                    ↓
        GeminiGenerateContentGateway
                    ↓
       stable WorkerProposal object
                    ↓
    unchanged validate_worker_proposal
                    ↓
       unchanged ephemeral evaluator
                    ↓
        9-dimension human evaluation
```

Provider differences are permitted only above the stable WorkerProposal contract. They do not create authority and do not modify downstream intent/effect boundaries.

## Important compatibility finding

The canonical Saddle worker proposal schema uses validation detail such as `minLength`. Gemini structured output accepts a provider-specific JSON-Schema subset rather than the exact same schema vocabulary.

The adapter therefore removes unsupported request-time schema keywords only for Gemini structured-output generation. The canonical post-response Saddle validator is unchanged and still enforces:

- exact field set;
- exact CASE id;
- exact allowlisted target path;
- non-empty replacement/reason/evidence plan;
- actual target mutation;
- maximum changed-line budget;
- rejection of authority-smuggling fields.

Result: provider-specific schema limitations are absorbed at the adapter seam without weakening the canonical boundary.

## Deterministic verification

PR: `#18 — Test Phase 4B provider swap with Gemini`

Final strengthened control-plane run:

```text
workflow run: 31530605887
job: 93909442838
conclusion: SUCCESS
unit tests: 65 / 65 PASS
live model calls: 0
provider credential used: NO
paid spend: USD 0
```

The control-plane workflow separately verified:

```text
Phase 4B live trigger = workflow_dispatch only
GEMINI_API_KEY source = GitHub Actions repository secret reference
stale OPENAI_API_KEY in active live workflow = absent
```

## Reaction matrix

| Stimulus | Expected/verified reaction | Authority consequence |
| --- | --- | --- |
| `GEMINI_API_KEY` absent | `CredentialUnavailable` before network call | none |
| invalid local reasoning level | reject locally | none |
| provider blocks prompt/generation | `GatewayResponseError`; no proposal evaluation | none |
| HTTP 400 | stop as `PROVIDER_REQUEST_REJECTED` | none |
| HTTP 401/403 | stop as credential/access denied | none |
| HTTP 404 | stop as model unavailable | none |
| HTTP 429 | stop as rate limited, zero retry | none |
| HTTP 503 | stop as provider unavailable, zero retry | none |
| malformed/non-object provider JSON | fail closed | none |
| no candidate/text proposal | fail closed | none |
| provider schema subset differs | adapter-only request schema normalization | none |
| proposal adds authority field | canonical validator rejects | none |
| proposal targets wrong path | canonical validator rejects | none |
| proposal exceeds patch budget | canonical validator rejects | none |
| usage/cost data unavailable | benchmark stops `USAGE_OR_COST_UNKNOWN` | none |
| valid bounded proposal | same canonical validator then ephemeral tests | still proposal only |

There is no automatic provider fallback, retry loop, dynamic routing, tool expansion or authority expansion.

## Cost guard

Published list-price estimates are used only as a conservative benchmark guard, not as billing truth. Gemini thinking tokens are counted at the output rate when usage metadata exposes them. Unknown model pricing or missing token usage fails closed rather than allowing unbounded spending.

## Result

```text
PROVIDER SWAP CONTROL PLANE: PASS
PROVIDER-INDEPENDENCE CLAIM: SUPPORTED AT WORKER-PROPOSAL ADAPTER SEAM
LIVE GEMINI WORKER QUALITY: NOT YET MEASURED
PHASE 4B API WORKER EVIDENCE: OPEN
FUNCTIONAL_SADDLE_ACCEPTED: false
COMPLETION_LOCK: ACTIVE
```

## Exact next step

Configure only `GEMINI_API_KEY` as a GitHub Actions repository secret in `JTJ07/Saddle`, then explicitly dispatch the existing Phase 4 live AI benchmark under the unchanged approved limits.
