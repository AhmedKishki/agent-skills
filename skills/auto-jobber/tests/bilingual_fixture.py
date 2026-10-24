"""Source-checked fictional German translations for workflow/render tests."""
from pathlib import Path

from support import BEFORE, fixture
from ja.applications import new_application
from ja.common import read_json, write_json, write_text
from ja.languages import localize_labels
from ja.profile import seal
from ja.voice import capture_wording

GERMAN = "Ich entwickle zuverlässige C-Software für eingebettete Geräte mit dokumentierten Tests."


def german_fixture(root):
    workspace, english = fixture(root)
    source = localize_labels((workspace / "cv.html").read_text(), "de")
    translations = {
        BEFORE: GERMAN,
        "Software Engineer": "Softwareentwickler",
        "Developed C software for embedded devices and documented test procedures.":
            "Entwickelte C-Software für eingebettete Geräte und dokumentierte Testverfahren.",
        "Investigated device failures with colleagues and maintained clear implementation notes.":
            "Untersuchte Gerätefehler mit Kollegen und dokumentierte die Umsetzung.",
        "Reviewed interfaces and contributed evidence to design decisions.":
            "Prüfte Schnittstellen und lieferte Grundlagen für Entwurfsentscheidungen."}
    for original, translated in translations.items():
        source = source.replace(original, translated)
    master = workspace / "cv.de.html"
    write_text(master, source)
    seal(workspace, "de", master)
    posting = Path(root) / "stelle.txt"
    write_text(posting, "Northstar Example sucht Softwareentwickler für eingebettete Systeme. "
                        "Erforderlich sind Erfahrungen mit C und dokumentierten Tests.")
    app = Path(new_application(workspace, job_file=posting, language="de")["application"])
    research = read_json(app / "research.json")
    research.update(status="unavailable", search_log=["Testfall: Unternehmensquellen nicht verfügbar."])
    write_json(app / "research.json", research)
    plan = read_json(app / "plan.json")
    plan["job"].update(company="Northstar Example", role="Softwareentwickler")
    plan["requirements"] = [{"id": "r-c", "text": "Erfahrung mit C", "importance": "required",
                              "status": "supported", "evidence_ids": ["e-summary"]}]
    plan["edits"] = [{"block_id": "summary", "before": GERMAN,
        "after": GERMAN.replace("zuverlässige", "getestete"), "evidence_ids": ["e-summary"],
        "requirement_ids": ["r-c"], "reason": "Belegte Testerfahrung hervorheben."}]
    plan["letter"].update(greeting="Sehr geehrtes Team,", closing="Mit freundlichen Grüßen",
        wording_quotes=["nah an der Hardware"], paragraphs=[
            {"sentences": [{"kind": "candidate", "text": GERMAN,
                             "evidence_ids": ["e-summary"], "company_fact_ids": []}]},
            {"sentences": [{"kind": "intent", "text": "Ich arbeite gern nah an der Hardware.",
                             "evidence_ids": [], "company_fact_ids": []}]}])
    write_json(app / "plan.json", plan)
    words = Path(root) / "de-user-words.txt"
    write_text(words, "Ich arbeite gern nah an der Hardware.")
    capture_wording(app, words, "Fiktive Originalworte des Bewerbers für diesen Test", language="de")
    return workspace, app
