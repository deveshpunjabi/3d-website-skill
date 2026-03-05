#!/usr/bin/env python3
"""
Validate that a SKILL.md file has correct frontmatter and structure.
Usage: python validate_skill.py <path-to-SKILL.md>
"""

import sys
import re
from pathlib import Path


def validate_skill(filepath: str) -> list[str]:
    """Validate a SKILL.md file. Returns list of issues found."""
    issues = []
    path = Path(filepath)

    if not path.exists():
        return [f"File not found: {filepath}"]

    content = path.read_text(encoding="utf-8")

    # Check frontmatter
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not frontmatter_match:
        issues.append("Missing YAML frontmatter (--- ... ---)")
    else:
        fm = frontmatter_match.group(1)
        if "name:" not in fm:
            issues.append("Frontmatter missing 'name' field")
        if "description:" not in fm:
            issues.append("Frontmatter missing 'description' field")

        # Check description length
        desc_match = re.search(
            r"description:\s*>?\s*\n?(.*?)(?=\n[a-zA-Z_-]+:|\Z)", fm, re.DOTALL
        )
        if desc_match:
            desc = desc_match.group(1).strip()
            word_count = len(desc.split())
            if word_count < 20:
                issues.append(
                    f"Description too short ({word_count} words) — aim for 40+ words for reliable triggering"
                )

    # Check line count
    lines = content.split("\n")
    if len(lines) > 700:
        issues.append(
            f"Skill is {len(lines)} lines — recommended max is 700 lines (move detail to references/)"
        )

    # Check for required sections
    if "## " not in content:
        issues.append("No H2 sections found — skill should have structured sections")

    # Check for heading hierarchy
    h1_count = len(re.findall(r"^# ", content, re.MULTILINE))
    if h1_count == 0:
        issues.append("No H1 heading found")
    elif h1_count > 1:
        issues.append(f"Multiple H1 headings found ({h1_count}) — use only one")

    # Check for reference file pointers (skill should reference its bundled docs)
    skill_dir = path.parent
    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        ref_files = list(refs_dir.glob("*.md"))
        for ref_file in ref_files:
            ref_name = ref_file.name
            if ref_name not in content:
                issues.append(
                    f"Reference file '{ref_name}' exists but is not mentioned in SKILL.md"
                )

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <path-to-SKILL.md>")
        sys.exit(1)

    filepath = sys.argv[1]
    issues = validate_skill(filepath)

    if issues:
        print(f"Found {len(issues)} issue(s) in {filepath}:\n")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        sys.exit(1)
    else:
        print(f"✓ {filepath} is valid")
        sys.exit(0)


if __name__ == "__main__":
    main()
