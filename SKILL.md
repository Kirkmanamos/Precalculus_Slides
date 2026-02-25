---
name: ppt-to-slidev-math
description: Convert PowerPoint math lessons into polished Slidev (Vue) decks with interactive SVG graphing components, teacher-controlled reveals, and rigorous mathematical accuracy. Prioritize PPT slide-by-slide alignment while upgrading key slides with purposeful animations and manipulatives.
---

# PPT → Slidev (Vue) Interactive Math Decks

Slidev runs on Vue.js, so you can:
- Import Vue components
- Use reactive state and computed properties
- Add sliders, toggles, and inputs
- Animate values intentionally
- Build interactive graphs (prefer Vue + SVG)

This skill’s goal is to convert an existing **PowerPoint deck** into a **Slidev deck** that stays faithful to the original while teaching concepts better through interactive, animated graphics.

## Core Philosophy

1. **Fidelity to the PPT** — Maintain slide order, pacing, hierarchy, and “what appears when.”
2. **Teach With Manipulatives** — Use interactivity to reveal cause/effect (transformations, asymptotes, constraints).
3. **Professional Design** — Clean, intentional typography/layout/motion; avoid generic templates.
4. **Math Rigor (Non-negotiable)** — Every plotted point, label, value, and table entry must be correct.
5. **Reusable Components** — Build a small set of graphing/lesson components and reuse across the curriculum.

---

## Phase 0: Detect Mode

First determine what the user wants:

**Mode A: New Slidev Lesson**
- User wants to create a new deck from scratch
- Proceed to Phase 1 (Content Discovery)

**Mode B: PPT Conversion (most common)**
- User has a `.ppt` / `.pptx` (or a PDF export) to convert
- Proceed to Phase 4 (PPT → Slidev Conversion)

**Mode C: Enhance an Existing Slidev Deck**
- User already has a Slidev deck and wants better visuals/interactions
- Read the current project and enhance components + slides

---

## Phase 1: Content Discovery (New Lessons)

Before designing, understand the content and pedagogy. Ask via AskUserQuestion.

### Step 1.1: Lesson Context

**Question 1: Goal**
- Header: "Goal"
- Question: "What should students be able to do by the end?"
- Options:
  - "Conceptual understanding" — mental model + intuitiond
  - "Procedural fluency" — reliable steps and practice
  - "Modeling / applications" — interpret context and build functions
  - "Assessment review" — targeted practice + common mistakes

**Question 2: Grade / Level**
- Header: "Level"
- Question: "What course and unit is this for?"
- Options:
  - "Precalculus" — trig, functions, modeling
  - "Algebra 2" — transformations, polynomials, rationals
  - "Geometry" — coordinate geometry, trig ratios

**Question 3: Interaction Density**
- Header: "Interactivity"
- Question: "How interactive should the deck be?"
- Options:
  - "Light (Recommended)" — a few key interactive slides
  - "Medium" — interactive visuals on most concept slides
  - "High" — lots of manipulatives + practice widgets

---

## Phase 2: Style Discovery (Show, Don’t Tell)

People don’t reliably choose styles via adjectives. Generate visual previews instead.

### Step 2.1: Mood Selection

**Question: Vibe**
- Header: "Vibe"
- Question: "What should the slides feel like?"
- Options:
  - "Chalkboard" — classroom, high-contrast, math-forward
  - "Graph Paper" — clean grids, graphing-centric, bright
  - "Midnight Executive" — premium dark, minimal, projector-safe
  - "Deep Space" — inspiring, subtle motion, atmospheric
- multiSelect: false <!-- TODO Why not true? -->

### Step 2.2: Generate Slidev Style Previews

Create **3 mini Slidev preview decks** (title slide only) so the user can compare.

Create in: `.claude-design/slidev-style-previews/`

```
.claude-design/slidev-style-previews/
  style-a/
    slides.md
    style.css
  style-b/
    slides.md
    style.css
  style-c/
    slides.md
    style.css
```

Preview requirements:
- Uses non-generic fonts (Google Fonts is fine).
- Demonstrates hierarchy (H1/H2/body), color palette, and reveal motion.
- Avoid default “Tailwind demo” look.

Then ask:
1) Which style is closest? 2) What to adjust?

---

## Phase 3: Build the Slidev Deck

### Suggested Project Skeleton

Use a consistent structure so decks scale across a full curriculum:

```
slides.md
public/
  ppt/
    slide-001.png
    slide-002.png
components/
  overlay/
    SlideOverlay.vue
    StepReveal.vue
  graphs/
    GraphFrame.vue
    Axes2D.vue
    FunctionPlot.vue
    DraggablePoint.vue
  lessons/
    TrigGraph.vue
    RationalFunction.vue
    UnitCircleExplorer.vue
composables/
  useDragPoint.ts
  useScales.ts
  useSampling.ts
```

Rules of thumb:
- Lesson-specific visuals → `components/lessons/`
- Reusable primitives → `components/graphs/` and `composables/`

### Teacher-Controlled Reveals

Worked examples and answers should be **teacher-controlled** (click/space to advance).

- Prefer Slidev-native reveal tools when possible.
- If insufficient, implement `StepReveal.vue` that:
  - Advances on click and keyboard,
  - Supports resetting per slide,
  - Respects reduced motion.

---

## Phase 4: PPT → Slidev Conversion (Align to Existing Slides)

This phase is the core of the skill: match the premade PPT while adding targeted interactive overlays.

### Step 4.1: Choose Conversion Mode

**Fidelity-first (recommended)**
- Export each PPT slide to an image.
- Use that image as the Slidev slide background.
- Overlay interactive Vue components on top.

**Semantic-first**
- Extract text/images and rebuild layout as real HTML/CSS.
- Best when the PPT is messy or when you need editable text and accessibility.
- More time-consuming and error-prone for layout matching.

Default to Fidelity-first unless the user explicitly needs semantic reconstruction.

### Step 4.2: Export PPT Slides to Images (Fidelity-first)

Goal: lock the look so you can focus on interaction and correctness.

- Export slides to PNG, named:
  - `public/ppt/slide-001.png`
  - `public/ppt/slide-002.png`
  - …

Quality bar:
- Crisp on a projector (1920×1080 or higher).
- No cropping or aspect ratio mismatch.

### Step 4.3: Create 1 Slidev Slide Per PPT Slide

Use Slidev slide frontmatter to set backgrounds and preserve numbering.

```md
---
background: /ppt/slide-001.png
---

<SlideOverlay :slide="1">
  <!-- overlays only if they add learning value -->
</SlideOverlay>
```

### Step 4.4: Overlay Interactive Elements (Only Where It Helps)

Examples of high-value overlays:
- Trig transformation sliders (A, B, C, D) + key points
- Draggable points on a curve to connect equation ↔ graph
- Rational function asymptote/holes toggles
- Unit circle draggable terminal point + reference triangle

Rule: usually **one main interaction per slide**.

---

## Interactive Graphing Strategy

### Option A: Pure Vue + SVG (Most Flexible, Recommended)

Build your own graphing components:
- Use `<svg>`
- Plot functions with computed point arrays
- Animate with reactive parameters
- Add draggable points and snapping
- Show asymptotes/holes dynamically

This gives total control and is ideal for teaching transformations.

### Graph Correctness Rules (Non-negotiable)

- Sample enough points for smooth curves.
- Plot key points explicitly (intercepts, extrema, asymptotes, holes).
- Handle discontinuities: never draw through a vertical asymptote.
- Remember SVG y-axis is inverted vs Cartesian; transform consistently.

### Exact-Value Conventions (Trig)

For special angles, display exact labels when conventional:
- `1/2`, `sqrt(3)/2`, `sqrt(2)/2`, `pi/6`, `pi/4`, `pi/3`, …

Compute numeric coordinates for plotting as needed, but show exact values to students where appropriate.

### Consistent Quadrant Colors (Use Everywhere)

Use this exact mapping across all diagrams:
- QI: `#4ade80` (green)
- QII: `#22d3ee` (cyan)
- QIII: `#f472b6` (pink)
- QIV: `#fbbf24` (gold)

Coordinate-plane right triangles:
- x-side: cyan
- y-side: pink
- r-side: green

---

## Reusable Lesson Components (Recommended Starter Set)

Build these and reuse across units:

- `<TrigGraph />` — transformations, key points, sliders, toggles
- `<RationalFunction />` — asymptotes, holes, domain restrictions
- `<PolynomialFactoringVisualizer />` — step reveal + pattern recognition
- `<UnitCircleExplorer />` — draggable point + exact labels + quadrant signs

---

## Practice / Questions (Align to the PPT)

When the PPT contains practice problems, keep prompts the same but upgrade interaction:

- Multiple choice: click options + teacher-controlled reveal + explanation
- Numeric input: validate format + show revealable solution path
- Graph ID: compare candidate transformations with toggles

Design rule: practice UI must remain slide-native (lightweight, not “web app UI”).

---

## Accessibility & Performance Checklist

- All controls have labels and are keyboard usable.
- Respect `prefers-reduced-motion` (disable non-essential motion).
- Avoid heavy render loops; prefer computed SVG updates and CSS transitions.
- Keep overlays stable (no jitter); sliders need sensible ranges/steps.

---

## QA Checklist Before Delivery

### PPT alignment
- Slide count and order match the PPT exactly.
- Background images are crisp and not stretched/cropped.
- Overlays align to the underlying visuals (no drift).

### Math correctness
- Verify all labeled values and key plotted points.
- Plug plotted points back into the defining equation.
- Discontinuities/asymptotes are handled correctly.

### Interaction quality
- Teacher-controlled reveals behave predictably.
- Dragging stays constrained (curve/circle) and feels stable.
- No console errors.
