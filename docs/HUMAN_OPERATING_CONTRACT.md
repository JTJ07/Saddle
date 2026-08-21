---
document: "Human operating contract"
status: "HUMAN-APPROVED / CURRENT INTERACTION CONTRACT"
effective_at: "2026-08-21"
semantic_owner: "HUMAN"
durable_repository: "JTJ07/Saddle"
scope: "Human ↔ AI operational task/handoff surface"
---

# HUMAN OPERATING CONTRACT

This file durably preserves the current Human-owned interaction contract. Saddle is the persistence/control-layer repository for this contract; the repository does not become the semantic owner of Human intent by storing it.

The current external collaboration surface is exactly:

```text
AKCJA
GDZIE
ODESŁAĆ
```

## AKCJA

`AKCJA = co jest robione + granice + wynik, jeśli już istnieje.`

State the exact work, the boundaries / forbidden scope, the completion condition, and any already-existing result that must be preserved rather than recomputed.

## GDZIE

`GDZIE = dokładna tożsamość scope; PINNED albo LIVE, gdy ma to znaczenie.`

- `PINNED` — exact repo / ref / SHA / artifact identity is fixed; do not silently move to a newer ref or SHA.
- `LIVE` — the task intentionally targets current state; resolve the actual current state before acting.
- Source/context presence does not by itself authorize changing that source or make it the work target.

## ODESŁAĆ

`ODESŁAĆ = dokładnie jedna następna rzecz / decyzja / autoryzacja potrzebna teraz od Human albo NIC.`

Do not return multiple competing next actions under `ODESŁAĆ`. If no Human handoff is currently required, use `NIC`.

## Authority boundary

Repository write, merge, deploy, release, tag, external communication, spending, secrets/permissions expansion, destructive action, or other consequential effect requires the authority applicable to that exact effect. Capability does not create permission.

```text
CAPABILITY != PERMISSION
PROPOSAL != DECISION != AUTHORITY != EFFECT
```

## Relation to internal repository handoff

This contract governs the Human-facing task/handoff interaction. It does **not** replace the repository-internal durable-state schema in `SESSION_HANDOFF.md` or create a new runtime, router, component, capability, product phase, or ownership relation.

Older response/output formats may remain in historical references. They do not supersede this current Human-owned contract unless the Human explicitly changes it later.
