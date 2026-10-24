"""Select approved English/German CV sources, not ad-hoc per-job translations."""
import re

from .common import read_json, require, safe_child, sha256, write_json

SUPPORTED = ("en", "de")


def localize_labels(source, language):
    require(language in SUPPORTED, "Document language must be en or de")
    if language == "de":
        labels = {"Profile": "Profil", "Experience": "Berufserfahrung", "Skills": "Fachkenntnisse",
                  "Education": "Ausbildung", "Projects": "Projekte", "Certificates": "Zertifikate",
                  "Languages": "Sprachen", "Online presence": "Online-Profile",
                  "Extracurricular Activity": "Weitere Tätigkeiten"}
        source = source.replace('<html lang="en">', '<html lang="de">')
        source = source.replace("<title>Curriculum vitae</title>", "<title>Lebenslauf</title>")
        for english, german in labels.items():
            source = source.replace(f'>{english}<span class="section__heading-underline">',
                                    f'>{german}<span class="section__heading-underline">')
    return source


def markup_language(source):
    match = re.search(r'<html\b[^>]*\blang=["\'](en|de)["\']', source, re.I)
    require(match is not None, 'CV needs <html lang="en"> or <html lang="de">')
    return match[1].lower()


def register_variant(workspace, revision, language):
    require(language in SUPPORTED, "Only English (en) and German (de) are supported")
    path = workspace / "variants.json"
    variants = read_json(path) if path.exists() else {}
    variants[language] = str(revision.relative_to(workspace))
    write_json(path, variants)


def choose_variant(workspace, language):
    from .profile import check_baseline
    require(language in SUPPORTED, "Offer language must be en or de")
    require((workspace / "variants.json").exists(), "Review and seal a CV baseline first")
    variants = read_json(workspace / "variants.json")
    require(language in variants, f"Create, review and seal a {language} CV variant first")
    folder = safe_child(workspace, variants[language])
    record = check_baseline(folder)
    require(record.get("language") == language, "Baseline language metadata differs")
    for name, digest in record["files"].items():
        if name not in {"cv.html", "cv.css"}:
            require(sha256(workspace / name) == digest,
                    f"Profile/source changed; review and reseal the {language} CV variant")
    return folder, record
