"""Tests for validate_skill.py"""

import sys
import os
import tempfile
import pytest

# Add scripts directory to path
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "scripts")
)

from validate_skill import validate_skill


class TestValidateSkill:
    """Test the validate_skill function."""

    def test_valid_skill(self):
        """A well-formed SKILL.md should pass validation."""
        skill_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "skills",
            "3d-website-architect",
            "SKILL.md",
        )
        issues = validate_skill(skill_path)
        assert issues == [], f"Unexpected issues: {issues}"

    def test_missing_name(self):
        """SKILL.md without a name field should fail."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write(
                "---\ndescription: >-\n  A fairly long description that has enough words to pass the minimum word count check.\n---\n# Test Skill\n\n## Section\nContent\n"
            )
            f.flush()
            issues = validate_skill(f.name)
        os.unlink(f.name)
        assert any("name" in i.lower() for i in issues)

    def test_missing_description(self):
        """SKILL.md without a description field should fail."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write("---\nname: test-skill\n---\n# Test Skill\n\n## Section\nContent\n")
            f.flush()
            issues = validate_skill(f.name)
        os.unlink(f.name)
        assert any("description" in i.lower() for i in issues)

    def test_no_frontmatter(self):
        """SKILL.md without frontmatter should fail."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write("# Test Skill\n\n## Section\nContent\n")
            f.flush()
            issues = validate_skill(f.name)
        os.unlink(f.name)
        assert any("frontmatter" in i.lower() for i in issues)

    def test_short_description(self):
        """SKILL.md with a very short description should warn."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write(
                "---\nname: test-skill\ndescription: Too short\n---\n# Test Skill\n\n## Section\nContent\n"
            )
            f.flush()
            issues = validate_skill(f.name)
        os.unlink(f.name)
        assert any("short" in i.lower() for i in issues)

    def test_file_not_found(self):
        """Non-existent file should return a file-not-found issue."""
        issues = validate_skill("/nonexistent/path/SKILL.md")
        assert len(issues) == 1
        assert "not found" in issues[0].lower()

    def test_multiple_h1(self):
        """SKILL.md with multiple H1 headings should warn."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write(
                "---\nname: test-skill\ndescription: >-\n  A description with enough words to pass the minimum check easily without issues.\n---\n# First\n\n## Section\nContent\n\n# Second\n"
            )
            f.flush()
            issues = validate_skill(f.name)
        os.unlink(f.name)
        assert any("h1" in i.lower() or "multiple" in i.lower() for i in issues)
