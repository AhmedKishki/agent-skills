"""Poppler readability, page geometry and text-completeness gates."""
from collections import Counter
from pathlib import Path
import re
import unicodedata

from .previews import run


def tokens(text: str) -> Counter:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return Counter(re.findall(r"\w+", normalized, flags=re.UNICODE))


def inspect_pdf(pdf: Path, expected: str, cap: int, paper: str, tools: dict) -> dict:
    # The shared runner fixes the locale for stable Poppler diagnostic labels.
    info = run([tools["pdfinfo"], "-enc", "UTF-8", str(pdf)])
    match = re.search(r"^Pages:\s+(\d+)\s*$", info, re.MULTILINE)
    if not match:
        raise ValueError(f"{pdf.name}: pdfinfo did not report a readable page count")
    pages = int(match.group(1))
    if not 1 <= pages <= cap:
        raise ValueError(f"{pdf.name}: {pages} pages exceeds permitted range 1..{cap}")
    sizes = {"A4": (595.276, 841.89), "Letter": (612, 792)}
    width, height = sizes[paper]
    for page in range(1, pages + 1):
        detail = run([tools["pdfinfo"], "-f", str(page), "-l", str(page), str(pdf)])
        size = re.search(r"(?:Page\s+\d+\s+size|Page size):\s*"
                         r"([\d.]+)\s+x\s+([\d.]+)\s+pts", detail)
        if not size or any(abs(float(actual) - wanted) > 1
                           for actual, wanted in zip(size.groups(), (width, height))):
            raise ValueError(f"{pdf.name}: page {page} is not portrait {paper}")
    text = run([tools["pdftotext"], "-enc", "UTF-8", "-layout", str(pdf), "-"])
    wanted = tokens(expected)
    if not wanted:
        raise ValueError(f"{pdf.name}: expected visible text is empty")
    missing = wanted - tokens(text)
    if missing:
        sample = ", ".join(f"{word} ({count})" for word, count in list(missing.items())[:20])
        raise ValueError(f"{pdf.name}: missing expected text tokens: {sample}")
    text_path = pdf.with_suffix(".txt")
    with text_path.open("x", encoding="utf-8") as handle:
        handle.write(text)
    return {"page_count": pages, "paper": paper, "text": text_path.name,
            "checks": {"readable": True, "page_limit": True, "paper_size": True,
                       "text_complete": True}, "expected_token_count": sum(wanted.values())}
