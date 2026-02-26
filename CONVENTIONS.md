# Project Conventions

Unified conventions for **all** output formats: HTML presentations, Slidev/Vue decks,
and Manim scenes. When in doubt, this file wins.

---

## 1. Colors

These colors must be used identically across HTML, Slidev CSS, and Manim Python.
Never invent alternatives.

### Quadrant Colors (ASTC)

| Quadrant | Role | Hex | Tailwind-ish name |
|---|---|---|---|
| QI | All positive | `#4ade80` | Green |
| QII | sin positive | `#22d3ee` | Cyan |
| QIII | tan positive | `#f472b6` | Pink |
| QIV | cos positive | `#fbbf24` | Gold/Amber |

### Right Triangle Side Colors

| Side | Description | Color |
|---|---|---|
| x-side | Horizontal leg | Cyan `#22d3ee` |
| y-side | Vertical leg | Pink `#f472b6` |
| r-side | Hypotenuse | Green `#4ade80` |

### Background / Text Palette

| Token | Dark Mode | Light Mode |
|---|---|---|
| `--bg-primary` | `#071018` | `#f7fbff` |
| `--bg-secondary` | `#081421` | `#eef5fb` |
| `--text-primary` | `#eef6ff` | `#102132` |
| `--text-muted` | `#a8bfd0` | `#475f73` |
| `--accent-teal` | `#5eead4` | `#0f766e` |
| `--accent-blue` | `#93c5fd` | `#1d4ed8` |
| `--accent-red` | `#fca5a5` | `#be123c` |

### CSS Custom Properties (Slidev / HTML)

```css
:root {
  --q1: #4ade80;
  --q2: #22d3ee;
  --q3: #f472b6;
  --q4: #fbbf24;
  --x-side: #22d3ee;
  --y-side: #f472b6;
  --r-side: #4ade80;
}
```

### Manim Color Constants

```python
# Always: from shared.colors import *
Q1_COLOR   = "#4ade80"   # Quadrant I   — green
Q2_COLOR   = "#22d3ee"   # Quadrant II  — cyan
Q3_COLOR   = "#f472b6"   # Quadrant III — pink
Q4_COLOR   = "#fbbf24"   # Quadrant IV  — gold

X_SIDE     = Q2_COLOR    # horizontal leg — cyan
Y_SIDE     = Q3_COLOR    # vertical leg   — pink
R_SIDE     = Q1_COLOR    # hypotenuse     — green

BG_COLOR   = "#071018"   # slide background
TEXT_COLOR = "#eef6ff"   # primary text
```

---

## 2. Typography

### Slidev / HTML

| Role | Font | Weight | Source |
|---|---|---|---|
| Display headings | Space Grotesk | 500, 700 | Google Fonts |
| Body text | IBM Plex Sans | 400, 500, 600 | Google Fonts |
| Code / math mono | IBM Plex Mono | 400, 500 | Google Fonts |

Do not substitute Inter, Roboto, or Arial for these fonts.

### Manim

```python
FONT_DISPLAY = "Space Grotesk"
FONT_BODY    = "IBM Plex Sans"
FONT_MONO    = "IBM Plex Mono"
```

---

## 3. Naming Conventions

| Format | Convention | Example |
|---|---|---|
| HTML presentation files | `unit.section-topic-name.html` | `4.7-modeling-sine-cosine.html` |
| Asset folders | `*-assets/` matching the HTML name | `4.7-assets/` |
| Slidev project folders | `unit.section-topic/` | `4.9-inverse-trig-prototype/` |
| Vue components | PascalCase | `ArcsinGraphDemo.vue` |
| Vue composables | camelCase with `use` prefix | `useScales.ts` |
| Manim scene files | `unit_topic_scene.py` snake_case | `4_9_inverse_trig_scene.py` |
| Manim scene classes | PascalCase | `ArcsinGraphScene` |
| Manim exported videos | `public/manim/scene-name.mp4` | inside the Slidev project |

---

## 4. Interactive Slider Ranges

Use these ranges consistently across all interactive graph components.

| Parameter | Label | Min | Max | Step | Default |
|---|---|---|---|---|---|
| Amplitude | A | 0.1 | 5 | 0.1 | 1 |
| Period multiplier | B | 0.25 | 4 | 0.25 | 1 |
| Phase shift | C | −π | π | π/12 | 0 |
| Vertical shift | D | −5 | 5 | 0.5 | 0 |

Slider labels must show the equation form: `y = A·sin(Bx + C) + D`.

---

## 5. SVG / Graphing Rules

### Coordinate System

SVG y-axis is **inverted** relative to Cartesian:
- Cartesian point `(x, y)` → SVG `(x · scale, −y · scale)`
- Always define a consistent `scale` constant and apply it uniformly.
- Standard scales: 20–25 px/unit for coordinate planes; 120 px radius for unit circle.

### Minimum Point Density

| Curve type | Minimum sample points |
|---|---|
| Linear | 2 |
| Quadratic / trig / other smooth | 30+ across visible domain |
| Near asymptote | Extra points at ±0.01 of discontinuity |

### Standard viewBox Sizes

| Diagram type | viewBox |
|---|---|
| Coordinate plane (general) | `-200 -150 400 300` |
| Unit circle | `-160 -160 320 320` |
| Polar graph | `-150 -150 300 300` |
| Trig function (one period) | `-250 -120 500 240` |

### Asymptotes

Never draw through a vertical asymptote. Break the `<path>` into separate
segments above and below each discontinuity.

### Required Diagram Elements

Every coordinate plane must include:
- Grid lines (minor and major, muted)
- Axes with arrowheads
- Tick marks at regular intervals with numeric labels
- Function curve
- Labeled key points (intercepts, extrema, inflection points, holes)

---

## 6. Mathematical Display Standards

### Exact vs. Decimal

Display exact values where conventional:
- Special angle trig values: `1/2`, `√3/2`, `√2/2`, `π/6`, `π/4`, `π/3`
- Show decimals only when context explicitly requires approximation

### KaTeX (Slidev)

Use KaTeX for all inline and block math:
```md
Inline: $\arcsin(x)$
Block: $$y = A\sin(Bx + C) + D$$
```

### HTML Presentations

Use Unicode and CSS monospace for math expressions:
- theta: `θ`, pi: `π`, sqrt: `√`, infinity: `∞`
- Fractions as text: `√3/2`, `1/2`
- Use `font-family: 'SF Mono', 'Monaco', 'Consolas', monospace` for all math

---

## 7. Teacher-Controlled Reveals

All worked examples and answer reveals must be **teacher-paced** (click or
space to advance). Never auto-animate answers.

### In Slidev

Use `v-click` for single items or `<v-clicks>` for lists.

```md
<v-clicks>
- Step 1: identify the reference angle
- Step 2: apply the ASTC sign rule
- Step 3: compute the result
</v-clicks>
```

### In HTML

```javascript
slide.addEventListener('click', () => {
  currentStep++;
  slide.querySelector(`.step-${currentStep}`)?.classList.add('active');
});
```

---

## 8. Special Angle Reference (Source of Truth)

Do not recalculate these. Copy from here.

| Degrees | Radians | sin | cos | tan |
|---|---|---|---|---|
| 0° | 0 | 0 | 1 | 0 |
| 30° | π/6 | 1/2 | √3/2 | √3/3 |
| 45° | π/4 | √2/2 | √2/2 | 1 |
| 60° | π/3 | √3/2 | 1/2 | √3 |
| 90° | π/2 | 1 | 0 | undefined |
| 120° | 2π/3 | √3/2 | −1/2 | −√3 |
| 135° | 3π/4 | √2/2 | −√2/2 | −1 |
| 150° | 5π/6 | 1/2 | −√3/2 | −√3/3 |
| 180° | π | 0 | −1 | 0 |
| 270° | 3π/2 | −1 | 0 | undefined |
| 360° | 2π | 0 | 1 | 0 |

---

## 9. Checklist Before Delivering Any Output

- [ ] Quadrant / side colors match the table in Section 1
- [ ] Fonts are Space Grotesk + IBM Plex (not Inter, Roboto, or Arial)
- [ ] SVG y-axis inversion applied correctly
- [ ] All plotted points verified by back-substitution
- [ ] Slider ranges match Section 4
- [ ] Teacher-controlled reveal on all worked examples
- [ ] New components logged in `COMPONENT_REGISTRY.md`
- [ ] `CHANGELOG.md` updated
