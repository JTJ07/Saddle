# ECOSYSTEM MAP — CURRENT

Reconciled: 2026-08-19
Status: `CURRENT CROSS-PROJECT OWNERSHIP MAP / NOT A COMMAND PIPELINE`

This map exists so a zero-history operator can recover current component roles and handoff boundaries. It is not a router, planner, roadmap or claim that Saddle owns the other repositories.

## Ownership network

```text
HUMAN
  owns intent / goal / DONE / normative decisions / consequential authority / final acceptance

GINSENG
  owns decision-space understanding / lineage / premises / alternatives / consequences / uncertainty

EXTERNAL / BASE INTELLIGENCE
  proposes/selects HOW and performs cognitive routing within accepted constraints

SADDLE
  validates proposed HOW against intent / goal / DONE / boundaries / invariants
  does NOT originate, rank, select or route direction

COS
  preserves durable high-level/cross-project state, continuity and provenance
  does NOT replace local semantic owners or operational HOW selection

CONTRACTS
  materialize/bind already accepted meaning and scope into bounded executable form
  do NOT create normative meaning, goal, HOW or effect authority

EXECUTOR
  governs authorized consequential effects within the accepted solution boundary

VERIFIER
  independently establishes facts
```

The ecosystem is an **ownership network with handoffs**, not a master command-control pipeline.

## Last observed repository snapshot

| Component/project | Observed main at source-snapshot reconciliation | Meaning of that snapshot for Saddle |
|---|---|---|
| `JTJ07/Saddle` | resolve live `main` at read time | functional product accepted; completion lock released; PR #29 security hardening, PR #33 durable-state reconciliation and PR #35 current-state reconciliation are Human-accepted/integrated; post-acceptance evaluation only |
| `JTJ07/COS` | `a9982d9f0ae73d8a09c3af8ce0825890784fa2ad` | Human-accepted ownership/state/continuity closure; later local/cross-project continuity may be newer |
| `JTJ07/Executor` | `111e9e5d4fca66412e287852abdec6db5a1225ab` | Executor 1.0 Human-accepted and integrated; final completion authority/current-state surfaces reconciled |
| `JTJ07/scriptops` | `5af0cd8ac65e72ae534827c677fe4bd12b23e4ca` | historical continuity observation; later accepted ScriptOps history includes bounded proposal view and Run 003 |
| `JTJ07/creative-os-project-reconstructor` | `eb21b04e7d04caf777d66721f86ae9e83aab1dd4` | Run 001 integration observation; later accepted local history includes validator root-containment P0 hardening |
| `JTJ07/executor-pilot-target` | `6c18230d2e1223a8145885b19c5073ec1ce20662` | deterministic technical benchmark substrate |

These SHAs are last-observed continuity snapshots from the source-snapshot reconciliation, not remote locks. Local detailed truth remains with each project and live state must be re-resolved from the local semantic owner before consequential use. Later accepted local-owner history may therefore be newer than this table without turning the table into a false `CURRENT LIVE` claim.

Saddle deliberately does not hard-code its own live `main` SHA here, because a self-pointer becomes stale as soon as this state record is merged; historical integration SHAs remain preserved in `PROJECT_STATE.md` and `SESSION_HANDOFF.md`.

## Saddle current product state

```text
FUNCTIONAL_SADDLE_ACCEPTED = true
COMPLETION_LOCK = RELEASED
ACTIVE COMPLETION GATE = NONE
ACTIVE PRODUCT ROADMAP = NONE
SECURITY HARDENING PR #29 = HUMAN ACCEPTED / MERGED
DURABLE-STATE RECONCILIATION PR #33 = HUMAN ACCEPTED / MERGED
CURRENT-STATE RECONCILIATION PR #35 = HUMAN ACCEPTED / MERGED
PRODUCTION REQUEST-ORIGIN / HUMAN-IDENTITY TRUST PROVIDER = OPEN
MATURITY CLAIM = NONE
```

The accepted product path and historical exact identities remain in `PROJECT_STATE.md`, decisions and evidence. Newer source observations do not rewrite historical evidence.

## Post-acceptance evaluation state

Method:

`docs/PROJECT_COMPLETION_AUTONOMY_TEST_PROTOCOL.md`

First whole-project target:

```text
JTJ07/Executor
RESULT = PROJECT COMPLETION PASS
HUMAN ACCEPTANCE = ACCEPTED
IMPLEMENTATION INTEGRATION = COMPLETE
FALSE SUCCESS PATHS IN FINAL TARGET EVIDENCE = 0
```

Saddle result record:

`evidence/PROJECT_COMPLETION_AUTONOMY_EXECUTOR_RESULT_2026-08-19.md`

Reconstructor Real-Value Run 001:

```text
REAL_VALUE_OBSERVED = YES
TARGET_CURRENT_STATE_CONTRADICTIONS_FOUND = 4
PROMPT_CHANGE_TRIGGERED = NO
```

Later accepted local Reconstructor history includes bounded validator root-containment/hardlink P0 hardening. That maintenance does not alter the Run 001 semantic result or authorize a prompt change.

ScriptOps Real Workloads 001–003:

```text
RUN 003 BOUNDED_UPSTREAM_CONTEXT = PASS
RUN 003 DOWNSTREAM_CANDIDATE = STAGED
RUN 003 CROSS_SCENE_PROPOSAL_COHERENCE = OBSERVED PASS
CANONICAL_EFFECT = NOT APPLIED
HUMAN_APPROVAL = NOT REQUESTED
GOAL_DONE = NO
CURRENT LOCAL WORK-STATE = WAITING_FOR_EVIDENCE / HUMAN_SEMANTIC_DECISION
```

Interpretation: **observed evaluation evidence only**. No automatic Saddle roadmap consequence. Reconstructor and ScriptOps supply materially different observed workloads, but no universal generalization claim follows automatically.

Whole-ecosystem adversarial integration remains a separate `TEST HYPOTHESIS / NOT EXECUTED`. It requires an explicit Human gate before execution and does not become active merely because earlier evaluation items completed.

## Current cross-project boundaries

### Human ↔ Intelligence

Human fixes goal/DONE, normative choices and consequential authority. Intelligence may choose route/HOW only inside that accepted envelope.

### Ginseng ↔ Intelligence

Ginseng maps the decision space and lineage. Intelligence chooses/proposes operational HOW. Ginseng analysis must not silently become route selection or effect authority.

### Intelligence ↔ Saddle

Intelligence supplies a proposed path. Saddle may validate or reject it against intent/boundaries. Saddle must remain removable from HOW generation/ranking/routing without disabling Intelligence's ability to choose HOW.

### Accepted meaning ↔ Contracts

Contracts bind accepted meaning/scope into executable representations. Contract formation must not invent goal, scope, solution semantics or Human authority merely because it can serialize them.

### Contracts/authority ↔ Executor

Executor receives exact bounded authorized effects. Capability to execute does not create permission. Execution planning may choreograph an already selected solution, but solution planning belongs upstream to Intelligence.

### Executor ↔ Verifier

Executor produces effects and evidence. Verifier establishes facts independently. Executor cannot establish final truth merely by declaring PASS.

### COS ↔ local project truth

COS may preserve high-level accepted state, provenance and local owner locators. A COS copy must never override newer authoritative local project truth.

## Current maintenance/evaluation queue relevant to Saddle

This is status information, not a product roadmap.

```text
P0 — security / authority / current-state correctness
     Saddle EffectAuthority hardening COMPLETE / Human accepted / PR #29 merged
     external-pointer reconciliation COMPLETE / Human accepted / PR #35 merged
     source SHAs are last-observed snapshots, not live locks

P1 — post-acceptance durable-state reconciliation
     COMPLETE / Human accepted / PR #33 merged

P2 — memory/repo recovery evidence from design sessions
     WAITING_FOR_EVIDENCE / inbox
     preserve with authority labels; no memory-to-canon promotion
     may preempt only when evidence changes safety, authority, current-state correctness or highest constraint

P3 — materially different project evaluations
     Reconstructor Run 001 COMPLETE / integrated observed evidence
     ScriptOps Runs 001–003 COMPLETE / integrated observed evidence
     ScriptOps local state WAITING_FOR_EVIDENCE / HUMAN_SEMANTIC_DECISION
     no new P3 execution item is self-authorized by Saddle
     whole-ecosystem adversarial integration = TEST HYPOTHESIS / NOT EXECUTED / HUMAN GATE REQUIRED

P4 — new capabilities
     only after a measured blocker and explicit Human product decision
```

Priority classes describe work risk/urgency. They do not transfer semantic ownership to Saddle or COS. A waiting P2 inbox does not create a replacement P3 task, and completion of prior evaluations does not authorize Saddle to select the next operational direction.

## Historical provenance that must not be mistaken for current state

Historical Phase-4C and Phase-7 exact source identities remain valid for those runs. See `PROJECT_STATE.md`, `SOURCE_REGISTRY.md` and their evidence refs. They must not be overwritten by newer observed source SHAs, but they also must not be labeled current.

Likewise, closed superseded PRs remain historical/supporting evidence; open state is not authority.

## Must remain true if any component is replaced

Replacing a component must not implicitly transfer another owner's semantic rights:

```text
Human intent remains Human-owned.
Decision-space understanding does not become route authority.
Intelligence retains HOW selection.
Saddle remains validation/integrity, not routing.
COS remains continuity, not local canon or HOW owner.
Contracts remain binding/materialization, not normative ownership.
Executor remains consequence governance, not goal ownership.
Verifier remains independent fact establishment.
```
