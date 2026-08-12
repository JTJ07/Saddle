from __future__ import annotations

import copy
import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase7_functional_acceptance import (  # noqa: E402
    RAW_HUMAN_INTENT,
    Phase7Error,
    effect_and_authority,
    intent_and_binding,
    origin_evidence,
    validate_config,
)
from tools.protocol_v01 import with_derived_identity  # noqa: E402


class Phase7FunctionalAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / "config" / "phase7-acceptance-run-v0.1.json").read_text(encoding="utf-8"))
        self.now = datetime(2026, 8, 12, 4, 0, 0, tzinfo=timezone.utc)
        self.env = {
            "PHASE7_EVENT_NAME": "push",
            "PHASE7_REPOSITORY": "JTJ07/Saddle",
            "PHASE7_ACTOR": "JTJ07",
            "PHASE7_REF": "refs/heads/main",
            "PHASE7_SHA": "1" * 40,
            "PHASE7_RUN_ID": "123456",
            "PHASE7_RUN_ATTEMPT": "1",
        }

    def test_config_preserves_literal_current_human_intent_and_bounds(self):
        validate_config(self.config)
        self.assertEqual(RAW_HUMAN_INTENT, "Kontynuuj Saddle od canonical GitHub state i wykonaj Phase 7")
        self.assertEqual(self.config["raw_human_intent"], RAW_HUMAN_INTENT)
        self.assertEqual(self.config["worker"]["model_id"], "gemini-3.6-flash")
        self.assertEqual(self.config["limits"]["max_model_calls"], 1)
        self.assertEqual(self.config["limits"]["automatic_retries"], 0)
        self.assertTrue(self.config["review"]["required"])

    def test_origin_requires_authenticated_main_push_by_expected_actor(self):
        event, ref_id, content_hash = origin_evidence(self.config, self.env, self.now)
        self.assertEqual(event["actor"], "JTJ07")
        self.assertEqual(event["principal_ref"], "github-user:JTJ07")
        self.assertIn(":push:", ref_id)
        self.assertTrue(content_hash.startswith("sha256:"))
        for key, value in (("PHASE7_ACTOR", "other"), ("PHASE7_REF", "refs/heads/agent/x"), ("PHASE7_EVENT_NAME", "workflow_dispatch")):
            env = dict(self.env)
            env[key] = value
            with self.subTest(key=key):
                with self.assertRaises(Phase7Error):
                    origin_evidence(self.config, env, self.now)

    def test_effect_is_exact_one_file_and_authority_is_separate_policy_object(self):
        _event, ref_id, content_hash = origin_evidence(self.config, self.env, self.now)
        intent, binding = intent_and_binding(self.config, ref_id, content_hash, self.now)
        worker = {"proposal": {"reason": "Validate the complete batch before mutation.", "evidence_plan": ["run target test", "run regression tests", "verify one-file diff"]}}
        proposal, authority = effect_and_authority(intent, binding, worker, ref_id, self.now)
        self.assertEqual(proposal["target"], {"kind": "FILE", "ref": "project_registry/registry.py"})
        self.assertEqual(authority["effect_id"], proposal["effect_id"])
        self.assertEqual(authority["issuer_kind"], "POLICY")
        self.assertEqual(authority["max_uses"], 1)
        self.assertNotIn("authority_id", worker)

    def test_different_effect_identity_cannot_reuse_exact_authority(self):
        _event, ref_id, content_hash = origin_evidence(self.config, self.env, self.now)
        intent, binding = intent_and_binding(self.config, ref_id, content_hash, self.now)
        worker = {"proposal": {"reason": "x", "evidence_plan": ["x"]}}
        proposal, authority = effect_and_authority(intent, binding, worker, ref_id, self.now)
        other = with_derived_identity({
            **{k: copy.deepcopy(v) for k, v in proposal.items() if k not in {"effect_id", "content_hash"}},
            "expected_effect": "different exact effect",
        })
        self.assertNotEqual(other["effect_id"], authority["effect_id"])


if __name__ == "__main__":
    unittest.main()
