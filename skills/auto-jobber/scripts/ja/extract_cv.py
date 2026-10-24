"""Local old-CV text extraction; the agent normalizes facts and asks about uncertainty."""
import subprocess
import zipfile
from pathlib import Path
from xml.etree import ElementTree

from .common import require, write_text
from .web_text import readable_text

LIMIT = 10 * 1024 * 1024


def _extract_cv(input_file, output_file):
    source, target = Path(input_file).expanduser(), Path(output_file).expanduser()
    require(source.is_file() and source.stat().st_size <= LIMIT, "CV must be a file up to 10 MiB")
    require(not target.exists() and not target.is_symlink(), "Extraction output already exists")
    suffix = source.suffix.lower()
    if suffix == ".pdf":
        result = subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", str(source), "-"],
                                capture_output=True, text=True, timeout=30, check=True)
        text = result.stdout
    elif suffix == ".docx":
        with zipfile.ZipFile(source) as archive:
            info = archive.getinfo("word/document.xml")
            require(info.file_size <= LIMIT, "DOCX document XML exceeds extraction limit")
            root = ElementTree.fromstring(archive.read(info))
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        text = "\n".join("".join(node.itertext()) for node in root.findall(".//w:p", ns))
    elif suffix in {".txt", ".md", ".html", ".htm"}:
        text = source.read_text(encoding="utf-8")
        if suffix in {".html", ".htm"}:
            text = readable_text(text)
    else:
        raise ValueError("Use PDF, DOCX, HTML or UTF-8 text; legacy DOC and image OCR are unsupported")
    require(len(text.strip()) >= 40, "Too little readable CV text; scanned PDFs need separate OCR")
    write_text(target, text)
    return {"text_file": str(target), "characters": len(text), "status": "needs-source-audit"}


def extract_cv(input_file, output_file):
    try:
        return _extract_cv(input_file, output_file)
    except (subprocess.SubprocessError, zipfile.BadZipFile, ElementTree.ParseError, KeyError) as error:
        raise ValueError(f"Cannot extract old CV: {error}; provide readable text or a valid document") from error
