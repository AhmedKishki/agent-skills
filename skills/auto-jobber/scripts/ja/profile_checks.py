"""Validate retained candidate data without inferring qualifications or character."""
from .blocks import read_blocks
from .common import indexed, require
from .html_safety import visible_text

CATEGORIES = ("study", "work", "experience", "certificates", "expertise", "languages",
              "projects", "online_presence")


def validate_details(profile):
    qualifications = profile.get("qualifications", {})
    require(isinstance(qualifications, dict), "qualifications must be an object")
    for category in CATEGORIES:
        for entry in indexed(qualifications.get(category, []), category).values():
            require(isinstance(entry.get("title"), str) and entry["title"].strip(),
                    f"{category} entries need a title")
            require(isinstance(entry.get("source"), str) and entry["source"].strip(),
                    f"{category} entries need a source")
            details = entry.get("details", [])
            require(isinstance(details, list) and all(isinstance(x, str) for x in details),
                    "Qualification details must be a list of source-backed strings")
    interests = profile.get("interests", [])
    require(isinstance(interests, list) and all(isinstance(x, str) for x in interests),
            "interests must be a list of user-supplied strings")
    voice = profile.get("voice", {})
    require(isinstance(voice, dict), "voice must be an object")
    for key in ("tone_preferences", "character_notes", "writing_preferences", "avoid", "samples"):
        require(isinstance(voice.get(key, []), list), f"voice.{key} must be a list")
        if key != "samples":
            require(all(isinstance(x, str) for x in voice.get(key, [])), f"voice.{key} must contain strings")


def validate_profile(profile, html):
    require(profile.get("schema_version") == 1, "Unsupported qualifications schema")
    person, policy = profile["person"], profile["policy"]
    require(isinstance(person.get("name"), str) and person["name"].strip(), "Add your name")
    require(person["name"] in visible_text(html), "Baseline CV must contain your name")
    validate_details(profile)
    evidence = indexed(profile["evidence"], "candidate evidence")
    require(evidence, "Add source-backed qualifications before sealing")
    for item in evidence.values():
        require(isinstance(item.get("text"), str) and item["text"].strip(), "Evidence needs text")
        require(isinstance(item.get("source"), str) and item["source"].strip(), "Evidence needs source")
        require(type(item.get("verified")) is bool, "Evidence needs a verified boolean")
    blocks = read_blocks(html)
    require(set(blocks) == set(profile["editable_blocks"]), "CV markers and editable_blocks differ")
    for key, block in profile["editable_blocks"].items():
        require(block.get("kind") in {"summary", "bullet", "skills"}, f"Invalid block kind: {key}")
        refs = block.get("evidence_ids", [])
        require(refs and all(ref in evidence and evidence[ref]["verified"] for ref in refs),
                f"Block {key} needs verified candidate evidence")
    for key in ("max_changed_blocks", "cv_max_pages", "letter_max_pages", "research_max_age_days"):
        require(type(policy[key]) is int and policy[key] > 0, f"Invalid policy: {key}")
    ratio = policy["max_changed_word_ratio"]
    require(type(ratio) in {int, float} and 0 <= ratio <= 1, "Invalid change ratio")
    require(policy["paper"] in {"A4", "Letter"}, "Paper must be A4 or Letter")
    return evidence
