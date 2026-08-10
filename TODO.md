# SADDLE TODO — OPERATIONAL COMPLETION QUEUE

Status: `ACTIVE / COMPLETION LOCK ENFORCED`
Updated: 2026-08-10

Authority: `DECISION_LOG.md` > `PROJECT_STATE.md` > `EXECUTION_PLAN.md` > `TODO.md` > `SESSION_HANDOFF.md` > draft analysis.

Rules: work top-to-bottom; one next gate at a time; `DONE` needs evidence; park new ideas; keep broken eval inputs reproducible; DEC-SAD-007 permits routine scheduled execution but not goal/lock/security/authority expansion or self-declared functional acceptance.

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

## T6 — Phase 4 AI proposal worker direction
Status: `DIRECTION PASS / SCAFFOLD FROZEN / LIVE MODEL EVIDENCE DEFERRED`

Completed:
- immutable CASE-001–003 pins;
- proposal-only WorkerProposal;
- thin ModelGateway;
- no model effect authority;
- exact target/hash/diff validation;
- Sol/Terra first-pass benchmark plan.

Still required before final functional acceptance:
- authorized external model runner;
- secure provider credential;
- approved paid benchmark budget;
- real two-model results;
- measured quality/cost/latency/tokens/retries;
- validated real-model proposal through controlled Executor/effect path.

Do not mark this live evidence complete until it actually occurs.

## T7 — Phase 5 strict verified-intent + effect-authority boundaries
Status: `DONE ON CURRENT CHANGE SET`

Human decisions:
- `DEC-SAD-008` — Saddle preserves intent integrity; does not authorize meaning;
- `DEC-SAD-009` — freeze Phase 1–4 foundations; advance strict Phase 5.

Artifacts:
- `authority/v0.1/verified-intent-binding.schema.json`;
- `authority/v0.1/effect-authority.schema.json`;
- `tools/phase5_boundaries.py`;
- `tests/test_phase5_boundaries.py`;
- `docs/PHASE5_STRICT_BOUNDARIES_v0.1.md`;
- `evidence/PHASE5_STRICT_BOUNDARY_TEST_2026-08-10.md`.

Evidence:
- compileall PASS;
- 15/15 Phase-5 tests PASS;
- goal-expanding AI interpretation without exact authority => BLOCK;
- raw-intent mutation => BLOCK;
- unverified origin => BLOCK;
- authority/proposal mismatch => BLOCK;
- action/target mismatch => BLOCK;
- stale/deny/replay/wrong-intent cases => BLOCK;
- exact positive control => ALLOW.

Trust provider remains intentionally unselected.

## T8 — Phase 6 first real user workflow
Status: `READY / NEXT`
Gate type: `HUMAN SEMANTIC BASE-SELECTION DECISION`.

Open decision:
select or reject `legacy/scriptops-v2-single.py` as the implementation base for the first real workflow.

Current technical recommendation: `YES — reuse v2`.

If selected, repair only:

```text
task
→ context
→ candidate
→ validation
→ impact report
→ human approve/reject/revision with why
→ correct accepted hash
→ Git commit
→ smoke evidence
```

No browser helper, autonomous approval, GUI, vector DB, graph platform, multi-user expansion, agent framework or capability expansion.

## T9 — Phase 7 functional Saddle acceptance
Status: `BLOCKED UNTIL REQUIRED T6 + T8 EVIDENCE`

Required fresh-session loop:

```text
human raw intent
→ integrity/origin binding
→ context recovery
→ real AI proposal
→ exact effect authority
→ bounded real execution
→ verifier evidence
→ required human review
→ StateDelta
→ second zero-history resume
```

Only required evidence + explicit human acceptance may produce `FUNCTIONAL_SADDLE_ACCEPTED`.

## T10 — Phase 8 post-acceptance direction
Status: `BLOCKED UNTIL T9`
Completion lock does not release automatically.

# EXPLICITLY NOT TODO BEFORE FUNCTIONAL ACCEPTANCE

No multi-agent/swarm runtime, Company Loop, full Ginseng runtime/UI, vector DB/general RAG, browser automation, broad MCP marketplace, dynamic model routing, hidden agent memory, dashboard, self-hosted model platform, generalized enterprise IAM, autonomous resource acquisition, self-preservation objective, or autonomous self-modification outside bounded eval/sandbox/adoption gates.
