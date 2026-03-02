# Changelog

Tracks what was built, when it was added, and the current state of the project.
Update this file whenever a new presentation, component, scene, or major feature is added.

---

## Current Status (as of 2026-03-01)

### Recently Added

**HTML Presentations:**
- `5.1-fundamental-identities.html` — Using Fundamental Identities (7 examples, HoffMath Classroom style)
- `5.2-verifying-trig-identities.html` — Verifying Trig Identities (6 examples + alternate methods, HoffMath Classroom style)
- `5.3-solving-trig-equations.html` — Solving Trig Equations (7 examples, caution/exception slides, HoffMath Classroom style)
- `5.4-sum-and-difference.html` — Sum and Difference Identities (7 examples, formula reference card, two-problem layouts, HoffMath Classroom style)
- `5.5-double-half-angle.html` — Double &amp; Half Angle Identities (6 examples, two reference cards, three-part answer grid, quadrant analysis, HoffMath Classroom style)

---

## Current Status (as of 2026-02-26)

### What's Done

**HTML Presentations (production-ready):**
- Unit 3: Rational Functions — Features and Graphing
- Unit 4: Trig Review (4.1–4.5), Spaghetti Activity, 4.6, 4.6b, 4.7, 4.8, 4.9

**Slidev Prototypes (proof-of-concept, not full decks):**
- `precalculus-prototype/` — covers special angles + trig modeling parameters
- `4.9-inverse-trig-prototype/` — arcsin definition, examples, interactive graph

**Project Infrastructure:**
- `agents.md` — full HTML presentation architecture guide
- `SKILL.md` — Slidev/Vue skill prompt for AI-assisted development
- `STYLE_PRESETS.md` — 10 named visual styles
- `CLAUDE.md` — AI working guide (this session)
- `CONVENTIONS.md` — unified color/naming/math conventions (this session)
- `COMPONENT_REGISTRY.md` — component catalog (this session)
- `manim/shared/colors.py` — Manim color constants (this session)

### What's In Progress

- Expanding Slidev prototypes into full lesson decks (4.6 → 4.9)
- Establishing Manim animation pipeline

### What's Next

- Build `GraphFrame.vue` and `FunctionPlot.vue` as foundational graphing primitives
- Build `TrigGraph.vue` with A/B/C/D sliders for 4.6 and 4.7
- Build `UnitCircleExplorer.vue` for trig review and 4.9
- First Manim scene: trig transformation animation for 4.6
- Convert 4.6 HTML deck to full Slidev deck using new components

---

## History

### 2026-02-26

**4.9 Slidev prototype stabilized and preview-verified**

- Added `slidev/4.9-inverse-trig-prototype/` as a parallel Slidev project (does
  not replace the production HTML deck `4.9-inverse-trig-functions.html`)
- Built a working prototype deck with:
  - `ThemeToggle.vue` + `global-top.vue` (dark/light toggle with system default)
  - `ArcsinGraphDemo.vue` (interactive SVG graph + slider/readouts)
  - click-to-reveal worked examples and composition example
  - KaTeX math rendering on concept slides
- Verified local `slidev build` succeeds for the prototype
- Added project `.gitignore` to prevent committing `node_modules/` and build
  outputs as the repo grows
- Note: the inverse-sine concept slide currently uses a markdown-first layout
  (instead of the earlier SVG-heavy raw slide) for parser stability in Slidev

### 2026-02-26

**Project scaffold created**
- Added `CLAUDE.md` — AI working guide with project map, quick links, active curriculum table
- Added `CONVENTIONS.md` — unified color, font, naming, slider, SVG, and math conventions
- Added `COMPONENT_REGISTRY.md` — catalog of existing components + planned components
- Added `CHANGELOG.md` — this file
- Added `manim/shared/colors.py` — Manim color/font constants matching Slidev palette

---

### 2026-02-25

**Slidev migration + project documentation**

- `0020b69` Added `slidev/precalculus-prototype/` — first Slidev deck covering
  special angles and sine modeling parameters. Establishes Space Grotesk +
  IBM Plex font stack and dark/light color system.

- Added `slidev/4.9-inverse-trig-prototype/` prototype work (finalized and
  build-verified on 2026-02-26) — 6-slide prototype with:
  - `ArcsinGraphDemo.vue` — interactive arcsin slider + SVG graph
  - `ThemeToggle.vue` — dark/light mode with localStorage + system preference
  - `global-top.vue` — global theme toggle overlay
  - KaTeX math rendering for inverse trig notation
  - Click-to-reveal (`v-click`, `<v-clicks>`) worked examples

- `6144421` Added Slidev VS Code workspace configs and slide assets

- `2b459a4` Updated `index.html` and `README.md` to include 4.8 and 4.9 links

- `9071641` Added graphical visualization slide (interactive arcsin graph demo)
  and enhanced step-by-step explanations for inverse trig examples in HTML deck

- `7c079fa` Standardized mathematical expressions using LaTeX syntax;
  converted HTML tables to Markdown format throughout 4.9 HTML deck

- `f70e7e1` Added `SKILL.md` (new) and `STYLE_PRESETS.md` (10 theme presets)

- `805e73d`, `5d08a20` Iterated on Slidev skill prompt alignment

---

### 2026-02-17

**Section 4.8 added**

- `f51267d` Added `4.8-graphs-other-trig-functions.html` — interactive HTML
  deck for tangent, cotangent, secant, and cosecant graphs. 82 image assets
  in `4.8-assets/`.

---

### 2026-02-11

**Section 4.7 added; 4.6b updated**

- `a6f6659` Added `4.7-modeling-sine-cosine.html` — sine/cosine modeling
  with real-world applications. 19 image assets in `4.7-assets/`.

- `a8924a5`, `221c9e9` Updated `index.html` and replaced `4.6b` with improved version.

---

### 2026-02-04

**Portal and hosting setup**

- `85c03fa`–`f84ceff` Set up `index.html` as the landing portal for all decks.
  Fixed links; added GitHub Pages live demo link.

- `ecf14ee` Added link to live online demo:
  https://kirkmanamos.github.io/Precalculus_Slides/

---

### 2026-02-03

**Project initialized; first five decks added**

- `0dc5c7d` Created `README.md` — initial project documentation.

- `dfff9d4` Added `4.6-graphs-sine-cosine.html` (first trig graphing deck)
  and `trig-review.html` (review of 4.1–4.5).

- `1eae35b` Created `index.html` with basic HTML structure.

- `2c4e602` Added `4.6b-graphs-sine-cosine-part2.html` and 7 image assets.

- `038a9f8`, `924f10b` Added Unit 3 Rational Functions (`RationalFeatures.html`,
  `RationalGraphing.html`) to `index.html`.

- `6549435`–`c48e851` Fixed unit labels and links; added Spaghetti Trig Activity.

- `Spaghetti_Trig_Slides.html` — hands-on spaghetti unit circle activity deck.

---

## Update Instructions

Add a new entry at the top of the History section when:
- A new HTML presentation is completed
- A new Slidev deck or prototype is added
- A new Vue component or composable is built
- A new Manim scene is created
- A major feature (new interactivity, new section coverage) is added

Format:
```
### YYYY-MM-DD

**Short description**

- What was added/changed and why
- File paths for new files
- Commit hash(es) if committing
```
