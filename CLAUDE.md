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
| HTML presentation rules | `agents.md` |
| Slidev/Vue skill (PPT conversion, interactive decks) | `SKILL.md` |
| Style preset reference | `STYLE_PRESETS.md` |

---

## Project Structure

```
precalculus_slides/
├── *.html                        HTML slide decks (no build step; load shared assets/)
├── assets/
│   ├── slides-core.css           Shared baseline CSS for all decks
│   └── slides-core.js            Shared SlidePresentation engine (window.SlidesCore)
├── *-assets/                     Image assets extracted from source PPTs
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
├── agents.md                     HTML presentation architecture and patterns
├── SKILL.md                      Slidev skill prompt (PPT → Slidev conversion)
└── STYLE_PRESETS.md              10 named visual styles with full specs
```

---

## Before Writing Any Code

1. **Check `COMPONENT_REGISTRY.md`** — the component you need may already exist.
2. **Check `CONVENTIONS.md`** — colors, naming, slider ranges, SVG rules.
3. **Check `CHANGELOG.md`** — understand current project status and what's in progress.
4. **Read the relevant skill** — `SKILL.md` for Slidev, `agents.md` for HTML.

### Updating an Older HTML Presentation?

> **Stop. Check `agents.md` → "Rebuild Checklist" first.**

Presentations built before the 5.5 standard use a legacy architecture (scroll-snap, opacity transitions, HTML-entity math) that is **incompatible with CSS patches**. Attempting to restyle legacy presentations by tweaking CSS on top of the old structure will fail — font sizes compound incorrectly, steps clip KaTeX math, and content overflows.

**If the presentation doesn't match the 5.5 architecture → rebuild it from scratch** using the skeleton in `agents.md`. This means extracting all content (text, math, SVGs) and re-assembling it in the current template. See `agents.md` for the full rebuild checklist and lessons learned.

---

## Output Format Rules (Summary)

### HTML Presentations
- Single `.html` file per deck. No npm, no build step, no frameworks.
- Decks link the shared `assets/slides-core.css` + `assets/slides-core.js` (one source of truth for layout, components, and the slide engine).
- Per-deck JS init: `<script>SlidesCore.init({ sectionTargets: [...] });</script>`.
- Deck-specific CSS goes in a small inline `<style>` block AFTER the `<link>` (e.g. `.read-aloud` in 6.1, modals in 6.3, SVG `.exp-*` in 6.4).
- All math rendered via KaTeX (`\[ \]` display, `\( \)` inline). No HTML entities or Unicode math.
- Follow the HoffMath Classroom architecture in `agents.md` exactly.
- Reference implementation: `6.7-conditional-probability.html` (canonical for the new shared-assets pattern).

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
| 3 | Rational Functions — Features | ✅ Complete | — |
| 3 | Rational Functions — Graphing | ✅ Complete | — |
| 4 | Trig Review (4.1–4.5) | ✅ Complete | — |
| 4 | Spaghetti Trig Activity | ✅ Complete | — |
| 4.6 | Graphs of Sine & Cosine | ✅ Complete | 🔄 Prototype |
| 4.6b | Graphs of Sine & Cosine Pt 2 | ✅ Complete | — |
| 4.7 | Modeling with Sine & Cosine | ✅ Complete | — |
| 4.8 | Graphs of Other Trig Functions | ✅ Complete | — |
| 4.9 | Inverse Trig Functions | ✅ Complete (rebuilt to 5.5 standard) | 🔄 Prototype |
| 5.1 | Using Fundamental Identities | ✅ Complete | — |
| 5.2 | Verifying Trig Identities | ✅ Complete | — |
| 5.3 | Solving Trig Equations | ✅ Complete | — |
| 5.4 | Sum and Difference Identities | ✅ Complete | — |
| 5.5 | Double &amp; Half Angle Identities | ✅ Complete | — |
| 6.1 | Sequences | ✅ Complete | — |
| 6.2 | Arithmetic Sequences | ✅ Complete | — |
| 6.3 | Geometric Sequences | ✅ Complete | — |
| 6.4 | The Binomial Theorem | ✅ Complete | — |
| 6.5 | Counting Principles | ✅ Complete | — |
| 6.6 | Probability | ✅ Complete | — |
| 6.7 | Conditional Probability | ✅ Complete | — |

**Next up:** Continue remaining precalculus HTML decks and add supporting review materials where needed.

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
