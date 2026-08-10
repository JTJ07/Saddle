# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

Authority: `DECISION_LOG.md` > `PROJECT_STATE.md` > `EXECUTION_PLAN.md` > `TODO.md` > `SESSION_HANDOFF.md` > draft analysis.

Rules: work top-to-bottom; one implementation item at a time; `DONE` needs evidence; park new ideas; keep broken eval inputs reproducible; DEC-SAD-007 permits routine scheduled execution but not goal/lock/security/authority expansion or self-declared functional acceptance.

## T0 — Durable-memory bootstrap
Status: `DONE`

## T1 — Preserve six-part test evidence
Status: `DONE`

## T2 — Preserve new ideas without activation
Status: `DONE`
IDEA-SAD-014/015 remain `PARKED`.

## T3 — Ecosystem reconciliation
Status: `DONE`
Evidence: canonical merge `2e0bd347...`.

## T4 — Freeze Saddle Protocol v0.1
Status: `DONE`
Evidence: canonical merge `819449ba...`, 14 protocol tests.

## T5 — Minimal audit + eval foundation
Status: `DONE`
Evidence: canonical merge `801f0561...`, 12 Phase-3 tests / 26 combined regression.

## T6 — First real AI worker through Saddle/Executor
Status: `READY / NEXT`
Execution condition: `BLOCKED ON EXTERNAL HUMAN/INFRASTRUCTURE GATE`.

Completed before blocker:
- exact CASE-001–003 broken commits pinned;
- proposal-only WorkerProposal schema;
- thin ModelGateway + OpenAI Responses adapter;
- no tools/shell/write/network authority for model;
- exact target/diff budget/control-plane hashes;
- non-secret preflight;
- pinned-checkout proposal runner;
- Sol/Terra first-pass candidate plan;
- 13 local scaffold tests PASS.

Current real preflight:
`BLOCKED / PROVIDER_CREDENTIAL_NOT_CONFIGURED`.

Real benchmark requires:
1. authorized runner with outbound provider HTTPS;
2. `OPENAI_API_KEY` in that runner's secret store/environment, never chat/GitHub/evidence;
3. explicit paid benchmark budget approval.

Recommended first pass: 3 cases × 2 models × 1 call, zero automatic retries, USD 5.00 hard cap.

After unblocking:
- verify account access to both model IDs;
- run identical pinned cases;
- route validated proposal through Executor effect boundary;
- record Phase-3 eval results;
- select one worker only from evidence.

Do not mark T6 DONE before real CASE-001–003 results.

## T7 — Verified intent / effect authority boundary
Status: `BLOCKED UNTIL T6`
Use Executor #51–#57 under Saddle ownership model; one minimal authority adapter only; no generalized IAM.

## T8 — Minimal ScriptOps real-domain path
Status: `HUMAN SEMANTIC GATE + BLOCKED ON T6–T7`
Open decision: select/reject `legacy/scriptops-v2-single.py`; technical recommendation remains YES/reuse v2.

## T9 — Functional Saddle acceptance
Status: `BLOCKED UNTIL T6–T8`
Required fresh-session loop: intent → IntentEnvelope → context recovery → real AI → EffectProposal → authority/effect gate → bounded execution → EffectReceipt/evidence → required human review → StateDelta → second zero-history resume.

## T10 — Post-acceptance human direction
Status: `BLOCKED UNTIL T9`
Completion lock does not release automatically.

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

No multi-agent/swarm runtime, Company Loop, full Ginseng runtime/UI, vector DB/general RAG, browser automation, broad MCP marketplace, dynamic model routing, hidden agent memory, dashboard, self-hosted model platform, generalized enterprise IAM, autonomous resource acquisition, self-preservation objective, or autonomous self-modification outside bounded eval/sandbox/adoption gates.
