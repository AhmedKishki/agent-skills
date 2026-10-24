"""Render escaped prose through the matching upstream-derived document layout."""
from html import escape
from string import Template
from datetime import date

from .common import ASSETS
from .html_safety import standalone


def cover_letter(plan, person, css):
    letter, job = plan["letter"], plan["job"]
    paragraphs = "\n".join(
        "<p>" + escape(" ".join(item["text"] for item in paragraph["sentences"])) + "</p>"
        for paragraph in letter["paragraphs"])
    contact = " | ".join(str(person.get(key, "")) for key in ("email", "phone") if person.get(key))
    german = job["language"] == "de"
    subject = f'Bewerbung als {job["role"]}' if german else f'Application for {job["role"]}'
    shown_date = date.fromisoformat(letter["date"]).strftime("%d.%m.%Y") if german else letter["date"]
    fields = {"language": job["language"], "title": subject,
              "name": person["name"], "location": person.get("location", ""),
              "contact": contact, "date": shown_date, "company": job["company"],
              "role": subject, "greeting": letter["greeting"], "closing": letter["closing"]}
    fields = {key: escape(str(value), quote=True) for key, value in fields.items()}
    fields["paragraphs"] = paragraphs
    template = Template((ASSETS / "cover-letter.html").read_text(encoding="utf-8"))
    return standalone(template.substitute(fields), css)
