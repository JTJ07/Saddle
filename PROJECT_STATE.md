---
project: Saddle
status: BOOTSTRAP / NOT YET FUNCTIONAL
completion_lock: ACTIVE
state_owner: PROJECT_STATE.md
updated_at: 2026-08-10
---

# PROJECT_STATE — Saddle

## 1. Current product definition

Saddle is the durable control layer between human intent and arbitrary AI capability.

It should preserve and verify the direction of travel without unnecessarily prescribing how the underlying intelligence solves the problem.

Core product rule:

> **Maximize usable AI capability; constrain unauthorized effects, not intelligence itself.**

## 2. Current objective

Finish the smallest end-to-end Saddle that can survive complete session loss and prove a real human-intent → AI → controlled effect → evidence → durable-state loop.

The project is in **completion mode**. New product development is frozen.

## 3. Confirmed current ecosystem

Five GitHub repositories are currently accessible under `litrgratis-pixel`:

1. `COS`
2. `creative-os-project-reconstructor`
3. `scriptops`
4. `Executor`
5. `executor-pilot-target`

### Current default-branch checkpoints observed on 2026-08-10

- COS: `3220310267c3d0ba2184daaf3f2adad259a9cb20`
- creative-os-project-reconstructor: `defc7b029097284f94136fec54b75c313ac12f68`
- scriptops: `90a5ba9863961c4b79472db84297cfb403cc5158`
- Executor: `788443c3ed5b290ac8f1de145a93d02d2dd15317`
- executor-pilot-target: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`

These are observation checkpoints, not permanent pins unless a later contract explicitly pins them.

## 4. What already exists and should be reused

### COS

Useful as canonical high-level state/project memory and session-resumption map.

Strong reusable ideas:

- Git-backed memory;
- one owner for each piece of information;
- explicit source hierarchy;
- `BOOT / WORK / AUDIT / PORTFOLIO` modes;
- truthful execution statuses;
- one next step;
- idea parking instead of scope hijack.

### Project Reconstructor

Useful as a context-recovery adapter for projects with fragmented conversations, attachments, aliases, and conflicting documentation.

Current strength: stable v1.0 prompt, deterministic repository validator, regression scenarios.

Current evidence gap: no long-term cross-model semantic validation or automated model eval runner.

### ScriptOps

Useful as the first strong real-domain candidate.

The existing v2 prototype already contains substantial reusable mechanics:

- CLI;
- Git state checks/commits;
- tasks;
- context construction;
- token budgets;
- prompts;
- pre/post AI validation;
- hashing/provenance;
- staging;
- candidate approval path;
- decision-log mechanics.

RC1 is not proven implemented as a separate later build in the accessible GitHub package.

### Executor

Most mature technical control/effect component.

Main already contains:

- request-to-contract phase-1 formation boundary;
- provenance separation of user request and model inference;
- task/project/policy validation;
- exact repository identity/snapshot checks;
- action-authorization machinery;
- networkless hardened Docker sandbox;
- evidence and replay-oriented runtime controls;
- controlled GP001 end-to-end path.

Critical gap: current GP001 solution is still a hard-coded known mutation, not an AI-discovered repair.

Critical main-branch authority gap: `RequestToContract001` stops at `AWAITING_VERIFIED_HUMAN_AUTHORIZATION`; verified human authority + freeze are intentionally not implemented on main.

### executor-pilot-target

Reusable deterministic laboratory with three pinned broken cases:

- CASE-001 atomic batch insertion;
- CASE-002 reopen authorization;
- CASE-003 deterministic output.

Use it to benchmark the first real AI worker without claiming business/product value.

## 5. Important active unmerged work

### Executor PR stack #51–#57

This active draft stack designs the verified-human-authority/trust boundary.

Most important current architectural finding:

```text
USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE
```

PR #57 compares:

- A1: externalized governed request intake;
- strengthened A2: Executor front door + direct external origin attestation before governed formation.

No provider or final A1/A2 selection is canonical yet.

### COS PR #18

Contains valuable ecosystem/Ginseng semantics, especially:

- Ginseng = Decision Intelligence Layer;
- `FACT / DECISION / HYPOTHESIS` separation;
- Decision Lineage;
- impact reasoning via `ELEMENT → FUNCTION/CAPABILITY → EFFECT`;
- prohibition on AI self-confirming its own relations.

Its product-status assumptions are stale relative to later Executor work and must be reconciled before canonical reuse.

## 6. Current gaps that must be closed for functional Saddle

1. Durable Saddle repository and cold-start continuity.
2. Cross-repo canonical-state reconciliation.
3. Minimal Saddle protocol contract.
4. Unified eval/evidence harness.
5. First real AI worker replacing the hard-coded GP001 solution proposal.
6. Verified intent / verified human authority bridge adequate for the first real effect path.
7. One real-domain path (recommended candidate: ScriptOps RC1, subject to source/access reconciliation).
8. Fresh-session end-to-end acceptance proving resumability.

## 7. Functional acceptance definition

`FUNCTIONAL_SADDLE_ACCEPTED` may be recorded only after a real run demonstrates:

1. a human provides a natural request;
2. the verbatim intent is durably preserved and has a stable identity;
3. correct project state/context is recovered without hidden chat memory;
4. real AI independently proposes the useful change/solution;
5. the proposal is not itself treated as authority;
6. a controlled effect path validates scope/permissions;
7. the effect runs in the bounded environment;
8. objective evidence verifies the result;
9. the human can review/accept/reject the result at the correct boundary;
10. canonical state and handoff are updated;
11. a new session with no prior conversation correctly resumes from GitHub alone.

## 8. Current blocker

Phase 0 is active: the Saddle repository now exists and is being populated with the durable bootstrap. The next acceptance condition is a zero-memory cold-start review against the committed repository state.

## 9. One next step

Complete the bootstrap import, verify all canonical files are present on `main`, and run a zero-memory cold-start review against `README.md` + `AGENTS.md` + `PROJECT_STATE.md` + `SESSION_HANDOFF.md`.
