#!/usr/bin/env python3
"""Validate scenario coverage and grade recorded end-to-end skill responses.

The script has no model or network dependency. A platform run records one
response per scenario plus explicit criterion judgements. This script enforces
the rubric and deterministic safety checks without allowing an average score to
hide a critical failure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_scenarios(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    scenarios = payload.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        return ["scenarios must be a non-empty list"]
    seen: set[str] = set()
    for index, scenario in enumerate(scenarios, start=1):
        if not isinstance(scenario, dict):
            errors.append(f"scenario {index} is not an object")
            continue
        scenario_id = scenario.get("id")
        if not isinstance(scenario_id, str) or not scenario_id:
            errors.append(f"scenario {index} has no id")
            continue
        if scenario_id in seen:
            errors.append(f"duplicate scenario id: {scenario_id}")
        seen.add(scenario_id)
        for field in ("request", "must", "must_not", "deterministic"):
            if field not in scenario:
                errors.append(f"{scenario_id}: missing {field}")
        deterministic = scenario.get("deterministic", {})
        for field in ("required_output_tokens", "forbidden_output_tokens", "forbid_long_dash"):
            if field not in deterministic:
                errors.append(f"{scenario_id}: deterministic check missing {field}")
    return errors


def grade_scenario(scenario: dict[str, Any], response: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    output = response.get("output")
    criteria = response.get("criteria")
    if not isinstance(output, str):
        return ["missing string output"]
    if not isinstance(criteria, dict):
        return ["missing criteria object"]
    primary_output = response.get("primary_output", output)
    if not isinstance(primary_output, str):
        return ["primary_output must be a string when supplied"]

    for criterion in scenario["must"]:
        if criteria.get(criterion) is not True:
            failures.append(f"required criterion did not pass: {criterion}")
    for criterion in scenario["must_not"]:
        if criteria.get(criterion) is not False:
            failures.append(f"prohibited behaviour was not explicitly cleared: {criterion}")

    lower = primary_output.lower()
    checks = scenario["deterministic"]
    for token in checks["required_output_tokens"]:
        if token.lower() not in lower:
            failures.append(f"required output token missing: {token}")
    for token in checks["forbidden_output_tokens"]:
        if token.lower() in lower:
            failures.append(f"forbidden output token found: {token}")
    if checks["forbid_long_dash"] and has_disallowed_long_dash(output):
        failures.append("long dash found")
    return failures


def has_disallowed_long_dash(text: str) -> bool:
    without_quotes = ""
    in_quote = False
    for char in text:
        if char in "\"'“”‘’":
            in_quote = not in_quote
            without_quotes += " "
            continue
        without_quotes += " " if in_quote else char
    for match in re.finditer(r"[—–]", without_quotes):
        start = max(0, match.start() - 16)
        end = min(len(without_quotes), match.end() + 16)
        window = without_quotes[start:end]
        if re.search(r"\d\s*[—–]\s*\d", window):
            continue
        return True
    return False


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenarios", default=str(skill_root / "evaluations" / "scenarios.json"))
    parser.add_argument("--responses", help="JSON file containing recorded platform responses and criterion judgements.")
    parser.add_argument("--result", help="Optional JSON result path.")
    parser.add_argument("--allow-partial", action="store_true", help="Grade only recorded scenarios and leave the rest pending.")
    args = parser.parse_args()

    scenarios_payload = load_json(Path(args.scenarios))
    schema_errors = validate_scenarios(scenarios_payload)
    if schema_errors:
        for error in schema_errors:
            print(f"SCHEMA FAIL: {error}")
        return 1

    scenarios = scenarios_payload["scenarios"]
    if not args.responses:
        print(f"Scenario contract valid: {len(scenarios)} scenarios")
        print("No responses supplied; model-assisted end-to-end grading remains pending.")
        return 0

    response_payload = load_json(Path(args.responses))
    raw_responses = response_payload.get("responses", response_payload)
    if not isinstance(raw_responses, list):
        print("RESPONSE FAIL: responses must be a list")
        return 1
    responses = {item.get("scenario_id"): item for item in raw_responses if isinstance(item, dict)}

    results: list[dict[str, Any]] = []
    failed = False
    pending = False
    for scenario in scenarios:
        scenario_id = scenario["id"]
        response = responses.get(scenario_id)
        if response is None and args.allow_partial:
            pending = True
            results.append({"scenario_id": scenario_id, "passed": None, "failures": [], "status": "pending"})
            print(f"PENDING: {scenario_id}")
            continue
        failures = ["missing recorded response"] if response is None else grade_scenario(scenario, response)
        passed = not failures
        failed = failed or not passed
        results.append({"scenario_id": scenario_id, "passed": passed, "failures": failures})
        print(f"{'PASS' if passed else 'FAIL'}: {scenario_id}")
        for failure in failures:
            print(f"  - {failure}")

    result_payload = {
        "scenario_version": scenarios_payload.get("version"),
        "passed": None if pending else not failed,
        "results": results,
        "criteria_kind": "self_reported_criteria_plus_deterministic_checks",
    }
    if args.result:
        Path(args.result).write_text(json.dumps(result_payload, indent=2) + "\n", encoding="utf-8")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
