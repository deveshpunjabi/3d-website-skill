# 3D Website Architect — Skill Guide

This guide explains how to use, customize, and extend the **3d-website-architect** skill.

---

## How the Skill Triggers

The skill activates when the agent detects prompts related to:

- Building modern websites with **3D interactions** or **Three.js / React Three Fiber**
- Designing **premium landing pages** with animations and immersive visuals
- Creating **SaaS**, **AI/ML**, **Web3**, **cybersecurity**, or **gaming** websites
- Requests mentioning **GSAP**, **Framer Motion**, **particle effects**, **3D hero sections**
- Any prompt asking for a **visually stunning**, **interactive**, or **immersive** web experience

The YAML `description` field in `SKILL.md` controls triggering — keep it rich with relevant keywords.

---

## Default Tech Stack

The skill defaults to:

| Layer | Technology |
|-------|------------|
| Framework | Next.js 14+ (App Router) |
| Language | TypeScript |
| Styling | Tailwind CSS |
| 3D Engine | Three.js + React Three Fiber |
| 3D Helpers | @react-three/drei, @react-three/postprocessing |
| Animation | Framer Motion + GSAP + ScrollTrigger |

To adjust defaults, edit the **Step 8: Frontend Technology Stack** section in `SKILL.md`.

---

## Adding New Niches

The skill includes a niche lookup table in **Step 1**. To add a new niche:

1. Open `skills/3d-website-architect/SKILL.md`
2. Find the `| Niche | Style Keywords | 3D Opportunity |` table
3. Add a new row with the niche name, style keywords, and 3D opportunities
4. Optionally add a matching color palette in `references/design-systems.md`
5. Add a matching eval case in `evals/evals.json`

---

## Adjusting Design Standards

Design tokens live in `references/design-systems.md`:

- **Typography** — Font pairings, type scales, fluid sizing
- **Colors** — Base palette, niche-specific palettes, 3D material colors
- **Spacing** — Scale system, section spacing
- **Effects** — Glassmorphism, gradients, glows, shadows

---

## Adding Reference Documents

Place new `.md` files in `skills/3d-website-architect/references/`. Common additions:

- `accessibility.md` — WCAG compliance patterns for 3D content
- `seo-patterns.md` — Structured data and meta tag templates
- `cms-integration.md` — Headless CMS patterns (Sanity, Contentful)
- `deployment.md` — Vercel/Netlify deployment configs

Reference the new file from `SKILL.md` so the agent knows to consult it.

---

## Extending with Other Skills

This skill pairs well with:

| Skill | Purpose |
|-------|---------|
| `modern-frontend-design` | General frontend patterns without 3D focus |
| `ui-component-library` | Reusable component systems |
| `api-integration` | Backend/API connection patterns |

---

## Directory Structure

```
skills/3d-website-architect/
├── SKILL.md                         # Core skill instructions
├── evals/
│   └── evals.json                   # Test cases & assertions
└── references/
    ├── design-systems.md            # Design tokens & palettes
    ├── 3d-integration.md            # Three.js / R3F patterns
    └── animation-patterns.md        # Framer Motion + GSAP cookbook
```

## Cross-Agent Compatibility

This skill format is compatible with all major AI coding agents:

| Agent | Skill Location | Trigger Mechanism |
|-------|---------------|-------------------|
| Claude Code | `npx skills add` or `.claude/skills/` | YAML description matching |
| Cursor | `.cursor/skills/` | YAML description matching |
| Windsurf | `.windsurf/skills/` | YAML description matching |
| Cline | `.cline/skills/` | YAML description matching |
| Codex | `.codex/skills/` or `.agents/skills/` | Instruction file loading |
| Aider | Referenced in `.aider.conf` | Direct file reference |
| Gemini | Agent instruction directory | Instruction file loading |

The skill uses standard Markdown with YAML frontmatter — no proprietary
syntax, no agent-specific tags. Any agent that can read Markdown instruction
files can use this skill.

### YAML Frontmatter Fields

| Field | Required | Used By | Purpose |
|-------|----------|---------|---------|
| `name` | Yes | All agents | Skill identifier |
| `description` | Yes | All agents | Trigger matching — when to activate |
| `version` | Recommended | skills.sh, registries | Semantic versioning |
| `author` | Recommended | skills.sh, registries | Creator attribution |
| `tags` | Recommended | Discovery, search | Keywords for finding the skill |

---

## Running Validations

```bash
# Validate skill structure
python scripts/validate_skill.py skills/3d-website-architect/SKILL.md

# View eval summary
python scripts/run_evals.py skills/3d-website-architect/evals/evals.json

# Run all tests
python -m pytest tests/ -v
```

---

## Tips for Skill Authors

1. **Keep SKILL.md focused** — Move detailed code recipes to `references/`
2. **Write rich descriptions** — 40–100 words in the YAML frontmatter for reliable triggering
3. **Test with diverse prompts** — Your evals should cover different niches and complexity levels
4. **Include anti-patterns** — Tell the agent what NOT to do (prevents common mistakes)
5. **Version your changes** — Update `skills-lock.json` when making significant updates
