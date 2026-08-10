import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.protocol_v01 import (  # noqa: E402
    ProtocolError,
    SchemaRegistry,
    SchemaValidationError,
    canonicalize,
    loads_strict,
    validate_bundle,
    validate_document,
    with_derived_identity,
)

SCHEMA_DIR = ROOT / "protocol" / "v0.1"


def ref(ref_id, kind="EVIDENCE", content_hash=None):
    value = {"ref_id": ref_id, "kind": kind}
    if content_hash:
        value["content_hash"] = content_hash
    return value


def intent_base():
    return {
        "schema_version": "saddle-intent/0.1",
        "raw_human_intent": "Napraw CASE-001 bez zmiany celu zadania.",
        "origin": {"status": "VERIFIED", "principal_ref": "human:owner", "evidence_refs": [ref("origin-event-1")]},
        "desired_outcome": "Wymagane testy przechodzą.",
        "success_evidence": [{"description": "unit tests pass"}],
        "human_owned_constraints": ["Do not modify tests."],
        "context_refs": [ref("repo:pilot", "REPOSITORY")],
        "budget": {"max_duration_ms": 60000},
        "created_at": "2026-08-10T17:30:00Z",
    }


def proposal_base(intent):
    return {
        "schema_version": "saddle-effect-proposal/0.1",
        "intent_id": intent["intent_id"],
        "action": "WRITE_REPOSITORY_FILE",
        "target": {"kind": "FILE", "ref": "project_registry/registry.py"},
        "expected_effect": "Atomic batch insertion without partial mutation on duplicate.",
        "required_capabilities": ["READ_REPOSITORY", "PROPOSE_PATCH"],
        "risk": {"level": "LOW", "notes": ["Single allowlisted file."]},
        "reason": "The existing implementation mutates before full validation.",
        "evidence_plan": [{"description": "compileall and unit tests pass"}],
        "created_at": "2026-08-10T17:31:00Z",
    }


def receipt_base(proposal):
    return {
        "schema_version": "saddle-effect-receipt/0.1",
        "effect_id": proposal["effect_id"],
        "authorization_ref": {
            "authority_id": "effect-permission-1",
            "authority_kind": "EFFECT_PERMISSION",
            "status": "ACTIVE",
            "binds_to": {"object_type": "EFFECT", "object_id": proposal["effect_id"], "content_hash": proposal["content_hash"]},
            "source_refs": [ref("human-approval-1")],
            "issued_at": "2026-08-10T17:32:00Z"
        },
        "status": "SUCCEEDED",
        "actual_effect": {"summary": "One file changed.", "result_refs": [ref("commit:abc", "COMMIT")]},
        "changed_objects": [ref("project_registry/registry.py", "FILE")],
        "evidence_refs": [ref("tests:run-1")],
        "tests": [{"name": "unit", "status": "PASS", "evidence_refs": [ref("tests:run-1")]}],
        "duration_ms": 1400,
        "observed_at": "2026-08-10T17:33:00Z"
    }


def delta_base(intent, proposal):
    return {
        "schema_version": "saddle-state-delta/0.1",
        "intent_id": intent["intent_id"],
        "effect_id": proposal["effect_id"],
        "facts_added": [{"fact_id": "fact:tests-pass", "statement": "Required tests passed.", "source_refs": [ref("tests:run-1")], "observed_at": "2026-08-10T17:33:00Z"}],
        "decisions_added": [],
        "hypotheses_added": [],
        "superseded": [],
        "project_status_change": None,
        "blockers": [],
        "next_step": "Human review of the bounded result.",
        "source_refs": [ref("tests:run-1")],
        "created_at": "2026-08-10T17:34:00Z"
    }


class CanonicalizationTests(unittest.TestCase):
    def test_property_order_does_not_change_hash_bytes(self):
        a = {"b": 2, "a": 1, "nested": {"z": "x", "a": "y"}}
        b = {"nested": {"a": "y", "z": "x"}, "a": 1, "b": 2}
        self.assertEqual(canonicalize(a), canonicalize(b))

    def test_utf16_property_sorting(self):
        obj = {"\ue000": 1, "\U00010000": 2}
        text = canonicalize(obj).decode("utf-8")
        self.assertLess(text.index("\U00010000"), text.index("\ue000"))

    def test_array_order_is_preserved(self):
        self.assertNotEqual(canonicalize([1, 2]), canonicalize([2, 1]))

    def test_float_rejected(self):
        with self.assertRaises(ProtocolError):
            canonicalize({"x": 1.5})

    def test_duplicate_json_property_rejected(self):
        with self.assertRaises(ProtocolError):
            loads_strict('{"x":1,"x":2}')


class SchemaTests(unittest.TestCase):
    def test_all_schemas_are_2020_12_and_resolvable(self):
        registry = SchemaRegistry(SCHEMA_DIR)
        self.assertEqual(len(registry.by_id), 5)
        for schema in registry.by_id.values():
            self.assertEqual(schema.get("$schema"), "https://json-schema.org/draft/2020-12/schema")

    def test_valid_protocol_bundle(self):
        intent = with_derived_identity(intent_base())
        proposal = with_derived_identity(proposal_base(intent))
        receipt = with_derived_identity(receipt_base(proposal))
        delta = with_derived_identity(delta_base(intent, proposal))
        validate_bundle(intent, proposal, receipt, delta, SCHEMA_DIR)

    def test_raw_intent_change_breaks_identity(self):
        intent = with_derived_identity(intent_base())
        intent["raw_human_intent"] += " altered"
        with self.assertRaises(ProtocolError):
            validate_document(intent, SCHEMA_DIR)

    def test_verified_origin_requires_evidence(self):
        value = intent_base()
        value["origin"] = {"status": "VERIFIED", "principal_ref": "human:owner", "evidence_refs": []}
        value = with_derived_identity(value)
        with self.assertRaises(ProtocolError):
            validate_document(value, SCHEMA_DIR)

    def test_effect_proposal_cannot_smuggle_authority(self):
        intent = with_derived_identity(intent_base())
        proposal = proposal_base(intent)
        proposal["authorization_ref"] = {"authority_id": "fake"}
        proposal = with_derived_identity(proposal)
        with self.assertRaises(SchemaValidationError):
            validate_document(proposal, SCHEMA_DIR)

    def test_receipt_requires_exact_effect_binding(self):
        intent = with_derived_identity(intent_base())
        proposal = with_derived_identity(proposal_base(intent))
        receipt = receipt_base(proposal)
        receipt["authorization_ref"]["binds_to"]["content_hash"] = "sha256:" + "0" * 64
        receipt = with_derived_identity(receipt)
        delta = with_derived_identity(delta_base(intent, proposal))
        with self.assertRaises(ProtocolError):
            validate_bundle(intent, proposal, receipt, delta, SCHEMA_DIR)

    def test_decision_record_requires_human_owner(self):
        intent = with_derived_identity(intent_base())
        proposal = with_derived_identity(proposal_base(intent))
        delta = delta_base(intent, proposal)
        delta["decisions_added"] = [{
            "decision_id": "decision:1",
            "statement": "Accept result.",
            "decision_owner_kind": "AI",
            "decision_owner_ref": "model:x",
            "source_refs": [ref("chat:event")],
            "decided_at": "2026-08-10T17:34:00Z"
        }]
        delta = with_derived_identity(delta)
        with self.assertRaises(SchemaValidationError):
            validate_document(delta, SCHEMA_DIR)

    def test_status_change_requires_same_delta_human_decision(self):
        intent = with_derived_identity(intent_base())
        proposal = with_derived_identity(proposal_base(intent))
        receipt = with_derived_identity(receipt_base(proposal))
        delta = delta_base(intent, proposal)
        delta["project_status_change"] = {"from": "A", "to": "B", "decision_ref": "decision:missing"}
        delta = with_derived_identity(delta)
        with self.assertRaises(ProtocolError):
            validate_bundle(intent, proposal, receipt, delta, SCHEMA_DIR)

    def test_unknown_property_fails_closed(self):
        base = intent_base()
        base["secret_extra"] = "should fail"
        intent = with_derived_identity(base)
        with self.assertRaises(SchemaValidationError):
            validate_document(intent, SCHEMA_DIR)


if __name__ == "__main__":
    unittest.main()
