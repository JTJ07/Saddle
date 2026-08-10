# Saddle Protocol v0.1

Status: `FROZEN CONTRACT ARTIFACTS / PHASE 2`

Files:

- `common.schema.json` — provider-independent shared source/evidence/authority/value definitions;
- `intent-envelope.schema.json` — exact human intent and durable binding;
- `effect-proposal.schema.json` — proposed consequential effect, explicitly not authority;
- `effect-receipt.schema.json` — execution result/evidence bound to exact effect authority;
- `state-delta.schema.json` — durable FACT/DECISION/HYPOTHESIS/state update.

Normative project description: `docs/SADDLE_PROTOCOL_v0.1.md`.

Deterministic utility/test implementation:

- `tools/protocol_v01.py`
- `tests/test_protocol_v01.py`

The schemas declare JSON Schema Draft 2020-12. Content identity uses the restricted Saddle v0.1 RFC-8785/JCS profile documented in the normative protocol file.
