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

> No scenes built yet. The `manim/shared/colors.py` constants file is ready.
> First scenes to build:

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
