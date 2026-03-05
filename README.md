# 3D Website Architect

A professional AI development skill that trains coding agents and LLMs to design,
build, test, and deploy modern premium websites with advanced animations and 3D
interactive experiences using Three.js, React Three Fiber, GSAP, and Framer Motion.

Instead of generating flat, generic templates, the agent thinks like a senior
frontend engineer, UI/UX designer, creative developer, 3D web developer, and
product designer — all at once. The result resembles award-winning websites
featured on Awwwards, not cookie-cutter layouts.

## How It Works

When you ask your coding agent to "build me an immersive landing page" or "create
a website with 3D elements", the skill automatically activates. It follows a
**13-Step Immersive Design Process** — a structured reasoning framework that
ensures every design, animation, and 3D decision is intentional:

1. **Product Understanding** — identifies product type, audience, value proposition,
   and conversion goal with niche-aware design direction
2. **Visual Inspiration Research** — references Awwwards-quality patterns: dark
   gradients, glassmorphism, bold typography, cinematic 3D hero sections
3. **Design System Creation** — establishes typography pairings, color palette with
   3D material colors, spacing scale, and shadow system
4. **Website Structure** — maps section hierarchy before coding
   (hero → social proof → features → interactive demo → pricing → CTA)
5. **Component Architecture** — builds modular, typed components including dedicated
   `three/` and `animations/` directories
6. **Advanced Animation System** — integrates Framer Motion scroll reveals, GSAP
   timelines, micro-interactions, and choreographed scroll sequences
7. **3D Interactive Experience** — creates Three.js/R3F scenes: floating geometry,
   globes, particle fields, morphing blobs, product viewers with post-processing
8. **Frontend Technology Stack** — Next.js, TypeScript, Tailwind, React Three Fiber,
   Framer Motion, GSAP
9. **Project Structure** — organized codebase with `components/three/`, `animations/`,
   `lib/`, `public/models/`
10. **Performance Optimization** — lazy-loaded 3D, compressed assets, 60fps targets,
    performance budgets
11. **Responsive Design** — pixel-perfect on all devices with progressive 3D
    degradation (full scene → simplified → CSS fallback)
12. **Testing & Quality Assurance** — Lighthouse audits, frame rate monitoring,
    WebGL compatibility, accessibility checks
13. **Production Build & Deployment** — optimized bundles for Vercel, Netlify,
    or Cloudflare Pages

The result is a frontend that looks like it came from a top-tier creative studio,
with immersive 3D elements that enhance the product narrative.

## Installation

### Claude Code

```bash
npx skills add deveshpunjabi/3d-website-architect
```

### Cursor

Copy the `skills/3d-website-architect/` folder into your project's
`.cursor/skills/` directory.

### Manual (Any Agent)

Copy the `skills/3d-website-architect/` directory into your agent's skills
folder. The skill is Markdown-based — no runtime dependencies required.

### Verify It Works

Start a new session and ask something like *"build me a premium landing page for
my AI startup with a 3D hero section and scroll animations"*. The agent should
analyze the product, plan a design system with 3D materials, and build an
immersive interface instead of jumping straight into generic code.

## What's Inside

### Skill

- **3d-website-architect** — 13-step Immersive Design Process: product analysis →
  visual research → design system (with 3D material palettes) → website structure →
  component architecture → advanced animation system → 3D interactive experience →
  tech stack → project structure → performance optimization → responsive 3D strategy →
  testing → production deployment. Includes niche-specific guidance for 10 industries,
  anti-pattern prevention, and cinematic 3D techniques.

### Reference Documents

- **references/design-systems.md** — Complete design system reference: typography
  pairings, 6 niche-specific color palettes (AI/SaaS, cybersecurity, creative,
  fintech, Web3, gaming), gradient/glow CSS recipes, glassmorphism patterns, spacing
  scales, shadow systems, and Three.js material palettes matched to 2D design tokens.

- **references/3d-integration.md** — Full Three.js/React Three Fiber reference:
  canvas setup, lighting systems, scene recipes (floating geometry, globe, particles,
  morphing blobs), shader materials, post-processing (bloom, chromatic aberration),
  mouse/scroll interaction, performance optimization (instanced meshes, dynamic
  imports), responsive 3D with device detection, WebGL error boundaries, and glTF
  model loading with Draco compression.

- **references/animation-patterns.md** — Animation cookbook: Framer Motion patterns
  (scroll reveal, stagger containers, hero entrance, counter animation, 3D tilt
  cards), GSAP patterns (pinned sections, horizontal scroll, text reveal, parallax
  layers), scroll choreography timing tables, micro-interactions (magnetic buttons,
  glow borders), page transitions, CSS recipes, performance guidelines, and
  accessibility (reduced motion support).

### Niche-Aware Design + 3D Direction

| Niche | Design Direction | 3D Opportunity |
|-------|-----------------|----------------|
| AI / ML platforms | Dark themes, glowing accents, futuristic gradients | Neural network viz, AI spheres, particle brains |
| Developer tools | Monospace accents, high-contrast, minimal | Rotating code blocks, floating geometry |
| Cybersecurity | Dark UI, terminal aesthetics, alert-driven | Shield models, data flow particles, globe |
| Creative agencies | Bold typography, warm tones, personality | Interactive art, morphing shapes |
| SaaS startups | Hero-driven, social proof, strong CTAs | Floating product mockups, abstract shapes |
| E-commerce | Product-focused, prominent CTAs, trust badges | 3D product viewers, 360° rotation |
| Fintech | Trust-heavy, clean, data-dense | Globe with transactions, 3D charts |
| Gaming | Vibrant, immersive, full-bleed | Character models, particle explosions |
| Portfolio | Scroll-driven narratives, personal brand | Scene transitions, camera fly-throughs |
| Web3 / Blockchain | Futuristic, neon, decentralized | Token viz, node networks, holographic UI |

### Anti-Patterns Prevented

| Anti-Pattern | What Goes Wrong |
|-------------|----------------|
| 3D carnival | Too many 3D elements competing for attention |
| Performance blindness | Beautiful but loads in 8 seconds |
| Mobile neglect | 3D crashes on phones without fallback |
| Rainbow soup | Too many unrelated colors |
| Shader overkill | Complex shaders tank frame rate |
| Animation overload | Everything moves, nothing rests |
| Decorative 3D | 3D elements with no product connection |
| Bootstrap syndrome | Default template look with swapped colors |
| Hover-only 3D | Touch devices can't interact |
| Wall of identical cards | No visual hierarchy |

## Project Structure

```
3d-website-architect/
├── skills/
│   └── 3d-website-architect/
│       ├── SKILL.md                        # Core skill (633 lines, 13-step process)
│       ├── references/
│       │   ├── design-systems.md           # Design system + 3D material reference
│       │   ├── 3d-integration.md           # Three.js / R3F complete reference
│       │   └── animation-patterns.md       # Framer Motion + GSAP cookbook
│       └── evals/
│           └── evals.json                  # 3 test cases, 45 assertions
├── examples/
│   ├── README.md                           # Example prompts & expected outputs
│   ├── ai-code-review-landing.json         # AI platform with 3D hero (CodeLens AI)
│   ├── creative-studio-portfolio.json      # Agency portfolio with morphing blob
│   └── cybersecurity-landing.json          # Security product with 3D globe
├── scripts/
│   ├── validate_skill.py                   # Validate SKILL.md structure
│   └── run_evals.py                        # Print eval summary
├── tests/
│   ├── test_validate_skill.py              # Skill validator tests (6 tests)
│   └── test_evals.py                       # Eval integrity tests (7 tests)
├── docs/
│   └── SKILL-GUIDE.md                      # How to customize or extend
├── .github/
│   └── workflows/
│       └── ci.yml                          # GitHub Actions CI pipeline
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Test Cases

| # | Scenario | Stack | Key Checks |
|---|----------|-------|------------|
| 1 | AI code review platform (CodeLens AI) | Next.js + Tailwind + R3F | 3D hero scene, bloom post-processing, scroll animations, 3-tier pricing |
| 2 | Creative studio portfolio (Nebula Creative) | Next.js + Tailwind + R3F + GSAP | Morphing blob, mouse-reactive 3D, GSAP text reveals, warm palette |
| 3 | Cybersecurity platform (ShieldNet) | Next.js + Tailwind + R3F | 3D globe with connections, animated stat counters, enterprise design |

3 test cases with 45 total verifiable assertions.

## Scripts

```bash
# Validate SKILL.md structure and frontmatter
python scripts/validate_skill.py skills/3d-website-architect/SKILL.md

# View eval summary
python scripts/run_evals.py skills/3d-website-architect/evals/evals.json

# Run all tests (13 tests)
python -m pytest tests/ -v
```

## Philosophy

- **Design-first** — understand the product before writing code
- **3D with purpose** — every 3D element reinforces the product narrative
- **Niche-aware** — every industry has visual and interaction conventions
- **Performance-conscious** — beautiful and fast, not one or the other
- **Progressive enhancement** — full 3D on desktop, graceful fallbacks on mobile
- **Production-ready** — real TypeScript code, not proof-of-concept demos

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

The short version:

1. Fork the repository
2. Create a branch for your changes
3. Follow the patterns in the existing skill
4. Run `python -m pytest tests/ -v` to verify nothing breaks
5. Submit a PR

## License

MIT — see [LICENSE](LICENSE)
