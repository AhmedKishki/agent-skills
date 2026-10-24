import shutil
import tempfile
import unittest
from pathlib import Path

import support
from ja.common import read_json, write_json
from ja.voice import capture_wording, remember_voice, validate_wording


class VoiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.app = self.root / "job-one"
        self.app.mkdir()
        self.text = self.root / "words.txt"
        self.text.write_text("I enjoy careful engineering and clear communication.")
        self.plan = {"letter": {"wording_quotes": ["I enjoy careful engineering"],
                     "paragraphs": [{"sentences": [{"text":
                         "I enjoy careful engineering and clear communication."}]}]}}
        write_json(self.app / "plan.json", self.plan)

    def capture(self):
        capture_wording(self.app, self.text, "User supplied text", ["clear communication"])
        self.plan = read_json(self.app / "plan.json")

    def test_missing(self):
        self.assertTrue(validate_wording(self.app, self.plan, {}))

    def test_valid_current_user_words(self):
        self.capture()
        self.assertEqual([], validate_wording(self.app, self.plan, {}))

    def test_wrong_hash(self):
        self.capture()
        (self.app / self.plan["user_input"]["file"]).write_text("Changed words")
        self.assertTrue(validate_wording(self.app, self.plan, {}))

    def test_not_user(self):
        self.capture()
        self.plan["user_input"]["authorship"] = "model"
        self.assertTrue(validate_wording(self.app, self.plan, {}))

    def test_wrong_quote_and_short_quote(self):
        self.capture()
        for quote in ("I love sales work", "I enjoy", "!!! !!! !!!"):
            self.plan["letter"]["wording_quotes"] = [quote]
            self.assertTrue(validate_wording(self.app, self.plan, {}))

    def test_wrong_job_even_with_copied_snapshot(self):
        self.capture()
        other = self.root / "job-two"
        shutil.copytree(self.app, other)
        self.assertTrue(validate_wording(other, self.plan, {}))

    def test_snapshot_not_overwritten(self):
        self.capture()
        old = self.app / self.plan["user_input"]["file"]
        self.capture()
        self.assertNotEqual(old.name, Path(self.plan["user_input"]["file"]).name)
        self.assertEqual(self.text.read_text(), old.read_text())

    def test_mandatory_phrase_and_verbatim_quote(self):
        self.capture()
        self.plan["letter"]["paragraphs"][0]["sentences"][0]["text"] = "Unrelated prose."
        self.assertTrue(validate_wording(self.app, self.plan, {}))

    def test_remember_raw_user_sample(self):
        write_json(self.root / "qualifications.json", {})
        sample = remember_voice(self.root, self.text, "User sample")
        self.assertEqual("user", sample["authorship"])
        self.assertEqual(self.text.read_text(), sample["text"])
        self.assertEqual([sample], read_json(self.root / "qualifications.json")["voice"]["samples"])
