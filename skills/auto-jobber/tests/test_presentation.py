"""Synthetic presentation regressions; never read a live candidate workspace."""
import copy
import sys
import unittest
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from ja.bootstrap_sections import render_section
from ja.html_safety import visible_text
from ja.intake_data import upstream_data


class PresentationTests(unittest.TestCase):
    def render(self, section, items):
        self.calls = []

        def record(block, kind, text, locator, context=""):
            self.calls.append((block, kind, text, locator, context))
            return f"<!-- cv:{block} -->{escape(text)}<!-- /cv:{block} -->"

        return render_section(section, items, record)

    def test_project_url_is_link_not_place(self):
        url = 'https://example.invalid/project?q=a&x="quoted"'
        html = self.render("projects", [{"title": "Project", "url": url,
                                        "date-range": "2023-04 – 2024"}])
        self.assertIn('class="project__link" href="' + escape(url) + '"', html)
        self.assertNotIn("section__location", html)
        self.assertIn('class="section__metadata"', html)
        self.assertIn("2023-04 – 2024", html)
        self.assertNotIn("<ul>", html)

    def test_actual_dates_places_and_escaping(self):
        html = self.render("experience", [{"institution": "A & B", "title": "<Role>",
            "location": 'Town <West> "Q"', "date-range": "2020-02 – present",
            "list-items": ["Built <safe> & tested"]}])
        rail = html.split('<div class="section__metadata">', 1)[1].split("</div>", 1)[0]
        self.assertIn("2020-02 – present", rail)
        self.assertIn("Town &lt;West&gt; &quot;Q&quot;", rail)
        self.assertIn("A &amp; B", html)
        self.assertIn("&lt;Role&gt;", html)
        self.assertIn("Built &lt;safe&gt; &amp; tested", html)
        self.assertNotIn("<safe>", html)

    def test_unsafe_project_urls_remain_escaped_text(self):
        for url in ('javascript:alert(1)', '//example.invalid', '<img src=x>',
                    'https://[invalid', 'https://example.invalid/\npath'):
            html = self.render("projects", [{"title": "Project", "url": url}])
            self.assertNotIn("href=", html)
            self.assertIn(escape(url), html)

    def test_title_only_skills_have_one_display_and_owned_marker(self):
        data = {"person": {"name": "Example"}, "qualifications": {
            "expertise": [{"title": "C & C++", "details": []}]}}
        skills = upstream_data(data)["skills"]
        self.assertEqual([], skills[0]["list-items"])
        html = self.render("skills", skills)
        self.assertEqual(1, visible_text(html).count("C & C++"))
        self.assertEqual("/skills/0/heading", self.calls[0][3])
        self.assertIn("<!-- cv:skills-1 -->", html)
        html = self.render("skills", [{"heading": "C", "list-items": ["C"]}])
        self.assertEqual("Skills C", visible_text(html))
        self.assertEqual("/skills/0/list-items", self.calls[0][3])

    def test_skill_details_and_empty_rows(self):
        html = self.render("skills", [{"heading": "Tools", "list-items": ["C", "Python"]},
                                       {"heading": "", "list-items": [" "]}])
        self.assertEqual(1, html.count("<tr>"))
        self.assertIn("C; Python", html)
        self.assertEqual("Tools", self.calls[0][4])
        self.assertEqual("", self.render("skills", [{"heading": "", "list-items": []}]))

    def test_duplicates_retained_until_provenance_aliasing_is_supported(self):
        role = {"title": "Engineer", "organisation": "Example", "location": "Town",
                "start": "2022-03", "end": "2024", "details": ["Tested devices"]}
        other = dict(role, title="Researcher")
        data = {"person": {"name": "Example"}, "qualifications": {
            "work": [dict(role, id="w", source="work-source")], "experience": [
                dict(role, id="e", source="experience-source"), other]}}
        before = copy.deepcopy(data)
        records = upstream_data(data)["experience"]
        html = self.render("experience", records)
        self.assertEqual(before, data)
        self.assertEqual(3, html.count('class="section__item"'))
        self.assertIn("Researcher", html)
        self.assertEqual(["/experience/0/list-items/0", "/experience/1/list-items/0",
                          "/experience/2/list-items/0"],
                         [call[3] for call in self.calls if call[1] == "bullet"])


if __name__ == "__main__":
    unittest.main()
