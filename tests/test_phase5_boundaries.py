import copy
import hashlib
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.phase5_boundaries import authorize_effect, raw_intent_hash, with_boundary_identity

NOW = datetime(2026, 8, 10, 18, 30, 0, tzinfo=timezone.utc)


def fake_hash(seed: str) -> str:
    return "sha256:" + hashlib.sha256(seed.encode()).hexdigest()


def intent():
    raw = "Dodaj funkcję X bez przebudowy całego systemu."
    return {
        "schema_version": "saddle-intent/0.1",
        "intent_id": "intent:sha256:" + "1" * 64,
        "content_hash": "sha256:" + "2" * 64,
        "raw_human_intent": raw,
        "origin": {
            "status": "VERIFIED",
            "principal_ref": "human:owner",
            "evidence_refs": [{"ref_id": "origin:1", "kind": "EVIDENCE"}],
        },
        "derived_interpretation": {
            "text": "Implement X minimally.",
            "proposed_by": "model:test",
            "source_refs": [{"ref_id": "intent:1", "kind": "INTENT"}],
        },
    }


def binding(i):
    return with_boundary_identity({
        "schema_version": "saddle-verified-intent-binding/0.1",
        "intent_id": i["intent_id"],
        "intent_content_hash": i["content_hash"],
        "raw_intent_hash": raw_intent_hash(i["raw_human_intent"]),
        "principal_ref": "human:owner",
        "origin_event": {
            "ref_id": "origin-event:1",
            "content_hash": fake_hash("origin-event"),
            "observed_at": "2026-08-10T18:20:00Z",
        },
        "status": "ACTIVE",
        "issued_at": "2026-08-10T18:21:00Z",
        "expires_at": "2026-08-10T19:21:00Z",
    })


def proposal(i, *, action="WRITE_REPOSITORY_FILE", target_ref="module/x.py"):
    return {
        "schema_version": "saddle-effect-proposal/0.1",
        "effect_id": "effect:sha256:" + "3" * 64,
        "content_hash": "sha256:" + "4" * 64,
        "intent_id": i["intent_id"],
        "action": action,
        "target": {"kind": "FILE", "ref": target_ref},
        "expected_effect": "Implement X.",
    }


def authority(b, p, *, decision="ALLOW"):
    return with_boundary_identity({
        "schema_version": "saddle-effect-authority/0.1",
        "decision": decision,
        "intent_binding_id": b["binding_id"],
        "intent_binding_hash": b["content_hash"],
        "effect_id": p["effect_id"],
        "effect_content_hash": p["content_hash"],
        "authorized_action": p["action"],
        "authorized_target": {"kind": p["target"]["kind"], "ref": p["target"]["ref"]},
        "evidence_requirements": ["tests pass"],
        "issuer_kind": "HUMAN",
        "issuer_ref": "human:owner",
        "source_refs": ["review:event:1"],
        "status": "ACTIVE",
        "max_uses": 1,
        "issued_at": "2026-08-10T18:25:00Z",
        "expires_at": "2026-08-10T19:25:00Z",
        "reason": "Exact effect reviewed against preserved human intent.",
    })


class Phase5BoundaryTests(unittest.TestCase):
    def test_exact_intent_and_exact_authority_allows(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p)
        self.assertEqual(authorize_effect(i, b, p, a, now=NOW, consumed_authority_ids=set())["status"], "ALLOW")

    def test_proposal_without_authority_blocks_even_if_it_references_intent(self):
        i = intent(); b = binding(i); p = proposal(i, action="REBUILD_SYSTEM", target_ref="*")
        result = authorize_effect(i, b, p, None, now=NOW)
        self.assertEqual(result["status"], "BLOCK")
        self.assertIn("EXPLICIT_EFFECT_AUTHORITY_REQUIRED", result["reasons"])

    def test_ai_interpretation_is_not_effect_permission(self):
        i = intent(); i["derived_interpretation"]["text"] = "User wants a whole-system rewrite."
        b = binding(i); p = proposal(i, action="REBUILD_SYSTEM", target_ref="system")
        self.assertEqual(authorize_effect(i, b, p, None, now=NOW)["status"], "BLOCK")

    def test_raw_intent_mutation_breaks_origin_binding(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p)
        i["raw_human_intent"] = "Przebuduj cały system."
        result = authorize_effect(i, b, p, a, now=NOW)
        self.assertEqual(result["status"], "BLOCK")
        self.assertIn("RAW_INTENT_HASH_BINDING_MISMATCH", result["reasons"])

    def test_derived_interpretation_can_change_without_changing_raw_anchor(self):
        i = intent(); before = raw_intent_hash(i["raw_human_intent"])
        i["derived_interpretation"]["text"] = "Alternative hypothesis Y."
        self.assertEqual(before, raw_intent_hash(i["raw_human_intent"]))

    def test_user_label_without_verified_origin_blocks(self):
        i = intent(); i["origin"]["status"] = "UNVERIFIED"
        b = binding(i); p = proposal(i); a = authority(b, p)
        result = authorize_effect(i, b, p, a, now=NOW)
        self.assertIn("INTENT_ORIGIN_NOT_VERIFIED", result["reasons"])

    def test_authority_for_other_effect_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p)
        p2 = copy.deepcopy(p); p2["effect_id"] = "effect:sha256:" + "5" * 64; p2["content_hash"] = "sha256:" + "6" * 64
        result = authorize_effect(i, b, p2, a, now=NOW)
        self.assertIn("AUTHORITY_EFFECT_ID_MISMATCH", result["reasons"])

    def test_mutated_proposal_after_authority_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p)
        p["content_hash"] = "sha256:" + "9" * 64
        self.assertIn("AUTHORITY_EFFECT_HASH_MISMATCH", authorize_effect(i, b, p, a, now=NOW)["reasons"])

    def test_action_scope_mismatch_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p); p["action"] = "DELETE_REPOSITORY"
        self.assertIn("AUTHORITY_ACTION_MISMATCH", authorize_effect(i, b, p, a, now=NOW)["reasons"])

    def test_target_scope_mismatch_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p); p["target"]["ref"] = "other/file.py"
        self.assertIn("AUTHORITY_TARGET_MISMATCH", authorize_effect(i, b, p, a, now=NOW)["reasons"])

    def test_deny_authority_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p, decision="DENY")
        self.assertIn("EFFECT_AUTHORITY_DENIES", authorize_effect(i, b, p, a, now=NOW)["reasons"])

    def test_expired_verified_intent_blocks(self):
        i = intent(); b0 = binding(i); b0.pop("binding_id"); b0.pop("content_hash"); b0["expires_at"] = "2026-08-10T18:29:59Z"
        b = with_boundary_identity(b0); p = proposal(i); a = authority(b, p)
        self.assertIn("VERIFIED_INTENT_BINDING_STALE", authorize_effect(i, b, p, a, now=NOW)["reasons"])

    def test_expired_effect_authority_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a0 = authority(b, p); a0.pop("authority_id"); a0.pop("content_hash"); a0["expires_at"] = "2026-08-10T18:29:59Z"
        a = with_boundary_identity(a0)
        self.assertIn("EFFECT_AUTHORITY_STALE", authorize_effect(i, b, p, a, now=NOW)["reasons"])

    def test_authority_replay_blocks_second_use(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p); consumed = set()
        self.assertEqual(authorize_effect(i, b, p, a, now=NOW, consumed_authority_ids=consumed)["status"], "ALLOW")
        self.assertIn("EFFECT_AUTHORITY_REPLAYED", authorize_effect(i, b, p, a, now=NOW, consumed_authority_ids=consumed)["reasons"])

    def test_wrong_intent_binding_blocks(self):
        i = intent(); b = binding(i); p = proposal(i); a = authority(b, p); p["intent_id"] = "intent:sha256:" + "7" * 64
        self.assertIn("PROPOSAL_INTENT_MISMATCH", authorize_effect(i, b, p, a, now=NOW)["reasons"])


if __name__ == "__main__":
    unittest.main()
