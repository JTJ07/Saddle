# Saddle Phase 5 authority boundary v0.1

This directory freezes two minimal boundary objects:

- `VerifiedIntentBinding` — proves integrity/origin binding for the exact preserved raw human input without claiming Saddle understands or authorizes its meaning.
- `EffectAuthority` — a separate, single-use, time-bounded decision for one exact `EffectProposal`.

These objects deliberately do not define an identity provider, enterprise IAM, delegation graph, model provider, agent framework, or semantic-intent classifier.

Core rule:

`raw human intent -> integrity/origin binding -> AI proposal -> separate exact effect authority -> governed effect`

No semantic similarity between intent and proposal creates permission.
