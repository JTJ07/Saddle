# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

Authority: `DECISION_LOG.md` > `PROJECT_STATE.md` > `EXECUTION_PLAN.md` > `TODO.md` > `SESSION_HANDOFF.md` > draft analysis.

Rules: work by current evidence dependency; require observable evidence for PASS/DONE; park new ideas; preserve broken benchmarks; do not broaden capability before the active proof gate. DEC-SAD-007 permits routine execution but not goal/lock/security/financial/authority expansion or self-declared functional acceptance.

## T0 — Durable-memory bootstrap
Status: `DONE`

## T1 — Preserve six-part test evidence
Status: `DONE`

## T2 — Preserve new ideas without activation
Status: `DONE`
IDEA-SAD-014/015 remain `PARKED`.

## T3 — Ecosystem / responsibility reconciliation
Status: `DONE / FROZEN`
Evidence: canonical merge `2e0bd347...`.

## T4 — Saddle Protocol v0.1
Status: `DONE / FROZEN`
Evidence: canonical merge `819449ba...`, 14 protocol tests.

## T5 — Audit + eval foundation
Status: `DONE / FROZEN`
Evidence: canonical merge `801f0561...`, fail-closed JSON/JSONL harness.

## T6A — Phase 4A web-AI cognitive calibration
Status: `BASELINE DONE / SUPPORTING EVIDENCE ONLY`
Human decision: `DEC-SAD-012`.

Purpose:
- calibrate the Saddle <-> Intelligence contract in a human-guided web environment;
- test proposal correctness, scope discipline, authority discipline, goal preservation, rationale and structure;
- refine the formal API eval before reproducible worker runs.

Evidence:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`;
- 3 manual CASE-001/002/003 runs;
- 3/3 boundary-discipline PASS;
- 0 scope violations;
- 0 authority invention/smuggling;
- 0 execution claims;
- reconstructed visible tests: 13/13 PASS for each proposal.

Limitation:
- all baseline runs were context-contaminated;
- independent model-solving ability is not evaluated or claimed;
- fresh web repeats are optional unless they reveal a contract defect.

Hard rule:

`WEB_AI_CALIBRATION != API_WORKER_EVIDENCE`.

## T6B — Phase 4B reproducible API worker evidence
Status: `READY / NEXT`
Blocker: `HUMAN SECURITY ACTION — OPENAI_API_KEY REPOSITORY SECRET REQUIRED`.
Direction/scaffold: `PASS / FROZEN`.
Formal worker evidence: `OPEN`.

Human approval: `DEC-SAD-011`.

```text
BUDGET: max USD 5
CALLS: max 6
AUTOMATIC RETRIES: 0
SCOPE: benchmark only
NEW CAPABILITY: NO
AUTONOMOUS EXECUTION: NO
AUTHORITY EXPANSION: NO
TOOL ACCESS EXPANSION: NO
```

Calibration-frozen evaluation dimensions:
1. proposal correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion beyond human task;
5. rationale quality;
6. structured-output stability;
7. objective evidence plan;
8. human corrections required.

Preflight evidence:
- PR #14 / run `31423378809` / job `93569214499`;
- GitHub runner available;
- Saddle regression `54 tests / OK`;
- missing `OPENAI_API_KEY` detected before any model call;
- calls `0`, retries `0`, spend `USD 0`, proposals `0`.

### NEXT HUMAN SECURITY ACTION — only active blocker

Configure GitHub Actions repository secret:

```text
Repository: litrgratis-pixel/Saddle
Secret name: OPENAI_API_KEY
```

Never place the secret in chat, source, PR comments, logs or evidence.

After configuration, rerun existing failed run `31423378809` / job `93569214499` under unchanged limits. Then compare Sol/Terra on the immutable cases, record calibrated eval dimensions + tokens/cost/latency/retries, and move results to `EVALUATION -> HUMAN DECISION`.

At least one later selected validated real-model proposal must cross the controlled Executor/effect boundary before live-AI evidence can fully close.

## T7 — Phase 5 strict verified-intent + effect-authority boundaries
Status: `DONE / FROZEN`

Evidence:
- `VerifiedIntentBinding` + independent raw-intent hash;
- separate exact `EffectAuthority`;
- 15/15 tests PASS;
- no semantic interpretation/user-label/model-confidence path can create permission;
- replay/stale/deny/mismatch/raw-intent mutation cases BLOCK.

Trust provider remains intentionally unselected.

## T8 — Phase 6 ScriptOps controlled workflow
Status: `DONE / CONTROLLED WORKFLOW MECHANISM PASS / NO MATURITY CLAIM`

Human decision: `DEC-SAD-010` / ScriptOps `DEC-SO-010`.

Canonical evidence:
- ScriptOps PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`;
- final verified head `acbfca79f96407dbd46f9806bf821caf6e02e1af`;
- repository verifier run `31421752036` SUCCESS;
- Phase-6 smoke run `31421752569` SUCCESS;
- Saddle evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

No ScriptOps maturity or independent product-value claim.

## T9 — Phase 7 functional Saddle acceptance
Status: `BLOCKED UNTIL T6B LIVE AI EVIDENCE`

Required fresh-session loop:

```text
human raw intent
→ integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ verifier / EffectReceipt evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

Only complete evidence + explicit human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## T10 — Phase 8 post-acceptance direction
Status: `BLOCKED UNTIL T9`
Completion lock does not release automatically.

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

No multi-agent/swarm runtime, Company Loop, full Ginseng runtime/UI, vector DB/general RAG, browser automation, broad MCP marketplace, dynamic model routing, hidden agent memory, dashboard, self-hosted model platform, generalized enterprise IAM, autonomous resource acquisition, self-preservation objective, or autonomous self-modification outside bounded eval/sandbox/adoption gates.
