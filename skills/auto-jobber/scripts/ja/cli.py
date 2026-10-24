"""The invoking agent owns the dialogue; these commands preserve its records."""
import shutil
import sys

from .applications import new_application
from .arguments import parser
from .build import build_application
from .common import read_json
from .freshness import confirm_current, freshness_status
from .manifest import archive, verify_manifest
from .profile import initialise, seal
from .sources import add_source
from .validate import check_application
from .voice import capture_wording, remember_voice


def main(argv=None):
    args = parser().parse_args(argv)
    if args.command == "init":
        return initialise(args.workspace)
    if args.command == "seal":
        return seal(args.workspace, args.language, args.html, args.css)
    if args.command == "status":
        return freshness_status(read_json(args.workspace / "qualifications.json"))
    if args.command == "confirm-current":
        return confirm_current(args.workspace, args.note)
    if args.command == "preview":
        from .baseline_preview import preview_baseline
        return preview_baseline(args.workspace, args.language, args.html, args.css)
    if args.command == "intake":
        from .intake import intake
        return intake(args.workspace, args.data)
    if args.command == "extract":
        from .extract_cv import extract_cv
        return extract_cv(args.input, args.output)
    if args.command == "bootstrap":
        from .bootstrap import bootstrap
        return bootstrap(args.workspace, args.data)
    if args.command == "remember-voice":
        return remember_voice(args.workspace, args.text_file, args.source)
    if args.command == "new":
        return new_application(args.workspace, args.job, args.url, args.language)
    if args.command == "source":
        return add_source(args.application, args.url, args.title, args.kind,
                          args.text_file, args.published_at)
    if args.command == "wording":
        return capture_wording(args.application, args.text_file, args.source, args.must_include, args.language)
    if args.command == "approve-translation":
        from .wording_translation import approve_translation
        return approve_translation(args.application, args.text_file, args.source, args.language)
    if args.command == "check":
        return check_application(args.application)["checks"]
    if args.command == "build":
        return build_application(args.application, args.html_only)
    if args.command == "archive":
        return archive(args.build)
    if args.command == "verify":
        return verify_manifest(args.build)
    from .render import browser_path
    tools = {name: shutil.which(name) for name in ("pdfinfo", "pdftotext", "pdftoppm")}
    return {"python": sys.version.split()[0], "chrome": browser_path(), "tools": tools,
            "ready_for_pdf": bool(browser_path() and tools["pdfinfo"] and tools["pdftotext"]),
            "note": "Agent dialogue, browsing and writing are separate from local scripts"}
