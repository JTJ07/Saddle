# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

Authority: `DECISION_LOG.md` > `PROJECT_STATE.md` > `EXECUTION_PLAN.md` > `TODO.md` > `SESSION_HANDOFF.md` > draft analysis.

Rules: work by the current evidence dependency, keep exactly one `READY / NEXT` item, require evidence for DONE/PASS, park new ideas, preserve broken benchmarks, and do not expand capability before the active proof gate. DEC-SAD-007 permits routine execution but not goal/lock/security/financial/authority expansion or self-declared functional acceptance.

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

## T6 — Phase 4 live AI-worker evidence
Status: `BLOCKED / NEXT HUMAN SECURITY ACTION`
Direction/scaffold: `PASS / FROZEN`.
Live evidence: `OPEN`.

Human authorization: `DEC-SAD-011`.

Approved bound:

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

Already completed:
- immutable CASE-001–003 pins;
- proposal-only WorkerProposal;
- thin ModelGateway;
- no model effect authority;
- exact target/hash/diff validation;
- Sol/Terra current public API availability reverified from official OpenAI sources;
- GitHub Actions benchmark runner created in PR #14;
- complete deterministic regression on that runner: `54 tests / OK`;
- runner/effect token permissions remain read-only;
- benchmark preflight run `31423378809`, job `93569214499` stopped before API because `OPENAI_API_KEY` is absent;
- model calls `0`, retries `0`, spend `USD 0`.

### READY / NEXT — only active item

Configure GitHub Actions repository secret:

```text
Repository: litrgratis-pixel/Saddle
Secret name: OPENAI_API_KEY
```

Do **not** place the secret in chat, source files, PR comments, logs or evidence.

After it is configured, re-run failed benchmark run `31423378809` / job `93569214499` under the unchanged approved limits.

Then:
1. compare Sol/Terra on CASE-001 first;
2. continue CASE-002/003 only within call/budget guard;
3. record proposal correctness, scope, structure, rationale, tests, tokens, cost, latency and retries;
4. move result to `EVALUATION -> HUMAN DECISION`;
5. do not automatically expand autonomy.

Later, at least one selected validated proposal must cross the controlled Executor/effect boundary before live-AI evidence can fully close.

No dynamic router, multi-agent, general tool expansion or unrestricted worker shell/write/network.

## T7 — Phase 5 strict verified-intent + effect-authority boundaries
Status: `DONE / FROZEN`

Evidence:
- `VerifiedIntentBinding` + independent raw-intent hash;
- exact separate `EffectAuthority`;
- 15/15 tests PASS;
- no semantic interpretation/user-label/model-confidence path can create permission;
- replay/stale/deny/mismatch/raw-intent mutation cases BLOCK.

Trust provider remains intentionally unselected.

## T8 — Phase 6 ScriptOps controlled workflow
Status: `DONE / CONTROLLED WORKFLOW MECHANISM PASS / NO MATURITY CLAIM`

Human decision: `DEC-SAD-010` / ScriptOps `DEC-SO-010`.

```text
BASE: legacy/scriptops-v2-single.py
REWRITE: NO
NEW CAPABILITY: NO
PHASE 6: reuse + hardening + proof
```

Canonical ScriptOps evidence:
- PR #7 merged as `daa6e5dc210e09171a530eeffe5601e0e74ae041`;
- final verified head `acbfca79f96407dbd46f9806bf821caf6e02e1af`;
- repository verifier run `31421752036` SUCCESS;
- Phase-6 smoke run `31421752569` SUCCESS;
- Saddle evidence: `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

B1–B5 closed: clean checkpoints, generated-artifact lifecycle, fresh accepted hash, mandatory `why`, impact report + end-to-end smoke. Historical v2 remained unchanged.

Do not infer ScriptOps maturity, independent product value, AI-worker success or functional Saddle from this proof.

## T9 — Phase 7 functional Saddle acceptance
Status: `BLOCKED UNTIL T6 LIVE AI EVIDENCE`

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

Only the complete evidence set + explicit human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## T10 — Phase 8 post-acceptance direction
Status: `BLOCKED UNTIL T9`
Completion lock does not release automatically.

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

No multi-agent/swarm runtime, Company Loop, full Ginseng runtime/UI, vector DB/general RAG, browser automation, broad MCP marketplace, dynamic model routing, hidden agent memory, dashboard, self-hosted model platform, generalized enterprise IAM, autonomous resource acquisition, self-preservation objective, or autonomous self-modification outside bounded eval/sandbox/adoption gates.
