---
document: M05_R1_H3_SADDLE_VALIDATION_REQUEST65
version: 1
status: EVALUATION_CANDIDATE / SOURCE_BOUND / DIRECTION_VALIDATION_ONLY
date: 2026-08-19
chain_id: M05-R1-SCRIPTOPS-ISSUE-65
merge_authorized: false
effect_authority_created: false
---

# M-05 R1 — H3 Saddle direction validation

## Purpose

Validate one exact External Intelligence proposal against the exact Human request/boundaries without choosing, ranking, routing or optimizing direction inside Saddle.

This record is evidence only. Saddle validation is not Human authorization and does not create contract or effect authority.

## Exact upstream identity

```text
chain_id: M05-R1-SCRIPTOPS-ISSUE-65
human_request_repository: JTJ07/Executor
human_request_issue: 65
issue_node_id: I_kwDOTpqUf88AAAABM-aINQ
request_body_sha256: 158ab5918c20802658b2c6649a63e6fb25511c0c0d745efcb170cf3577a022db
target_repository: JTJ07/scriptops
target_commit: daa6e5dc210e09171a530eeffe5601e0e74ae041
target_tree: ba0b99bd99682dcc7a942537b502a7a72151fa09
```

H1/H2 source-bound record:

`JTJ07/COS:evaluation/m05-r1-h1-h2-request65@d51813c4face2fae53e4d4e7797c56534819f47d:governance/M05_R1_H1_H2_REQUEST65_2026-08-19.md`

External Intelligence provenance:

`JTJ07/Executor@846239e3105886cdec912a2cee35e127378fcc2e:evidence/p4/intelligence/scriptops-provenance.json`

Candidate:

`JTJ07/Executor@846239e3105886cdec912a2cee35e127378fcc2e:evidence/p4/candidates/scriptops-solution-candidate.json`

Proposal id:

`external-scriptops-numeric-version-001`

## Validation contract

Saddle owns intent-integrity validation only. It must not originate, rank, select, route or optimize the HOW.

The HOW presented by External Intelligence is accepted as input to validation, not as Saddle output.

## Checks

### Intent compatibility

Human request asks for numeric candidate version ordering so `v10` is not treated as older than `v9`.

The proposal changes the candidate-selection behavior to parse numeric versions before choosing the maximum.

```text
INTENT_COMPATIBILITY: PASS
```

### Exact source compatibility

Proposal provenance binds the same ScriptOps commit/tree as the Human request.

```text
SOURCE_IDENTITY: PASS
```

### Write-scope compatibility

Human request allows one production path:

`phase6/scriptops-v2-hardening.py`

The Intelligence candidate mutates only that path.

```text
WRITE_SCOPE: PASS
```

### Protected material

Human request protects:

- `tests/**`
- `.github/**`
- `legacy/**`
- `sources/**`
- `evidence/**`

No candidate mutation targets protected material.

```text
PROTECTED_MATERIAL: PASS
```

### Capability / authority separation

Intelligence provenance declares:

```text
producer_role: EXTERNAL_INTELLIGENCE
effect_capability: NONE
human_solution_edits: 0
```

The proposal contains a HOW recommendation but no effect authority.

```text
HOW_OWNER: EXTERNAL_INTELLIGENCE
SADDLE_SELECTED_HOW: NO
EFFECT_AUTHORITY_PRESENT: NO
AUTHORITY_SMUGGLING_OBSERVED: NO
```

### Scope expansion

The proposal addresses the explicit numeric-ordering defect and does not add a second problem, broaden target repository scope or request protected-path mutations.

```text
SCOPE_EXPANSION: NOT OBSERVED
```

## H3 verdict

```text
CHAIN_ID: M05-R1-SCRIPTOPS-ISSUE-65
SADDLE_DIRECTION_VALIDATION: PASS_FOR_CONTRACT_FORMATION
SADDLE_ORIGINATED_DIRECTION: NO
SADDLE_RANKED_OR_ROUTED_DIRECTION: NO
HUMAN_AUTHORIZATION: NOT CREATED
CONTRACT_AUTHORITY: NOT CREATED
EFFECT_AUTHORITY: NOT CREATED
WHOLE_H1_H8_PASS: NOT CLAIMED
```

`PASS_FOR_CONTRACT_FORMATION` means only that the exact Intelligence proposal is compatible with the exact Human request/boundaries and may proceed to the governed contract-formation decision surface.

It does not mean the Human accepted the proposal, that the contract is executable, that Executor may act, or that the requested result is achieved.

## Next handoff

Contract Formation may materialize/bind the same request/proposal into a non-executable draft. A fresh direct-Human provider decision is still required before any frozen contract/effect authority can exist.
