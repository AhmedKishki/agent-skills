"""Structural and minimal-edit gates for an agent-authored application plan."""
from datetime import date

from .blocks import apply_edits, changed_words
from .claims import check_numbers, evidence_refs, validate_sentence
from .common import indexed, require
from .html_safety import visible_text


def validate_plan(plan, profile, research, baseline):
    require(plan.get("schema_version") == 1, "Unsupported plan schema")
    evidence = indexed(profile["evidence"], "candidate evidence")
    facts = indexed(research["facts"], "company facts")
    job, policy = plan["job"], profile["policy"]
    require(all(isinstance(job.get(key), str) and job[key].strip()
                for key in ("company", "role", "language")), "Add company, role and language")
    require(job["language"] in {"en", "de"}, "Offer language must be English or German")
    requirements = indexed(plan["requirements"], "requirements")
    require(requirements, "Extract the vacancy requirements before drafting")
    for item in requirements.values():
        require(item.get("status") in {"supported", "partial", "gap", "unknown"},
                "Requirement status must be supported, partial, gap or unknown")
        require(item.get("importance") in {"required", "preferred"}, "Invalid requirement importance")
        require(isinstance(item.get("text"), str) and item["text"].strip(), "Empty requirement")
        evidence_refs(item.get("evidence_ids", []), evidence, item["id"],
                      needed=item["status"] in {"supported", "partial"})
    edits = plan["edits"]
    require(isinstance(edits, list), "edits must be a list")
    require(len(edits) <= policy["max_changed_blocks"], "CV edit-block budget exceeded")
    changed = 0
    for edit in edits:
        key = edit["block_id"]
        require(key in profile["editable_blocks"], f"Block is not approved for editing: {key}")
        support = evidence_refs(edit.get("evidence_ids", []), evidence, key, needed=True)
        require(edit.get("reason", "").strip(), f"Explain why {key} needs changing")
        refs = edit.get("requirement_ids", [])
        require(refs and all(ref in requirements for ref in refs), "Edit needs valid requirement IDs")
        check_numbers(edit["after"], support, key)
        changed += changed_words(edit["before"], edit["after"])
    tailored = apply_edits(baseline, edits)
    ratio = changed / max(1, len(visible_text(baseline).split()))
    require(ratio <= policy["max_changed_word_ratio"],
            f"CV word-change budget exceeded: {ratio:.1%}; revise, do not silently raise the limit")
    letter = plan["letter"]
    require(date.fromisoformat(letter["date"]) <= date.today(), "Letter date is in the future")
    require(all(isinstance(letter.get(key), str) and letter[key].strip()
                for key in ("greeting", "closing")), "Letter needs greeting and closing")
    require(isinstance(letter["paragraphs"], list) and 2 <= len(letter["paragraphs"]) <= 6,
            "Letter needs 2–6 paragraphs")
    warnings, texts = [], []
    has_candidate = False
    for paragraph in letter["paragraphs"]:
        sentences = paragraph["sentences"]
        require(isinstance(sentences, list) and sentences, "Empty letter paragraph")
        for sentence in sentences:
            if validate_sentence(sentence, evidence, facts):
                warnings.append("Review bridge sentence: evidence references do not prove entailment")
            has_candidate |= sentence["kind"] in {"candidate", "bridge"}
            texts.append(sentence["text"])
    require(has_candidate, "Letter must contain candidate-backed evidence")
    require(len(" ".join(texts).split()) <= 450, "Letter exceeds the 450-word drafting ceiling")
    return tailored, {"changed_blocks": len(edits), "changed_word_ratio": ratio}, warnings
