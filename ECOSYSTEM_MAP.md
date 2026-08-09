# SADDLE ECOSYSTEM MAP

Observed: 2026-08-10

## System view

```text
HUMAN
  │
  ▼
SADDLE
  ├─ durable intent / state / authority / evidence protocol
  │
  ├─ COS ───────────── canonical high-level project state
  ├─ Reconstructor ─── recovery from fragmented project history
  ├─ Ginseng semantics decision lineage / impact reasoning (runtime not required now)
  │
  ├─ AI capability ─── model / coding agent / future intelligence
  │
  ├─ Executor ──────── controlled consequential effects
  └─ Verifier/evals ── evidence that claimed results occurred

First real domain candidate:
  ScriptOps

Controlled technical laboratory:
  executor-pilot-target
```

## Repository registry

### 1. COS
URL: https://github.com/litrgratis-pixel/COS
Observed main: `3220310267c3d0ba2184daaf3f2adad259a9cb20`

Reuse:
- canonical project/portfolio memory pattern;
- `START_HERE` single-entrypoint pattern;
- source hierarchy;
- one-next-step/session handoff discipline;
- truthful execution statuses;
- idea parking.

Caution:
- default-branch state predates the latest Executor progress;
- COS PR #18 contains valuable newer ecosystem/Ginseng semantics but stale gate/status assumptions.

Open high-value draft:
- PR #18: https://github.com/litrgratis-pixel/COS/pull/18

### 2. creative-os-project-reconstructor
URL: https://github.com/litrgratis-pixel/creative-os-project-reconstructor
Observed main: `defc7b029097284f94136fec54b75c313ac12f68`

Reuse:
- project reconstruction methodology;
- stable v1.0 prompt;
- evidence/status separation;
- source-of-truth recovery;
- regression-test mindset;
- deterministic repo validator.

Missing for Saddle maturity:
- automated semantic/cross-model eval runner;
- larger real-project validation set.

### 3. scriptops
URL: https://github.com/litrgratis-pixel/scriptops
Observed main: `90a5ba9863961c4b79472db84297cfb403cc5158`

Reuse from preserved v2:
- CLI;
- Git state/commit mechanics;
- context builder;
- token budgeting;
- task artifacts;
- prompts;
- pre/post AI validation;
- hashes/provenance;
- staging;
- approval/decision-log foundation.

Current canonical project blocker says `ACCESS CHECK REQUIRED` for a later RC1/Codex implementation. No such later implementation repository was visible in the accessible GitHub package during the 2026-08-10 audit. Local/off-GitHub artifacts remain unknown.

RC1 gap candidates if no later artifact exists:
- generic task/RC1 shape;
- HANDSHAKE v2;
- complete validation;
- minimal impact report;
- approve/reject/revision + mandatory why;
- canonical commit semantics;
- smoke test.

### 4. Executor
URL: https://github.com/litrgratis-pixel/Executor
Observed main: `788443c3ed5b290ac8f1de145a93d02d2dd15317`

Reuse:
- policy-first execution;
- exact repository/commit/source verification;
- contract validation;
- state/checkpoint mechanics;
- action authorization;
- hardened Docker sandbox;
- evidence/replay architecture;
- GP001 controlled external fixture path;
- request-to-contract phase-1 formation boundary.

Current critical gaps:
- GP001 solution generation is hard-coded rather than produced by real AI;
- verified external human authority + contract freeze are intentionally blocked on main.

Active trust-design stack:
- #51 https://github.com/litrgratis-pixel/Executor/pull/51
- #52 https://github.com/litrgratis-pixel/Executor/pull/52
- #53 https://github.com/litrgratis-pixel/Executor/pull/53
- #54 https://github.com/litrgratis-pixel/Executor/pull/54
- #55 https://github.com/litrgratis-pixel/Executor/pull/55
- #56 https://github.com/litrgratis-pixel/Executor/pull/56
- #57 https://github.com/litrgratis-pixel/Executor/pull/57

PR #57 current design question:
Where does the trusted request-origin event begin?

Key finding:
`USER provenance != VERIFIED REQUEST-ORIGIN EVIDENCE`.

### 5. executor-pilot-target
URL: https://github.com/litrgratis-pixel/executor-pilot-target
Observed main: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`

Role:
controlled deterministic lab, not business-value proof.

Cases:
- CASE-001: atomic batch insertion;
- CASE-002: CLOSED→ACTIVE requires reason;
- CASE-003: deterministic canonical output.

Best immediate use:
first real AI-worker benchmark under Executor controls.

## Component boundary principle

Do not merge these repositories into a monolith merely for conceptual neatness.

Saddle should initially reference/integrate them through narrow contracts and preserve each repository's existing source of truth until a specific consolidation benefit is proven.
