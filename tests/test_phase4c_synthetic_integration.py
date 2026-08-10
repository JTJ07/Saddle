import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase4c_synthetic_integration import (  # noqa: E402
    OLD_BLOCK,
    TARGET_PATH,
    authorize_declared_effect,
    build_authority,
    build_binding,
    build_intent,
    build_receipt_and_delta,
    controlled_worker_proposal,
    normalize_effect_proposal,
)
from tools.protocol_v01 import validate_bundle, validate_document, with_derived_identity  # noqa: E402

SCHEMA_DIR = ROOT / "protocol" / "v0.1"


class Phase4CSyntheticIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.before = "from typing import Iterable\n\n" + OLD_BLOCK
        self.intent = build_intent()
        self.binding = build_binding(self.intent)
        self.worker = controlled_worker_proposal(self.before)
        self.proposal, self.mutation = normalize_effect_proposal(self.intent, self.worker, self.before)
        self.authority = build_authority(self.binding, self.proposal)

    def test_happy_proposal_is_protocol_valid_and_exact_scope(self):
        validate_document(self.intent, SCHEMA_DIR)
        validate_document(self.proposal, SCHEMA_DIR)
        self.assertEqual(self.proposal["target"], {"kind": "FILE", "ref": TARGET_PATH})
        self.assertEqual(self.mutation["path"], TARGET_PATH)
        self.assertLessEqual(self.mutation["changed_lines"], 80)

    def test_scope_drift_blocks_before_authority(self):
        drift = with_derived_identity({
            **{k: copy.deepcopy(v) for k, v in self.proposal.items() if k not in {"effect_id", "content_hash"}},
            "action": "REBUILD_MODULE",
            "target": {"kind": "DIRECTORY", "ref": "project_registry"},
        })
        result = authorize_declared_effect(self.intent, self.binding, drift, None, consumed=set())
        self.assertEqual(result, {"status": "BLOCK", "reasons": ["PROPOSAL_EXCEEDS_DECLARED_INTENT_SCOPE"]})

    def test_authority_mismatch_blocks(self):
        other = with_derived_identity({
            **{k: copy.deepcopy(v) for k, v in self.proposal.items() if k not in {"effect_id", "content_hash"}},
            "expected_effect": "Different effect identity.",
        })
        authority_for_other = build_authority(self.binding, other)
        result = authorize_declared_effect(self.intent, self.binding, self.proposal, authority_for_other, consumed=set())
        self.assertEqual(result["status"], "BLOCK")
        self.assertTrue(
            "AUTHORITY_EFFECT_ID_MISMATCH" in result["reasons"]
            or "AUTHORITY_EFFECT_HASH_MISMATCH" in result["reasons"]
        )

    def test_replay_blocks_second_use(self):
        consumed = set()
        first = authorize_declared_effect(self.intent, self.binding, self.proposal, self.authority, consumed=consumed)
        second = authorize_declared_effect(self.intent, self.binding, self.proposal, self.authority, consumed=consumed)
        self.assertEqual(first["status"], "ALLOW")
        self.assertEqual(second["status"], "BLOCK")
        self.assertIn("EFFECT_AUTHORITY_REPLAYED", second["reasons"])

    def test_executor_evidence_can_close_protocol_bundle_without_new_decision(self):
        report = {
            "schema_version": "executor-gp001-runtime-result/1.0",
            "status": "ACTION_COMPLETED_REVIEW_REQUIRED",
            "changed_paths": [TARGET_PATH],
            "human_decision_required": True,
            "evidence": {
                "fixture_authority": "BOUND",
                "input_identity": "MATCH",
                "pre_change_target_test": "FAIL",
                "post_change_target_test": "PASS",
                "regression_checks": "PASS",
                "diff_scope": "ALLOWED",
                "protected_material": "UNCHANGED",
                "execution_limits": "RESPECTED",
                "result_artifact": "PRESENT",
            },
        }
        receipt, delta = build_receipt_and_delta(
            self.intent, self.proposal, self.authority, report, duration_ms=10
        )
        validate_bundle(self.intent, self.proposal, receipt, delta, SCHEMA_DIR)
        self.assertEqual(receipt["status"], "SUCCEEDED")
        self.assertEqual(delta["decisions_added"], [])
        self.assertIsNone(delta["project_status_change"])


if __name__ == "__main__":
    unittest.main()
