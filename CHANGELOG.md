# Changelog

Tracks what was built, when it was added, and the current state of the project.
Update this file whenever a new presentation, component, scene, or major feature is added.

---

## 2026-05-12

### New HTML Decks - Unit 4 Sections 4.1–4.5 (rebuilt to 5.5 standard)

Authored five brand-new dedicated section decks for the first half of Unit 4
against the shared-assets standard (`assets/slides-core.css` +
`slides-core.js`, KaTeX, teacher-controlled step reveals). These replace the
single bundled `trig-review.html` for daily classroom use; the legacy review
deck is preserved for end-of-chapter mixed practice.

- **4.1 Right Triangle Trigonometry** (`4.1-right-triangle-trigonometry.html`) — 16 slides. SOHCAHTOA concept with a colored reference triangle (cyan x-side / pink y-side / green hypotenuse), reference card for all six ratios with reciprocal pairings, full identity bundle (reciprocal, quotient, Pythagorean, cofunction with the "co = complementary" hook), DMS notation and conversion, and seven worked examples — six trig functions of angle G (21-28-35 → 3-4-5), cos θ = 7/8 → other five (rationalized), exact values from a bisected equilateral (30-60-90 derivation of \(\sin 30°,\cos 30°,\sin 60°,\cos 60°\)), tan θ = 1/3 → cot, sec via two methods (reference triangle and Pythagorean identity), sec(9°40'12") via decimal-degree conversion, an angle-of-depression chair/pen problem, and a two-triangle smokestack height problem (\(35°\) and \(53°\) elevations from 200 ft). All triangle SVGs use true proportions verified against the Pythagorean theorem; \(\sqrt{}\) glyphs render with `<tspan text-decoration="overline">`.
- **4.2 Radian and Degree Measure** (`4.2-radian-and-degree-measure.html`) — 16 slides. Standard-position angle (vertex/initial/terminal), CCW vs. CW direction with 120° and −145° illustrations, coterminal angles (\(\theta \pm 360°k\) / \(\theta \pm 2\pi k\)), a full unit-circle reference figure with all 16 standard angles double-labeled (degrees and radians, 720×480 SVG), the foundational \(180° = \pi\) bridge with a half-rotation illustration, conversion-rule reference card, three conversions (\(130° \to 13\pi/18\), \(-3\pi/10 \to -54°\), \(2 \text{ rad} \to 360°/\pi \approx 114.59°\)), complementary vs. supplementary diagrams + two examples (\(148°\) — complement undefined, supplement 32°; \(2\pi/5\) — complement \(\pi/10\), supplement \(3\pi/5\)), and a "where is 3 radians?" Q2 placement exercise.
- **4.3 Linear and Angular Speed** (`4.3-linear-and-angular-speed.html`) — 12 slides. Radian-as-proportion derivation (\(s/r = \theta\)), one-radian and two-radian visualizations, arc-length reference \(s = \theta r\), 240°-reflex-angle example (\(r = 4 \to s = 16\pi/3 \approx 16.76\) in), sector-area reference \(A = \tfrac{1}{2}\theta r^2\) with the underlying proportion, linear-vs-angular speed conceptual split with the rev/time × (\(2\pi\) rad/rev or circumference/rev) framework, and three modeling examples — clock second-hand tip (10.2 cm → ≈1.068 cm/sec), wind turbine (116 ft blade, 15 rpm → \(30\pi\) rad/min and \(3480\pi \approx 10{,}932.7\) ft/min), and a wheel-to-mph conversion (d = 24 in, 800 rpm → ≈57.1 mph) showing the full unit-conversion chain.
- **4.4 Trig Functions: The Unit Circle** (`4.4-trig-functions-unit-circle.html`) — 16 slides. Special-right-triangle refresher (45-45-90 and 30-60-90), three Q1-derivation slides building \((\sqrt{3}/2, 1/2)\) at \(\pi/6\), \((\sqrt{2}/2, \sqrt{2}/2)\) at \(\pi/4\), and \((1/2, \sqrt{3}/2)\) at \(\pi/3\) from the inscribed right triangle. The "memorize this" full unit-circle reference shows all 16 standard angles with radian labels and coordinate pairs (overlined radicals). Coordinates-mean-cos-sin concept slide unlocks the other four ratios. ASTC mnemonic chart with A/S/T/C corner letters. Five examples — \(5\pi/4\) → (−√2/2, −√2/2) → all six, \(-\pi/3 \equiv 5\pi/3\) → (1/2, −√3/2) → all six, periodicity reduction \(13\pi/6 \to \pi/6\), calculator (sin 2π/3 ≈ 0.866, cot 1.5 ≈ 0.071), and a five-step identity verification \(\sin(-x)\tan(-x) + \cos(-x) = \sec(x)\) using even/odd + Pythagorean.
- **4.5 Trig Functions of Any Angle** (`4.5-trig-functions-of-any-angle.html`) — 15 slides. Reference-angle definition with a four-quadrant SVG mosaic, the quadrant-by-quadrant formulas (deg + rad), and seven worked examples — \(330° \to 30°\), \(-5\pi/6 \equiv 7\pi/6 \to \pi/6\), \(2.3 \text{ rad} \to \pi - 2.3 \approx 0.8416\), then trig from a terminal-side point (\((8, -15)\) → r = 17 → six trig functions), a two-constraint problem (\(\sin\theta = -2/3\) and \(\tan\theta > 0\) → Q3 → \(\cos = -\sqrt{5}/3\), \(\cot = \sqrt{5}/2\)), and the "given a value, find both angles in one revolution" pair — \(\tan\theta = -0.4623 \to 155.2°, 335.2°\) and \(\cos\theta = -0.3842 \to 1.9651, 4.3181\) rad. Closes with a 6-skill wrap-up emphasizing "expect two answers" when solving for θ.

Each deck stays under 60K, with inline `<style>` blocks held to 23–39 lines
(only deck-specific SVG primitives — all layout uses the shared
`assets/slides-core.css` components). Step-box palette is restricted to
teal (setup) and dark (final answer) to match the established lesson-deck
pattern from Unit 3. Curriculum table in CLAUDE.md updated; the legacy
`trig-review.html` stays in place as an end-of-chapter review.

---

### New HTML Decks - Unit 3 Exponential &amp; Logarithmic Functions (5 decks)

Added the full Unit 3 sequence built against the shared-assets standard
(`assets/slides-core.css` + `slides-core.js`, KaTeX, teacher-controlled
step reveals). All five decks follow the HoffMath Classroom step-box
pattern used in Unit 2.

- **3.1 Exponential Functions &amp; Their Graphs** (`3.1-exponential-functions-and-their-graphs.html`) — 13 slides. Growth-vs-decay intro with both curve families plotted on one axis (\(y = 2^x, 3^x, 10^x, 1.3^x\) and \(y = (1/2)^x, (1/6)^x, (3/4)^x\)), parent-function reference table, transformation card for \(a(b)^{x-h}+k\), four full analyze-and-sketch examples (\((1/2)^x - 3\), \(4^{x-1} + 2\), find \(ab^x\) from two points, find \(ab^{-x}+c\) from HA and two points), the natural base \(e\) with \(y = e^x\) labeled at \((-1, 1/e), (0,1), (1, e)\), composition \((g\circ f)(0)\) for \(f(x) = e^{3x} - 2\), and the compound interest formulas with US-population and \$12{,}000 quarterly-vs-continuous worked examples.
- **3.2 Logarithmic Functions &amp; Their Graphs** (`3.2-logarithmic-functions-and-their-graphs.html`) — 15 slides. Log definition + iff biconditional, parts-of-a-log diagram, conversion example, common/natural log definitions, basic properties table (\(\log_a 1, \log_a a, \log_a a^x, a^{\log_a x}\), one-to-one), four simplify/solve examples covering both common log and \(\ln\), inverse of \(g(x) = -2 + \log_{3}(x+1)\) via swap-and-solve, reflection-across-\(y=x\) visual for base 2 and base \(e\) pairs, three log curves on one axis (base 2, \(e\), 10), exp-vs-log comparison table, the seven-step "How to Graph a Log Function" recipe, and two analyze-and-sketch examples — \(\log_{6}(x-1) + 4\) and \(-\log_{3}(x+1) - 3\).
- **3.3 Properties of Logarithms** (`3.3-properties-of-logarithms.html`) — 9 slides. Product/quotient/power/change-of-base reference card, red "NOT log identities" mistake card, simplify (Examples 1–3), condense (Examples 4–6 including the bracketed \(\tfrac{1}{3}[\ldots]\) case that ends with a cube root), expand (Examples 7–8 with \(\ln(3x^2 y^5)\) and \(\log(x^3 y^2/\sqrt{z+1})\)), write-in-terms-of (Examples 9–10), and change-of-base evaluations \(\log_7 8 \approx 1.068\) and \(\log_2 12 \approx 3.585\).
- **3.4 Solving Exponential &amp; Log Equations** (`3.4-solving-exponential-and-log-equations.html`) — 11 slides. Three-strategy overview card (exponential, log, and "variable in two exponents"), then 9 worked examples — \(4e^{2x} - 3 = 2\), \(2(3^{2t-5}) - 4 = 11\), \(5^{2x+1} = 6^{x-2}\) (different bases, take \(\ln\)), \(4(2^x) + 8(2^{-x}) = 33\) and \((5^x - 5^{-x})/2 = 3\) (the \(u = b^x\) substitution trick, including a quadratic that gives one negative root to discard), \(5 + 2\ln x = 4\), \(\log_5(2x+3) = \log_5 11 + \log_5 5\), \(\log_2 x + \log_2(x+2) = 3\) (with explicit extraneous-root check on \(x = -4\)), and the challenge problem \(\log \sqrt[3]{x} = \sqrt{\log x}\) with substitution \(u = \sqrt{\log x}\).
- **3.5 Exponential Applications** (`3.5-exponential-applications.html`) — 7 slides. Three-formula reference (compound, continuous, growth/decay), then five contextual applications — \$500 doubling at 6.75% continuous (\(t \approx 10.27\) years), tuition doubling under \(40000(1.072)^t\) (year ≈ 2030), world population reaching 10 billion under \(P = 7021.7 e^{0.01076 t}\) (year ≈ 2033, with care taken about \(t = 10\) representing 2010), bacteria with 40%/hr continuous growth (model, count at \(t = 10\), and time to reach 80,000), and Polonium-210 half-life of 140 days with mass decay to 200 mg (\(t \approx 81.9\) days).

Each deck includes a small inline SVG plot helper (axes, gridlines, dashed
asymptotes, polyline curves, labeled points, annotations) so the deck stays
self-contained while still loading the shared assets — no new files added
to `assets/`. Index, CLAUDE.md curriculum table, and the "Next up" line
all updated. Pre-existing supplemental rational-functions decks remain
linked under their own section.

---

### New HTML Deck - 2.8 Graphs of Rational Functions (Unit 2 complete)

Added `2.8-graphs-of-rational-functions.html`, 9 slides covering the four-step
graphing procedure (asymptotes → intercepts → test points → smooth curves)
and five worked-graph examples — a simple parent-shifted hyperbola
\(\tfrac{3}{x-2}\), a two-VA equal-degree case \(\tfrac{x^2}{x^2-x-2}\), a
hole example \(\tfrac{x^2-9}{x^2-2x-3}\) with a visible open dot at
\((3, \tfrac{3}{2})\), and two slant-asymptote cases
\(\tfrac{x^2+x}{x-1}\) (slant \(y = x + 2\)) and \(\tfrac{x^3}{x^2-4}\)
(slant \(y = x\), two VAs).

- Extended the GraphBuilder helper with `slantAsym(m, b)` which clips the
  slant line `y = mx + b` to the visible math window before drawing it.
- This completes Unit 2.

### New HTML Deck - 2.7 Rational Functions and Asymptotes

Added `2.7-rational-functions-and-asymptotes.html`, 12 slides covering the
definition of a rational function (simple and standard forms) with the
parent \(1/x\) hyperbola sketched alongside its properties, a gallery of
four representative shapes — \(\tfrac{3x}{x+1}\), \(\tfrac{x}{(x+1)(x-2)}\),
\(\tfrac{3}{x^2+1}\), \(\tfrac{3}{(x+1)^2}\) — the vertical/horizontal
asymptote definitions, the consolidated rules table (VA, two HA cases, hole,
slant), behavior-near-singularity tables for \(\tfrac{1}{x-1}\), and six
examples — including a hole from \((x+4)\) cancellation, a full analysis with
hole + VA + HA + intercepts on \(\tfrac{x^2+x-6}{x^2-x-2}\), a cubic-over-
cubic with non-real complex denominator roots, and a two-VA quartic
\(\tfrac{x^2-16}{x^2+8x}\).

- Extended the GraphBuilder helper with `asymptoteV` / `asymptoteH` (dashed
  red/green guide lines), a `holeAt` open-circle method, and a `curve()`
  variant that splits sampling around discontinuities so the curve doesn't
  draw across a vertical asymptote.
- Linked from `index.html`.

### New HTML Deck - 2.6 Fundamental Theorem of Algebra

Added `2.6-fundamental-theorem-of-algebra.html`, 9 slides covering the FTA
statement with the linear-factorization corollary, a cubic complete-
factorization example \(x^3 + x^2 - 4x + 6\) requiring quadratic-formula
closure with complex roots, a quintic with a missing \(x^4\) term whose
zeros include a double rational root and a pure-imaginary conjugate pair
\(\pm 3i\), the complex-conjugate and irrational-conjugate zero theorems,
a build-cubic from \(2,\sqrt{3}\) with \(g(4)=13\), a build-cubic from
\(2,1-i\) with \(f(1)=3\), and a quartic with a given complex zero
\(1+3i\) — long-divided by \(x^2-2x+10\) to reveal the second conjugate
pair \(2\pm 5i\).

- Reuses the `.synth` table styling from 2.4 for synthetic-division
  layouts.
- Linked from `index.html`.

### New HTML Deck - 2.5 Complex Numbers

Added `2.5-complex-numbers.html`, 14 slides covering the nested number-set
hierarchy (Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real ⊂ Complex, with
Irrational and Imaginary as sibling sets at their levels), the standard form
\(a + bi\), five arithmetic examples (sum-to-zero, sign distribution,
monomial × binomial, binomial squared, and a radical-conversion product),
complex conjugates and their real-valued product, dividing complex numbers
by conjugation, two quadratic equations with complex roots (\(2x^2 + 50 = 0\)
and \(5x^2 + 2x + 1 = 0\)), and building a quadratic from a complex zero
pair \(3 \pm 2i\) using the conjugate-pair difference-of-squares trick.

- Number-set diagram is a single nested-rectangle SVG with distinct colors
  per set.
- Linked from `index.html`.

### New HTML Deck - 2.4 Dividing Polynomials

Added `2.4-dividing-polynomials.html`, 14 slides covering the polynomial
division algorithm (with integer-division analogy), two long-division
examples (linear divisor and quadratic divisor), the mechanism of synthetic
division, four synthetic-division examples — \((2x^3-3x^2-4x+2) \div (x+2)\),
\(P(x) = 2x^4 - 8x^2 + 5x - 7\) divided by \((x-3)\) to demonstrate the
Remainder Theorem, evaluating \(f(-1)\) via synthetic division, and verifying
\((x-2)\) and \((x+3)\) as factors of \(2x^4 + 7x^3 - 4x^2 - 27x - 18\) —
then the Remainder & Factor Theorems reference, the Rational Zero Theorem,
and two zero-finding examples (factor-by-grouping cubic and an
irrational-root cubic requiring the quadratic formula).

- Introduces a `.synth` table style for synthetic-division layouts: red
  divisor cell, products row in muted gray, bottom-row result with the
  remainder cell highlighted in amber/red.
- Reuses the standard shared-assets pattern (no new graph helper needed
  since 2.4 is algebraic, not graphical).
- Linked from `index.html`.

### New HTML Deck - 2.3 Zeros of Polynomial Functions

Added `2.3-zeros-of-polynomial-functions.html`, 13 slides covering the unifying
vocabulary (zero / root / solution / factor / x-intercept), four factor-and-
sketch examples — \(x^3-x^2-2x\), \((x-2)^2(x+2)\) with a tangent double-root,
\(-2x^4-x^3+3x^2\) with a tangent at the origin, and the quadratic-type
\(x^4-12x^2+27\) — two reverse-engineering examples (clearing fractional
zeros and pairing conjugate radicals), the Intermediate Value Theorem with a
diagrammatic explainer, an IVT application on \(x^4-4x+1\), and a visual
confirmation graph showing the sign change.

- Reuses the same `GraphBuilder` helper from 2.2 (and the trig decks) for
  dense, gridded math graphs.
- Linked from `index.html`.

## 2026-05-11

### New HTML Deck - 2.2 Graphs of Polynomial Functions

Added `2.2-graphs-of-polynomial-functions.html`, 15 slides covering continuity
& smoothness (four-panel example/counter-example diagram), monomial behavior
(\(x^n\) for \(n=1..4\)), two factored-form warm-up sketches (quadratic and
cubic), the zeros/turning-points ceiling, the four-case Leading Coefficient
Test reference table (with inline sample SVGs), multiplicity (cross vs.
tangent with mini-graphs), and the source PDF's seven examples — the \(-3x^4\)
multiple choice, two end-behavior identifications, two factored-form sketches,
the dual turning-point count, and writing the equation of a degree-4
polynomial from its graph.

- Uses the same shared-asset pattern as 2.1.
- Reuses the deck-level pattern of stroke-only SVG classes + fill-only label
  classes so text never renders outlined.
- Linked from `index.html`.

### New HTML Deck - 2.1 Quadratic Functions

Added `2.1-quadratic-functions.html`, the first deck for Unit 2 (Polynomial &
Rational Functions). Built on the shared-assets pattern (`assets/slides-core.css`
+ `assets/slides-core.js`), matching the 6.7 canonical reference.

- 11 slides covering: polynomial classification by degree (constant through
  quartic), anatomy of a parabola (custom labeled SVG with vertex, axis of
  symmetry, intercepts), vertex form vs. standard form (key features table),
  completing-the-square procedure, and four worked examples — convert to vertex
  form & sketch, build the equation from vertex + point, taco-truck min-cost
  application, and the quadratic-type substitution \(x^6+7x^3=8\).
- Mirrors the original Hoff Math student handout (`original_notes/2.1
  Quadratic Functions STUDENT.pdf`) so blanks/structure stay teacher-familiar.
- Linked from `index.html` under a new Unit 2 section.

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
