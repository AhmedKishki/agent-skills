"""Map source-backed intake records to the pinned upstream CV data structure."""
from html import escape


def entry_text(item):
    values = [str(item.get(key) or "") for key in
              ("title", "organisation", "location", "start", "end", "level", "url")]
    return " | ".join(value for value in values if value) + ". " + " ".join(item.get("details", []))


def upstream_data(data):
    person, qualifications = data["person"], data["qualifications"]
    name = person["name"].split(" ", 1)
    about = {"first-name": name[0], "last-name": name[1] if len(name) > 1 else "",
             "email": person.get("email", ""), "location": person.get("location", ""),
             "mobile-display": person.get("phone", ""), "position": person.get("headline", ""),
             "description": data.get("summary", "")}
    result = {"about-me": about}
    mapping = {"study": "education", "work": "experience", "experience": "experience",
               "projects": "projects"}
    for category, target in mapping.items():
        for item in qualifications.get(category, []):
            record = {"institution": item.get("organisation", ""), "title": item["title"],
                      "study": item["title"], "description": item.get("description", ""),
                      "location": item.get("location", ""), "url": item.get("url", ""),
                      "date-range": " – ".join(str(item[key]) for key in ("start", "end") if item.get(key)),
                      "list-items": item.get("details", [])}
            if item.get("gpa") is not None:
                record["gpa"] = item["gpa"]
            result.setdefault(target, []).append(record)
    result["skills"] = [{"heading": item["title"], "list-items": item.get("details") or [item["title"]]}
                        for item in qualifications.get("expertise", [])]
    return result


def extra_section(title, category, items):
    if not items:
        return ""
    rows = []
    for item in items:
        rows.append("<li>" + escape(entry_text(item)) + "</li>")
    return (f'<section class="{category}"><h2 class="section__heading">{escape(title)}'
            '<span class="section__heading-underline"></span></h2><ul>' + "".join(rows) + "</ul></section>")
