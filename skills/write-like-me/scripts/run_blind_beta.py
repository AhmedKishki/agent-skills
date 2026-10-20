#!/usr/bin/env python3
"""Prepare and score a blinded Write Like Me versus strong-prompt beta.

The script has no model or network dependency. It keeps the system identity in
a separate answer key, validates human ballots, and reports critical safety
failures separately from preference scores.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import secrets
import statistics
import sys
from pathlib import Path
from typing import Any


CHOICES = {"A", "B", "TIE"}
BURDEN_VALUES = {0, 1, 2, 3, 4}
NO_FAILURE_VALUES = {"", "NONE", "NO", "N/A"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def validate_cases(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    cases = payload.get("cases")
    if not isinstance(payload.get("study_id"), str) or not payload.get("study_id", "").strip():
        errors.append("study_id must be a non-empty string")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"]

    trial_ids: set[str] = set()
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"case {index} is not an object")
            continue
        for field in ("participant_id", "trial_id", "task_context", "baseline_output", "write_like_me_output"):
            if not isinstance(case.get(field), str) or not case.get(field, "").strip():
                errors.append(f"case {index}: {field} must be a non-empty string")
        trial_id = case.get("trial_id")
        if isinstance(trial_id, str):
            if trial_id in trial_ids:
                errors.append(f"duplicate trial_id: {trial_id}")
            trial_ids.add(trial_id)
        if case.get("baseline_output", "").strip() == case.get("write_like_me_output", "").strip():
            errors.append(f"{trial_id or f'case {index}'}: outputs are identical")
    return errors


def prepare(payload: dict[str, Any], seed: int) -> tuple[dict[str, Any], dict[str, Any]]:
    errors = validate_cases(payload)
    if errors:
        raise ValueError("\n".join(errors))

    rng = random.Random(seed)
    cases = list(payload["cases"])
    indices_by_participant: dict[str, list[int]] = {}
    for index, case in enumerate(cases):
        indices_by_participant.setdefault(case["participant_id"], []).append(index)
    free_as_a: set[int] = set()
    for indices in indices_by_participant.values():
        rng.shuffle(indices)
        free_first = bool(rng.getrandbits(1))
        for position, index in enumerate(indices):
            if (position % 2 == 0) == free_first:
                free_as_a.add(index)

    blinded_trials: list[dict[str, Any]] = []
    key_trials: list[dict[str, Any]] = []
    for index, case in enumerate(cases):
        if index in free_as_a:
            output_a = case["write_like_me_output"]
            output_b = case["baseline_output"]
            system_a = "write_like_me"
            system_b = "strong_plain_prompt"
        else:
            output_a = case["baseline_output"]
            output_b = case["write_like_me_output"]
            system_a = "strong_plain_prompt"
            system_b = "write_like_me"
        blinded_trials.append({
            "participant_id": case["participant_id"],
            "trial_id": case["trial_id"],
            "task_context": case["task_context"],
            "output_a": output_a,
            "output_b": output_b,
        })
        key_trials.append({
            "participant_id": case["participant_id"],
            "trial_id": case["trial_id"],
            "system_a": system_a,
            "system_b": system_b,
        })

    pack = {
        "study_id": payload["study_id"],
        "instructions": "Judge A and B without guessing which system produced them. Complete one ballot row per trial.",
        "trials": blinded_trials,
    }
    key = {
        "study_id": payload["study_id"],
        "seed": seed,
        "trials": key_trials,
    }
    return pack, key


def normalize_choice(value: str) -> str:
    return value.strip().upper()


def parse_burden(value: str, field: str, row_number: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"ballot row {row_number}: {field} must be 0, 1, 2, 3, or 4") from exc
    if parsed not in BURDEN_VALUES:
        raise ValueError(f"ballot row {row_number}: {field} must be 0, 1, 2, 3, or 4")
    return parsed


def has_critical_failure(value: str) -> bool:
    return value.strip().upper() not in NO_FAILURE_VALUES


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def wilson_interval(successes: int, total: int, z: float = 1.96) -> tuple[float | None, float | None]:
    if total == 0:
        return None, None
    proportion = successes / total
    denominator = 1 + (z * z / total)
    centre = (proportion + z * z / (2 * total)) / denominator
    margin = z * math.sqrt((proportion * (1 - proportion) + z * z / (4 * total)) / total) / denominator
    return max(0.0, centre - margin), min(1.0, centre + margin)


def mapped_choice(choice: str, mapping: dict[str, str]) -> str:
    if choice == "TIE":
        return "tie"
    return mapping[f"system_{choice.lower()}"]


def rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def median(values: list[int]) -> float | None:
    return statistics.median(values) if values else None


def score(answer_key: dict[str, Any], ballot_rows: list[dict[str, str]], participant_rows: list[dict[str, str]]) -> dict[str, Any]:
    key_by_trial = {trial["trial_id"]: trial for trial in answer_key.get("trials", [])}
    if not key_by_trial:
        raise ValueError("answer key has no trials")

    required_ballot_fields = {
        "participant_id", "trial_id", "sounds_like_me", "preserves_meaning", "less_editing",
        "overall_preference", "edit_burden_a", "edit_burden_b", "critical_failure_a", "critical_failure_b",
    }
    choice_counts = {
        metric: {"write_like_me": 0, "strong_plain_prompt": 0, "tie": 0}
        for metric in ("sounds_like_me", "preserves_meaning", "less_editing", "overall_preference")
    }
    burdens = {"write_like_me": [], "strong_plain_prompt": []}
    critical_failures = {"write_like_me": [], "strong_plain_prompt": []}
    seen_trials: set[str] = set()
    participants: set[str] = set()

    for row_number, row in enumerate(ballot_rows, start=2):
        missing = required_ballot_fields - set(row)
        if missing:
            raise ValueError(f"ballot CSV missing columns: {', '.join(sorted(missing))}")
        trial_id = row["trial_id"].strip()
        participant_id = row["participant_id"].strip()
        if trial_id not in key_by_trial:
            raise ValueError(f"ballot row {row_number}: unknown trial_id {trial_id}")
        if trial_id in seen_trials:
            raise ValueError(f"ballot row {row_number}: duplicate trial_id {trial_id}")
        mapping = key_by_trial[trial_id]
        if participant_id != mapping["participant_id"]:
            raise ValueError(f"ballot row {row_number}: participant_id does not match answer key")
        seen_trials.add(trial_id)
        participants.add(participant_id)

        for metric in choice_counts:
            choice = normalize_choice(row[metric])
            if choice not in CHOICES:
                raise ValueError(f"ballot row {row_number}: {metric} must be A, B, or TIE")
            choice_counts[metric][mapped_choice(choice, mapping)] += 1

        burden_a = parse_burden(row["edit_burden_a"], "edit_burden_a", row_number)
        burden_b = parse_burden(row["edit_burden_b"], "edit_burden_b", row_number)
        burdens[mapping["system_a"]].append(burden_a)
        burdens[mapping["system_b"]].append(burden_b)

        for label in ("a", "b"):
            field = f"critical_failure_{label}"
            value = row[field].strip()
            if has_critical_failure(value):
                critical_failures[mapping[f"system_{label}"]].append({
                    "participant_id": participant_id,
                    "trial_id": trial_id,
                    "blind_label": label.upper(),
                    "failure": value,
                })

    if seen_trials != set(key_by_trial):
        missing_trials = sorted(set(key_by_trial) - seen_trials)
        raise ValueError(f"ballots missing trials: {', '.join(missing_trials)}")

    participant_required = {
        "participant_id", "completed_onboarding", "minutes_to_first_rewrite", "reused_file_fresh_chat",
        "reused_without_help", "understands_starter", "understands_unknown", "would_use_again",
    }
    participant_seen: set[str] = set()
    binary_totals = {
        "completed_onboarding": [0, 0],
        "reused_file_fresh_chat": [0, 0],
        "reused_without_help": [0, 0],
        "understands_starter": [0, 0],
        "understands_unknown": [0, 0],
        "would_use_again": [0, 0],
    }
    time_to_first_rewrite: list[float] = []
    for row_number, row in enumerate(participant_rows, start=2):
        missing = participant_required - set(row)
        if missing:
            raise ValueError(f"participant CSV missing columns: {', '.join(sorted(missing))}")
        participant_id = row["participant_id"].strip()
        if participant_id in participant_seen:
            raise ValueError(f"participant row {row_number}: duplicate participant_id {participant_id}")
        if participant_id not in participants:
            raise ValueError(f"participant row {row_number}: participant has no ballot")
        participant_seen.add(participant_id)
        try:
            minutes = float(row["minutes_to_first_rewrite"])
        except ValueError as exc:
            raise ValueError(f"participant row {row_number}: minutes_to_first_rewrite must be numeric") from exc
        if minutes < 0:
            raise ValueError(f"participant row {row_number}: minutes_to_first_rewrite cannot be negative")
        time_to_first_rewrite.append(minutes)
        for field, counts in binary_totals.items():
            value = row[field].strip().upper()
            if value not in {"YES", "NO", "N/A"}:
                raise ValueError(f"participant row {row_number}: {field} must be YES, NO, or N/A")
            if value != "N/A":
                counts[1] += 1
                if value == "YES":
                    counts[0] += 1
    if participant_seen != participants:
        missing_participants = sorted(participants - participant_seen)
        raise ValueError(f"participant outcomes missing: {', '.join(missing_participants)}")

    overall = choice_counts["overall_preference"]
    non_ties = overall["write_like_me"] + overall["strong_plain_prompt"]
    write_like_me_rate = rate(overall["write_like_me"], non_ties)
    ci_low, ci_high = wilson_interval(overall["write_like_me"], non_ties)
    write_like_me_critical = len(critical_failures["write_like_me"])
    completed_writers = len(participants)
    completed_trials = len(ballot_rows)
    reuse_yes, reuse_total = binary_totals["reused_without_help"]
    starter_yes, starter_total = binary_totals["understands_starter"]
    unknown_yes, unknown_total = binary_totals["understands_unknown"]

    if write_like_me_critical:
        decision = "blocked_safety_failure"
    elif completed_writers < 10 or completed_trials < 20:
        decision = "collect_more_data"
    elif write_like_me_rate is not None and write_like_me_rate >= 0.60:
        decision = "directional_product_advantage"
    elif write_like_me_rate is not None and write_like_me_rate >= 0.45:
        decision = "tie_or_positioning_shift"
    else:
        decision = "baseline_advantage"

    reuse_rate = rate(reuse_yes, reuse_total)
    comprehension_rate = rate(starter_yes + unknown_yes, starter_total + unknown_total)
    release_signal = (
        "evidence_supports_wider_release"
        if decision == "directional_product_advantage" and (reuse_rate is None or reuse_rate >= 0.70)
        else "wider_release_not_yet_supported_by_this_beta"
    )

    metric_summary: dict[str, Any] = {}
    for metric, counts in choice_counts.items():
        metric_non_ties = counts["write_like_me"] + counts["strong_plain_prompt"]
        metric_summary[metric] = {
            **counts,
            "write_like_me_rate_excluding_ties": rate(counts["write_like_me"], metric_non_ties),
        }

    return {
        "study_id": answer_key.get("study_id"),
        "decision": decision,
        "release_signal": release_signal,
        "interpretation": "Directional private-beta evidence only; do not publish a percentage claim from this result.",
        "sample": {"writers": completed_writers, "trials": completed_trials, "non_tied_overall_choices": non_ties},
        "primary_kpi": {
            "name": "blind overall preference for Write Like Me versus strong plain prompt",
            "write_like_me_rate_excluding_ties": write_like_me_rate,
            "wilson_95_percent_interval": [ci_low, ci_high],
            "counts": overall,
        },
        "comparison_metrics": metric_summary,
        "editing_burden": {
            system: {"median": median(values), "mean": statistics.fmean(values) if values else None, "n": len(values)}
            for system, values in burdens.items()
        },
        "guardrails": {
            "critical_failure_counts": {system: len(items) for system, items in critical_failures.items()},
            "critical_failures": critical_failures,
        },
        "participant_outcomes": {
            field: {"yes": values[0], "eligible": values[1], "rate": rate(values[0], values[1])}
            for field, values in binary_totals.items()
        } | {
            "median_minutes_to_first_rewrite": statistics.median(time_to_first_rewrite) if time_to_first_rewrite else None,
            "reuse_without_help_rate": reuse_rate,
            "starter_and_unknown_comprehension_rate": comprehension_rate,
        },
        "pre_registered_directional_gate": {
            "minimum_writers": 10,
            "minimum_trials": 20,
            "zero_write_like_me_critical_failures": write_like_me_critical == 0,
            "product_preference_threshold_excluding_ties": 0.60,
            "reuse_without_help_target": 0.70,
            "starter_and_unknown_comprehension_target": 0.80,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare_parser = subparsers.add_parser("prepare", help="Create a blinded review pack and separate answer key.")
    prepare_parser.add_argument("--cases", required=True, help="JSON containing paired system outputs.")
    prepare_parser.add_argument("--pack", required=True, help="Output path for the blinded review pack.")
    prepare_parser.add_argument("--key", required=True, help="Output path for the private answer key.")
    prepare_parser.add_argument("--seed", type=int, help="Optional reproducible randomization seed.")

    score_parser = subparsers.add_parser("score", help="Unblind completed ballots and summarize the beta.")
    score_parser.add_argument("--key", required=True, help="Private answer-key JSON from prepare.")
    score_parser.add_argument("--ballots", required=True, help="Completed trial-level ballot CSV.")
    score_parser.add_argument("--participants", required=True, help="Completed participant-level outcome CSV.")
    score_parser.add_argument("--result", required=True, help="Output path for the scored JSON result.")

    args = parser.parse_args()
    try:
        if args.command == "prepare":
            seed = args.seed if args.seed is not None else secrets.randbelow(2**31)
            pack, key = prepare(load_json(Path(args.cases)), seed)
            write_json(Path(args.pack), pack)
            write_json(Path(args.key), key)
            print(f"Prepared {len(pack['trials'])} blinded trials with seed {seed}.")
            print(f"Reviewer pack: {args.pack}")
            print(f"Private answer key: {args.key}")
            return 0
        result = score(load_json(Path(args.key)), read_csv(Path(args.ballots)), read_csv(Path(args.participants)))
        write_json(Path(args.result), result)
        print(f"Decision: {result['decision']}")
        print(f"Writers: {result['sample']['writers']}; trials: {result['sample']['trials']}")
        print(f"Result: {args.result}")
        return 1 if result["decision"] == "blocked_safety_failure" else 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"BETA FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
