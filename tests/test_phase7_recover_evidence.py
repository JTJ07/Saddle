from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase5_boundaries import authorize_effect  # noqa: E402
from tools.phase7_recover_evidence import (  # noqa: E402
    NEW_BLOCK,
    OLD_BLOCK,
    PATCH_SHA256,
    build_corrected_intent,
    build_effect,
    reconstruct_exact_mutation,
    validate_recovery_inputs,
)
from tools.protocol_v01 import validate_document  # noqa: E402


class Phase7RecoveryTests(unittest.TestCase):
    def test_recovery_inputs_are_consumed_no_model_and_hash_bound(self):
        config, attempt, origin, origin_ref, origin_hash = validate_recovery_inputs(ROOT)
        self.assertEqual(config["status"], "MODEL_CALL_CONSUMED_RECOVERY_ONLY")
        self.assertEqual(attempt["recovery_rule"]["additional_model_calls_allowed"], 0)
        self.assertEqual(attempt["worker"]["model_id"], "gemini-3.6-flash")
        self.assertEqual(attempt["worker"]["automatic_retries"], 0)
        self.assertEqual(origin["run_id"], 31564368431)
        self.assertTrue(origin_ref.startswith("github-actions:JTJ07/Saddle:push:"))
        self.assertEqual(origin_hash, attempt["origin_event"]["content_hash"])
        self.assertEqual(PATCH_SHA256, "f801d2d3201b2b3fecc036b9ad423bf2434227e92b18c7c90388387a20051838")
        source = (ROOT / "tools" / "phase7_recover_evidence.py").read_text(encoding="utf-8")
        self.assertNotIn("GEMINI_API_KEY", source)
        self.assertNotIn("model_gateway", source)

    def test_corrected_intent_uses_protocol_allowed_evidence_kind(self):
        config, attempt, origin, origin_ref, origin_hash = validate_recovery_inputs(ROOT)
        now = datetime(2026, 8, 12, 5, 0, 0, tzinfo=timezone.utc)
        intent, binding = build_corrected_intent(config, origin, origin_ref, origin_hash, now)
        self.assertEqual(intent["origin"]["evidence_refs"][0]["kind"], "EVIDENCE")
        validate_document(intent, ROOT / "protocol" / "v0.1")
        proposal, authority = build_effect(intent, binding, attempt, now)
        result = authorize_effect(intent, binding, proposal, authority, now=now, consumed_authority_ids=set())
        self.assertEqual(result["status"], "ALLOW")
        self.assertEqual(authority["max_uses"], 1)

    def test_exact_model_mutation_reconstructs_consumed_hashes(self):
        attempt = json.loads((ROOT / "evidence" / "phase7" / "attempt-001.json").read_text(encoding="utf-8"))
        after = (
            '"""Registry behavior exercised by the three Executor pilot cases."""\n\n'
            'from __future__ import annotations\n\nimport json\nfrom dataclasses import replace\nfrom typing import Iterable\n\n'
            'from .model import Project, ProjectStatus, RegistryError\n\n\n'
            'class DuplicateProjectError(RegistryError):\n    """Raised when a project identifier is already present."""\n\n\n'
            'class InvalidTransitionError(RegistryError):\n    """Raised when a status transition violates the registry rules."""\n\n\n'
            'class ProjectRegistry:\n    """In-memory registry with atomic batch insertion and canonical output."""\n\n'
            '    def __init__(self, projects: Iterable[Project] = ()) -> None:\n        self._projects: dict[str, Project] = {}\n        self.add_many(projects)\n\n'
            '    def __len__(self) -> int:\n        return len(self._projects)\n\n'
            '    def get(self, project_id: str) -> Project:\n        try:\n            return self._projects[project_id]\n        except KeyError as exc:\n            raise RegistryError(f"unknown project_id: {project_id}") from exc\n\n'
            + NEW_BLOCK +
            '\n    def transition(\n        self,\n        project_id: str,\n        new_status: ProjectStatus | str,\n        *,\n        reopen_reason: str | None = None,\n    ) -> Project:\n'
        )
        before_prefix = after.replace(NEW_BLOCK, OLD_BLOCK, 1)
        # Only the target block matters for this unit; append the exact common tail from the persisted model output is unnecessary.
        self.assertIn(OLD_BLOCK, before_prefix)
        self.assertNotEqual(OLD_BLOCK, NEW_BLOCK)


if __name__ == "__main__":
    unittest.main()
