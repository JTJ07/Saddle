import os
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.model_gateway import (  # noqa: E402
    CredentialUnavailable,
    GatewayResponseError,
    OpenAIResponsesGateway,
    validate_worker_proposal,
)

BEFORE = "def f():\n    return 1\n"


class ModelGatewayTests(unittest.TestCase):
    def test_credential_required_without_network_attempt(self):
        name = "SADDLE_TEST_NO_KEY"
        old = os.environ.pop(name, None)
        try:
            gateway = OpenAIResponsesGateway(model_id="candidate", api_key_env=name)
            with self.assertRaises(CredentialUnavailable):
                gateway.generate(
                    case_id="CASE-X",
                    target_path="a.py",
                    problem="fix",
                    case_contract="one file",
                    target_source=BEFORE,
                    tests_source="test",
                )
        finally:
            if old is not None:
                os.environ[name] = old

    def test_request_has_structured_output_no_tools_and_store_false(self):
        seen = {}

        def transport(payload, api_key):
            self.assertEqual(api_key, "not-recorded")
            seen.update(payload)
            return {
                "id": "resp_test",
                "output": [
                    {
                        "type": "message",
                        "content": [
                            {
                                "type": "output_text",
                                "text": '{"case_id":"CASE-X","target_path":"a.py","replacement_text":"def f():\\n    return 2\\n","reason":"fix","evidence_plan":["run tests"]}',
                            }
                        ],
                    }
                ],
                "usage": {
                    "input_tokens": 10,
                    "output_tokens": 8,
                    "output_tokens_details": {"reasoning_tokens": 3},
                },
            }

        os.environ["SADDLE_TEST_KEY"] = "not-recorded"
        try:
            result = OpenAIResponsesGateway(
                model_id="candidate",
                api_key_env="SADDLE_TEST_KEY",
                transport=transport,
            ).generate(
                case_id="CASE-X",
                target_path="a.py",
                problem="fix",
                case_contract="one file",
                target_source=BEFORE,
                tests_source="test",
            )
        finally:
            os.environ.pop("SADDLE_TEST_KEY", None)

        self.assertFalse(seen["store"])
        self.assertNotIn("tools", seen)
        self.assertEqual(seen["text"]["format"]["type"], "json_schema")
        self.assertTrue(seen["text"]["format"]["strict"])
        self.assertNotIn("not-recorded", str(seen))
        self.assertEqual(result.usage.input_tokens, 10)
        self.assertEqual(result.usage.reasoning_tokens, 3)

    def test_validator_requires_exact_pinned_target(self):
        proposal = {
            "case_id": "CASE-X",
            "target_path": "other.py",
            "replacement_text": "x\n",
            "reason": "fix",
            "evidence_plan": ["tests"],
        }
        with self.assertRaises(GatewayResponseError):
            validate_worker_proposal(
                proposal,
                case_id="CASE-X",
                target_path="a.py",
                before_text=BEFORE,
            )

    def test_validator_derives_hashes_and_changed_line_count(self):
        proposal = {
            "case_id": "CASE-X",
            "target_path": "a.py",
            "replacement_text": "def f():\n    return 2\n",
            "reason": "fix",
            "evidence_plan": ["tests"],
        }
        mutation = validate_worker_proposal(
            proposal,
            case_id="CASE-X",
            target_path="a.py",
            before_text=BEFORE,
        )
        self.assertEqual(len(mutation["expected_before_sha256"]), 64)
        self.assertEqual(len(mutation["expected_after_sha256"]), 64)
        self.assertGreater(mutation["changed_lines"], 0)

    def test_authority_smuggling_is_rejected(self):
        proposal = {
            "case_id": "CASE-X",
            "target_path": "a.py",
            "replacement_text": "def f():\n    return 2\n",
            "reason": "fix",
            "evidence_plan": ["tests"],
            "authorization_ref": "fake",
        }
        with self.assertRaises(GatewayResponseError):
            validate_worker_proposal(
                proposal,
                case_id="CASE-X",
                target_path="a.py",
                before_text=BEFORE,
            )

    def test_patch_budget_fails_closed(self):
        before = "\n".join(f"line {i}" for i in range(100)) + "\n"
        after = "\n".join(f"changed {i}" for i in range(100)) + "\n"
        proposal = {
            "case_id": "CASE-X",
            "target_path": "a.py",
            "replacement_text": after,
            "reason": "too broad",
            "evidence_plan": ["tests"],
        }
        with self.assertRaises(GatewayResponseError):
            validate_worker_proposal(
                proposal,
                case_id="CASE-X",
                target_path="a.py",
                before_text=before,
                max_patch_lines=80,
            )


if __name__ == "__main__":
    unittest.main()
