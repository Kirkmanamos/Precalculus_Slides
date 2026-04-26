# Changelog

Tracks what was built, when it was added, and the current state of the project.
Update this file whenever a new presentation, component, scene, or major feature is added.

---

## 2026-04-22

### New HTML Deck - 5.3 Amplitude-Phase Form

Added `5.3-amplitude-phase-form.html`, a shared-assets HoffMath deck that
replaces the broken raw React component saved as
`5.3-ampliftude-phase-form.html`. The misspelled filename now redirects to the
canonical deck. The new deck includes exact examples, a plain HTML/SVG/JS
interactive coefficient explorer, and a solving example using
\(a\sin x+b\cos x=R\sin(x+\theta)\).

### New Manim Scene - Amplitude-Phase Form

Added a standalone ManimCE concept animation for rewriting a linear combination
of sine and cosine as one shifted sine wave.

- **`manim/scenes/5_4_amplitude_phase_form.py`** - `AmplitudePhaseForm`
  - Starts from `√3 sin x − cos x = 2 sin(x − π/6)` as a concrete hook.
  - Overlays both functions on shared axes and uses a moving vertical guide to
    show matching outputs.
  - Expands `R sin(x + θ)`, boxes matched coefficients, and connects
    `R cos θ = a`, `R sin θ = b`.
  - Builds vector diagrams for `(a,b)` and for `(√3,-1)`, emphasizing
    rectangular-to-polar thinking.
  - Adds a focused phase-angle explanation: use `θ = atan2(b,a)`, compute
    `tan θ = b/a`, use signs to choose the quadrant, then recognize
    `atan2(-1,√3) ≈ −0.524 = −π/6` when an exact special angle is available.
  - Ends with a plain-language summary and the general formula, now held for
    7 seconds so the video does not feel clipped.
- Checks run: Python syntax compile passed; 1080p60 Manim render completed with
  ManimCE v0.19.2.

## 2026-04-19

### New HTML Deck Set - Unit 1: Functions and Their Graphs (1.1–1.7)

Seven new decks covering the complete Unit 1 curriculum. All use the shared-assets architecture (`assets/slides-core.css` + `assets/slides-core.js`). Source material: Hoff Math "Functions and Their Graphs" PPT/PDF set.

| File | Slides | Key patterns |
|---|---|---|
| `1.1-slopes-and-equations-of-lines.html` | 13 | SVG slope diagram with custom labels |
| `1.2-non-linear-inequalities.html` | 14 | Sign-chart step-boxes, SVG number lines, `.sign-pos/.sign-neg` |
| `1.3-functions.html` | 15 | VLT, mapping diagrams, piecewise, `.eq-card.is-fn/.not-fn` |
| `1.4-graphs-of-functions.html` | 14 | Floor/ceiling paired reveals via `MutationObserver`, `.int-table` |
| `1.5-transformations.html` | 12 | Parent gallery 3×2 SVG grid, D.R.S. color arc, `.ans-hide`/`g.svg-step` reveals |
| `1.6-operations-with-functions.html` | 12 | Composition notation, domain intersection, `.compose-table` |
| `1.7-inverse-functions.html` | 12 | SVG mapping diagram with `<tspan>` f⁻¹, HLT one-to-one, `.ll-card.yes/.no` |

**New patterns introduced (documented in `AGENTS.md` Gotchas and `SKILL_HTML.md`):**
- Table-cell reveals: `.ans-cell.ans-hide` (visibility-based, preserves table layout)
- SVG group reveals: `g.svg-step` (opacity-based, preserves inline context)
- `MutationObserver` for paired reveals (multiple elements per click)
- D.R.S. palette: Dilate=orange, Reflect=blue, Shift=green
- Rule: KaTeX auto-render does not walk into SVG `<text>` — use `<tspan>` for italic/superscript

---

## 2026-04-17

### Fill-in-the-blank reveal pattern across Unit 6

All seven Unit 6 HTML decks now mirror the `\blank{}` macros in the LaTeX
teacher notes with inline click-to-reveal blanks. Students see a dashed
placeholder, and each click fills in an orange-highlighted answer aligned
with what they are writing on paper — making it unambiguous where in the
notes the class currently is.

- Shared CSS `.notes-list` + `.fb / .fb-blank / .fb-answer` block added
  after the `.annotation` rule in each file.
- Uses the existing `data-steps` + `.visible` step mechanism (no JS changes).
- Applied to concept/reference slides in **6.1** (sequences, convergent/divergent),
  **6.2** (arithmetic sequence definition, linear/slope, arithmetic means),
  **6.3** (geometric sequence definition, geometric means, infinite sums),
  **6.4** (Binomial Theorem definitions), **6.5** (Counting Principle,
  Permutations, Combinations), **6.6** (vocabulary, probability forms,
  theoretical/experimental, Addition Rule, Multiplication Rule, Complement),
  and **6.7** (Conditional Probability definition).

### Other Unit 6 updates (2026-04-17)
- **6.3**: Moved Ratio Playground to a new slide-7b position immediately
  before the Finite and Infinite Geometric Sums slide to act as a hook for
  partial and infinite sums.
- **6.4**: Realigned example numbering and problems with
  `notes/sections/04-binomial.tex`. Mismatched problems were relabeled as
  "Your Turn" practice slides and retained.

## 2026-04-08

### New HTML Deck Set - Unit 6: Sequences, Series, and Probability

Added a full consolidated Unit 6 HTML deck set in the HoffMath Classroom format.
All seven decks follow the `5.5-double-half-angle.html` architecture with KaTeX,
teacher-paced step reveals, horizontal slide navigation, and the mobile phone patch.

- **`generate_unit6_decks.py`** - New generator that renders the Unit 6 deck set from shared deck definitions and the common 5.5-style shell
- **`6.1-sequences.html`** - Sequences, explicit rules, recursive rules, factorial, and sigma notation
- **`6.2-arithmetic-sequences.html`** - Arithmetic nth-term formulas, arithmetic means, and finite arithmetic sums
- **`6.3-geometric-sequences.html`** - Geometric nth-term formulas, geometric means, finite sums, and infinite sums
- **`6.4-binomial-theorem.html`** - Pascal's Triangle, combinations, binomial expansions, and specific-term problems
- **`6.5-counting-principles.html`** - Fundamental Counting Principle, permutations, combinations, and non-distinct permutations
- **`6.6-probability.html`** - Probability vocabulary, addition and multiplication rules, counting-based probability, and complements
- **`6.7-conditional-probability.html`** - Conditional probability using two-way tables, Venn diagrams, and tree diagrams
- **`README.md`** and **`index.html`** updated with Unit 6 navigation
- **`CLAUDE.md`** active curriculum table updated to mark Unit 6 as complete

### New Manim Scenes - Unit 6 Sequence Concepts

Added two short ManimCE videos for Unit 6.1 sequence foundations plus a scene-spec markdown file.

- **`manim/scenes/6_1_sequence_videos_scenes.md`** - Scene composition notes for the two sequence videos
- **`manim/scenes/6_1_sequence_intro.py`** - `SequenceAsOrderedFunction`
  - Bright, clean introduction to sequences as ordered lists
  - Shows term labels `a_1, a_2, a_3, a_4`, a brief order-matters swap, and a transformation to a discrete graph on default Cartesian axes
  - Ends with the function viewpoint: a sequence is a function on the positive integers
- **`manim/scenes/6_1_convergent_vs_divergent.py`** - `ConvergentVsDivergentSequences`
  - Side-by-side comparison of `a_n = 1/n` and `b_n = (-1)^n`
  - Uses default Cartesian grids, discrete points, a highlighted band around `y = 0`, and escape arrows on the divergent side
  - Closes with a note that `c_n = n` is another classic divergent example
- Low-quality preview renders completed successfully for both scenes with ManimCE v0.19.2

## 2026-03-29

### New Manim Scenes — 5.5 Double & Half-Angle Identities (6 videos)

Created 6 Manim scene files for all worked examples in the 5.5 presentation.
Each uses a **left-2/3 + right-1/3 split layout** (math visuals left, step annotations right).

- **`manim/shared/helpers.py`** — New shared module with layout constants, `build_unit_circle()`, `build_angle_arc()`, `build_reference_triangle()`, `TextPanel` class, `build_result_banner()`, `build_quadrant_highlight()`, `build_terminal_point()`

- **`manim/scenes/5_5_double_angle_given_info.py`** — `DoubleAngleGivenInfo`
  - Find sin(2θ), cos(2θ), tan(2θ) given cos θ = 5/13 in QIV
  - Unit circle + 5-12-13 triangle + formula application, ~26s

- **`manim/scenes/5_5_double_angle_equation.py`** — `DoubleAngleEquation`
  - Solve 2cos x + sin(2x) = 0 on [0, 2π)
  - Identity sub → factor → unit circle solutions, ~27s

- **`manim/scenes/5_5_pattern_recognition.py`** — `PatternRecognition`
  - Rewrite cos²(5α) − sin²(5α) = cos(10α)
  - Color-coded pattern matching with template, ~20s

- **`manim/scenes/5_5_half_angle_exact_value.py`** — `HalfAngleExactValue`
  - Find cos 165° using half-angle (165° = 330°/2)
  - Two angles on unit circle + 30-60-90 triangle + sign from QII, ~24s

- **`manim/scenes/5_5_half_angle_given_info_qi.py`** — `HalfAngleGivenInfoQI`
  - Given sin x = 2/5 in QI, find cos(x/2)
  - Right triangle + quadrant analysis + formula, ~23s

- **`manim/scenes/5_5_half_angle_quadrant_analysis.py`** — `HalfAngleQuadrantAnalysis`
  - Given cos θ = 5/13 in QIV, find sin(θ/2)
  - **Capstone**: shows θ/2 lands in QII (not QIV) — addresses #1 misconception, ~23s

All 6 rendered at 480p15 (low quality preview). Total: ~143s of educational animation.

---

## 2026-03-12

### New Manim Scenes — 5.3 Examples 4 & 5

- **`manim/scenes/5_3_pyth_sub_graphical.py`** — `PythSubGraphicalAnalysis`
  - Graphical solution of `2sin²x + 3cos x - 3 = 0` for all solutions
  - Pythagorean substitution → factor into `(2cos x - 1)(cos x - 1) = 0`
  - Two-panel layout: cos x = 1/2 (green, QI/QIV dots) and cos x = 1 (blue, 3 dots)
  - Both cases valid → double ✓ labels + combined solution banner
  - 58 animations, rendered at 1080p60

- **`manim/scenes/5_3_squaring_graphical.py`** — `SquaringGraphicalAnalysis`
  - Graphical solution of `cos x + 1 = sin x` on [0, 2π)
  - Single-panel: plots y = cos x + 1 (teal) vs y = sin x (pink)
  - Two valid intersections (π/2, π) marked with green ✓
  - Extraneous candidate at 3π/2 highlighted: red ✗ + dashed gap line + annotation
  - Warning box about squaring introducing extraneous solutions
  - 39 animations, rendered at 1080p60

---

## 2026-03-09 (session 2)

### `CotFactoringGraphicalAnalysis` — v2 rebuild

Rebuilt `manim/scenes/5_3_cot_factoring_graphical.py` to fix 4 issues from v1:

1. **Longer intro + "All Solutions" statement** — title and subtitle now hold for
   1.5 s before advancing; subtitle reads "Find: **all solutions** — no domain
   restriction on x" in a styled box.

2. **Cot curve clipping** — replaced raw `np.cos(x)/np.sin(x)` with
   `_cot_clipped(x) = np.clip(cos/sin, -3.75, 3.75)` and reduced plot step to
   `0.005`. Curve now stays entirely within the panel border.
   (`SurroundingRectangle` is visual-only and does not clip rendered content —
   clamping the function value is the only reliable fix.)

3. **Algebra steps phase** (`_phase_math_steps()`) — new phase between intro and
   panels. Shows 3 numbered steps: original → subtract 2cot x → factor. Then the
   zero-product-property split with Case 1 (green) and Case 2 (red) color-coded.
   Warning box: "Do NOT divide by cot x — that erases Case 1!" Bridge line fades
   algebra before panels appear.

4. **Better in-panel annotations** — Panel A now includes a `cot x = cos x/sin x = 0
   ⟹ cos x = 0` annotation explaining the connection to the zeros, plus a general
   solution box `x = π/2 + πn, n ∈ ℤ` inside the panel before it shrinks. Panel B
   adds a gap arrow pointing into the shaded region with label "cos²x never reaches 2".

Rendered: 59 animations, no errors.

---

## Current Status (as of 2026-03-02)

### 4.9 Architectural Rebuild

- **`4.9-inverse-trig-functions.html`** fully rebuilt from scratch to match the 5.5 HoffMath Classroom standard
- Converted all math from HTML entities/Unicode to **KaTeX** via CDN
- Replaced legacy `data-step` + opacity transitions with **ID-based step reveals** (`display: none/block`)
- Added **flexbox autoscaling** (`.slide-body` + `.steps-area`) — content fills the screen on any display
- Added **step-box cards** (`.step-box` with `.step-label` + `.step-math`) for all worked examples
- Replaced legacy `#slides-container` with `.slides-wrapper` horizontal transition model
- Preserved all 11 SVG graphs (`GraphBuilder` class) and interactive table behavior
- Triangle SVGs (Examples 9/10) rebuilt with larger viewBox and repositioned labels

### Documentation Overhaul

- **`agents.md`** completely rewritten — now documents the 5.5 HoffMath Classroom architecture as the gold standard, including the full HTML skeleton, JS controller, step-box system, rebuild checklist, and lessons learned from failed approaches
- **`CLAUDE.md`** updated with rebuild guidance: "If the presentation doesn't match 5.5 → rebuild from scratch"
- **`CONVENTIONS.md`** updated: KaTeX is now the standard math renderer for HTML (deprecating Unicode/monospace), step reveal conventions updated to match `display: none/block` pattern

---

### Step Reveal Overhaul (5.1–5.5)

- **`display: none` / keyframe reveal** — replaced `max-height` + `overflow: hidden` collapse with `display: none` → `display: block/flex` + `@keyframes stepReveal`. Steps now render at full natural height with zero clipping, even for tall nested KaTeX fractions.
- **Scrollable `.steps-area`** — `overflow-y: auto; flex: 1; min-height: 0; padding-bottom: 3.5rem`. Steps that exceed the visible area scroll within the slide. `scrollIntoView({ behavior: 'smooth', block: 'nearest' })` auto-scrolls to each newly revealed step.
- **Bidirectional step navigation** — left/up arrow retreats one step before going to previous slide
- **Mobile-friendly** — no fixed height constraints; content adapts to any screen size
- **Copyright removed from 5.1** — all 9 `© Hoff Math` lines and CSS block removed

---

### Recently Added

#### 2026-03-09 — First Manim Scene + manim_skill

- **`manim/scenes/5_3_solving_trig_graphical.py`** — `TanEquationGraphicalAnalysis`
  - First working ManimCE scene in the project (rendered v0.19.2)
  - Graphical solution of `tan²θ − 3 = 0` on `[0, 2π)`: builds axes + `y = tan θ` (3 branches), drops `y = ±√3` reference lines, marks all four intersections with drop-lines, quadrant tags, and θ-labels, closes with a solution banner
  - Uses full project color palette from `shared/colors.py`
  - Modular phase structure (`_phase_*` methods) + reusable `_mark_solution()` helper
- **`manim/scenes/5_3_cot_factoring_graphical.py`** — `CotFactoringGraphicalAnalysis`
  - Graphical solution of `cot x · cos²x = 2cot x` for **all** solutions
  - 3-period `y = cot x` plot with zeros marked at π/2, 3π/2, 5π/2 + n-tags
  - Inset panel (DR corner): `y = cos²x` vs `y = 2` — shaded red gap proves no intersection
  - Factor-not-divide warning; general solution banner `x = π/2 + πn, n ∈ ℤ`
- **`npx skills add adithya-s-k/manim_skill`** — installed `manim-composer`, `manimce-best-practices`, `manimgl-best-practices` skills

**HTML Presentations:**
- `5.1-fundamental-identities.html` — Using Fundamental Identities (7 examples, HoffMath Classroom style)
- `5.2-verifying-trig-identities.html` — Verifying Trig Identities (6 examples + alternate methods, HoffMath Classroom style)
- `5.3-solving-trig-equations.html` — Solving Trig Equations (7 examples, caution/exception slides, HoffMath Classroom style)
- `5.4-sum-and-difference.html` — Sum and Difference Identities (7 examples, formula reference card, two-problem layouts, HoffMath Classroom style)
- `5.5-double-half-angle.html` — Double &amp; Half Angle Identities (6 examples, two reference cards, three-part answer grid, quadrant analysis, HoffMath Classroom style)

**5.5 Refinements:**
- Boxed step cards with descriptive subtitle labels (new step reveal style, user-approved for future decks)
- Bidirectional step navigation — left/up arrow retreats one step at a time before going to previous slide
- Dynamic font scaling (`_fitContent`) — after each reveal/retreat, measures available height and reduces slide `font-size` proportionally so all steps always fit without overflow; scales KaTeX math with it; minimum 14px floor
- Hidden steps collapse to `max-height: 0` so they take no layout space until revealed
- Formula reference rows vertically center the function label with the math

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
