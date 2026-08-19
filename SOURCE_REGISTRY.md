# SOURCE REGISTRY — Saddle

Reconciled: 2026-08-19

Purpose: keep current external source observations separate from historical evidence identities. Repository location or a newer SHA does not transfer semantic ownership or rewrite historical proof.

## Current live source observations

| Source | Observed current main | Current role |
|---|---|---|
| `JTJ07/COS` | `23152cb1bf5443574da9ff44600a5a8c8c136025` | durable high-level/cross-project state, continuity and provenance |
| `JTJ07/creative-os-project-reconstructor` | `defc7b029097284f94136fec54b75c313ac12f68` | project/context reconstruction |
| `JTJ07/scriptops` | `daa6e5dc210e09171a530eeffe5601e0e74ae041` | Phase-6 controlled workflow mechanism proof / local canon-control substrate |
| `JTJ07/Executor` | `d115578cf05ed7edf55c50a2b5d29af16d13fb4d` | Human-accepted and integrated governed effect engine |
| `JTJ07/executor-pilot-target` | `6c18230d2e1223a8145885b19c5073ec1ce20662` | deterministic technical benchmark repository |

Machine-readable copy: `config/source-repos.json`.

These are **observations**, not claims that Saddle owns each project's local truth. Live state must still be read from the local semantic owner when needed.

## Historical Saddle acceptance provenance — do not rewrite

The following identities remain evidence for the exact historical runs that used them:

### Phase 4C synthetic integration

```text
Executor: litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
pilot fixture: litrgratis-pixel/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0
```

Those old locators are historical provenance only. They are not the current live repository snapshot.

### Phase 7 accepted completion path

The Phase-7/current-self identity used during Saddle functional acceptance was:

```text
JTJ07/Executor@728d23e56ec9f76fb7a37673ceb20efccf91e03d
```

At that checkpoint it was current and was part of the accepted Phase-7 evidence chain. It is **not** the current live Executor main in this registry.

### Executor whole-project post-acceptance evaluation

Human-accepted product candidate:

```text
JTJ07/Executor
HEAD f60829f90ea2f69dc501582daf109b59676be07e
TREE 1c4c141415505dd26e1fe307ca1aba987782cfba
```

Verified controlled integration:

```text
merge d3ebe93e9b9d6ec29ff859e931939c89b57ed468
tree 0b569a5abc432ba17d82cb3387e705adf3eb68e6
```

Current live Executor main is later: `d115578cf05ed7edf55c50a2b5d29af16d13fb4d`. The later main does not replace the accepted candidate identity or integration evidence.

## Current project/evaluation facts relevant to Saddle

### Saddle

```text
FUNCTIONAL_SADDLE_ACCEPTED = true
COMPLETION_LOCK = RELEASED
ACTIVE PRODUCT ROADMAP = NONE
POST_ACCEPTANCE_EVALUATION = OBSERVATIONAL
```

### COS

COS has Human-accepted ownership/state/continuity closure. It preserves cross-project state and provenance; local component truth remains local. COS does not own operational HOW/cognitive routing.

### ScriptOps

Current local status at the observed main:

```text
PHASE 6 CONTROLLED WORKFLOW MECHANISM PASS
NO MATURITY CLAIM
SADDLE LIVE MODEL EVIDENCE NEXT
```

This is a local ScriptOps state, not a new Saddle product claim.

### Executor

Current durable target records establish:

```text
PROJECT COMPLETION: PASS
EXECUTOR 1.0: HUMAN ACCEPTED
IMPLEMENTATION INTEGRATION: COMPLETE
```

Saddle captures only the cross-project evaluation result in `evidence/PROJECT_COMPLETION_AUTONOMY_EXECUTOR_RESULT_2026-08-19.md`; detailed Executor truth remains in Executor.

## Source authority rules

```text
CURRENT LIVE SHA != HISTORICAL ACCEPTED IDENTITY
REPO LOCATION != SEMANTIC OWNERSHIP
OPEN PR != CURRENT AUTHORITY
AI MEMORY != REPO FACT
RECORDING != HUMAN AUTHORIZATION
TECHNICAL PASS != HUMAN ACCEPTANCE
```

Before using an external source for consequential work, recheck its live repository state. This registry is durable continuity, not a remote locking mechanism.
