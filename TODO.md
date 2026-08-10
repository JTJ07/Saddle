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
Status: `DONE / ACCEPTED / COGNITIVE CALIBRATION ONLY`
Human decision: `DEC-SAD-012` + `DEC-SAD-013`.

Evidence:
- `docs/PHASE4A_WEB_AI_CALIBRATION.md`;
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md`;
- 3 manual CASE-001/002/003 runs;
- boundary-discipline PASS 3/3;
- scope violations 0;
- authority invention/smuggling 0;
- execution claims 0;
- reconstructed visible tests 13/13 PASS per proposal.

Hard limits:
- all baseline runs remain `CONTEXT_CONTAMINATED`;
- independent model-solving ability is not evaluated or claimed;
- `WEB_AI_CALIBRATION != API_WORKER_EVIDENCE`.

Do not perform more Phase-4A design/calibration unless Phase 4B evidence reveals a contract defect.

## T6B — Phase 4B reproducible API worker evidence
Status: `READY / NEXT`
Blocker: `HUMAN SECURITY ACTION — OPENAI_API_KEY REPOSITORY SECRET REQUIRED`.
Formal worker evidence: `OPEN`.

Human approval `DEC-SAD-011`:

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

Canonical runner:
- PR #15 merged as `3547d42266c8711df35d7694b2839a5be3a11200`;
- proposal-only;
- no model shell/tools/repo write/effect authority;
- ephemeral pinned checkouts only;
- no target-repo push.

Evaluation contract:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion beyond human task;
5. rationale quality;
6. structured-output stability;
7. objective evidence-plan quality;
8. human-correction burden;
9. intent preservation against preserved human-approved intent — no lost goal, added goal or silent priority change.

`Intent preservation` must not become an automated semantic-authority mechanism.

Preflight evidence:
- PR #15 run `31425549563`, job `93576264688`;
- deterministic scaffold tests PASS;
- missing `OPENAI_API_KEY` detected before any model call;
- calls 0, retries 0, spend USD 0, proposals 0.

### READY / NEXT — only active item

Configure GitHub Actions repository secret:

```text
Repository: litrgratis-pixel/Saddle
Secret name: OPENAI_API_KEY
```

Never place the secret in chat, source, PR comments, workflow YAML, logs or evidence.

After configuration, rerun the approved benchmark under unchanged bounds. Start CASE-001 Sol/Terra, then CASE-002/003 only within the same call/budget guard. Record the nine eval dimensions + tokens/cost/latency/retries.

Then:

```text
BENCHMARK RESULT -> EVALUATION -> HUMAN DECISION
```

No automatic model selection or autonomy/capability expansion.

At least one later selected validated real-model proposal must cross the controlled Executor/effect boundary before live-AI evidence fully closes.

## T7 — Phase 5 strict verified-intent + effect-authority boundaries
Status: `DONE / FROZEN`

Evidence: `VerifiedIntentBinding`, independent raw-intent hash, separate exact `EffectAuthority`, 15/15 tests PASS, fail-closed replay/stale/deny/mismatch/raw-mutation cases. Trust provider intentionally unselected.

## T8 — Phase 6 ScriptOps controlled workflow
Status: `DONE / CONTROLLED WORKFLOW MECHANISM PASS / NO MATURITY CLAIM`

Human decision: `DEC-SAD-010` / ScriptOps `DEC-SO-010`.
Evidence: ScriptOps PR #7 merge `daa6e5dc210e09171a530eeffe5601e0e74ae041`; repository verifier run `31421752036` SUCCESS; Phase-6 smoke `31421752569` SUCCESS; `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md`.

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
