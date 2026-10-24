"""Validate controlled CV markup and make a standalone, script-free HTML file."""
import re
from html.parser import HTMLParser

from .common import require
from .css_safety import validate_css

TAGS = set("html head title meta link style body main header footer section article div "
           "h1 h2 h3 h4 h5 h6 p span strong em b i ul ol li hr br a time address "
           "table thead tbody tfoot tr td th dl dt dd small sup sub".split())
CSP = ("default-src 'none'; script-src 'none'; style-src 'unsafe-inline'; "
       "img-src 'none'; font-src 'none'; connect-src 'none'; base-uri 'none'; "
       "form-action 'none'; frame-src 'none'; object-src 'none'")


class Markup(HTMLParser):
    def __init__(self, validate=False):
        super().__init__(convert_charrefs=True)
        self.validate, self.hidden, self.parts, self.styles = validate, [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.validate:
            require(tag in TAGS, f"Unsupported HTML element: {tag}")
            for key, value in attrs.items():
                require(not key.lower().startswith("on"), "Event handlers are forbidden")
                require(key not in {"src", "srcset", "background", "action", "http-equiv"},
                        f"Resource/active HTML attribute is forbidden: {key}")
                if key == "style":
                    validate_css(value or "")
            if "href" in attrs:
                target = attrs["href"] or ""
                allowed = re.match(r"^(?:https?://|mailto:|tel:|#)", target, re.I)
                require(tag == "a" and allowed or tag == "link" and target == "cv.css",
                        "Only contact links and the local cv.css stylesheet are supported")
            if tag == "link":
                require(attrs.get("rel") == "stylesheet" and attrs.get("href") == "cv.css",
                        "Only a local cv.css stylesheet link is supported")
        if tag in {"head", "style", "script"}:
            self.hidden.append(tag)
        self.parts.append(" ")

    def handle_endtag(self, tag):
        if tag in self.hidden:
            self.hidden.remove(tag)
        self.parts.append(" ")

    def handle_data(self, data):
        if "style" in self.hidden:
            self.styles.append(data)
        if not self.hidden:
            self.parts.append(data)


def visible_text(source):
    parser = Markup()
    parser.feed(source)
    return " ".join(" ".join(parser.parts).split())


def standalone(source, css):
    validate_css(css)
    parser = Markup(validate=True)
    parser.feed(source)
    validate_css("\n".join(parser.styles))
    require(len(re.findall(r"<head\s*>", source, re.I)) == 1,
            "CV must contain exactly one plain <head> element")
    source = re.sub(r"<link\b[^>]*>", "", source, flags=re.I)
    addition = f'<meta http-equiv="Content-Security-Policy" content="{CSP}">'
    return re.sub(r"<head\s*>", lambda m: m[0] + addition + "<style>" + css + "</style>",
                  source, count=1, flags=re.I)
