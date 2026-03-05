# Contributing

Thanks for your interest in improving the 3D Website Architect skill.

## How to Contribute

### Improving the Skill

The skill lives in `skills/3d-website-architect/SKILL.md`. When editing:

- Keep the file under 700 lines (currently 633) — if it grows beyond that,
  move detail into `references/` files
- Explain *why* a design or 3D principle matters, not just *what* to do
- Avoid rigid MUST/NEVER rules — explain the reasoning so the agent can
  generalize to new scenarios
- Test your changes against the eval cases before submitting

### Improving References

Reference files live in `skills/3d-website-architect/references/`:

- **design-systems.md** — Color palettes, typography, spacing, 3D materials
- **3d-integration.md** — Three.js / React Three Fiber patterns and recipes
- **animation-patterns.md** — Framer Motion, GSAP, CSS animation cookbook

These are loaded on demand by the agent, so they can be longer than SKILL.md.
Include a table of contents for files over 300 lines.

### Adding Test Cases

Test cases are in `skills/3d-website-architect/evals/evals.json`. Good test
cases:

- Use realistic, detailed prompts (not "build a 3D page")
- Cover different niches (AI, cybersecurity, creative, gaming, etc.)
- Include 10-16 verifiable assertions each
- Test edge cases (no 3D, different frameworks, specific 3D elements)
- Include assertions for 3D-specific quality (Suspense wrapping, mobile fallback,
  post-processing, loading states)

### Adding Examples

Drop new examples in `examples/` as JSON files following the existing format:

```json
{
  "name": "Descriptive Name",
  "prompt": "The full user prompt",
  "expected": {
    "framework": "Tech stack",
    "styling": "CSS approach",
    "theme": "light or dark",
    "sections": ["list", "of", "sections"],
    "3d_elements": ["list", "of", "3D", "elements"],
    "animations": ["list", "of", "animation", "types"],
    "design_notes": "What makes the design appropriate for this niche"
  }
}
```

### Adding New 3D Scene Recipes

If you have a great Three.js pattern (new geometry, shader, or interaction
model), add it to `references/3d-integration.md` under the appropriate section.
Include:

- A brief explanation of when to use it
- Complete working code (TypeScript + React Three Fiber)
- Performance notes (triangle count, GPU impact)

## Development Setup

```bash
# Clone
git clone https://github.com/deveshpunjabi/3d-website-architect.git
cd 3d-website-architect

# Validate the skill
python scripts/validate_skill.py skills/3d-website-architect/SKILL.md

# View eval summary
python scripts/run_evals.py skills/3d-website-architect/evals/evals.json

# Run tests
python -m pytest tests/ -v
```

## Pull Request Process

1. Fork and create a branch (`git checkout -b add-globe-recipe`)
2. Make your changes
3. Run `python -m pytest tests/ -v` — all tests must pass
4. Run `python scripts/validate_skill.py skills/3d-website-architect/SKILL.md`
5. Submit a PR with a clear description of what changed and why

## Code of Conduct

Be respectful. Focus on improving the quality of AI-generated immersive web
experiences for everyone.
