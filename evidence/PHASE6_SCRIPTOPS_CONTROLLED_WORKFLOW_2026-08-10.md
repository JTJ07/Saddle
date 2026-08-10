# Saddle Phase 6 — ScriptOps Controlled Workflow Evidence

Date: 2026-08-10
Status: `CROSS-REPO EVIDENCE / CONTROLLED WORKFLOW MECHANISM PASS / NO MATURITY CLAIM`

## Human decision

The user explicitly selected the first real-workflow base:

```text
DECISION: YES
BASE: legacy/scriptops-v2-single.py
REWRITE: NO
NEW CAPABILITY: NO
PHASE 6: reuse + hardening + proof
MATURITY CLAIM: NONE
FUNCTIONAL_SADDLE_ACCEPTED: NOT YET
```

This is recorded in ScriptOps as `DEC-SO-010` and in Saddle as `DEC-SAD-010` on the synchronization change set.

## Canonical ScriptOps result

Repository: `litrgratis-pixel/scriptops`

Merged PR: `#7 — Phase 6: harden ScriptOps v2 and prove one controlled workflow`

Canonical merge commit:

`daa6e5dc210e09171a530eeffe5601e0e74ae041`

Final verified pre-merge head:

`acbfca79f96407dbd46f9806bf821caf6e02e1af`

The historical `legacy/scriptops-v2-single.py` was preserved unchanged. Phase 6 added a small auditable hardening shim over it rather than rewriting the substrate.

## B1–B5 result

| Blocker | Result | Proof |
|---|---|---|
| B1 task creation conflicts with clean preflight | PASS | task is committed as a durable checkpoint before preflight |
| B2 generated evidence/candidate dirt blocks approval | PASS | preflight/context/candidate input/impact are explicit checkpoints; unrelated dirty state blocks |
| B3 accepted hash stale after status change | PASS | accepted artifact is written with a freshly recomputed scene hash |
| B4 approval lacks rationale | PASS | `approve --why` is mandatory and rationale is persisted |
| B5 no impact report / smoke proof | PASS | `impact-report.json` plus full temporary-Git end-to-end smoke |

## Controlled path proved

```text
review
→ task checkpoint
→ check-pre
→ preflight evidence checkpoint
→ context-build
→ context checkpoint
→ candidate input checkpoint
→ check-post validation/staging
→ impact report
→ explicit human-style approve --why
→ canonical accepted scene
→ fresh accepted identity/hash
→ decision log
→ Git commit
```

Candidate material remains a proposal artifact until the explicit human decision. ScriptOps does not gain its own intent interpretation, effect authority or autonomous goal planning.

## Final GitHub Actions evidence

On final head `acbfca79f96407dbd46f9806bf821caf6e02e1af`:

- `Verify repository state` — run `31421752036` — `success`;
- `Phase 6 ScriptOps smoke` — run `31421752569` — `success`.

An earlier run exposed stale assertions in ScriptOps' existing continuity verifier: it still required the historical `ACCESS CHECK REQUIRED` state even though canonical ScriptOps had already advanced beyond that gate. The verifier was corrected to validate the current bounded Phase-6 state while preserving the byte-for-byte historical v2 integrity check. Both final checks then passed together.

## Responsibility-model result

Phase 6 supports the current Saddle split:

```text
candidate = proposal, not authority
impact report = evidence for review, not permission
human decision = semantic approval
ScriptOps execution = bounded consequence
Git + decision log = durable evidence
```

It does not make ScriptOps a replacement for Saddle or Executor.

## What this proves

It proves that an existing real workflow substrate can be reused and hardened into one controlled proposal-to-human-decision-to-durable-change loop without rewrite or capability expansion.

## What this does NOT prove

- no ScriptOps v5/RC1 maturity claim;
- no independent external-user/product-value validation;
- no live real-model Saddle worker benchmark;
- no real-model proposal routed through Executor yet;
- no production request-origin/identity provider;
- no complete Saddle `EffectReceipt -> StateDelta -> zero-history resume` acceptance loop;
- no `FUNCTIONAL_SADDLE_ACCEPTED`.

## Next evidence gate

Per the user's explicit ordering, after this Phase-6 mechanism proof Saddle returns to the still-open live AI-worker evidence:

1. authorized external model runner with provider HTTPS;
2. provider credential in secure secret storage, never chat/repo/evidence;
3. explicit paid benchmark budget approval;
4. same immutable CASE-001–003 run across at least two current suitable model candidates;
5. validated real-model proposal through the controlled Executor/effect path;
6. Phase-3 eval evidence before any first worker selection.
