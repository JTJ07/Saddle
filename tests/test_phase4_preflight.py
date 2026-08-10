import json
import os
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase4_preflight import PreflightError, run_preflight  # noqa: E402


def write_fixture(root: Path, candidates=2, cases=3):
    (root / "config").mkdir()
    model_items = [
        {"model_id": f"model-{index}", "reasoning_effort": "medium"}
        for index in range(candidates)
    ]
    (root / "config" / "model-benchmark-v0.1.json").write_text(
        json.dumps({"candidates": model_items}), encoding="utf-8"
    )
    case_items = []
    for index in range(cases):
        case_items.append(
            {
                "case_id": f"CASE-00{index + 1}",
                "commit": f"{index + 1:x}" * 40,
                "target_path": "project_registry/registry.py",
                "tests_paths": ["tests/test_registry.py"],
            }
        )
    (root / "config" / "worker-cases-v0.1.json").write_text(
        json.dumps({"cases": case_items}), encoding="utf-8"
    )


class Phase4PreflightTests(unittest.TestCase):
    def test_missing_credential_is_blocked_without_secret_value(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture(root)
            name = "SADDLE_PREFLIGHT_MISSING"
            old = os.environ.pop(name, None)
            try:
                result = run_preflight(root, credential_env=name)
            finally:
                if old is not None:
                    os.environ[name] = old
            self.assertEqual(result["status"], "BLOCKED")
            self.assertFalse(result["credential_present"])
            self.assertEqual(result["reasons"], ["PROVIDER_CREDENTIAL_NOT_CONFIGURED"])

    def test_present_credential_reports_boolean_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture(root)
            os.environ["SADDLE_PREFLIGHT_KEY"] = "super-secret-value"
            try:
                result = run_preflight(root, credential_env="SADDLE_PREFLIGHT_KEY")
            finally:
                os.environ.pop("SADDLE_PREFLIGHT_KEY", None)
            serialized = json.dumps(result)
            self.assertEqual(result["status"], "READY_FOR_EXTERNAL_BENCHMARK")
            self.assertTrue(result["credential_present"])
            self.assertNotIn("super-secret-value", serialized)

    def test_requires_at_least_two_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture(root, candidates=1)
            with self.assertRaises(PreflightError):
                run_preflight(root)

    def test_requires_exact_three_cases(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture(root, cases=2)
            with self.assertRaises(PreflightError):
                run_preflight(root)


if __name__ == "__main__":
    unittest.main()
