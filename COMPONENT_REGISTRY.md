# Component Registry

Every reusable Vue component, composable, and Manim scene lives here.
**Check this file before building anything new.** Update it when you add something.

---

## Slidev / Vue Components

### Graphing Primitives (`components/graphs/`)

> None built yet. These are the recommended next components to create.
> See "Planned Components" section below.

---

### Lesson Components (`components/lessons/`)

> None built yet.

---

### Utility Components

#### `ThemeToggle.vue`

**File:** `slidev/4.9-inverse-trig-prototype/components/ThemeToggle.vue`
**Lines:** 72
**Status:** ✅ Working
**What it does:** Dark/light mode toggle with localStorage persistence and
`prefers-color-scheme` system detection. Sets `data-precalc-theme` attribute
on `<html>`, which CSS uses to switch color variables.

**Props:** None (self-contained)
**Emits:** None
**Side effects:** Writes `precalc-slidev-theme` key to localStorage; sets
`data-precalc-theme="dark"|"light"` on `document.documentElement`.

**Usage:**
```vue
<ThemeToggle />
```

**To reuse in a new deck:**
Copy `ThemeToggle.vue` to the new deck's `components/` folder and include the
theme CSS variables in that deck's `styles/index.css`.

---

#### `global-top.vue`

**File:** `slidev/4.9-inverse-trig-prototype/global-top.vue`
**Lines:** 10
**Status:** ✅ Working
**What it does:** Slidev global layout wrapper. Mounts `ThemeToggle` in the
fixed top-right corner of every slide.

**Usage:** Automatically picked up by Slidev when named `global-top.vue`.
No manual import needed.

---

### Interactive Demo Components

#### `RevealCard.vue`

**File:** `slidev/4.9-inverse-trig-prototype/components/RevealCard.vue`
**Lines:** 94
**Status:** ✅ Working
**What it does:** A click-to-reveal card for conceptual discovery moments. Shows
a question/prompt face; clicking reveals the answer with a smooth fade+slide
transition. Clicking again collapses it. Respects `prefers-reduced-motion`.

**Slots:**
- `#prompt` — question or concept label shown by default
- `#answer` — revealed content (supports KaTeX inline math via `$...$`)

**Props:** None (self-contained state via `ref(false)`)

**Usage:**
```vue
<RevealCard>
  <template #prompt>What is the domain of arcsin?</template>
  <template #answer>$-1 \le x \le 1$ — only ratios that sine can produce.</template>
</RevealCard>
```

**Layout helpers (styles/index.css):**
- `.reveal-grid` — 3-column grid of RevealCards (collapses to 1-col on narrow screens)
- `.reveal-col` — single-column stack of RevealCards

**To reuse in a new deck:**
Copy `RevealCard.vue` to the new deck's `components/` folder. The component reads
all color/font tokens from `--deck-*` CSS variables.

---

#### `ArcsinGraphDemo.vue`

**File:** `slidev/4.9-inverse-trig-prototype/components/ArcsinGraphDemo.vue`
**Lines:** 424
**Status:** ✅ Working
**Covers:** Section 4.9 — Inverse Sine

**What it does:**
- Range slider for x input (−1 to 1, step 0.01)
- Number input field (synchronized with slider)
- Preset buttons: x = −1/2, 0, 1/2, √2/2
- SVG canvas: plots y = arcsin(x) with grid, axes, curve
- Reference lines: shows how (x, arcsin(x)) is read from the graph
- Real-time readout: input value, output in radians, output in degrees
- Exact value recognition (displays `π/6`, `−π/4`, etc. instead of decimals
  for the common special angles)
- Responsive: collapses to single column on narrow screens
- Theming: reads `data-precalc-theme` attribute for dark/light colors

**Key computed properties:**
```ts
yValue    // arcsin(x) in radians
yDegrees  // output in degrees
pointX    // SVG x-coordinate of the active point
pointY    // SVG y-coordinate of the active point
curvePath // SVG <path> d-attribute for the full arcsin curve
```

**Key helpers:**
```ts
clamp(v, min, max)      // clamp a number
sx(x)                   // Cartesian x → SVG x
sy(y)                   // Cartesian y → SVG y (handles inversion)
almostEqual(a, b, eps)  // fuzzy equality for exact-value matching
```

**Exact label map (subset):**
```ts
{ value: Math.PI / 6,  label: "π/6"   }
{ value: Math.PI / 4,  label: "π/4"   }
{ value: Math.PI / 3,  label: "π/3"   }
{ value: Math.PI / 2,  label: "π/2"   }
// ... and their negatives
```

**Props:** None (self-contained)

**Usage:**
```md
<!-- In slides.md -->
<ArcsinGraphDemo />
```

**To extend:** Add `arccosGraphDemo.vue` and `arctanGraphDemo.vue` following
the same structure. Factor shared SVG axes/grid logic into `components/graphs/`
primitives.

---

## Composables (`composables/`)

> None built yet. Recommended to extract from `ArcsinGraphDemo.vue`:

| Planned composable | What it should do |
|---|---|
| `useScales.ts` | SVG ↔ Cartesian coordinate transforms (`sx`, `sy`, `clamp`) |
| `useSampling.ts` | Generate point arrays for smooth function curves |
| `useDragPoint.ts` | Draggable SVG point with optional curve/circle constraint |

---

## Manim Scenes

### `TanEquationGraphicalAnalysis`

**File:** `manim/scenes/5_3_solving_trig_graphical.py`
**Class:** `TanEquationGraphicalAnalysis`
**Status:** ✅ Working (rendered 2026-03-09, ManimCE v0.19.2)
**Covers:** Section 5.3 — Solving Trig Equations

**What it does:**
Animated graphical solution of `tan²θ − 3 = 0` on `[0, 2π)`.

1. Title + algebraic bridge `tan²θ = 3 → tanθ = ±√3`
2. Builds axes and draws `y = tan θ` in three branches (with asymptote dashes at π/2, 3π/2)
3. Drops horizontal reference line `y = √3` (green) → reveals π/3 (QI) and 4π/3 (QIII) with vertical drop-lines and quadrant tags
4. Drops horizontal reference line `y = −√3` (pink) → reveals 2π/3 (QII) and 5π/3 (QIV)
5. Solution banner: `θ = π/3, 2π/3, 4π/3, 5π/3` (gold on dark card)

**Color coding (project palette):**
- `y = tan θ` curve → `ACCENT_TEAL` (`#5eead4`)
- `y = √3` line + QI/QIII labels → `Q1_COLOR` (`#4ade80`, green)
- `y = −√3` line + QII/QIV labels → `Q3_COLOR` (`#f472b6`, pink)
- Solution dots + θ-labels → `HIGHLIGHT` (`#fbbf24`, gold)

**Private helpers:**
- `_phase_intro()` — title and algebraic bridge
- `_phase_axes()` — axes, tick labels, ±√3 y-labels
- `_phase_curve()` — asymptotes + three-branch tan curve
- `_phase_positive_root()` — y=√3 line + π/3, 4π/3 markers
- `_phase_negative_root()` — y=−√3 line + 2π/3, 5π/3 markers
- `_phase_solution_banner()` — final solution card
- `_mark_solution(axes, theta, y_val, color, theta_str, quad, q_dir)` — reusable intersection marker

**Render:**
```bash
cd manim
manim -pql scenes/5_3_solving_trig_graphical.py TanEquationGraphicalAnalysis  # preview
manim -pqh scenes/5_3_solving_trig_graphical.py TanEquationGraphicalAnalysis  # final
```

---

### `CotFactoringGraphicalAnalysis`

**File:** `manim/scenes/5_3_cot_factoring_graphical.py`
**Class:** `CotFactoringGraphicalAnalysis`
**Status:** ✅ Working (rendered 2026-03-09, ManimCE v0.19.2) — v2 rebuild
**Covers:** Section 5.3 — Solving Trig Equations

**What it does:**
Full narrative animation for `cot x · cos²x = 2cot x` — **all solutions**.
Includes an algebra-steps phase before the graphical verification, ensuring viewers
understand the algebraic motivation. Two-panel modular layout: each panel fills the
scene during its annotation phase, then shrinks to a thumbnail.

1. Title + "All Solutions — no domain restriction" statement (held on screen)
2. **Algebra steps phase** — original equation → subtract → factor → zero product
   property; Case 1 (green) vs Case 2 (red) color-coded; warning box: don't divide by cot x
3. **Panel A** (green border, full scene) — `y = cot x` over `[0, 3π]` (curve
   **clipped** with `np.clip` to stay inside panel border); asymptotes at π, 2π;
   `cot x = cos x/sin x = 0 ⟹ cos x = 0` annotation; gold zeros at π/2, 3π/2, 5π/2
   with n=0,1,2 tags; general solution box `x = π/2 + πn, n ∈ ℤ` inside panel
4. Panel A shrinks to left thumbnail
5. **Panel B** (red border, full scene) — `y = cos²x` vs dashed ceiling `y=1` vs
   target `y=2`; red-shaded gap; gap arrow annotation; "No intersection!" + proof stamp
6. Panel B shrinks to right thumbnail — both visible simultaneously with ✓/✗ labels
7. General solution banner: `x = π/2 + πn, n ∈ ℤ`

**Key implementation detail — curve clipping:**
```python
Y_CLIP = 3.75
def _cot_clipped(x):
    s = np.sin(x)
    if abs(s) < 1e-9:
        return float(np.sign(np.cos(x)) * Y_CLIP)
    return float(np.clip(np.cos(x) / s, -Y_CLIP, Y_CLIP))
# Plot with step=0.005 for smooth clip boundary:
b1 = axes.plot(_cot_clipped, x_range=[0+EPS, PI-EPS, 0.005], ...)
```
`SurroundingRectangle` does not clip rendered content — clamping the function value
is the only reliable way to keep discontinuous curves inside a panel border.

**Panel mechanics:**
- Both panels built at full-size (`x_length≈9.6/8.5`), content created at correct `c2p()` positions
- Each panel is a `VGroup(border, label, axes, all_content)`
- Thumbnail transition: `vg.animate.scale(0.47).move_to(thumb_pos)` — all content scales uniformly

**Color coding (project palette):**
- Panel A border + Case 1 elements → `Q1_COLOR` (`#4ade80`, green)
- Panel B border + impossible case elements → `ACCENT_RED` (`#fca5a5`)
- `y = cot x` / `y = cos²x` curves → `ACCENT_TEAL` / `ACCENT_BLUE`
- Zero dots + x-labels + solution box → `HIGHLIGHT` (`#fbbf24`, gold)

**Private helpers:**
- `_phase_intro()` — title + "All Solutions" subtitle box
- `_phase_math_steps()` — 3 algebra steps with annotations, ZPP split, warning, bridge
- `_phase_cot_panel()` — builds + annotates Panel A (with general solution box), shrinks to `COT_THUMB`
- `_phase_cos2_panel()` — builds + annotates Panel B (with gap arrow), shrinks to `COS_THUMB`
- `_phase_banner()` — ✓/✗ thumbnail labels + solution card

**Render:**
```bash
cd manim
manim -pql scenes/5_3_cot_factoring_graphical.py CotFactoringGraphicalAnalysis  # preview
manim -pqh scenes/5_3_cot_factoring_graphical.py CotFactoringGraphicalAnalysis  # final
```

---

### `PythSubGraphicalAnalysis`

**File:** `manim/scenes/5_3_pyth_sub_graphical.py`
**Class:** `PythSubGraphicalAnalysis`
**Status:** ✅ Working (rendered 2026-03-12, ManimCE v0.19.2)
**Covers:** Section 5.3 — Solving Trig Equations (Example 4)

**What it does:**
Full narrative animation for `2sin²x + 3cos x - 3 = 0` — **all solutions**.
Pythagorean substitution converts to a quadratic in cos x, then factors into two valid cases.
Two-panel modular layout with scrim pattern.

1. Title + "All Solutions — no domain restriction" statement
2. **Algebra steps** — original → Pythagorean sub (`sin²x = 1 - cos²x`) → expand/simplify → factor;
   ZPP split: Case 1 `cos x = 1/2` (green) vs Case 2 `cos x = 1` (blue); bridge text
3. **Panel A** (green border, `[0, 2π]`) — `y = cos x` with dashed `y = 1/2` reference;
   intersections at `π/3` (QI, green dot) and `5π/3` (QIV, gold dot); general solution box
4. Panel A shrinks to left thumbnail
5. **Panel B** (blue border, `[0, 4π]`) — `y = cos x` with dashed `y = 1` reference;
   intersections at `0, 2π, 4π` (blue dots with n-tags); general solution box
6. Panel B shrinks to right thumbnail (scrim fades out)
7. Both panels get ✓ labels + combined solution banner

**Color coding:**
- Panel A border + QI elements → `Q1_COLOR`; QIV dot → `Q4_COLOR`
- Panel B border + elements → `ACCENT_BLUE`
- `y = cos x` curves → `ACCENT_TEAL`
- Solution dots + banner → `HIGHLIGHT`

**Render:**
```bash
cd manim
manim -pql scenes/5_3_pyth_sub_graphical.py PythSubGraphicalAnalysis  # preview
manim -pqh scenes/5_3_pyth_sub_graphical.py PythSubGraphicalAnalysis  # final
```

---

### `SquaringGraphicalAnalysis`

**File:** `manim/scenes/5_3_squaring_graphical.py`
**Class:** `SquaringGraphicalAnalysis`
**Status:** ✅ Working (rendered 2026-03-12, ManimCE v0.19.2)
**Covers:** Section 5.3 — Solving Trig Equations (Example 5)

**What it does:**
Single-panel graphical analysis of `cos x + 1 = sin x` on **[0, 2π)**.
Squaring both sides introduces an extraneous solution — the graph makes this visually obvious.

1. Title + "[0, 2π) — restricted domain" badge
2. **Algebra steps** — original → square both sides → Pythagorean sub → factor;
   warning box: "Squaring can introduce extraneous solutions — must verify!";
   ZPP split: `cos x = 0` (green) vs `cos x = -1` (blue); candidates: `π/2, 3π/2, π`
3. **Single full-scene graph** — `y = cos x + 1` (teal) vs `y = sin x` (pink) on `[0, 2π]`
   - ✓ green dot at `π/2` (both curves = 1)
   - ✓ green dot at `π` (both curves = 0)
   - ✗ red dots at `3π/2` with dashed gap line showing LHS = 1, RHS = -1 (gap = 2)
   - "Extraneous!" annotation with algebraic proof
4. Solution banner: `x = π/2, x = π`

**Color coding:**
- `y = cos x + 1` → `ACCENT_TEAL`; `y = sin x` → `Q3_COLOR` (pink)
- Valid intersections → `Q1_COLOR` (green ✓)
- Extraneous candidate → `ACCENT_RED` (✗ + gap)
- Banner → `HIGHLIGHT`

**Render:**
```bash
cd manim
manim -pql scenes/5_3_squaring_graphical.py SquaringGraphicalAnalysis  # preview
manim -pqh scenes/5_3_squaring_graphical.py SquaringGraphicalAnalysis  # final
```

---

### Shared Helpers Module

**File:** `manim/shared/helpers.py`
**Status:** ✅ Working (created 2026-03-29)
**What it does:** Shared layout helpers for scenes using a left-2/3 + right-1/3 split layout.

**Exports:**
- Layout constants: `DIVIDER_X`, `LEFT_CENTER_X`, `RIGHT_CENTER_X`, `CIRCLE_CENTER`, `RIGHT_TOP`
- `build_unit_circle(center, radius, show_ticks)` — Circle + axes + tick labels VGroup
- `build_angle_arc(axes, angle_rad, color, ...)` — Colored arc from +x-axis
- `build_reference_triangle(axes, x_val, y_val, ...)` — Right triangle with colored sides (x=cyan, y=pink, r=green)
- `TextPanel` class — Manages right-1/3 text panel: `add_entry()`, `add_text()`, `add_math()`, `clear()`
- `build_title(tex_string)` — Full-width title at top
- `build_result_banner(tex_string)` — Gold-bordered answer banner at bottom
- `build_quadrant_highlight(axes, quadrant, color)` — Shaded rectangle for one quadrant
- `build_terminal_point(axes, angle_rad)` — Dot at (cos θ, sin θ) on unit circle

---

### `DoubleAngleGivenInfo` (5.5 Example 1)

**File:** `manim/scenes/5_5_double_angle_given_info.py`
**Class:** `DoubleAngleGivenInfo`
**Status:** ✅ Working (rendered 2026-03-29, ManimCE v0.19.2)
**Covers:** Section 5.5 — Double-Angle Identities

**What it does:**
Find sin(2θ), cos(2θ), tan(2θ) given cos θ = 5/13 in QIV.
Unit circle with angle in QIV, 5-12-13 reference triangle, step-by-step formula application.
Duration: ~26s.

**Render:**
```bash
cd manim
manim -pql scenes/5_5_double_angle_given_info.py DoubleAngleGivenInfo
```

---

### `DoubleAngleEquation` (5.5 Example 2)

**File:** `manim/scenes/5_5_double_angle_equation.py`
**Class:** `DoubleAngleEquation`
**Status:** ✅ Working (rendered 2026-03-29, ManimCE v0.19.2)
**Covers:** Section 5.5 — Solving Double-Angle Equations

**What it does:**
Solve 2cos x + sin(2x) = 0 on [0, 2π). Identity substitution → factoring → unit circle
with solutions at π/2 and 3π/2. Notes that 3π/2 satisfies both cases.
Duration: ~27s.

**Render:**
```bash
cd manim
manim -pql scenes/5_5_double_angle_equation.py DoubleAngleEquation
```

---

### `PatternRecognition` (5.5 Example 3)

**File:** `manim/scenes/5_5_pattern_recognition.py`
**Class:** `PatternRecognition`
**Status:** ✅ Working (rendered 2026-03-29, ManimCE v0.19.2)
**Covers:** Section 5.5 — Double-Angle Identity Pattern

**What it does:**
Rewrite cos²(5α) − sin²(5α) using double-angle identity. Shows template matching
with color-coded u ↔ 5α substitution, transforms expression to cos(10α).
Shortest scene. Duration: ~20s.

**Render:**
```bash
cd manim
manim -pql scenes/5_5_pattern_recognition.py PatternRecognition
```

---

### `HalfAngleExactValue` (5.5 Example 4)

**File:** `manim/scenes/5_5_half_angle_exact_value.py`
**Class:** `HalfAngleExactValue`
**Status:** ✅ Working (rendered 2026-03-29, ManimCE v0.19.2)
**Covers:** Section 5.5 — Half-Angle Identities

**What it does:**
Find cos 165°. Shows 165° = 330°/2 on unit circle, 30-60-90 reference triangle for 330°,
sign determination (QII → negative), and formula application.
Duration: ~24s.

**Render:**
```bash
cd manim
manim -pql scenes/5_5_half_angle_exact_value.py HalfAngleExactValue
```

---

### `HalfAngleGivenInfoQI` (5.5 Example 5)

**File:** `manim/scenes/5_5_half_angle_given_info_qi.py`
**Class:** `HalfAngleGivenInfoQI`
**Status:** ✅ Working (rendered 2026-03-29, ManimCE v0.19.2)
**Covers:** Section 5.5 — Half-Angle from Given Info

**What it does:**
Given sin x = 2/5 in QI, find cos(x/2). Builds right triangle (opp=2, hyp=5, adj=√21),
finds cos x, determines x/2 is also in QI (cos positive), applies formula.
Duration: ~23s.

**Render:**
```bash
cd manim
manim -pql scenes/5_5_half_angle_given_info_qi.py HalfAngleGivenInfoQI
```

---

### `HalfAngleQuadrantAnalysis` (5.5 Example 6 — Capstone)

**File:** `manim/scenes/5_5_half_angle_quadrant_analysis.py`
**Class:** `HalfAngleQuadrantAnalysis`
**Status:** ✅ Working (rendered 2026-03-29, ManimCE v0.19.2)
**Covers:** Section 5.5 — Half-Angle Quadrant Analysis

**What it does:**
Given cos θ = 5/13 in QIV, find sin(θ/2). THE key pedagogical scene — shows that
θ/2 lands in QII (not QIV), so sine is positive. Displays both θ and θ/2 arcs
simultaneously on the unit circle. Addresses the #1 student misconception about
sign determination.
Duration: ~23s.

**Render:**
```bash
cd manim
manim -pql scenes/5_5_half_angle_quadrant_analysis.py HalfAngleQuadrantAnalysis
```

---

### Planned Scenes

| Planned scene | File | Covers |
|---|---|---|
| `TrigTransformation` | `manim/scenes/4_6_trig_graphs.py` | A·sin(Bx+C)+D transformations |
| `ArcsinGraphConstruction` | `manim/scenes/4_9_inverse_trig.py` | Building arcsin by reflecting sine |
| `UnitCircleWalkthrough` | `manim/scenes/unit_circle.py` | Dragging a point around the unit circle |

---

## Planned Components (Build These Next)

### `GraphFrame.vue`
**Target:** `slidev/components/graphs/GraphFrame.vue`
**What it should do:** Render a coordinate plane with configurable domain/range,
grid, axes, tick marks, and labels. Accept slot content for curves and points.

**Proposed props:**
```ts
xMin: number    // default -5
xMax: number    // default 5
yMin: number    // default -4
yMax: number    // default 4
xStep: number   // tick interval, default 1
yStep: number   // tick interval, default 1
width: number   // SVG width in px, default 500
height: number  // SVG height in px, default 400
showGrid: boolean // default true
```

---

### `FunctionPlot.vue`
**Target:** `slidev/components/graphs/FunctionPlot.vue`
**What it should do:** Plot one or more functions on a `GraphFrame`. Compute
SVG path from a JS function reference. Handle discontinuities.

**Proposed props:**
```ts
fn: (x: number) => number   // function to plot
color: string                // stroke color
domain: [number, number]     // plot range
samples: number              // default 200
discontinuities?: number[]   // x values to break path at
```

---

### `TrigGraph.vue`
**Target:** `slidev/components/graphs/TrigGraph.vue`
**What it should do:** Sine/cosine transformation explorer.
A, B, C, D sliders with live graph update.
Show key points (maxima, minima, zero crossings).

**Proposed props:**
```ts
fn: 'sin' | 'cos'         // which function
showSliders: boolean       // default true
showKeyPoints: boolean     // default true
initialA: number           // default 1
initialB: number           // default 1
initialC: number           // default 0
initialD: number           // default 0
```

---

### `UnitCircleExplorer.vue`
**Target:** `slidev/components/graphs/UnitCircleExplorer.vue`
**What it should do:** Draggable terminal point on a unit circle.
Shows reference angle, quadrant color, reference triangle with
side colors, exact trig values.

**Proposed props:**
```ts
angle: number              // initial angle in degrees, default 30
showExactValues: boolean   // default true
showReferenceTriangle: boolean // default true
showQuadrantColors: boolean    // default true
```

---

## Registry Update Protocol

When you build any new component or Manim scene:

1. Add it to the appropriate section above.
2. Include: file path, line count, status, what it does, props, usage example.
3. Move it out of "Planned" and into the appropriate existing section.
4. Add an entry to `CHANGELOG.md`.
