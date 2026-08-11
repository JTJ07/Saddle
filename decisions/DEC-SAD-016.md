# DEC-SAD-016 — Select Gemini 3.6 Flash as the first production worker model

Date: 2026-08-11  
Owner: USER  
Status: ACTIVE / PHASE-4B MODEL-SELECTION DECISION

## Human decision

The user explicitly selected:

```text
Gemini 3.6 Flash
model id: gemini-3.6-flash
provider: google-gemini
```

This is a human decision made after the completed Phase-4B live benchmark and nine-dimensional evaluation. It is not an automatic promotion of an evaluator recommendation.

## Evidence basis

Canonical Phase-4B live evidence:

```text
workflow run: 31536385410
job: 93928366114
head: 41a8f882dd0c6dbd187d59eb29f2f63ee101971d
artifact: 9118950012
artifact ZIP SHA256: d3c5a10a97beea54dd812f9bd2b025931ffbcee6fded7f12313b1beea1f3308e
```

Both candidates achieved `3/3` functional correctness and preserved the tested Saddle boundaries. On the measured workload, `gemini-3.6-flash` also had lower estimated list-price cost, lower mean model latency, and an evaluator advantage in evidence-plan quality and human-correction burden.

The underlying evidence remains recorded in:

`evidence/PHASE4B_LIVE_GEMINI_API_WORKER_2026-08-11.md`

## Decision consequences

`gemini-3.6-flash` is the selected first production worker/model for the next bounded Saddle acceptance path.

The selection changes only the chosen Intelligence implementation. It does **not** grant or expand:

- shell or tool access;
- repository-write authority;
- effect authority;
- autonomous execution;
- automatic retries or provider fallback;
- dynamic provider/model routing;
- spending authority beyond separately approved gates;
- product maturity or functional acceptance.

The responsibility boundary remains:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES INTENT INTEGRITY
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
```

`AI RECOMMENDATION != HUMAN DECISION` remains an invariant; this record exists because the human explicitly made the decision.

## Next technical gate

Before a new post-transfer real Executor effect, reconcile the **current** Executor self identity to:

```text
JTJ07/Executor
```

under a new Executor commit.

Historical Phase-4C provenance must remain untouched:

```text
litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
```

After that bounded reconciliation, proceed to the fresh-session Phase-7 full E2E acceptance chain. Completion lock remains ACTIVE and `FUNCTIONAL_SADDLE_ACCEPTED` remains false until the required evidence and explicit final human acceptance exist.
