import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.eval_harness import (  # noqa: E402
    HISTORICAL_EXECUTOR_FIRST_TARGET,
    HUMAN_OPERATING_CONTRACT_PATH,
    RUN94_EXECUTOR_IMPLEMENTATION,
    RUN94_EXECUTOR_TREE,
    audit_repository,
)


def write_current_saddle_fixture(root: Path) -> None:
    for rel in ["AGENTS.md", "EXECUTION_PLAN.md", "RESTRICTIONS.md", "DECISION_LOG.md", "ECOSYSTEM_MAP.md", "SOURCE_REGISTRY.md"]:
        (root / rel).write_text("ok\n", encoding="utf-8")

    state_status = "PHASE_7_ACCEPTED / FUNCTIONAL_SADDLE_ACCEPTED / COMPLETION_LOCK_RELEASED"
    state = f"""---
project: Saddle
status: {state_status}
completion_lock: RELEASED
---
{HISTORICAL_EXECUTOR_FIRST_TARGET}
CURRENT RUN94 HUMAN-ACCEPTED IMPLEMENTATION: {RUN94_EXECUTOR_IMPLEMENTATION}
CURRENT RUN94 HUMAN-ACCEPTED TREE: {RUN94_EXECUTOR_TREE}
OBSERVED SHA != LIVE LOCK
{HUMAN_OPERATING_CONTRACT_PATH}
## 9. One next step
No active product-development step.
"""
    handoff = f"""---
project: Saddle
status: {state_status}
---
HISTORICAL FIRST-TARGET HUMAN-ACCEPTED IDENTITY: {HISTORICAL_EXECUTOR_FIRST_TARGET}
CURRENT RUN94 HUMAN-ACCEPTED IMPLEMENTATION: {RUN94_EXECUTOR_IMPLEMENTATION}
CURRENT RUN94 HUMAN-ACCEPTED TREE: {RUN94_EXECUTOR_TREE}
OBSERVED SHA != LIVE LOCK
{HUMAN_OPERATING_CONTRACT_PATH}
## ONE NEXT STEP
Human review only.
"""
    (root / "PROJECT_STATE.md").write_text(state, encoding="utf-8")
    (root / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")
    (root / "TODO.md").write_text("no active gate\n", encoding="utf-8")

    docs = root / "docs"
    docs.mkdir()
    (docs / "SADDLE_PROTOCOL_v0.1.md").write_text("frozen\n", encoding="utf-8")
    (docs / "SADDLE_PROTOCOL_v0.1_DRAFT.md").write_text("SUPERSEDED\n", encoding="utf-8")
    (root / HUMAN_OPERATING_CONTRACT_PATH).write_text(
        """---
semantic_owner: "HUMAN"
---
AKCJA = co jest robione + granice + wynik, jeśli już istnieje.
GDZIE = dokładna tożsamość scope; PINNED albo LIVE, gdy ma to znaczenie.
ODESŁAĆ = dokładnie jedna następna rzecz / decyzja / autoryzacja potrzebna teraz od Human albo NIC.
CAPABILITY != PERMISSION
""",
        encoding="utf-8",
    )

    config = root / "config"
    config.mkdir()
    (config / "completion-lock.json").write_text(
        json.dumps({"schema_version": "saddle-completion-lock/0.1", "status": "RELEASED"}),
        encoding="utf-8",
    )
    (config / "source-repos.json").write_text(
        json.dumps({"repositories": [{"name": "JTJ07/Executor", "observed_main": "a" * 40, "role": "snapshot"}]}),
        encoding="utf-8",
    )


class SemanticCurrentnessTests(unittest.TestCase):
    def test_current_fixture_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current_saddle_fixture(root)
            self.assertEqual(audit_repository(root)["overall"], "PASS")

    def test_run94_current_identity_cannot_disappear(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current_saddle_fixture(root)
            p = root / "SESSION_HANDOFF.md"
            p.write_text(p.read_text(encoding="utf-8").replace(RUN94_EXECUTOR_IMPLEMENTATION, "0" * 40), encoding="utf-8")
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_historical_first_target_cannot_be_repromoted_as_current(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current_saddle_fixture(root)
            p = root / "SESSION_HANDOFF.md"
            p.write_text(
                p.read_text(encoding="utf-8")
                + f"\nThe exact Human-accepted Executor product candidate remains `{HISTORICAL_EXECUTOR_FIRST_TARGET}`\n",
                encoding="utf-8",
            )
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_observed_sha_must_remain_non_live_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current_saddle_fixture(root)
            p = root / "PROJECT_STATE.md"
            p.write_text(p.read_text(encoding="utf-8").replace("OBSERVED SHA != LIVE LOCK", ""), encoding="utf-8")
            self.assertEqual(audit_repository(root)["overall"], "FAIL")

    def test_human_operating_contract_is_recoverable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current_saddle_fixture(root)
            p = root / HUMAN_OPERATING_CONTRACT_PATH
            p.write_text(p.read_text(encoding="utf-8").replace("ODESŁAĆ =", "OLD_FORMAT ="), encoding="utf-8")
            self.assertEqual(audit_repository(root)["overall"], "FAIL")


class CanonicalRecoverySurfaceTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_r01_dec_sad_006_role_placement_is_superseded_by_later_human_decision(self):
        log = self.read("DECISION_LOG.md")
        decision = self.read("decisions/DEC-SAD-019.md")
        state = self.read("PROJECT_STATE.md")
        handoff = self.read("SESSION_HANDOFF.md")

        self.assertIn("## DEC-SAD-006 — Responsibility ownership boundary", log)
        self.assertIn("Status: ACTIVE CORE / ROLE PLACEMENT SUPERSEDED BY DEC-SAD-019", log)
        self.assertIn("## DEC-SAD-019 — Current ownership-semantics reconciliation", log)
        self.assertLess(log.index("## DEC-SAD-006"), log.index("## DEC-SAD-019"))
        self.assertIn("SUPERSEDED FOR CURRENT OWNERSHIP SEMANTICS", decision)
        self.assertIn("SUPERSEDES:\nDEC-SAD-006 / ROLE-PLACEMENT AND FRONT-DOOR TOPOLOGY ONLY", decision)

        for text in (state, handoff):
            self.assertIn("GINSENG", text)
            self.assertIn("INTELLIGENCE", text)
            self.assertIn("SADDLE", text)
            self.assertIn("EXECUTOR", text)
        self.assertIn("DEC-SAD-019", state)
        self.assertIn("DEC-SAD-019", handoff)

    def test_r02_pr41_integration_is_current_while_pre_rework_evidence_stays_rework_required(self):
        state = self.read("PROJECT_STATE.md")
        handoff = self.read("SESSION_HANDOFF.md")
        recheck = self.read("evidence/POST_RECONCILIATION_SEMANTIC_FRESHNESS_RECHECK_2026-08-21.md")

        for text in (state, handoff):
            self.assertIn("4018ea2a0a2f80e326ecd65bfcf9f0d5ae59b4bb", text)
            self.assertIn("5080f60bb3a96b5dd09e2cf720c536e126ceeac9", text)
            self.assertIn("HUMAN ACCEPTED", text)
            self.assertIn("CANONICALLY INTEGRATED", text)

        self.assertNotIn(
            "NARROW SEMANTIC-FRESHNESS RECONCILIATION RECORD — VERIFIED MAINTENANCE RESULT / HUMAN ACCEPTANCE EXTERNAL TO THIS FILE",
            handoff,
        )
        self.assertNotIn(
            "Repository acceptance and integration of this maintenance result are external Human-controlled effects.",
            handoff,
        )
        self.assertIn("VERDICT:\nREWORK REQUIRED", recheck)
        self.assertIn("AUD-007 REOPENED", recheck)
        self.assertIn("RECHECK-R01 OPEN", recheck)
        self.assertIn("RECHECK-R02 OPEN", recheck)

    def test_gap_entry_c0_remains_unimplemented_and_live_untested(self):
        handoff = self.read("SESSION_HANDOFF.md")
        self.assertIn("C0 PAPER SUFFICIENCY — PASS", handoff)
        self.assertIn("C0 LIVE SUFFICIENCY — NOT TESTED", handoff)
        self.assertIn("C0 SOLUTION — NOT HUMAN ACCEPTED", handoff)
        self.assertIn("C0 IMPLEMENTATION — NOT AUTHORIZED", handoff)


if __name__ == "__main__":
    unittest.main()
