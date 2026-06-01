# Precalculus Teaching Materials — Claude Code Guide

> Read this file before doing anything else. It is the single source of truth
> for project structure, conventions, and what already exists.

---

## Quick Links

| What you need | File |
|---|---|
| Visual style (colors, fonts, themes) | `CONVENTIONS.md` |
| What components/scenes already exist | `COMPONENT_REGISTRY.md` |
| History of what was built and when | `CHANGELOG.md` |
| HTML presentation rules | `AGENTS.md` |
| Cross-agent handoff notes | `AGENT_HANDOFF.md` |
| Slidev/Vue skill (PPT conversion, interactive decks) | `SKILL.md` |
| Style preset reference | `STYLE_PRESETS.md` |
| Structural deck verifier (run before finishing HTML edits) | `verify_decks.py` |

---

## Project Structure

```
precalculus_slides/
├── *.html                        HTML slide decks (no build step; load shared assets/)
├── assets/
│   ├── slides-core.css           Shared baseline CSS for all decks
│   └── slides-core.js            Shared SlidePresentation engine (window.SlidesCore)
├── *-assets/                     Image assets extracted from source PPTs
├── verify_decks.py               Structural checker for shared-engine decks (run before committing HTML)
│
├── slidev/                       Slidev (Vue 3) interactive decks
│   ├── precalculus-prototype/    Main prototype — trig graphing, sliders
│   ├── 4.9-inverse-trig-prototype/  Most developed — ArcsinGraphDemo, ThemeToggle
│   └── trial-run/                Minimal starter template
│
├── manim/                        Manim animation pipeline (in development)
│   └── shared/                   Shared constants — import before writing any scene
│       ├── colors.py             Color constants (must match HTML/Slidev palette)
│       ├── styles.py             Text and Mobject styles (create when needed)
│       └── helpers.py            Reusable scene utilities (create when needed)
│
├── CLAUDE.md                     ← YOU ARE HERE
├── CONVENTIONS.md                Unified conventions: colors, naming, math, SVG
├── COMPONENT_REGISTRY.md         Catalog of all reusable Vue components + Manim scenes
├── CHANGELOG.md                  What was built, when, and current status
├── AGENTS.md                     HTML presentation architecture and patterns
├── AGENT_HANDOFF.md              Current cross-agent handoff notes
├── SKILL.md                      Slidev skill prompt (PPT → Slidev conversion)
└── STYLE_PRESETS.md              10 named visual styles with full specs
```

---

## Before Writing Any Code

1. **Check `COMPONENT_REGISTRY.md`** — the component you need may already exist.
2. **Check `CONVENTIONS.md`** — colors, naming, slider ranges, SVG rules.
3. **Check `CHANGELOG.md`** — understand current project status and what's in progress.
4. **Check `AGENT_HANDOFF.md`** — continue any active handoff before starting overlapping work.
5. **Read the relevant skill** — `SKILL.md` for Slidev, `AGENTS.md` for HTML.

### Updating an Older HTML Presentation?

> **Stop. Check `AGENTS.md` → "Rebuild Checklist" first.**

Presentations built before the 5.5 standard use a legacy architecture (scroll-snap, opacity transitions, HTML-entity math) that is **incompatible with CSS patches**. Attempting to restyle legacy presentations by tweaking CSS on top of the old structure will fail — font sizes compound incorrectly, steps clip KaTeX math, and content overflows.

**If the presentation doesn't match the 5.5 architecture → rebuild it from scratch** using the skeleton in `AGENTS.md`. This means extracting all content (text, math, SVGs) and re-assembling it in the current template. See `AGENTS.md` for the full rebuild checklist and lessons learned.

---

## Output Format Rules (Summary)

### HTML Presentations
- Single `.html` file per deck. No npm, no build step, no frameworks.
- Decks link the shared `assets/slides-core.css` + `assets/slides-core.js` (one source of truth for layout, components, and the slide engine).
- Per-deck JS init: `<script>SlidesCore.init({ sectionTargets: [...] });</script>`.
- Deck-specific CSS goes in a small inline `<style>` block AFTER the `<link>` (e.g. `.read-aloud` in 6.1, modals in 6.3, SVG `.exp-*` in 6.4).
- All math rendered via KaTeX (`\[ \]` display, `\( \)` inline). No HTML entities or Unicode math.
- Follow the HoffMath Classroom architecture in `AGENTS.md` exactly.
- Reference implementation: `6.7-conditional-probability.html` (canonical for the new shared-assets pattern).
- **Before finishing any HTML edit, run `python3 verify_decks.py`** (repo root). It checks `<section>` balance, KaTeX `\(\)`/`\[\]` balance, shared-asset wiring, and `data-steps` on every shared-engine deck. Must exit 0.

### LaTeX Guided Notes (companion repo)
- The guided notes live in a **separate repo**: `/Users/kirkmanamos/Desktop/precalculus`, organized as `Unit N - .../notes/`.
- There is **no single root `build.sh`** — each unit has its own `notes/build.sh` that compiles **four variants** (`student-regular`, `student-honors`, `teacher-regular`, `teacher-honors`). Run it from inside that unit's `notes/` folder.
- When a slide deck and its matching notes section share a value (worked examples, coordinates, final answers), keep them **identical**. A mismatch in either is a bug — fix both and rebuild the affected unit's four variants.

### Slidev / Vue Decks
- Stack: Slidev v52.2.0, Vue 3, KaTeX for math, SVG for graphs.
- Fonts: Space Grotesk (display) + IBM Plex Sans/Mono (body).
- New reusable components go in `components/graphs/` or `components/lessons/`.
- Log every new component in `COMPONENT_REGISTRY.md` before finishing.
- Follow the skill flow in `SKILL.md`.

### Manim Scenes
- Always `from manim.shared.colors import *` at the top of every scene file.
- Scene files: `unit_topic_scene.py` (snake_case).
- Log every new scene in `COMPONENT_REGISTRY.md`.
- Export to `public/manim/` inside the relevant Slidev deck for embedding.

---

## Active Curriculum

| Unit | Topic | HTML Status | Slidev Status |
|---|---|---|---|
| 1.1 | Slopes and Equations of Lines | ✅ Complete | — |
| 1.2 | Non-Linear Inequalities | ✅ Complete | — |
| 1.3 | Functions | ✅ Complete | — |
| 1.4 | Graphs of Functions | ✅ Complete | — |
| 1.5 | Transformations of Functions | ✅ Complete | — |
| 1.6 | Operations with Functions | ✅ Complete | — |
| 1.7 | Inverse Functions | ✅ Complete | — |
| 2.1 | Quadratic Functions | ✅ Complete | — |
| 2.2 | Graphs of Polynomial Functions | ✅ Complete | — |
| 2.3 | Zeros of Polynomial Functions | ✅ Complete | — |
| 2.4 | Dividing Polynomials | ✅ Complete | — |
| 2.5 | Complex Numbers | ✅ Complete | — |
| 2.6 | Fundamental Theorem of Algebra | ✅ Complete | — |
| 2.7 | Rational Functions and Asymptotes | ✅ Complete | — |
| 2.8 | Graphs of Rational Functions | ✅ Complete | — |
| 3.1 | Exponential Functions &amp; Their Graphs | ✅ Complete | — |
| 3.2 | Logarithmic Functions &amp; Their Graphs | ✅ Complete | — |
| 3.3 | Properties of Logarithms | ✅ Complete | — |
| 3.4 | Solving Exponential &amp; Log Equations | ✅ Complete | — |
| 3.5 | Exponential Applications | ✅ Complete | — |
| 3 (suppl.) | Rational Functions — Features | ✅ Complete | — |
| 3 (suppl.) | Rational Functions — Graphing | ✅ Complete | — |
| 4.1 | Right Triangle Trigonometry | ✅ Complete (5.5 standard) | — |
| 4.2 | Radian and Degree Measure | ✅ Complete (5.5 standard) | — |
| 4.3 | Linear and Angular Speed | ✅ Complete (5.5 standard) | — |
| 4.4 | Trig Functions: The Unit Circle | ✅ Complete (5.5 standard) | — |
| 4.5 | Trig Functions of Any Angle | ✅ Complete (5.5 standard) | — |
| 4 (legacy) | Trig Review (4.1–4.5) | ✅ Complete (legacy `trig-review.html`) | — |
| 4 | Spaghetti Trig Activity | ✅ Complete | — |
| 5.1 | Graphs of Sine & Cosine | ✅ Complete (5.5 standard) | 🔄 Prototype |
| 5.2 | Graphs of Sine & Cosine Pt 2 | ✅ Complete (5.5 standard) | — |
| 5.3 | Modeling with Sine & Cosine | ✅ Complete (5.5 standard) | — |
| 5.4 | Graphs of Other Trig Functions | ✅ Complete (5.5 standard) | — |
| 5.5 | Inverse Trig Functions | ✅ Complete (5.5 standard) | 🔄 Prototype |
| 6.1 | Using Fundamental Identities | ✅ Complete (shared-assets cleanup) | — |
| 6.2 | Verifying Trig Identities | ✅ Complete (shared-assets cleanup) | — |
| 6.3 | Solving Trig Equations | ✅ Complete (shared-assets cleanup) | — |
| 6.4 | Sum and Difference Identities | ✅ Complete (shared-assets cleanup) | — |
| 6.5 | Double &amp; Half Angle Identities | ✅ Complete (shared-assets cleanup) | — |
| 7.1 | Sequences | ✅ Complete | — |
| 7.2 | Arithmetic Sequences | ✅ Complete | — |
| 7.3 | Geometric Sequences | ✅ Complete | — |
| 7.4 | The Binomial Theorem | ✅ Complete | — |
| 7.5 | Counting Principles | ✅ Complete | — |
| 7.6 | Probability | ✅ Complete | — |
| 7.7 | Conditional Probability | ✅ Complete | — |
| 8.1 | Polar Coordinates | ✅ Complete (5.5 standard) | — |
| 8.2 | Polar Graphs | ✅ Complete (5.5 standard) | — |
| 8.3 | Polar Form of Complex Numbers | ✅ Complete (5.5 standard) | — |
| 8.4 | Parametric Equations | ✅ Complete (5.5 standard) | — |
| 8.5 | Parametric Graphs | ✅ Complete (5.5 standard) | — |
| 8.6 | Vectors | ✅ Complete (5.5 standard) | — |
| 9.1 | Finding Limits: Numerical & Graphical | ✅ Complete (5.5 standard) | — |
| 9.2 | Finding Limits: Properties of Limits | ✅ Complete (5.5 standard) | — |
| 9.3 | Continuity | ✅ Complete (5.5 standard) | — |
| 9.4 | Derivatives | ✅ Complete (5.5 standard) | — |

**Next up:** Unit 1 complete (1.1–1.7); **Unit 2 complete (2.1–2.8)**; **Unit 3 complete (3.1–3.5)**; **Unit 4 sections 4.1–4.5 complete**; **Unit 5 sections 5.1–5.5 newly built or rebuilt to 5.5 standard**; **Unit 6 daily decks now use the shared-assets engine while preserving their existing organization and visual identity**; **Unit 7 complete (7.1–7.7)**; **Unit 8 sections 8.1–8.6 complete**; **Unit 9 sections 9.1–9.4 complete**. Pre-existing supplemental Rational Functions decks remain in place. Up next: other supplemental review materials.

---

## Math Conventions (Quick Reference)

Full details in `CONVENTIONS.md`. Critical rules:

- **Quadrant colors:** QI green `#4ade80`, QII cyan `#22d3ee`, QIII pink `#f472b6`, QIV gold `#fbbf24`
- **Triangle sides:** x=cyan, y=pink, r=green
- **SVG y-axis is inverted** — Cartesian (x, y) plots at SVG (x·scale, −y·scale)
- **Exact values** for special angles (½, √3/2, π/6, etc.), not decimals
- **Teacher-controlled reveals** on all worked examples (click/space to advance)

---

## Updating This File

After any significant addition (new component, new deck, new Manim scene):
1. Update `COMPONENT_REGISTRY.md` with the new item.
2. Add an entry to `CHANGELOG.md`.
3. Update the Active Curriculum table above if a deck status changed.
