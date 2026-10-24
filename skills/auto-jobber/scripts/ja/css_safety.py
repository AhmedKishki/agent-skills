"""Conservative closed-document CSS policy; no fetching or hidden overflow."""
import re

from .common import require


def validate_css(css):
    require("</style" not in css.lower(), "CSS must not close its HTML style element")
    plain = re.sub(r"/\*.*?\*/", "", css, flags=re.S).lower()
    require("\\" not in plain, "CSS escapes are unsupported; use literal CSS names")
    require(not re.search(r"url\s*\(|@import|expression\s*\(|-moz-binding|behavior\s*:", plain),
            "CSS cannot load assets, import sheets or execute expressions")
    rules = re.findall(r"@([a-z-]+)", plain)
    require(all(rule in {"page", "media", "supports"} for rule in rules),
            "Only @page, @media and @supports rules are supported")
    require(not re.search(r"overflow(?:-x|-y)?\s*:\s*(?:hidden|clip)", plain),
            "Hidden/clipped overflow can silently remove CV content")
