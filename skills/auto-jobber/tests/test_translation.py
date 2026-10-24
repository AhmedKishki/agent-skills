import tempfile
import unittest
from pathlib import Path

from support import fixture
from ja.common import read_json, write_json, write_text
from ja.voice import capture_wording, validate_wording
from ja.wording_translation import approve_translation


class TranslationTests(unittest.TestCase):
    def test_cross_language_wording_needs_explicit_approved_translation(self):
        with tempfile.TemporaryDirectory() as root:
            _, app = fixture(root)
            plan = read_json(app / "plan.json")
            plan["job"]["language"] = "de"
            plan["letter"]["wording_quotes"] = ["nah an der Hardware"]
            plan["letter"]["paragraphs"][-1]["sentences"][0]["text"] = "Ich arbeite gern nah an der Hardware."
            write_json(app / "plan.json", plan)
            original, translated = Path(root) / "english.txt", Path(root) / "german.txt"
            write_text(original, "I prefer working close to the hardware.")
            capture_wording(app, original, "Fictional user English wording", language="en")
            plan = read_json(app / "plan.json")
            self.assertTrue(validate_wording(app, plan, {}))
            write_text(translated, "Ich arbeite gern nah an der Hardware.")
            approve_translation(app, translated, "Fictional explicit user translation approval", "de")
            plan = read_json(app / "plan.json")
            self.assertEqual([], validate_wording(app, plan, {}))
            self.assertEqual(original.read_text(), (app / plan["user_input"]["file"]).read_text())
            write_text(app / plan["user_input"]["translation"]["file"], "Different German prose")
            self.assertTrue(validate_wording(app, plan, {}))


if __name__ == "__main__":
    unittest.main()
