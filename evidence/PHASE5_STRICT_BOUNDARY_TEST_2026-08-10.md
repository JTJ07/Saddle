# PHASE 5 STRICT BOUNDARY TEST — 2026-08-10

Status: `LOCAL DETERMINISTIC EVIDENCE / NOT FULL SADDLE ACCEPTANCE`

## Human decision basis

The user explicitly accepted the responsibility architecture, ownership model and Phase-4 AI-worker direction, kept trust boundaries intentionally open, froze Phase 1–4 foundations, and directed the next work to strict Phase 5 boundary proof.

Recorded as:
- `DEC-SAD-008` — Saddle preserves intent integrity; it does not authorize meaning;
- `DEC-SAD-009` — freeze Phase 1–4 foundations; advance to strict Phase 5 boundary proof.

## Implemented slice

- `authority/v0.1/verified-intent-binding.schema.json`;
- `authority/v0.1/effect-authority.schema.json`;
- `tools/phase5_boundaries.py`;
- `tests/test_phase5_boundaries.py`;
- `docs/PHASE5_STRICT_BOUNDARIES_v0.1.md`.

## Test commands

```text
python -m compileall -q tools tests
PASS

python -m unittest discover -s tests -p 'test_phase5_boundaries.py' -v
Ran 15 tests
OK
```

The local deterministic reference slice corresponding to the committed Phase-5 implementation passed all 15 Phase-5 tests before canonicalization.

No GitHub CI result is claimed.

## Negative/adversarial cases proven fail-closed

1. proposal references intent but has no separate authority → BLOCK;
2. AI derived interpretation expands goal but has no authority → BLOCK;
3. raw human intent mutates after origin binding → BLOCK;
4. USER-like origin without verified status → BLOCK;
5. authority belongs to another effect → BLOCK;
6. effect proposal content changes after authority → BLOCK;
7. action changes after authority → BLOCK;
8. target changes after authority → BLOCK;
9. explicit DENY authority → BLOCK;
10. expired verified-intent binding → BLOCK;
11. expired effect authority → BLOCK;
12. replayed single-use authority → BLOCK;
13. proposal binds another intent → BLOCK.

## Positive control

Exact active `VerifiedIntentBinding` + exact active one-use `ALLOW` `EffectAuthority` bound to the same exact proposal returns `ALLOW`.

## Important semantic result

`raw_intent_hash` is derived directly from exact UTF-8 `raw_human_intent` and is independent of `derived_interpretation`.

Therefore AI may revise its interpretation without silently rewriting the preserved human statement.

## Evidence boundary

This phase does NOT prove:

- production request-origin/identity provider authenticity;
- organization-wide authorization;
- live model benchmark;
- Executor runtime execution using this new boundary object;
- real-world business value;
- full functional Saddle.

Trust-provider selection remains intentionally open.

The live Phase-4 Sol/Terra benchmark remains unexecuted and must not be inferred from this result.
