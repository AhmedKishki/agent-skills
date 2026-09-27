import csv
import importlib.util
import io
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "run_blind_beta.py"
SPEC = importlib.util.spec_from_file_location("run_blind_beta", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def csv_rows(text):
    return list(csv.DictReader(io.StringIO(text)))


class BlindBetaTests(unittest.TestCase):
    def make_cases(self, count=20):
        return {
            "study_id": "test-study",
            "cases": [
                {
                    "participant_id": f"P{index // 2 + 1:03d}",
                    "trial_id": f"T{index + 1:03d}",
                    "task_context": "email",
                    "baseline_output": f"Baseline {index}",
                    "write_like_me_output": f"Free {index}",
                }
                for index in range(count)
            ],
        }

    def test_prepare_balances_blind_positions(self):
        pack, key = MODULE.prepare(self.make_cases(), seed=42)
        self.assertEqual(len(pack["trials"]), 20)
        self.assertEqual(len(key["trials"]), 20)
        free_as_a = sum(item["system_a"] == "write_like_me" for item in key["trials"])
        self.assertEqual(free_as_a, 10)
        for participant_number in range(1, 11):
            participant = f"P{participant_number:03d}"
            assignments = [item for item in key["trials"] if item["participant_id"] == participant]
            self.assertEqual(sum(item["system_a"] == "write_like_me" for item in assignments), 1)
        self.assertNotIn("write_like_me", str(pack).lower())

    def test_identical_outputs_are_rejected(self):
        payload = self.make_cases(1)
        payload["cases"][0]["write_like_me_output"] = payload["cases"][0]["baseline_output"]
        self.assertTrue(any("identical" in error for error in MODULE.validate_cases(payload)))

    def test_score_unblinds_preference_and_keeps_safety_separate(self):
        _, key = MODULE.prepare(self.make_cases(2), seed=7)
        ballot_lines = [
            "participant_id,trial_id,sounds_like_me,preserves_meaning,less_editing,overall_preference,edit_burden_a,edit_burden_b,critical_failure_a,critical_failure_b,rejected_reason,notes"
        ]
        for mapping in key["trials"]:
            free_label = "A" if mapping["system_a"] == "write_like_me" else "B"
            burden_a, burden_b = (1, 3) if free_label == "A" else (3, 1)
            critical_a, critical_b = ("BIOGRAPHY", "NONE") if free_label == "A" else ("NONE", "BIOGRAPHY")
            ballot_lines.append(
                f"{mapping['participant_id']},{mapping['trial_id']},{free_label},{free_label},{free_label},{free_label},"
                f"{burden_a},{burden_b},{critical_a},{critical_b},baseline felt generic,"
            )
        participant_csv = """participant_id,completed_onboarding,minutes_to_first_rewrite,reused_file_fresh_chat,reused_without_help,understands_starter,understands_unknown,would_use_again,notes
P001,YES,2.5,YES,YES,YES,YES,YES,
"""
        result = MODULE.score(key, csv_rows("\n".join(ballot_lines)), csv_rows(participant_csv))
        self.assertEqual(result["primary_kpi"]["counts"]["write_like_me"], 2)
        self.assertEqual(result["editing_burden"]["write_like_me"]["median"], 1.0)
        self.assertEqual(result["guardrails"]["critical_failure_counts"]["write_like_me"], 2)
        self.assertEqual(result["decision"], "blocked_safety_failure")

    def test_directional_gate_requires_minimum_sample(self):
        _, key = MODULE.prepare(self.make_cases(2), seed=3)
        ballot_lines = [
            "participant_id,trial_id,sounds_like_me,preserves_meaning,less_editing,overall_preference,edit_burden_a,edit_burden_b,critical_failure_a,critical_failure_b,rejected_reason,notes"
        ]
        for mapping in key["trials"]:
            free_label = "A" if mapping["system_a"] == "write_like_me" else "B"
            ballot_lines.append(
                f"{mapping['participant_id']},{mapping['trial_id']},{free_label},{free_label},{free_label},{free_label},1,2,NONE,NONE,,"
            )
        participant_csv = """participant_id,completed_onboarding,minutes_to_first_rewrite,reused_file_fresh_chat,reused_without_help,understands_starter,understands_unknown,would_use_again,notes
P001,YES,3,YES,YES,YES,YES,YES,
"""
        result = MODULE.score(key, csv_rows("\n".join(ballot_lines)), csv_rows(participant_csv))
        self.assertEqual(result["decision"], "collect_more_data")

    def test_complete_sample_can_report_directional_product_advantage(self):
        _, key = MODULE.prepare(self.make_cases(20), seed=11)
        ballot_lines = [
            "participant_id,trial_id,sounds_like_me,preserves_meaning,less_editing,overall_preference,edit_burden_a,edit_burden_b,critical_failure_a,critical_failure_b,rejected_reason,notes"
        ]
        for index, mapping in enumerate(key["trials"]):
            product_label = "A" if mapping["system_a"] == "write_like_me" else "B"
            baseline_label = "B" if product_label == "A" else "A"
            overall = product_label if index < 12 else baseline_label
            burden_a, burden_b = (1, 2) if product_label == "A" else (2, 1)
            ballot_lines.append(
                f"{mapping['participant_id']},{mapping['trial_id']},{product_label},{product_label},{product_label},{overall},"
                f"{burden_a},{burden_b},NONE,NONE,,"
            )
        participant_lines = [
            "participant_id,completed_onboarding,minutes_to_first_rewrite,reused_file_fresh_chat,reused_without_help,understands_starter,understands_unknown,would_use_again,notes"
        ]
        for index in range(1, 11):
            participant_lines.append(f"P{index:03d},YES,3,YES,YES,YES,YES,YES,")
        result = MODULE.score(key, csv_rows("\n".join(ballot_lines)), csv_rows("\n".join(participant_lines)))
        self.assertEqual(result["decision"], "directional_product_advantage")
        self.assertEqual(result["primary_kpi"]["write_like_me_rate_excluding_ties"], 0.6)
        self.assertEqual(result["release_signal"], "evidence_supports_wider_release")


if __name__ == "__main__":
    unittest.main()
