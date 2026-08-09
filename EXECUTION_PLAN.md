# SADDLE EXECUTION PLAN — COMPLETION PATH

Status: `ACTIVE`

Rule: phases are gates. Do not implement a later phase to avoid finishing an earlier one.

## PHASE 0 — DURABLE MEMORY BOOTSTRAP

### Goal
Create the canonical `litrgratis-pixel/Saddle` repository and prove a fresh session can recover the project without this conversation.

### Work
- import this bootstrap package;
- verify default-branch files;
- preserve source registry and observed checkpoints;
- run an independent cold-start audit using only repository content;
- correct only continuity failures found by the cold start.

### DoD
- repository exists;
- root instructions/state/plan/handoff are readable;
- fresh agent identifies product definition, active completion lock, current blocker, and one next step correctly;
- no chat transcript is required.

### Forbidden
- AI worker implementation;
- authority provider selection;
- new framework installation;
- new product features.

---

## PHASE 1 — ECOSYSTEM RECONCILIATION

### Goal
Make Saddle the current index of what is canonical, draft, experimental, superseded, temporary, and reusable across the existing repositories.

### Work
- classify relevant open Executor PRs, especially #51–#57 and older experimental stacks;
- classify COS PR #18 material by semantic value vs stale status;
- close the GitHub-side ScriptOps access check: document that no later RC1 repo/build is visible in the accessible package; preserve explicit uncertainty about local/off-GitHub artifacts;
- map current component responsibilities;
- update `ECOSYSTEM_MAP.md`, `SOURCE_REGISTRY.md`, `PROJECT_STATE.md`.

### DoD
A fresh agent can answer, without guessing:

- what is canonical now;
- what is only a draft;
- which components Saddle reuses;
- which historical experiments are evidence only;
- what is blocked.

### Forbidden
Do not merge/rewrite source repositories merely to make the map look cleaner.

---

## PHASE 2 — FREEZE SADDLE PROTOCOL v0.1

### Goal
Define the smallest provider/model/agent-independent coupling contract.

### Required objects

1. `IntentEnvelope`
2. `EffectProposal`
3. `EffectReceipt`
4. `StateDelta`

### Work
- convert `docs/SADDLE_PROTOCOL_v0.1_DRAFT.md` into reviewed JSON Schemas;
- define canonical hashing/identity rules;
- define provenance fields;
- define authority references without choosing a provider;
- add deterministic schema tests.

### DoD
Four schemas can represent the first planned end-to-end path without requiring knowledge of OpenAI/Anthropic/Google, agent frameworks, ScriptOps internals, or a particular authority provider.

### Forbidden
- provider SDK framework;
- agent orchestration;
- UI;
- database unless schema tests prove plain files insufficient.

---

## PHASE 3 — AUDIT + EVAL FOUNDATION

### Goal
Make progress measurable and prevent documentation/state drift.

### Work
Build the smallest plain-Python tools needed for:

- ecosystem audit snapshot;
- eval case execution/aggregation;
- JSON/JSONL result recording;
- model/prompt/version + tokens/cost/latency + result + scope violations;
- deterministic validation of state/handoff invariants.

### Initial eval lanes

- Reconstructor regression cases;
- COS cold-start/resumption cases;
- Executor security/policy tests;
- executor-pilot-target CASE-001–003;
- later ScriptOps smoke path.

### DoD
One command produces a reviewable result set and cannot silently convert failures into PASS.

### Forbidden
No Langfuse/LangGraph/full observability platform unless plain records demonstrably block progress.

---

## PHASE 4 — FIRST REAL AI WORKER

### Goal
Replace the hard-coded GP001 repair proposal with a real model-generated proposal while keeping Executor as the effect gate.

### Architecture

```text
pinned task + source + tests
        ↓
ModelGateway (control plane)
        ↓
AI proposal only
        ↓
validation / bounded mutation conversion
        ↓
Executor effect path
        ↓
tests + evidence
```

### Work
- implement the thinnest model adapter needed for the benchmark;
- keep provider credential outside worker sandbox and evidence artifacts;
- benchmark at least two current capable models on the same cases before selecting the first production worker model;
- deploy one winner for the first slice, not a dynamic routing platform.

### DoD
CASE-001–003 are solved by real AI-generated proposals from clean starts with:

- zero manual solution edits;
- no protected-file changes;
- no policy violations;
- full tests passing;
- recorded cost/latency/retries/human review.

### Forbidden
- model gets unrestricted write/shell authority;
- general worker internet;
- multi-agent worker;
- generalized provider framework.

---

## PHASE 5 — VERIFIED INTENT / HUMAN AUTHORITY BRIDGE

### Goal
Close the gap between a verbatim user request and independently trustworthy authority for the exact intended transaction.

### Inputs
Reuse and reconcile Executor PR #51–#57 design work.

### Required semantic separation

```text
human request content
!= AI interpretation
!= verified request origin
!= approval of exact contract
!= downstream effect permission
```

### Work
- decide the Saddle-level front-door/verified-intent boundary;
- preserve raw human intent;
- define/implement a first `VerifiedIntentEnvelope` compatible with `IntentEnvelope` without coupling Saddle to one vendor;
- implement only the first authority adapter necessary for the real pilot;
- prove replay/staleness/scope attacks fail closed.

### DoD
The first real effect cannot become executable from self-declared model/user metadata alone.

### Forbidden
- enterprise IAM platform;
- cross-provider identity federation;
- generalized delegation graph;
- quorum/organization roles unless required by the first pilot.

---

## PHASE 6 — SCRIPTOPS RC1 RECOVERY / FIRST REAL DOMAIN

### Goal
Use an existing real workflow instead of inventing a demo domain.

### Work
First resolve whether any later local/off-GitHub RC1/Codex artifact exists.

If none exists, evolve the preserved v2 prototype with the smallest RC1 deltas:

- generic task contract;
- HANDSHAKE/context export required by RC1;
- complete validation;
- minimal impact report;
- human `approve / reject / revision` with mandatory `why`;
- clear canonical-commit semantics;
- full RC1 smoke test.

Reuse existing v2 CLI/Git/context/hash/staging machinery. Do not rewrite from zero.

### DoD
One real narrative/canon change crosses the complete loop with human decision and evidence.

### Forbidden
Follow the existing RC1 scope lock: no browser helper, direct model automation, autonomous writing approval, GUI, vector DB, AI Guard, semantic graph platform, cloud sync, etc. unless Saddle functional acceptance has already been achieved and a new phase is authorized.

---

## PHASE 7 — FUNCTIONAL SADDLE ACCEPTANCE

### Goal
Prove the product, not the components.

### Test
Run from a fresh session with no prior chat memory.

```text
human intent
→ Saddle durable intent
→ context recovery
→ AI problem solving
→ effect proposal
→ authority/effect gate
→ real bounded execution
→ evidence
→ human review
→ durable state delta
→ second fresh-session resume
```

### Required evidence
- input/request identity;
- source/context references;
- model and proposal record;
- effect authorization binding;
- exact changed artifacts;
- tests/verifier result;
- cost/latency;
- human decision where required;
- updated project state/handoff;
- independent cold-start resume result.

### DoD
Only here may `PROJECT_STATE.md` be changed to:

`FUNCTIONAL_SADDLE_ACCEPTED`

---

## PHASE 8 — RELEASE COMPLETION LOCK

This phase does not automatically start.

The human reviews the evidence and explicitly decides whether to:

- continue hardening the current product;
- activate one parked idea;
- broaden domains;
- increase autonomy;
- add more models/agents/tools.

Until that decision, `FUTURE_IDEAS.md` remains parking only.
