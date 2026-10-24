import tempfile
import unittest
from datetime import datetime
from pathlib import Path

import support
from ja.common import read_json, write_json
from ja.freshness import confirm_current, freshness_status, require_current


def date(value):
    return datetime.fromisoformat(value).astimezone()


class FreshnessTests(unittest.TestCase):
    def status(self, entry, now, **extra):
        return freshness_status({"qualifications": {"employment": [{"end": entry}]},
                                 **extra}, date(now))

    def test_september_to_october(self):
        self.assertTrue(self.status("2026-09-30", "2026-10-01T12:00")["needs_confirmation"])

    def test_same_month_long_duration(self):
        self.assertFalse(self.status("2026-10-01", "2026-10-31T23:59")["needs_confirmation"])

    def test_year_rollover(self):
        self.assertTrue(self.status("2025-12-31", "2026-01-01T12:00")["needs_confirmation"])

    def test_current_confirmation_overrides_old_employment(self):
        self.assertFalse(self.status("2020-01-01", "2026-10-24T12:00",
                         last_reviewed_at="2026-10-01T00:00:00+00:00")["needs_confirmation"])

    def test_future_review_rejected(self):
        with self.assertRaisesRegex(ValueError, "future"):
            self.status("2020", "2026-10-24T12:00", last_reviewed_at="2026-11-01")

    def test_missing_and_future_entries(self):
        for entry in ("present", "future", "2030-01-01", None):
            self.assertTrue(self.status(entry, "2026-10-24T12:00")["needs_confirmation"])
        with self.assertRaisesRegex(ValueError, "2026-10-24.*confirm"):
            require_current({}, date("2026-10-24T12:00"))

    def test_confirmation_persisted(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root)
            write_json(path / "qualifications.json", {})
            self.assertFalse(confirm_current(path, "No changes")["needs_confirmation"])
            profile = read_json(path / "qualifications.json")
            self.assertEqual("No changes", profile["current_confirmation"]["note"])
