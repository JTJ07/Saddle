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


if __name__ == "__main__":
    unittest.main()
