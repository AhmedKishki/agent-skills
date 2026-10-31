"""Presentation fragments; inputs to item_header are already HTML-escaped."""
from html import escape
from urllib.parse import urlsplit


def project_link(value):
    """Only ordinary absolute HTTP(S) links become navigable."""
    try:
        parsed = urlsplit(value)
        safe = parsed.scheme.lower() in {"http", "https"} and bool(parsed.netloc)
    except ValueError:
        safe = False
    if safe and not any(ord(char) < 33 for char in value):
        return f'<a class="project__link" href="{value}">{value}</a>'
    return f'<span class="project__link">{value}</span>'


def item_header(section, values):
    heading = "project__title" if section == "projects" else "education__institution"
    identity = []
    if values[0]:
        identity.append(f'<h4 class="{heading} section__subheading">{values[0]}</h4>')
    if values[1]:
        identity.append(f'<h5 class="section__subsubheading">{values[1]}</h5>')
    if section == "projects" and values[2]:
        identity.append(project_link(values[2]))
    metadata = []
    if values[3]:
        metadata.append(f'<h5 class="section__date-range">{values[3]}</h5>')
    if section != "projects" and values[2]:
        metadata.append(f'<h4 class="section__location">{values[2]}</h4>')
    parts = ['<div class="section__identity">' + "".join(identity) + "</div>"] if identity else []
    if metadata:
        parts.append('<div class="section__metadata">' + "".join(metadata) + "</div>")
    return '<div class="section__item-header">' + "".join(parts) + "</div>" if parts else ""


def skill_row(item, index, locator, record):
    heading = item.get("heading", "")
    details = [text for text in item.get("list-items", []) if text.strip()]
    text = "; ".join(details)
    if not text or details == [heading]:
        if not heading.strip():
            return ""
        # Keep the editable marker on the sole displayed skill, at its actual source.
        source = "/list-items" if details else "/heading"
        marked = record(f"skills-{index}", "skills", heading, locator + source)
        return '<tr><td class="skills__heading" colspan="2">' + marked + "</td></tr>"
    marked = record(f"skills-{index}", "skills", text, locator + "/list-items", heading)
    label = '<td class="skills__heading">' + escape(heading) + "</td>" if heading else ""
    span = "" if heading else ' colspan="2"'
    return '<tr>' + label + f'<td class="skills__list"{span}>' + marked + "</td></tr>"
