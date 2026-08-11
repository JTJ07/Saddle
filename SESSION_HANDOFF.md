---
project: Saddle
status: PHASE_6_ACCEPTED / PHASE_4_ACTIVE / PHASE_4A_ACCEPTED / PHASE_4C_SYNTHETIC_INTEGRATION_ACCEPTED / PHASE_4B_READY_PAUSED / NOT_YET_FUNCTIONAL
updated_at: 2026-08-11
---

# SESSION HANDOFF

## STATUS

Canonical/frozen foundations: Phases 0–3 and Phase 5. Phase 6 ScriptOps controlled-workflow mechanism is accepted with no maturity claim. Phase 4A and Phase 4C are accepted in their recorded evidence classes.

Current order:

```text
4A WEB AI COGNITIVE CALIBRATION — ACCEPTED
        ↓
4C SYNTHETIC INTELLIGENCE INTEGRATION — ACCEPTED
        ↓
4B GEMINI PROVIDER-SWAP CONTROL PLANE — PASS
        ↓
4B CONTROLLED LIVE API WORKER EVIDENCE — READY / NEXT
        ↓
9-DIMENSION EVALUATION
        ↓
HUMAN DECISION
```

Saddle remains `NOT_YET_FUNCTIONAL`. Completion lock remains ACTIVE.

## ACTIVE GATE

`PHASE 4B — CONTROLLED REPRODUCIBLE LIVE API WORKER EVIDENCE`

The live benchmark is still required. No live Gemini model call has been made by the provider-swap work.

## HUMAN DECISIONS

- `DEC-SAD-010`: ScriptOps v2 selected; no rewrite/new capability; Phase-6 mechanism proof only.
- `DEC-SAD-011`: API benchmark max USD 5 / 6 calls / 0 automatic retries / benchmark only / proposal only / no capability, autonomy, authority or tool-access expansion.
- `DEC-SAD-012`: web AI = Phase 4A calibration; API = Phase 4B worker evidence.
- `DEC-SAD-013`: Phase 4A accepted; nine-dimensional Phase-4B evaluation including intent preservation.
- `DEC-SAD-014`: Phase 4C synthetic system integration precedes API-worker measurement.
- `DEC-SAD-015`: use Gemini for Phase 4B instead of the previously planned OpenAI provider and use the provider substitution as a resilience test. Detailed record: `decisions/DEC-SAD-015.md`.

`DEC-SAD-015` supersedes only the old Phase-4B provider/model/secret choice. It does not change the budget, calls, retry policy, immutable cases, proposal-only rule, authority boundary or post-benchmark human decision.

## WHAT CHANGED — GEMINI PROVIDER SWAP

Active Phase-4B configuration:

```text
provider: google-gemini
API: generateContent
quality-first: gemini-3.1-pro-preview
balanced: gemini-3.6-flash
secret: GEMINI_API_KEY
```

The provider-specific adapter now absorbs Gemini request/response/schema/usage differences before the stable Saddle WorkerProposal contract.

Important compatibility finding: Gemini structured output accepts a provider-specific JSON-Schema subset rather than the exact canonical schema vocabulary. The adapter normalizes only the request-time provider schema. The canonical post-response `validate_worker_proposal` remains unchanged and continues to enforce exact fields, CASE, path, non-empty content, actual mutation and patch-line budget, including rejection of authority-smuggling fields.

No generalized provider framework, dynamic routing, fallback provider, tools, shell access or new authority was added.

## PROVIDER-SWAP CONTROL-PLANE EVIDENCE

Evidence file:

`evidence/PHASE4B_GEMINI_PROVIDER_SWAP_CONTROL_PLANE_2026-08-11.md`

PR #18 deterministic strengthened run:

```text
workflow run: 31530605887
job: 93909442838
conclusion: SUCCESS
unit tests: 65 / 65 PASS
live model calls: 0
provider credential used: NO
spend: USD 0
```

The workflow also verified:

```text
Phase 4B live trigger = workflow_dispatch only
GEMINI_API_KEY source = GitHub Actions repository secret reference
stale OPENAI_API_KEY in active live workflow = absent
```

Provider reaction behavior at the control-plane level:

```text
missing GEMINI_API_KEY       -> BLOCK before network
invalid reasoning config     -> BLOCK locally
provider prompt block        -> BLOCK / no evaluator effect
HTTP 400                     -> STOP / request rejected
HTTP 401 or 403              -> STOP / credential-access denied
HTTP 404                     -> STOP / model unavailable
HTTP 429                     -> STOP / rate limited / zero retry
HTTP 503                     -> STOP / provider unavailable / zero retry
malformed provider output    -> BLOCK
unknown price                -> BLOCK before paid call
missing usage/cost evidence  -> STOP
wrong path / extra authority -> canonical validator BLOCK
valid bounded proposal       -> unchanged validator + ephemeral evaluator
```

Evidence classification:

```text
PROVIDER-SWAP CONTROL-PLANE EVIDENCE: PASS
API WORKER PERFORMANCE EVIDENCE: OPEN
MODEL QUALITY EVIDENCE: OPEN
FUNCTIONAL ACCEPTANCE: OPEN
MATURITY CLAIM: NONE
```

## PRESERVED HISTORICAL EVIDENCE

Phase 4C remains accepted exactly in its historical evidence class:

```text
PR: #16
workflow run: 31429931199
job: 93590584463
Saddle regression: 59 tests / OK
Executor historical locator: litrgratis-pixel/Executor@788443c3ed5b290ac8f1de145a93d02d2dd15317
fixture historical locator: litrgratis-pixel/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0
artifact: 9078675806
artifact ZIP sha256: cac22ce36e2bfff030f1e3fb1aea3a5323dd55abf75a02d70962cda6165a75e1
```

Current repo locators are `JTJ07/...`; old locators above remain historical provenance.

## MIGRATION / DOWNSTREAM EXECUTOR NOTE

GitHub migration is `DONE / VERIFIED`.

Immutable benchmark identities remain unchanged:

```text
CASE-001 3934a94a5eebf750079200589d6dc40e024d44a0
CASE-002 c3683bf37ad6a3f1d49c0ca05ebdd41627e9a5be
CASE-003 c42bead2bbbff9c84486f17637ec80f35eeffa25
Executor  788443c3ed5b290ac8f1de145a93d02d2dd15317
```

PR #17 migration validation showed that historical Executor commit `788443c3...` internally expects repository identity `litrgratis-pixel/Executor`. That is a downstream bounded reconciliation required before a new post-transfer real Executor effect. It does not block Phase 4B and does not invalidate Phase 4C.

## LIVE PHASE-4B CONTRACT

```text
budget <= USD 5
calls <= 6
automatic retries = 0
benchmark only
proposal only
model tools = NONE
model shell = NONE
target repo write = NONE
effect authority = NONE
autonomous execution = NO
provider fallback = NO
automatic model selection = NO
```

Immutable cases remain CASE-001/002/003. The live workflow remains manual `workflow_dispatch` only.

Nine evaluation dimensions remain:
1. correctness against pinned tests;
2. scope compliance;
3. no authority invention/smuggling;
4. no goal expansion;
5. rationale quality;
6. structured-output stability;
7. objective evidence-plan quality;
8. human-correction burden;
9. intent preservation against preserved human-approved intent and explicit constraints.

After the run:

```text
BENCHMARK RESULT
→ 9-DIMENSION EVALUATION
→ HUMAN DECISION
```

No automatic autonomy/capability increase follows.

## BLOCKERS / OPEN EVIDENCE

Current external prerequisite only:

`GEMINI_API_KEY` is not yet established as available to the canonical live runner.

Still not claimed:
- no reproducible live Gemini proposal yet;
- no live Gemini cost/latency/token evidence yet;
- no first production worker selected;
- no production request-origin/trust provider selected;
- no final fresh-session full E2E acceptance;
- no functional Saddle claim.

## EXACT FILES / REFS TO OPEN NEXT

1. `PROJECT_STATE.md`
2. `TODO.md` — T6B
3. `DECISION_LOG.md`
4. `decisions/DEC-SAD-015.md`
5. `evidence/PHASE4B_GEMINI_PROVIDER_SWAP_CONTROL_PLANE_2026-08-11.md`
6. `config/model-benchmark-v0.1.json`
7. `config/worker-cases-v0.1.json`
8. `tools/model_gateway.py`
9. `tools/phase4_benchmark.py`
10. `tools/phase4_live_benchmark.py`
11. `.github/workflows/phase4-live-ai-benchmark.yml`
12. `JTJ07/executor-pilot-target@3934a94a5eebf750079200589d6dc40e024d44a0`

## ONE NEXT STEP

Configure `GEMINI_API_KEY` as a GitHub Actions repository secret in `JTJ07/Saddle`.
