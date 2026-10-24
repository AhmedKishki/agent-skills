"""Print pre-sanitized self-contained HTML using a sandboxed Chrome CLI."""
import os
from pathlib import Path
import shutil
import tempfile

from .html_safety import visible_text
from .pdf_checks import inspect_pdf
from .previews import make_previews, run


def browser_path() -> str | None:
    configured = os.environ.get("CHROME_BIN")
    if configured:
        return shutil.which(configured)
    return next((found for name in ("google-chrome", "chromium", "chromium-browser")
                 if (found := shutil.which(name))), None)


def render_documents(output_dir: Path, policy: dict, stems=("cv", "cover-letter")) -> dict:
    output_dir = output_dir.resolve(strict=True)
    paper = policy.get("paper", "A4")
    if paper not in ("A4", "Letter"):
        raise ValueError("paper must be A4 or Letter")
    caps = {"cv": policy.get("cv_max_pages", 2),
             "cover-letter": policy.get("letter_max_pages", 1)}
    if not stems or any(stem not in caps for stem in stems):
        raise ValueError("Unknown document selection")
    caps = {stem: caps[stem] for stem in stems}
    if any(type(cap) is not int or cap < 1 for cap in caps.values()):
        raise ValueError("Page limits must be positive integers")
    tools = {name: shutil.which(name) for name in ("pdfinfo", "pdftotext", "pdftoppm")}
    missing = [name for name in ("pdfinfo", "pdftotext") if not tools[name]]
    if missing:
        raise RuntimeError("Required Poppler tools missing: " + ", ".join(missing))
    browser = browser_path()
    if not browser:
        raise RuntimeError("Chrome not found; set CHROME_BIN or provide google-chrome/chromium")
    for stem in caps:
        source = output_dir / f"{stem}.html"
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"Expected regular sanitized input: {source.name}")
        for suffix in ("pdf", "txt"):
            if os.path.lexists(output_dir / f"{stem}.{suffix}"):
                raise ValueError(f"Refusing existing output: {stem}.{suffix}")
        if list(output_dir.glob(f"{stem}-page-*.png")):
            raise ValueError(f"Refusing existing previews for {stem}")
    report = {"passed": True, "chrome_version": run([browser, "--version"]).strip(),
              "documents": {}, "caveat": "Text checks cannot establish visual readability; "
              "review every preview for clipping, overlap and layout. Network flags are "
              "defense in depth, not hard network isolation."}
    for stem, cap in caps.items():
        source = output_dir / f"{stem}.html"
        pdf = output_dir / f"{stem}.pdf"
        expected = visible_text(source.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory(prefix="ja-chrome-") as profile:
            run([browser, "--headless", "--disable-gpu", f"--user-data-dir={profile}",
                 "--no-first-run", "--no-default-browser-check", "--disable-extensions",
                 "--disable-background-networking", "--disable-sync", "--disable-component-update",
                 "--host-resolver-rules=MAP * ~NOTFOUND", "--no-pdf-header-footer",
                 "--print-to-pdf-no-header", f"--print-to-pdf={pdf}", source.as_uri()])
        if not pdf.is_file() or pdf.stat().st_size == 0:
            raise RuntimeError(f"Chrome did not create {pdf.name}")
        result = inspect_pdf(pdf, expected, cap, paper, tools)
        result["pdf"] = pdf.name
        result["previews"] = make_previews(pdf, result["page_count"], tools["pdftoppm"])
        report["documents"][stem] = result
    return report
