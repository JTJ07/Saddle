import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.eval_harness import EvalError, aggregate, audit_repository, validate_result, with_run_id


def base_record(result="PASS"):
    return with_run_id({
        "schema_version": "saddle-eval-result/0.1",
        "lane_id": "pilot-case-001",
        "case_id": "CASE-001",
        "subject_ref": "fixture:case-001",
        "result": result,
        "model": None,
        "prompt_version": None,
        "metrics": {"latency_ms": None, "input_tokens": None, "output_tokens": None, "cost_minor": None, "currency": None, "retries": 0, "human_corrections": 0},
        "scope_violations": [],
        "policy_violations": [],
        "evidence_refs": ["evidence:test"],
        "started_at": "2026-08-10T18:00:00Z",
        "finished_at": "2026-08-10T18:00:01Z",
        "notes": []
    })


def write_good_repo(root: Path, state_phase=3, handoff_phase=3, ready_count=1, human_review_count=0):
    for rel in ["AGENTS.md", "EXECUTION_PLAN.md", "RESTRICTIONS.md", "DECISION_LOG.md", "ECOSYSTEM_MAP.md", "SOURCE_REGISTRY.md"]:
        (root / rel).write_text("ok\n", encoding="utf-8")
    (root / "PROJECT_STATE.md").write_text(f"---\nstatus: PHASE_2_ACCEPTED / PHASE_{state_phase}_ACTIVE / NOT_YET_FUNCTIONAL\ncompletion_lock: ACTIVE\n---\n## 9. One next step\nDo it.\n", encoding="utf-8")
    (root / "SESSION_HANDOFF.md").write_text(f"---\nstatus: PHASE_2_ACCEPTED / PHASE_{handoff_phase}_ACTIVE / NOT_YET_FUNCTIONAL\n---\n## ONE NEXT STEP\nDo it.\n", encoding="utf-8")
    ready = "\n".join(["Status: `READY / NEXT`" for _ in range(ready_count)])
    human_review = "\n".join(["Status: `TECHNICAL E2E COMPLETE THROUGH HUMAN-REVIEW BOUNDARY / HUMAN REVIEW OPEN`" for _ in range(human_review_count)])
    (root / "TODO.md").write_text("\n".join(item for item in (ready, human_review) if item) + "\n", encoding="utf-8")
    (root / "docs").mkdir()
    (root / "docs" / "SADDLE_PROTOCOL_v0.1.md").write_text("frozen\n", encoding="utf-8")
    (root / "docs" / "SADDLE_PROTOCOL_v0.1_DRAFT.md").write_text("SUPERSEDED\n", encoding="utf-8")
    (root / "config").mkdir()
    (root / "config" / "source-repos.json").write_text(json.dumps({"repositories": [{"name": "x/y", "observed_main": "a" * 40, "role": "test"}]}), encoding="utf-8")


class EvalResultTests(unittest.TestCase):
    def test_valid_record(self):
        validate_result(base_record())

    def test_run_id_detects_mutation(self):
        record = base_record()
        record["case_id"] = "changed"
        with self.assertRaises(EvalError):
            validate_result(record)

    def test_empty_aggregate_is_blocked_not_pass(self):
        self.assertEqual(aggregate([])["overall"], "BLOCKED")

    def test_all_pass_is_pass(self):
        self.assertEqual(aggregate([base_record(), base_record()])["overall"], "PASS")

    def test_fail_cannot_be_hidden(self):
        self.assertEqual(aggregate([base_record(), base_record("FAIL")])["overall"], "FAIL")

    def test_scope_violation_forces_effective_fail(self):
        record = base_record("PASS")
        record["scope_violations"] = ["protected file changed"]
        record = with_run_id({k: v for k, v in record.items() if k != "run_id"})
        summary = aggregate([record])
        self.assertEqual(summary["overall"], "FAIL")
        self.assertTrue(any("SCOPE_VIOLATION" in reason for reason in summary["reasons"]))

    def test_policy_violation_forces_effective_fail(self):
        record = base_record("PASS")
        record["policy_violations"] = ["network used"]
        record = with_run_id({k: v for k, v in record.items() if k != "run_id"})
        self.assertEqual(aggregate([record])["overall"], "FAIL")

    def test_unknown_field_rejected(self):
        record = base_record()
        record["surprise"] = 1
        with self.assertRaises(EvalError):
            validate_result(record)


class RepositoryAuditTests(unittest.TestCase):
    def test_good_repo_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root)
            result = audit_repository(root)
            self.assertEqual(result["overall"], "PASS")
            self.assertEqual(result["source_snapshot"][0]["observed_main"], "a" * 40)

    def test_phase_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root, state_phase=3, handoff_phase=2)
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_multiple_ready_next_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root, ready_count=2)
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_human_review_gate_passes_without_ready_next(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root, ready_count=0, human_review_count=1)
            self.assertEqual(audit_repository(root)["overall"], "PASS")

    def test_multiple_human_review_gates_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root, ready_count=0, human_review_count=2)
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_mixed_ready_next_and_human_review_gate_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root, ready_count=1, human_review_count=1)
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_missing_active_gate_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root, ready_count=0)
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_missing_completion_lock_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_good_repo(root)
            p = root / "PROJECT_STATE.md"
            p.write_text(p.read_text().replace("completion_lock: ACTIVE\n", ""), encoding="utf-8")
            self.assertEqual(audit_repository(root)["overall"], "FAIL")


if __name__ == "__main__":
    unittest.main()
