# PHASE 2 — SADDLE PROTOCOL v0.1 TEST EVIDENCE

Date: 2026-08-10
Status: `LOCAL DETERMINISTIC EVIDENCE / NO GITHUB CI CLAIM`
Branch: `agent/phase2-protocol-v01`

## Scope tested

Exact Phase-2 artifact set:

- `protocol/v0.1/common.schema.json`
- `protocol/v0.1/intent-envelope.schema.json`
- `protocol/v0.1/effect-proposal.schema.json`
- `protocol/v0.1/effect-receipt.schema.json`
- `protocol/v0.1/state-delta.schema.json`
- `tools/protocol_v01.py`
- `tests/test_protocol_v01.py`
- `docs/SADDLE_PROTOCOL_v0.1.md`

## Standards basis

- JSON Schema Draft 2020-12 for schemas.
- RFC 8785 JCS rules for canonical JSON identity, under the documented Saddle v0.1 restricted profile.
- Saddle v0.1 additionally rejects floating-point JSON numbers and integers outside the safe I-JSON interoperability range to avoid cross-language numeric identity ambiguity in the first slice.

## Commands executed

```text
python -m compileall -q tools tests
```

Result: `PASS`

```text
python -m unittest discover -s tests -v
```

Result:

```text
Ran 14 tests
OK
```

No GitHub Actions run is claimed for this change set.

## Passing test set

1. object property reordering does not change canonical bytes;
2. UTF-16 object-key sorting follows the JCS ordering requirement;
3. array order remains significant;
4. floating-point JSON numbers fail closed in Protocol v0.1;
5. duplicate JSON properties fail closed;
6. all five schema files declare JSON Schema Draft 2020-12 and cross-references resolve;
7. one valid IntentEnvelope → EffectProposal → EffectReceipt → StateDelta bundle passes;
8. changing `raw_human_intent` after identity assignment invalidates content identity;
9. `VERIFIED` intent origin without evidence fails closed;
10. attempting to add `authorization_ref` to EffectProposal fails closed;
11. EffectReceipt authority bound to the wrong proposal content hash fails closed;
12. `decision_owner_kind = AI` fails the StateDelta decision schema;
13. project status change without a matching human decision in the same StateDelta fails closed;
14. unknown protocol properties fail closed.

## What this evidence proves

- the four protocol objects have deterministic schemas and bindings;
- top-level object identities are content-addressed;
- raw intent is mutation-detectable;
- proposal/authority are structurally separated;
- receipt authority must bind exact effect identity/content;
- FACT/DECISION/HYPOTHESIS remain structurally separate;
- project status change cannot be produced by an unbound AI decision record;
- no provider/model/agent framework is required by the protocol mechanics.

## What this evidence does not prove

- a real identity/request-origin provider;
- a real effect-authority adapter;
- a real AI worker;
- Executor integration;
- ScriptOps end-to-end operation;
- product-level `FUNCTIONAL_SADDLE_ACCEPTED`.

Those remain later gates.
