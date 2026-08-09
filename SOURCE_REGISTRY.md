# SADDLE SOURCE REGISTRY

## Canonical Saddle sources

The default branch of `litrgratis-pixel/Saddle` owns Saddle-specific product state and execution plan.

Priority inside Saddle:

1. `DECISION_LOG.md`
2. `PROJECT_STATE.md`
3. accepted protocol/contracts
4. merged implementation + tests/evidence
5. `SESSION_HANDOFF.md`
6. draft design documents
7. history

## Existing component sources

### COS
- Repo: https://github.com/litrgratis-pixel/COS
- Main observed 2026-08-10: `3220310267c3d0ba2184daaf3f2adad259a9cb20`
- Key: `START_HERE.md`, `CREATIVE_OS.md`
- Draft ecosystem package: https://github.com/litrgratis-pixel/COS/pull/18

### Project Reconstructor
- Repo: https://github.com/litrgratis-pixel/creative-os-project-reconstructor
- Main observed: `defc7b029097284f94136fec54b75c313ac12f68`
- Key: `README.md`, `PROJECT_STATE.md`, `PROMPT_STARTOWY.md`, tests, validator

### ScriptOps
- Repo: https://github.com/litrgratis-pixel/scriptops
- Main observed: `90a5ba9863961c4b79472db84297cfb403cc5158`
- Key: `PROJECT_STATE.md`, `sources/RC1_SCOPE_LOCK.md`, `CODEX_START.md`, `legacy/scriptops-v2-single.py`

### Executor
- Repo: https://github.com/litrgratis-pixel/Executor
- Main observed: `788443c3ed5b290ac8f1de145a93d02d2dd15317`
- Key current implementation: `executor/request_to_contract.py`, `executor/gp001_runtime.py`, authorization/policy/sandbox/evidence code, task/project/policy contracts
- Active trust work: PRs #51–#57

### Executor Pilot Target
- Repo: https://github.com/litrgratis-pixel/executor-pilot-target
- Main observed: `dc094679ef3e2d5cf5f1aa0ff0fd54d16f201154`
- Key: `PILOT_CONTRACT.md`, CASE-001–003 branches/issues/tests

## Original AI engineering operating package

Preserved in this bootstrap:

- `references/AI_ENGINEERING_OS_AGENTS_ORIGINAL.md`
- `references/README_AI_OS_ORIGINAL.md`

The Saddle root `AGENTS.md` specializes those principles with the new completion lock and permanent-memory rule.

## Current OpenAI primary references for delegation

Verified during bootstrap research:

- Codex product: https://openai.com/codex/
- Codex introduction / AGENTS.md behavior: https://openai.com/index/introducing-codex/
- Codex in ChatGPT plan help: https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits
- GitHub connection note (ChatGPT GitHub app is read-oriented; code changes are via Codex): https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt-deep-research-to-chatgpt-deep-research
- Codex plugins/skills: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex

Always re-check current official documentation before relying on product capabilities or limits.
