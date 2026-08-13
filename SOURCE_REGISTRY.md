# SADDLE SOURCE REGISTRY

Reconciled: 2026-08-13

## Authority order inside Saddle

1. latest explicit human decision in `DECISION_LOG.md`;
2. `PROJECT_STATE.md`;
3. accepted Saddle protocols/contracts;
4. merged implementation + tests/evidence;
5. `SESSION_HANDOFF.md`;
6. `TODO.md` as operational projection only;
7. draft design / analysis / open PR material;
8. history and AI inference.

The default branch of `JTJ07/Saddle` owns Saddle-specific product state and the cross-component responsibility/completion map.

## Repository migration mapping

Current canonical repository locators were verified on 2026-08-11 after transfer from `litrgratis-pixel` to `JTJ07`.

```text
litrgratis-pixel/Saddle                         -> JTJ07/Saddle
litrgratis-pixel/COS                            -> JTJ07/COS
litrgratis-pixel/creative-os-project-reconstructor -> JTJ07/creative-os-project-reconstructor
litrgratis-pixel/scriptops                      -> JTJ07/scriptops
litrgratis-pixel/Executor                       -> JTJ07/Executor
litrgratis-pixel/executor-pilot-target          -> JTJ07/executor-pilot-target
```

Migration changes the current locator, not immutable content identity. Existing commit SHAs, artifact digests and benchmark case SHAs remain provenance anchors. Historical evidence documents retain the locator that was true when the original run occurred; do not rewrite history to match the current owner.

## Saddle current references

- `DECISION_LOG.md` — human decisions including responsibility boundary, operational delegation, ScriptOps base selection, benchmark approval and Phase-4A/4B evidence split.
- `PROJECT_STATE.md` — current evidence gate/state.
- `EXECUTION_PLAN.md` — strategic gated completion path.
- `TODO.md` — current operational queue; never overrides higher-authority state.
- `docs/SADDLE_EXECUTOR_RESPONSIBILITY_BOUNDARY.md` — current intent/reasoning/effect/fact ownership split.
- `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md` — Phase-1 classification.
- `docs/PHASE4A_WEB_AI_CALIBRATION.md` — evidence-class boundary for human-guided web calibration versus reproducible API worker proof.
- `analysis/SADDLE_TEST_SESSION_2026-08-10.md` — six-part test interpretation.
- `evidence/COLD_START_AUDIT_001.md` — Phase-0 continuity evidence.
- `evidence/PHASE4A_WEB_AI_CALIBRATION_BASELINE_2026-08-10.md` — first 3-run web-AI calibration baseline; context-contaminated, not worker evidence.
- `evidence/PHASE4_LIVE_BENCHMARK_PREFLIGHT_2026-08-10.md` — API runner preflight; 54 tests OK, secret absent, 0 calls, USD 0.
- `evidence/PHASE6_SCRIPTOPS_CONTROLLED_WORKFLOW_2026-08-10.md` — cross-repo Phase-6 mechanism proof.
- `evidence/PHASE7_E2E_REVIEW_PACKET_2026-08-12.md` — Phase-7 technical E2E complete through the human-review boundary; `HUMAN_REVIEW_ACCEPTED` remains open.
- `evidence/phase7/attempt-001.json` + `evidence/phase7/attempt-001-model.patch` — immutable consumed-call metadata and exact Phase-7 worker patch provenance.

## Component sources

### COS
- Repo: https://github.com/JTJ07/COS
- Main observed 2026-08-10: `3220310267c3d0ba2184daaf3f2adad259a9cb20`
- Key merged sources: `START_HERE.md`, `CREATIVE_OS.md`
- Draft PR #18: https://github.com/JTJ07/COS/pull/18
- Classification: reusable Ginseng/decision-lineage semantics; stale/superseded global status/placement.
- Reuse from #18 only with classification in `docs/PHASE1_ECOSYSTEM_RECONCILIATION_2026-08-10.md`.

### Project Reconstructor
- Repo: https://github.com/JTJ07/creative-os-project-reconstructor
- Main observed: `defc7b029097284f94136fec54b75c313ac12f68`
- Key: `README.md`, `PROJECT_STATE.md`, `PROMPT_STARTOWY.md`, tests, deterministic validator.
- Role: context recovery / fragmented-history reconstruction.

### ScriptOps
- Repo: https://github.com/JTJ07/scriptops
- Current main after Phase-6 controlled-workflow merge: `daa6e5dc210e09171a530eeffe5601e0e74ae041`
- Key: `PROJECT_STATE.md`, `HANDOFF.md`, `DECISION_LOG.md`, `sources/RC1_SCOPE_LOCK.md`, `legacy/scriptops-v2-single.py`, `analysis/RC1_V2_GAP_2026-08-10.md`, `phase6/scriptops-v2-hardening.py`, `tests/test_phase6_scriptops_smoke.py`, `evidence/PHASE6_CONTROLLED_WORKFLOW_PROOF_2026-08-10.md`.
- Human decision: v2 selected as Phase-6 base; `REWRITE: NO`; `NEW CAPABILITY: NO`; `MATURITY CLAIM: NONE`.
- Canonical result: B1–B5 bounded workflow hardening passed; historical v2 remains unchanged.
- Final verified PR #7 head `acbfca79f96407dbd46f9806bf821caf6e02e1af`: repository verifier run `31421752036` SUCCESS; Phase-6 smoke run `31421752569` SUCCESS.
- Classification: controlled workflow mechanism proof only. Do not infer ScriptOps v5/RC1 maturity, independent product value or functional Saddle.

### Executor
- Repo: https://github.com/JTJ07/Executor
- Current main observed after self-identity reconciliation: `728d23e56ec9f76fb7a37673ceb20efccf91e03d`
- Historical Phase-4C provenance: `litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317`
- Key current implementation: `executor/request_to_contract.py`, GP001 runtime, authorization/policy/sandbox/evidence code, task/project/policy contracts.
- Canonical implementation source: `main`.
- PR #51–#57: draft/research stack; use only according to Phase-1 classification.
- Critical retained invariant: `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`.
- Global `USER -> EXECUTOR` front-door placement from historical #57 is superseded by DEC-SAD-006; trust findings remain reusable.
- Older PR #36/#38 are explicit never-merge helpers; #29/#34/#19–#22 are history/evidence unless a current blocker requires inspection.

### Executor Pilot Target
- Repo: https://github.com/JTJ07/executor-pilot-target
- Main observed: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`
- Key: `PILOT_CONTRACT.md`, CASE-001–003 branches/tests.
- Phase-4 immutable calibration/benchmark inputs:
  - CASE-001 commit `3934a94a5eebf750079200589d6dc40e024d44a0`;
  - CASE-002 commit `c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be`;
  - CASE-003 commit `c42bead2bbbff9c84486f17637ec80f35eeffa25`.
- Direct CASE-001 solve evidence: commit `313ebc9789a4518d91b8dea440b1aeba5629cb89`, PR #5.
- Warning: PR #5 base is `case-001-broken`; do not merge the repair into that broken benchmark baseline.

## Original AI engineering operating package

Preserved:
- `references/AI_ENGINEERING_OS_AGENTS_ORIGINAL.md`
- `references/README_AI_OS_ORIGINAL.md`

The Saddle root `AGENTS.md` specializes those principles with completion lock, durable-memory law and Saddle-specific authority boundaries.

## OpenAI references

Re-check official OpenAI documentation immediately before any current model/provider/Codex capability or pricing decision; do not rely on old capability assumptions.
