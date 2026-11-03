---
name: changelog.md
description: Records the enduring user-visible history of the guided-learning skill.
---

# Changelog

This is the single enduring changelog for `guided-learning`. Current behaviour is governed by `SKILL.md`; historical entries describe the behaviour of their version.

## 1.0.0 — 2026-11-03

- First version. Replaces `collaborative-learning`, which is removed from the collection.
- Diagnoses the student's level with multiple-choice and free-thought questions, then proposes a syllabus built from that level, which the student approves and can revise at any time.
- Teaches lesson by lesson. Each lesson ends with the student's questions and a check of 1–5 questions; missed ideas are re-explained and checked again with new questions.
- Cites every claim. Ebooks are read through an ebook MCP server when one is connected, web sources are used when the student names none, and claims from the agent's own knowledge are marked unsourced when no source confirms them.
- Records `progress.md` and lesson notes per subject. Projects created by `collaborative-learning` (`learning-plan.md`, `sessions/`) are not resumed.
