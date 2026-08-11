# Phase 4B live run 31535468562 — launch block

Date: 2026-08-11
Repository: `JTJ07/Saddle`
Workflow: `Phase 4 live AI benchmark`
Run: `31535468562`
Job: `93925415280`
Head: `53f2b3b0e937ce656d28c069f0a4955438f4717d`
Trigger: `workflow_dispatch`

## FACT

The first live Gemini Phase-4B workflow dispatch after `GEMINI_API_KEY` was configured reached the real GitHub Actions runner and proved credential propagation, but the benchmark process itself did not start.

Observed job steps:

```text
Checkout Saddle                         PASS
Set up Python                           PASS
Verify deterministic scaffold tests    PASS — 65 / 65
Check benchmark credential              PASS
Run approved benchmark                  FAIL
Upload artifact step                    PASS, no benchmark files found
```

The credential gate printed only `Credential presence check: PASS (value not printed).` The secret value was masked in the runner environment.

## FAILURE

The workflow invoked:

```text
python tools/phase4_live_benchmark.py ...
```

and Python failed during module import before benchmark `main()` could execute:

```text
ModuleNotFoundError: No module named 'tools'
```

Root cause: direct script execution makes the script directory (`tools/`) the import-path entry. The benchmark source imports `tools.model_gateway` and `tools.phase4_benchmark`, which require the repository root on `sys.path`.

## EVIDENCE CLASSIFICATION

```text
GEMINI SECRET REFERENCE IN WORKFLOW:      PASS
RUNTIME SECRET PROPAGATION:               PASS
DETERMINISTIC SADDLE REGRESSION:           PASS — 65 / 65
LIVE BENCHMARK PROCESS LAUNCHED:           NO
LIVE GEMINI MODEL CALLS:                   0
LIVE MODEL COST:                           USD 0
API WORKER PERFORMANCE EVIDENCE:           OPEN
MODEL QUALITY EVIDENCE:                    OPEN
FUNCTIONAL SADDLE ACCEPTANCE:              OPEN
MATURITY CLAIM:                            NONE
```

No Gemini request could occur because the Python process failed while importing the benchmark module. No proposal artifact or benchmark result was created.

## DECISION / SCOPE

No product, provider, authority, budget, retry, immutable CASE, evaluator or completion-lock change is required.

This is a bounded launcher defect in the GitHub Actions invocation only.

## FIX

Launch the benchmark as a repository-root module:

```text
python -m tools.phase4_live_benchmark ...
```

and add deterministic CI coverage that:

1. `python -m tools.phase4_live_benchmark --help` imports successfully;
2. the live workflow contains the module launch;
3. direct `python tools/phase4_live_benchmark.py` launch is rejected by the workflow invariant test.

## EXACT NEXT STEP

Merge the bounded launcher fix, then explicitly dispatch the canonical Phase-4B live workflow again on the new `main` head under the unchanged contract:

```text
budget <= USD 5
calls <= 6
automatic retries = 0
proposal only
no model tools/shell/repository write/effect authority
no provider fallback
```

This failed run is workflow/credential/launcher evidence only. It must not be counted as a Gemini worker-performance run or as one of the model calls.