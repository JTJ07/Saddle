# SADDLE AUDIT + EVAL FOUNDATION v0.1

Status: `ACCEPTED FOUNDATION / TERMINAL-STATE AWARE`

Purpose: keep Saddle progress and post-acceptance evaluation measurable with plain files and deterministic code before introducing any observability platform.

## 1. Eval record

Schema: `eval/v0.1/eval-result.schema.json`.

Each run records identity, lane/case, subject/source, `PASS / FAIL / BLOCKED / ERROR`, model/provider when actually used, measured metrics only, violations, evidence refs, timestamps and notes. Unknown metrics remain `null`; they must not be fabricated.

## 2. Fail-closed aggregation

`tools/eval_harness.py aggregate` remains fail-closed:

- zero records → `BLOCKED`;
- any `ERROR` → `ERROR`;
- otherwise any `FAIL` → `FAIL`;
- otherwise any `BLOCKED` → `BLOCKED`;
- only all-PASS → `PASS`;
- any scope/policy violation forces effective `FAIL` even if the candidate declared PASS.

## 3. Repository audit — current semantics

`tools/eval_harness.py audit --root .` supports both historical active-completion mode and the accepted terminal functional state.

Current terminal-state expectations are:

```text
FUNCTIONAL_SADDLE_ACCEPTED present in PROJECT_STATE and SESSION_HANDOFF
active phase = NONE
active operational TODO gate count = 0
PROJECT_STATE completion_lock = RELEASED
config/completion-lock.json status = RELEASED
```

Before functional acceptance, the historical fail-closed behavior remains: state/handoff require a matching active phase, completion lock ACTIVE and exactly one active operational gate.

The audit also checks required root continuity/governance files, frozen Protocol v0.1, superseded historical protocol draft, and machine-readable source repository snapshots.

`config/source-repos.json` records observations. Audit validity does not mean those remote SHAs are eternally current; live GitHub must be rechecked before consequential use.

## 4. Eval lane registry

`config/eval-lanes.json` is a lightweight evidence locator/status registry, not a dashboard or scheduler.

It now distinguishes:

- accepted historical foundations/baselines;
- completed Phase-4 live evidence;
- accepted Phase-7 functional evidence;
- ScriptOps Phase-6 controlled workflow proof;
- post-acceptance whole-project completion autonomy evaluation;
- Reconstructor real-value repetition as a future evaluation candidate.

Lane status does not activate a product roadmap or authorize an effect.

## 5. CLI

```text
python tools/eval_harness.py validate path/to/results.jsonl
python tools/eval_harness.py aggregate path/to/results.jsonl --output evidence/summary.json
python tools/eval_harness.py audit --root . --output evidence/repo-audit.json
```

Exit behavior:

- `0` only for PASS;
- `1` for valid but non-PASS aggregate/audit;
- `2` for malformed/invalid evidence.

## 6. Evidence discipline

A historical result may be encoded only with metrics that actually exist. Missing values stay null.

```text
CANDIDATE PASS != VERIFIED PASS
EXECUTION != PROOF
TECHNICAL PASS != HUMAN ACCEPTANCE
CURRENT LIVE SHA != HISTORICAL ACCEPTED IDENTITY
```

Evidence refs must be non-empty.

## 7. Explicit non-goals

This foundation does not add:

- an observability platform;
- agent orchestration;
- a database;
- automatic remote GitHub crawling;
- a provider selector;
- a model worker;
- a trust/authority provider;
- an autonomous roadmap;
- a new memory layer.

The foundation exists only to make state and evaluation objectively auditable.
