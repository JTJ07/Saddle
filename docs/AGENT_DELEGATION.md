# DELEGATING SADDLE WORK TO OPENAI CODEX

Status: `RECOMMENDED OPERATING SHAPE / HUMAN ACTIVATION REQUIRED`

## Short answer

Yes. The coding/engineering execution of Saddle can be delegated to OpenAI Codex, provided the repository is the durable authority and Codex is treated as an execution agent rather than the owner of product direction.

Current OpenAI product documentation describes Codex as a coding agent that can work end-to-end on software tasks, operate in cloud worktrees/environments, work in parallel, run tests, and be guided by repository `AGENTS.md` instructions. OpenAI also documents Skills/plugins and background/scheduled Codex work.

## Correct division of responsibility

### Human owns
- Saddle's product goal;
- changing the completion definition;
- disabling the completion lock;
- high-risk permissions;
- semantic/canonical decisions when not already explicitly delegated;
- final product acceptance.

### Codex may own operationally
- reading current state;
- selecting the first incomplete gate from the approved plan;
- inspecting code;
- implementing the smallest required delta;
- running tests/evals;
- debugging within the gate;
- updating documentation/handoff;
- preparing commits/branches/draft PRs;
- reporting blockers with evidence;
- parking newly discovered ideas instead of implementing them.

## Repository contract Codex should receive

At the start of every task, Codex must obey root `AGENTS.md` and read:

1. `PROJECT_STATE.md`
2. `EXECUTION_PLAN.md`
3. `RESTRICTIONS.md`
4. `SESSION_HANDOFF.md`

The agent should not need the original ChatGPT conversation.

## Recommended operating cycle

```text
BOOT FROM REPO
→ identify ACTIVE GATE
→ inspect exact source
→ define proof
→ implement minimum delta
→ run checks/evals
→ update durable state
→ park new ideas
→ prepare reviewable PR/evidence
→ stop on human-decision boundary
```

## Recommended permissions during completion phase

Start conservative:

- read all Saddle/component repos required for the gate;
- write only to the task branch/repo explicitly in scope;
- run local/container tests;
- no production deploy;
- no auto-merge unless a specific class is later explicitly delegated;
- no secret expansion;
- no arbitrary internet in worker sandboxes;
- provider credentials remain control-plane concerns.

## Why Codex rather than the read-only GitHub ChatGPT app

OpenAI's GitHub app documentation states that the ordinary ChatGPT GitHub connection is used to read/analyze repositories; direct code generation/edit/push workflows are provided via Codex.

## Can Codex “lead the work”?

Operationally: yes, within a durable plan and explicit authority envelope.

Architecturally: it should **not** become the hidden source of truth or silently invent the roadmap.

The desired mode is:

```text
Human defines product direction + gates once
Repository preserves them
Codex repeatedly advances the first permitted incomplete gate
Tests/evidence determine progress
Human is interrupted only for genuine direction/authority decisions
```

That is substantially more autonomous than micromanaging every code edit, while preserving Saddle's central principle.

## First Codex work order after bootstrap

Do not ask Codex to “build Saddle”.

Give it:

> Read `AGENTS.md`, `PROJECT_STATE.md`, `EXECUTION_PLAN.md`, `RESTRICTIONS.md`, and `SESSION_HANDOFF.md`. Work only on the active Phase-0 gate. Do not implement future phases. Run a zero-memory continuity audit and make only the smallest changes necessary for a fresh agent to recover product definition, status, blocker, and one next step from the repository. Record evidence and update the handoff. Park any new ideas instead of implementing them.

Only after Phase 0 passes should the next work order advance to Phase 1.
