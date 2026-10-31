"""Normalize only the local stylesheet explicitly selected for a CV source."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from .common import require


class Stylesheets(HTMLParser):
    def __init__(self, html_file, css_file):
        super().__init__(convert_charrefs=True)
        self.html_file, self.css_file = Path(html_file), Path(css_file)
        self.replacements = []

    def handle_starttag(self, tag, attrs):
        if tag != "link":
            return
        require(len(dict(attrs)) == len(attrs), "Duplicate stylesheet attributes are forbidden")
        values = dict(attrs)
        target = values.get("href") or ""
        if target == "cv.css":
            return
        require(values.get("rel") == "stylesheet", "Only a stylesheet link is supported")
        parsed = urlsplit(target)
        require(target and not any((parsed.scheme, parsed.netloc, parsed.query, parsed.fragment))
                and not Path(target).is_absolute() and "\\" not in target and "%" not in target
                and all(ord(char) >= 32 for char in target), "Stylesheet must be a local relative file")
        selected = self.css_file.expanduser().resolve(strict=True)
        linked = (self.html_file.parent / target).resolve(strict=True)
        require(selected.is_file() and linked == selected,
                "Stylesheet link must match the explicitly selected CSS file")
        rendered = " ".join(key if value is None else
                            f'{key}="{escape("cv.css" if key == "href" else value, quote=True)}"'
                            for key, value in attrs)
        self.replacements.append((self.get_starttag_text(), f"<link {rendered}>"))


def normalize_stylesheet(source, html_file=None, css_file=None):
    if html_file is None or css_file is None:
        return source
    parser = Stylesheets(html_file, css_file)
    parser.feed(source)
    for original, replacement in parser.replacements:
        source = source.replace(original, replacement)
    return source
