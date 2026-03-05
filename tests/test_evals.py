"""Tests for evals.json structure and content."""

import json
import os
import pytest

EVALS_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "skills",
    "3d-website-architect",
    "evals",
    "evals.json",
)


class TestEvalsStructure:
    """Validate the evals.json file."""

    @pytest.fixture(autouse=True)
    def load_evals(self):
        with open(EVALS_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_has_skill_name(self):
        assert "skill_name" in self.data
        assert self.data["skill_name"] == "3d-website-architect"

    def test_has_evals_array(self):
        assert "evals" in self.data
        assert isinstance(self.data["evals"], list)

    def test_minimum_eval_count(self):
        assert len(self.data["evals"]) >= 3, "Need at least 3 eval cases"

    def test_eval_has_required_fields(self):
        for ev in self.data["evals"]:
            assert "id" in ev, "Each eval must have an id"
            assert "prompt" in ev, "Each eval must have a prompt"
            assert "expected_output" in ev, "Each eval must have expected_output"
            assert "expectations" in ev, "Each eval must have expectations"

    def test_expectations_are_lists(self):
        for ev in self.data["evals"]:
            assert isinstance(ev["expectations"], list)
            assert len(ev["expectations"]) > 0, f"Eval {ev['id']} has no expectations"

    def test_prompts_are_non_empty(self):
        for ev in self.data["evals"]:
            assert len(ev["prompt"].strip()) > 20, (
                f"Eval {ev['id']} prompt is too short"
            )

    def test_total_assertion_count(self):
        total = sum(len(ev["expectations"]) for ev in self.data["evals"])
        assert total >= 30, f"Only {total} total assertions — aim for 30+"
