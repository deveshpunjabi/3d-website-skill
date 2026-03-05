#!/usr/bin/env python3
"""
Run eval prompts from evals.json and print a summary.
Usage: python run_evals.py <path-to-evals.json>
"""

import json
import sys
from pathlib import Path


def load_evals(filepath: str) -> dict:
    """Load and validate evals.json."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: {filepath} not found")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def print_eval_summary(data: dict):
    """Print a formatted summary of all eval cases."""
    skill_name = data.get("skill_name", "unknown")
    evals = data.get("evals", [])

    print(f"Skill: {skill_name}")
    print(f"Total eval cases: {len(evals)}")
    print("=" * 60)

    total_expectations = 0
    for ev in evals:
        eid = ev.get("id", "?")
        prompt = ev.get("prompt", "")
        expected = ev.get("expected_output", "")
        expectations = ev.get("expectations", [])
        total_expectations += len(expectations)

        print(f"\n--- Eval #{eid} ---")
        print(f"Prompt: {prompt[:120]}{'...' if len(prompt) > 120 else ''}")
        print(f"Expected: {expected[:120]}{'...' if len(expected) > 120 else ''}")
        print(f"Assertions: {len(expectations)}")
        for i, exp in enumerate(expectations, 1):
            print(f"  {i}. {exp}")

    print("\n" + "=" * 60)
    print(f"Total: {len(evals)} evals, {total_expectations} assertions")


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_evals.py <path-to-evals.json>")
        sys.exit(1)

    data = load_evals(sys.argv[1])
    print_eval_summary(data)


if __name__ == "__main__":
    main()
