import importlib.util
import json
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "evaluate_scenarios.py"
SPEC = importlib.util.spec_from_file_location("evaluate_scenarios", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class ScenarioContractTests(unittest.TestCase):
    def test_scenario_schema_is_executable(self):
        payload = json.loads((SKILL_ROOT / "evaluations" / "scenarios.json").read_text(encoding="utf-8"))
        self.assertRegex(
            payload["version"],
            r"^1\.0\.0-rc\.7\+codex\.[0-9]{14}$",
        )
        self.assertEqual(MODULE.validate_scenarios(payload), [])
        self.assertGreaterEqual(len(payload["scenarios"]), 18)

    def test_language_variety_and_paste_ready_scenarios_are_present(self):
        payload = json.loads((SKILL_ROOT / "evaluations" / "scenarios.json").read_text(encoding="utf-8"))
        scenario_ids = {scenario["id"] for scenario in payload["scenarios"]}
        self.assertTrue(
            {
                "preserve-evidenced-indian-english",
                "do-not-perform-australian-dialect",
                "paste-ready-personal-reply",
            }.issubset(scenario_ids)
        )

    def test_authorial_decision_boundaries_are_present(self):
        payload = json.loads((SKILL_ROOT / "evaluations" / "scenarios.json").read_text(encoding="utf-8"))
        scenario_ids = {scenario["id"] for scenario in payload["scenarios"]}
        self.assertTrue(
            {
                "deep-authorial-pass-ai-first",
                "ordinary-email-no-structural-lab",
                "detector-evasion-reframe",
            }.issubset(scenario_ids)
        )

    def test_critical_checks_cannot_be_averaged_away(self):
        scenario = {
            "must": ["preserve claims"],
            "must_not": ["invent a meeting"],
            "deterministic": {
                "required_output_tokens": ["not approved"],
                "forbidden_output_tokens": ["client told me"],
                "forbid_long_dash": True,
            },
        }
        response = {
            "output": "It is not approved — a client told me why.",
            "criteria": {"preserve claims": True, "invent a meeting": False},
        }
        failures = MODULE.grade_scenario(scenario, response)
        self.assertTrue(any("forbidden output token" in failure for failure in failures))
        self.assertIn("long dash found", failures)


if __name__ == "__main__":
    unittest.main()
