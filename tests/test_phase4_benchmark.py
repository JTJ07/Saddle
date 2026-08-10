import json
import subprocess
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase4_benchmark import BenchmarkError, load_case  # noqa: E402


def git(path: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(path), *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def fixture():
    tmp = tempfile.TemporaryDirectory()
    base = Path(tmp.name)
    root = base / "saddle"
    checkout = base / "case"
    (root / "config").mkdir(parents=True)
    (checkout / "cases").mkdir(parents=True)
    (checkout / "project_registry").mkdir()
    (checkout / "tests").mkdir()
    (checkout / "cases" / "CASE-001.md").write_text("Fix it.\n", encoding="utf-8")
    (checkout / "project_registry" / "registry.py").write_text("x = 1\n", encoding="utf-8")
    (checkout / "tests" / "test_registry.py").write_text("# tests\n", encoding="utf-8")
    git(checkout, "init", "-q")
    git(checkout, "config", "user.email", "test@example.invalid")
    git(checkout, "config", "user.name", "Saddle Test")
    git(checkout, "add", ".")
    git(checkout, "commit", "-qm", "fixture")
    commit = git(checkout, "rev-parse", "HEAD")
    config = {
        "repository": "example/pilot",
        "cases": [
            {
                "case_id": "CASE-001",
                "commit": commit,
                "case_doc": "cases/CASE-001.md",
                "target_path": "project_registry/registry.py",
                "tests_paths": ["tests/test_registry.py"],
                "target_tests": ["test"],
                "max_patch_lines": 80,
            }
        ],
    }
    (root / "config" / "worker-cases-v0.1.json").write_text(
        json.dumps(config), encoding="utf-8"
    )
    return tmp, root, checkout, commit


class Phase4BenchmarkTests(unittest.TestCase):
    def test_load_case_requires_exact_checkout_commit(self):
        tmp, root, checkout, commit = fixture()
        with tmp:
            case = load_case(root, checkout, "CASE-001")
            self.assertEqual(case["commit"], commit)
            self.assertEqual(case["target_source"], "x = 1\n")

    def test_checkout_drift_fails_closed(self):
        tmp, root, checkout, _commit = fixture()
        with tmp:
            (checkout / "extra.txt").write_text("later\n", encoding="utf-8")
            git(checkout, "add", ".")
            git(checkout, "commit", "-qm", "drift")
            with self.assertRaises(BenchmarkError):
                load_case(root, checkout, "CASE-001")

    def test_unknown_case_fails_closed(self):
        tmp, root, checkout, _commit = fixture()
        with tmp:
            with self.assertRaises(BenchmarkError):
                load_case(root, checkout, "CASE-404")


if __name__ == "__main__":
    unittest.main()
