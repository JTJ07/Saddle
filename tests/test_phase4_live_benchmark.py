import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase4_live_benchmark import (  # noqa: E402
    LiveBenchmarkError,
    _conservative_max_call_cost,
    _estimated_cost,
)


class Phase4LiveBenchmarkTests(unittest.TestCase):
    def test_estimated_cost_includes_thinking_tokens(self):
        cost = _estimated_cost(
            "gemini-3.1-pro-preview",
            {"input_tokens": 1000, "output_tokens": 500, "reasoning_tokens": 250},
        )
        self.assertAlmostEqual(cost, (1000 * 2.0 + 750 * 12.0) / 1_000_000)

    def test_estimated_cost_requires_usage(self):
        self.assertIsNone(
            _estimated_cost(
                "gemini-3.6-flash",
                {"input_tokens": None, "output_tokens": 10, "reasoning_tokens": 1},
            )
        )

    def test_conservative_guard_reserves_thinking_allowance(self):
        case = {
            "problem": "p",
            "case_contract": "c",
            "target_source": "s",
            "tests_source": "t",
        }
        cost = _conservative_max_call_cost("gemini-3.1-pro-preview", case, 8192)
        output_only_floor = (8192 * 12.0) / 1_000_000
        self.assertGreater(cost, output_only_floor)
        self.assertLess(cost, 5.0)

    def test_unknown_model_fails_closed_before_call(self):
        case = {
            "problem": "p",
            "case_contract": "c",
            "target_source": "s",
            "tests_source": "t",
        }
        with self.assertRaises(LiveBenchmarkError):
            _conservative_max_call_cost("unknown-model", case, 8192)


if __name__ == "__main__":
    unittest.main()
