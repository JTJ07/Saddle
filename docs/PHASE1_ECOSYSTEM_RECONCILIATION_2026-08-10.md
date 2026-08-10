# PHASE 1 ECOSYSTEM RECONCILIATION — 2026-08-10

Status: `PHASE 1 WORKING RESULT / READY FOR CANONICAL SYNC`
Purpose: classify the current reusable, draft, superseded, experimental and temporary material needed by Saddle before Phase 2.

This document does not merge or rewrite component repositories merely to make the ecosystem look clean. It records what Saddle may safely rely on.

## 1. Observed canonical component checkpoints

Observed on 2026-08-10:

- Saddle `main`: Phase 0 closure merged at `b950660c84c6dcad1a093a7aba5ad2d70d472ee4`.
- Executor `main`: `788443c3ed5b290ac8f1de145a93d02d2dd15317` — merged PR #50 / `REQUEST_TO_CONTRACT_001` formation boundary.
- COS `main`: `3220310267c3d0ba2184daaf3f2adad259a9cb20`.
- ScriptOps `main`: `90a5ba9863961c4b79472db84297cfb403cc5158`.

Existing recorded checkpoints for Reconstructor and executor-pilot-target remain observation refs and must be rechecked when their implementation becomes active.

## 2. Current global responsibility model

Human decisions in Saddle now establish:

```text
HUMAN OWNS INTENT
SADDLE PRESERVES AND BINDS INTENT
INTELLIGENCE PROPOSES HOW
EXECUTOR GOVERNS CONSEQUENCES
VERIFIER ESTABLISHES FACTS
NO LAYER MAY SUBSTITUTE FOR A HIGHER-ORDER OWNER
```

Therefore the historical global assumption:

```text
USER -> EXECUTOR
```

is superseded as the Saddle product front door by:

```text
USER -> SADDLE -> INTELLIGENCE -> EXECUTOR
```

This does not discard Executor trust research. It remaps request-origin/meaning concerns to the Saddle intent boundary and concrete effect authority to Executor.

---

# 3. Executor classification

## Canonical now: Executor/main

`Executor/main` at `788443c...` is the canonical implementation source.

Confirmed role:

- `REQUEST_TO_CONTRACT_001` phase-1 formation exists;
- raw/verbatim user request and AI interpretation are separated;
- the flow intentionally stops before verified human authority/freeze;
- `AUTHORIZED_AND_FROZEN` is not implemented by current main;
- Executor remains the most mature bounded effect/sandbox/evidence component;
- the GP001 repair proposal remains hard-coded and is not proof of a real AI worker.

## PR #51 — Verified Human Authority Model

Classification:

`ACTIVE DRAFT DESIGN + REUSABLE SEMANTICS / NOT CANONICAL IMPLEMENTATION`

Retain:

- `HUMAN ACTION != VERIFIED HUMAN AUTHORITY`;
- `AUTHENTICATION != AUTHORIZATION`;
- `AI INTERPRETATION != USER INTENT`;
- exact-contract binding;
- `INTENT AUTHORITY != RESOURCE / ACTION AUTHORITY`;
- bounded authority rather than general delegation;
- formation approval does not automatically authorize downstream write/merge/deploy/network/secret effects.

Do not treat the draft as merged runtime.

## PR #52 — Minimal Human Decision Receipt

Classification:

`ACTIVE DRAFT DESIGN + REUSABLE EVIDENCE/TRUST SEMANTICS`

Retain:

- `HUMAN DECISION RECEIPT != VERIFIED AUTHORITY EVIDENCE`;
- `EVIDENCE REF != TRUST SELECTOR`;
- trust source/profile cannot be caller-selected;
- exact reviewed decision/contract bindings;
- authority dimensions must not collapse into one approval.

## PR #53 — Verified Human Authority Implementation Contract

Classification:

`DRAFT NON-EXECUTABLE CONTRACT + REUSABLE REQUIREMENTS`

Retain:

- verified formation state is distinct from structures supplied by callers;
- identity equality requires trusted identity equivalence, not subject-string equality;
- request origin and decision actor need independently verifiable binding;
- freeze/effect authorization remains a separate later boundary.

No implementation was started in this PR.

## PR #54 — Technology-Agnostic External Trust Boundary

Classification:

`ACTIVE DRAFT DESIGN + REUSABLE TRUST-BOUNDARY SEMANTICS`

Retain:

- `EXECUTOR VERIFIES AUTHORITY != EXECUTOR OWNS IDENTITY AUTHORITY`;
- exact external event identity/content binding;
- direct-principal action provenance;
- mutable/rebound external evidence must fail closed.

Saddle reinterpretation: request-origin portions primarily inform the Saddle intent boundary; Executor remains a consumer/verifier of effect authority rather than the semantic owner of identity/intent.

## PR #55 — Trust Technology Comparison

Classification:

`RESEARCH / EVIDENCE + REUSABLE SELECTION PRINCIPLE`

Retain:

- `THE TRUST CONTRACT MUST SELECT THE TECHNOLOGY; THE TECHNOLOGY MUST NOT REDEFINE THE TRUST CONTRACT`;
- F-22 retroactive request-origin attribution;
- F-23 review/signing-surface substitution;
- generic authentication/approval primitives are not automatically complete intent-authority domains.

Do not select a provider from this comparison alone.

## PR #56 — Pattern A Technology Evaluation

Classification:

`RESEARCH / EVIDENCE / PROVIDER UNSELECTED`

Retain:

- `APPROVAL PLATFORM != COMPLETE REQUEST-INTENT AUTHORITY DOMAIN`;
- the distinction between an approval event and proof of exact original request origination.

Historical A1/A2 placement remains design input, not current product canon.

## PR #57 — A1 vs A2 Architecture Attack

Classification:

`REUSABLE ADVERSARIAL TRUST SEMANTICS + PARTIALLY SUPERSEDED PRODUCT PLACEMENT`

Retain:

- `USER PROVENANCE != VERIFIED REQUEST-ORIGIN EVIDENCE`;
- naive A2 is rejected;
- strengthened A2 requires direct transaction-specific external attestation bound to the exact immutable request before governed formation relies on it;
- later authentication cannot retroactively prove earlier request origination;
- front-door ownership must be explicit.

Superseded at the global Saddle level:

- treating `USER -> EXECUTOR` as the default product front door;
- treating A1 vs A2 primarily as a decision about where to place Executor.

Current Saddle reinterpretation:

- strengthened-A2 trust principle is retained at the Saddle intent boundary;
- A1 is a valid explicitly delegated/enterprise intake variant upstream of Saddle;
- provider remains unselected.

## Older Executor draft/experimental debt

### PR #36 and #38

Classification: `TEMPORARY / NEVER-MERGE EVIDENCE HELPERS`.

Their PR bodies explicitly say never merge. Preserve only as historical CI/test evidence.

### PR #29

Classification: `HISTORICAL REWORK / EXPERIMENTAL IMPLEMENTATION EVIDENCE`.

It is not the current canonical runtime and must not be revived automatically. Its controlled-fetch/scope/evidence lessons may be consulted if a current Executor blocker needs them.

### PR #34

Classification: `GOVERNANCE DRAFT / REUSABLE HISTORICAL PRODUCT-BOUNDARY INPUT`.

Useful as evidence of earlier attempts to bound Executor to controlled execution and human review. Do not promote its older product hierarchy over DEC-SAD-006.

### PR #19–#22 and similar earlier M3 experiments

Classification: `EXPERIMENTAL / EVIDENCE ONLY / NOT CURRENT COMPLETION PATH`.

They contain useful replay/evidence/atomic-consumption ideas but are not current canonical state. Reactivate only for a named blocker after checking current main.

---

# 4. COS PR #18 classification

PR #18 is open/draft/unmerged and based on COS main `322031...`.

Overall classification:

`REUSABLE GINSENG SEMANTICS + STALE/SUPERSEDED GLOBAL STATUS/PLACEMENT`

## Reuse now as semantics

- `GINSENG = DECISION INTELLIGENCE LAYER`;
- `FACT / DECISION / HYPOTHESIS` remain distinct;
- important decisions require Decision Lineage;
- AI cannot promote its own hypothesis/relation into confirmed truth;
- relation source/proposer/confidence/status remain visible;
- impact may be explained through `ELEMENT -> FUNCTION / CAPABILITY -> EFFECT`;
- Ginseng is not the executor, canonical truth owner, graph product or dashboard;
- graph/storage/UI technology is implementation detail, not semantic identity.

These semantics are directly compatible with Saddle `StateDelta`, decision logging and later impact reasoning.

## Do not import as current global truth

The following are historical/stale relative to Saddle:

- `ACTIVE_PRIORITY: EXECUTOR P1 / PR #32`;
- the old development gate ordering tied specifically to Executor P1/P3;
- the global architecture `User -> Ginseng -> Creative OS -> ... -> Executor` as the current Saddle product map;
- `Creative OS owns canon` if interpreted as global ownership of Saddle truth. COS may own its local/cross-project memory role, while Saddle's own canonical state remains in the Saddle repository.

## Runtime decision

Do not activate a Ginseng runtime, graph UI, graph database or broad impact platform during the completion lock.

Ginseng semantics are reusable now; Ginseng runtime remains parked.

---

# 5. ScriptOps classification

Canonical `scriptops/main` remains `90a5ba...`.

PR #6 is open/draft/unmerged at the time of this analysis and contains no runtime code change.

Classification:

`KNOWLEDGE RECONCILIATION CANDIDATE / SAFE TO CANONICALIZE AS STATE ANALYSIS`

Retain:

- accessible-GitHub access check found no separate later RC1 implementation/build;
- local/off-GitHub artifacts remain explicitly unknown;
- existing `legacy/scriptops-v2-single.py` already provides much of the needed CLI/Git/context/validation/hash/staging/decision machinery;
- one-slice blockers are concrete rather than reasons for rewrite:
  1. task/evidence artifacts conflict with clean-tree checks;
  2. dirty-tree state can block approval;
  3. accepted hash becomes stale after candidate -> accepted transition;
  4. approval lacks mandatory `why`;
  5. impact report and final smoke proof are absent.

Technical recommendation:

Use v2 as the base for the smallest one-case RC1 repair slice.

Decision status:

`RECOMMENDATION, NOT YET A HUMAN BASE-SELECTION DECISION`.

The analysis/state PR may be merged without silently selecting v2 as runtime base.

---

# 6. executor-pilot-target classification

Role:

`IMMUTABLE/REPEATABLE AI-WORKER + EXECUTOR LAB`

CASE-001 direct Codex solve at commit `313ebc...` is valuable evidence:

`AI_WORKER_CAPABILITY BASELINE = DEMONSTRATED`

but:

`FULL SADDLE EXECUTION = NOT PROVEN`.

Critical rule:

Do not merge the successful repair PR into `case-001-broken`. Broken benchmark inputs must remain reproducible.

---

# 7. Phase-1 canonical conclusions

A zero-history agent should now be able to rely on the following classification:

- Saddle owns the human-intent coupling/state boundary.
- Arbitrary intelligence owns solution search, not authority.
- Executor is canonical for bounded consequential execution/evidence and consumes effect authority; it does not own human intent.
- Executor #51–#57 are reusable trust research/drafts, not current runtime; #57 placement is partially superseded by Saddle while its attack findings survive.
- COS #18 provides reusable decision-intelligence semantics but stale global status/architecture; do not merge it merely to make Saddle consistent.
- ScriptOps v2 is the strongest first real-domain base candidate, but base selection is still a human semantic decision.
- executor-pilot-target remains a repeatable benchmark lab and its broken branches must stay broken.
- no trust provider, production model/provider, Ginseng runtime or multi-agent architecture is selected.

## Phase-1 remaining gate

After this classification is synchronized into `ECOSYSTEM_MAP.md`, `SOURCE_REGISTRY.md`, `PROJECT_STATE.md`, `SESSION_HANDOFF.md` and `TODO.md`, Phase 1 may be closed.

The next phase must be Phase 2 / T4: freeze the minimal provider-independent Saddle protocol. Do not jump directly to model/provider or authority technology selection.
