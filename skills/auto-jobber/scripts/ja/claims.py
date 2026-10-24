"""Check evidence references and literal numbers, not semantic truth."""
import re

from .common import require


def evidence_refs(ids, evidence, label, needed=False):
    require(isinstance(ids, list) and all(isinstance(key, str) for key in ids),
            f"{label}: evidence references must be a list of IDs")
    require(len(ids) == len(set(ids)), f"{label}: duplicate evidence references")
    require(not needed or ids, f"{label}: evidence is required")
    for key in ids:
        require(key in evidence, f"{label}: unknown evidence {key}")
        require(evidence[key].get("verified") is True, f"{label}: unverified evidence {key}")
    return "\n".join(evidence[key]["text"] for key in ids)


def company_refs(ids, facts, label, needed=False):
    require(isinstance(ids, list) and all(isinstance(key, str) for key in ids),
            f"{label}: company references must be a list of IDs")
    require(not needed or ids, f"{label}: company evidence is required")
    require(all(key in facts for key in ids), f"{label}: unknown company fact")
    # Only source quotations, not agent-authored summaries, can back numbers.
    return "\n".join(facts[key]["quote"] for key in ids)


def check_numbers(text, support, label):
    numbers = lambda value: set(re.findall(r"\d+(?:[.,]\d+)*", value))
    missing = numbers(text) - numbers(support)
    require(not missing, f"{label}: unsupported numeric literals {sorted(missing)}")


def validate_sentence(sentence, evidence, facts):
    kind, text = sentence["kind"], sentence["text"]
    require(isinstance(text, str) and text.strip(), "Letter sentences cannot be empty")
    require(kind in {"candidate", "company", "bridge", "intent"}, "Invalid sentence kind")
    candidate = evidence_refs(sentence.get("evidence_ids", []), evidence, "letter",
                              needed=kind in {"candidate", "bridge"})
    company = company_refs(sentence.get("company_fact_ids", []), facts, "letter",
                           needed=kind in {"company", "bridge"})
    if kind == "candidate":
        require(not sentence.get("company_fact_ids"), "Candidate claims cannot borrow employer facts")
    if kind == "company":
        require(not sentence.get("evidence_ids"), "Keep employer and candidate claims separate")
    if kind == "intent":
        require(not candidate and not company, "Intent sentences must not hide factual claims")
    check_numbers(text, candidate + "\n" + company, "letter")
    return kind == "bridge"
