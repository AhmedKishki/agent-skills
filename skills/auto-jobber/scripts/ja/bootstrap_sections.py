"""Escaped, local-only rendering for the pinned awesome-cv-html data shape."""
from html import escape

from .common import require
from .presentation import item_header, skill_row

FIELDS = {
    "experience": ("institution", "title", "location", "date-range"),
    "education": ("institution", "study", "location", "date-range", "gpa"),
    "projects": ("title", "description", "url", "date-range"),
    "extracurricular": ("role", "organization", "location", "date-range"),
    "skills": ("heading",),
}
ABOUT = ("first-name", "last-name", "position", "location", "email",
         "mobile-display", "description", "github", "website")


def validate(data):
    require(isinstance(data, dict), "Candidate source must be a JSON object")
    about = data.get("about-me")
    require(isinstance(about, dict), "Candidate source needs about-me")
    for key in ABOUT:
        require(isinstance(about.get(key, ""), str), f"about-me.{key} must be text")
    require(any(about.get(key, "").strip() for key in ("first-name", "last-name")),
            "Candidate source needs a name")
    for section, fields in FIELDS.items():
        require(isinstance(data.get(section, []), list), f"{section} must be a list")
        for item in data.get(section, []):
            require(isinstance(item, dict), f"{section} entries must be objects")
            for key in fields:
                value = item.get(key, "")
                numeric_gpa = key == "gpa" and type(value) in {int, float}
                require(isinstance(value, str) or numeric_gpa, f"{section}.{key} must be text")
            bullets = item.get("list-items", [])
            require(isinstance(bullets, list) and all(isinstance(s, str) for s in bullets),
                    f"{section}.list-items must contain text")


def render_section(section, items, record):
    if not items:
        return ""
    title = "Extracurricular Activity" if section == "extracurricular" else section.title()
    parts = [f'<section class="{section}"><h2 class="section__heading">{title}'
             '<span class="section__heading-underline"></span></h2>']
    if section == "skills":
        rows = [skill_row(item, index, f"/skills/{index - 1}", record)
                for index, item in enumerate(items, 1)]
        rows = [row for row in rows if row]
        return "\n".join(parts + ["<table>", *rows, "</table></section>"]) if rows else ""
    for index, item in enumerate(items, 1):
        locator = f"/{section}/{index - 1}"
        fields = FIELDS[section]
        values = [escape(str(item.get(key, ""))) for key in fields]
        if section == "education" and values[4]:
            values[1] += " | GPA: " + values[4]
        parts.append('<div class="section__item">' + item_header(section, values))
        context = " | ".join(str(item[key]) for key in fields if item.get(key) is not None and key in item)
        prefix = "project" if section == "projects" else section
        if context.strip(" |"):
            record(f"{prefix}-{index}-facts", "fact", context, locator)
        bullets = []
        for number, text in enumerate(item.get("list-items", []), 1):
            if text.strip():
                marked = record(f"{prefix}-{index}-bullet-{number}", "bullet", text,
                                f"{locator}/list-items/{number - 1}", context)
                bullets.append(f"<li>{marked}</li>")
        if bullets:
            parts.append("<ul>" + "".join(bullets) + "</ul>")
        parts.append("</div>")
    return "\n".join(parts + ["</section>"])
