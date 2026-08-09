# SADDLE DECISION LOG

Only explicit human decisions or decisions already clearly established by the project are recorded as `DECISION`.

## DEC-SAD-001 — GitHub is durable project memory

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE
- Decision: Every session may be lost permanently; all knowledge required to resume Saddle must be durably preserved in GitHub.
- Consequence: chat memory is never a canonical dependency.

## DEC-SAD-002 — Completion lock

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE
- Decision: Do not develop new ideas/features before Saddle is functional. Preserve every new idea in future-development files and return to completion work.
- Consequence: `FUTURE_IDEAS.md` is append-only parking until functional acceptance or explicit human override.

## DEC-SAD-003 — Saddle product direction

- Date: 2026-08-10
- Owner: USER
- Status: ACTIVE
- Decision: Saddle should be capable of coupling to increasingly powerful AI without needing to know or dictate how that intelligence thinks; it should integrate, preserve direction, and avoid falling off rather than slow the underlying capability.
- Consequence: prompts, model choices, agent structures, workflows, and OS conventions are replaceable implementation mechanisms, not the permanent product abstraction.

## DEC-SAD-004 — Intelligence freedom / effect control

- Date: 2026-08-10
- Owner: USER direction + architecture interpretation pending empirical validation
- Status: ACTIVE PRINCIPLE
- Decision: Avoid unnecessary restrictions on AI problem-solving; focus restrictions on goal integrity and consequential effects.
- Consequence: architecture must separate reasoning/proposal from effect authority.

## DEC-SAD-005 — Reuse before rewrite

- Date: 2026-08-10
- Owner: USER goal interpreted through completed ecosystem audit
- Status: ACTIVE WORKING DECISION
- Decision: The existing `litrgratis-pixel` package is the starting asset base. Determine what can be reused and completed before replacing it.
- Consequence: COS, Reconstructor, ScriptOps, Executor and pilot-target are treated as candidate Saddle components/evidence, not discarded by default.

## Not yet a decision

The following remain open until explicitly selected or proven:

- A1 vs strengthened A2 trust-front-door architecture;
- concrete human-authority provider;
- first production model/provider;
- whether ScriptOps RC1 is the final first real-domain acceptance case;
- whether/when Ginseng runtime is activated;
- multi-agent architecture.
