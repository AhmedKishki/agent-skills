"""Run deterministic application gates without claiming semantic verification."""
from .applications import check_snapshot
from .common import read_json, require
from .freshness import require_current
from .html_safety import standalone
from .plan_checks import validate_plan
from .profile import validate_profile
from .research import validate_research
from .voice import validate_wording


def check_application(application):
    app = check_snapshot(application)
    profile = read_json(app / "input" / "qualifications.json")
    baseline = (app / "input" / "cv.html").read_text(encoding="utf-8")
    css = (app / "input" / "cv.css").read_text(encoding="utf-8")
    validate_profile(profile, baseline)
    require_current(profile)
    standalone(baseline, css)
    warnings = validate_research(app, profile["policy"])
    plan, research = read_json(app / "plan.json"), read_json(app / "research.json")
    require(plan["job"]["language"] == read_json(app / "application.json")["language"],
            "Plan language differs from the selected offer-language CV baseline")
    wording_errors = validate_wording(app, plan, profile)
    require(not wording_errors, "; ".join(wording_errors))
    tailored, changes, notes = validate_plan(plan, profile, research, baseline)
    warnings.extend(notes)
    warnings.append("Reference and numeric checks do not establish semantic truth; review every claim")
    return {"app": app, "profile": profile, "baseline": baseline, "css": css,
            "plan": plan, "research": research, "tailored": tailored,
            "checks": {"passed": True, "changes": changes, "warnings": warnings}}
