# Agents Guide: HTML Slide Presentations

This document is for any AI agent (Claude, Claude Code, ChatGPT, Gemini, Deepseek, Codex, Copilot, or others) working on HTML slide presentations in this repository. Read this entire file before making any modifications.

---

## Core Philosophy

1. **Zero Dependencies** -- Every presentation is a single self-contained HTML file with inline CSS and JS. No npm, no build tools, no frameworks, no external JS libraries. The only external resources allowed are font stylesheets (Google Fonts, Fontshare).

2. **Show, Don't Tell** -- Non-designers discover their aesthetic through visual exploration. When creating new presentations, generate style preview files rather than describing styles in words.

3. **Distinctive Design** -- Avoid generic "AI slop" aesthetics. Every presentation should feel custom-crafted. See the [Anti-Patterns](#anti-patterns-avoid-these) section.

4. **Mathematical Rigor** -- When presentations contain math, graphs, tables, or data visualizations, **every value must be computed correctly**. Never approximate, guess, or use placeholder numbers. See the [Mathematical Accuracy](#mathematical-accuracy) section.

5. **Production Quality** -- Code must be well-commented, accessible, performant, and responsive.

---

## File Structure

Each presentation in this repo follows one of these patterns:

```
presentation-name.html          # Self-contained single file
presentation-name-assets/       # Optional: images extracted from PPT conversions
```

All CSS and JS live inline within the HTML file. There are no shared stylesheets or script files across presentations.

---

## HTML Architecture

Every presentation follows this skeleton. Do not deviate from this structure when creating or modifying slides.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentation Title</title>

    <!-- Fonts: use Fontshare or Google Fonts only -->
    <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=...">

    <style>
        /* ===========================================
           CSS CUSTOM PROPERTIES (THEME)
           Change these to change the entire look.
           =========================================== */
        :root {
            /* Colors */
            --bg-primary: #0a0f1c;
            --bg-secondary: #111827;
            --text-primary: #ffffff;
            --text-secondary: #9ca3af;
            --accent: #00ffcc;
            --accent-glow: rgba(0, 255, 204, 0.3);

            /* Typography */
            --font-display: 'Clash Display', sans-serif;
            --font-body: 'Satoshi', sans-serif;

            /* Spacing */
            --slide-padding: clamp(2rem, 5vw, 4rem);

            /* Animation */
            --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
            --duration-normal: 0.6s;
        }

        /* ===========================================
           BASE STYLES
           =========================================== */
        * { margin: 0; padding: 0; box-sizing: border-box; }

        html {
            scroll-behavior: smooth;
            scroll-snap-type: y mandatory;
        }

        body {
            font-family: var(--font-body);
            background: var(--bg-primary);
            color: var(--text-primary);
            overflow-x: hidden;
        }

        /* ===========================================
           SLIDE CONTAINER
           Each <section> is one slide.
           =========================================== */
        .slide {
            min-height: 100vh;
            padding: var(--slide-padding);
            scroll-snap-align: start;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        /* ===========================================
           ANIMATIONS
           .visible is added by the Intersection Observer in JS.
           =========================================== */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity var(--duration-normal) var(--ease-out-expo),
                        transform var(--duration-normal) var(--ease-out-expo);
        }

        .slide.visible .reveal {
            opacity: 1;
            transform: translateY(0);
        }

        /* Stagger children */
        .reveal:nth-child(1) { transition-delay: 0.1s; }
        .reveal:nth-child(2) { transition-delay: 0.2s; }
        .reveal:nth-child(3) { transition-delay: 0.3s; }
        .reveal:nth-child(4) { transition-delay: 0.4s; }

        /* Reduced motion */
        @media (prefers-reduced-motion: reduce) {
            .reveal {
                transition: opacity 0.3s ease;
                transform: none;
            }
        }

        /* Mobile */
        @media (max-width: 768px) {
            .nav-dots, .keyboard-hint { display: none; }
        }
    </style>
</head>
<body>
    <!-- Optional: progress bar -->
    <div class="progress-bar"></div>

    <!-- Optional: navigation dots -->
    <nav class="nav-dots"></nav>

    <!-- Slides -->
    <section class="slide title-slide">
        <h1 class="reveal">Title</h1>
        <p class="reveal">Subtitle</p>
    </section>

    <section class="slide">
        <h2 class="reveal">Slide Title</h2>
        <p class="reveal">Content</p>
    </section>

    <script>
        /* ===========================================
           SLIDE PRESENTATION CONTROLLER
           =========================================== */
        class SlidePresentation {
            constructor() { /* ... */ }
        }
        new SlidePresentation();
    </script>
</body>
</html>
```

### Required JavaScript Features

Every presentation must include:

1. **SlidePresentation class** -- main controller handling:
   - Keyboard navigation (arrow keys, space bar)
   - Touch/swipe support for mobile
   - Mouse wheel navigation
   - Progress bar updates
   - Navigation dots (optional but recommended)

2. **Intersection Observer** -- for scroll-triggered animations:
   - Adds `.visible` class when slides enter the viewport
   - Triggers CSS transitions defined on `.reveal` elements

3. **Optional enhancements** (match to the chosen style):
   - Custom cursor with trail
   - Particle system background (canvas)
   - Parallax effects
   - 3D tilt on hover
   - Counter animations
   - Typewriter text reveals

---

## Design Principles

### Typography

Use distinctive font pairings. Every presentation should have a **display font** (for headings) and a **body font** (for content). Source fonts from Fontshare or Google Fonts.

**Recommended pairings:**

| Vibe | Display Font | Body Font | Source |
|------|-------------|-----------|--------|
| Techy/Modern | Clash Display | Satoshi | Fontshare |
| Professional | Libre Baskerville | Source Sans 3 | Google |
| Space/Future | Space Grotesk | DM Sans | Google |
| Developer | JetBrains Mono | JetBrains Mono | JetBrains |
| Editorial | Cormorant Garamond | Source Serif 4 | Google |
| Swiss/Minimal | Archivo | Nunito | Google |
| Playful | Nunito | Nunito | Google |
| Magazine | Playfair Display | Work Sans | Google |
| Brutalist | Anton | IBM Plex Mono | Google |
| SaaS Modern | Cabinet Grotesk | Inter | Fontshare/Google |

### Color

Define all colors as CSS custom properties in `:root`. Every theme needs at minimum:
- `--bg-primary` and `--bg-secondary`
- `--text-primary` and `--text-secondary`
- `--accent` (and optionally `--accent-secondary`)

### Animation Easing Reference

```css
:root {
    --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);    /* Standard */
    --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);   /* Smooth */
    --ease-out-cubic: cubic-bezier(0.33, 1, 0.68, 1);   /* Gentle */
    --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);   /* Bouncy */
    --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Spring */
    --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);        /* Material */
    --ease-snappy: cubic-bezier(0.68, -0.55, 0.265, 1.55); /* Snappy */
}
```

### Style-to-Feeling Mapping

Match animation speed and intensity to the intended mood:

| Feeling | Animation Speed | Movement | Background |
|---------|----------------|----------|------------|
| Dramatic/Cinematic | Slow (0.8-1.5s) | Large scale transitions | Dark with spotlights, parallax |
| Techy/Futuristic | Medium (0.5-0.8s) | Slide + fade | Neon glows, particles, grids |
| Playful/Friendly | Medium with overshoot | Bouncy spring physics | Pastel, blob shapes |
| Professional/Corporate | Fast (0.2-0.3s) | Subtle fades | Clean, minimal decoration |
| Calm/Minimal | Slow, subtle | Gentle fades only | High whitespace, muted palette |
| Editorial/Magazine | Medium (0.4-0.6s) | Understated | Strong type hierarchy, one accent |

### Accessibility Requirements

- Semantic HTML: use `<section>`, `<nav>`, `<main>`, `<h1>`-`<h6>` correctly
- Keyboard navigation must work completely
- Add ARIA labels where needed
- Support `prefers-reduced-motion` with a `@media` query
- Ensure sufficient color contrast

### Responsive Requirements

- Single-column layout on mobile
- Disable heavy canvas effects below 768px
- Touch-friendly interactions (minimum 44px tap targets)
- Use `clamp()` for fluid spacing and font sizes

---

## Mathematical Accuracy

**This is non-negotiable.** When a presentation involves math, every number, coordinate, graph point, table value, and computed result must be mathematically correct. Do not estimate. Do not use "close enough" values. Verify every calculation.

### General Rules

1. **Compute, don't approximate.** If a problem asks for sin(30deg), the answer is exactly 1/2, not 0.5 displayed as a decimal unless the context requires it.

2. **Verify with the Pythagorean theorem.** For any right triangle with sides a, b, and hypotenuse c, confirm that a^2 + b^2 = c^2 before rendering.

3. **Check sign conventions.** In coordinate geometry, quadrant signs matter. Point (-3, 4) is in Quadrant II. The x-component is negative. The y-component is positive. Get this right.

4. **Use exact values where conventional.** Display fractions and radicals (1/2, sqrt(3)/2, sqrt(2)/2) for special angles rather than decimal approximations, unless the context specifically calls for decimals.

5. **Validate graph coordinates.** Before drawing any SVG path or placing any point, verify the (x, y) coordinates by plugging back into the original equation.

6. **Double-check tables.** For T-tables (input/output tables), compute every output value from the given function. Verify the first and last rows, then spot-check at least two middle rows.

### T-Tables (Input/Output Tables)

When creating a T-table for a function f(x):

1. Choose appropriate x-values that reveal the function's behavior (intercepts, turning points, asymptote approaches).
2. Compute f(x) for each x-value exactly.
3. Verify at least 3 values independently before rendering.
4. Display using a clean, aligned layout:

```html
<div class="t-table">
    <div class="t-header">
        <span>x</span>
        <span>f(x) = 2x + 3</span>
    </div>
    <div class="t-row">
        <span>-2</span>
        <span>-1</span>   <!-- 2(-2) + 3 = -4 + 3 = -1 -->
    </div>
    <div class="t-row">
        <span>0</span>
        <span>3</span>    <!-- 2(0) + 3 = 0 + 3 = 3 -->
    </div>
    <!-- ... -->
</div>
```

### Graph Accuracy

#### SVG Coordinate System

Understand the SVG coordinate system before plotting:
- SVG y-axis is **inverted** (positive y goes downward)
- To plot a Cartesian point (x, y), the SVG coordinates are (x * scale, **-y** * scale)
- Always define a consistent scale (e.g., 20-25 pixels per unit) and apply it uniformly

#### Plotting Functions

When drawing a function curve as an SVG `<path>`:

1. **Sample enough points** for smooth curves (at minimum 20-30 points across the visible domain for non-linear functions).
2. **Use `<path>` with line segments or cubic beziers**, not freehand approximations.
3. **Mark key points explicitly**: intercepts, maxima, minima, inflection points, asymptote intersections.
4. **Label axes** with correct tick marks and numbers at consistent intervals.
5. **Handle discontinuities**: for rational functions with vertical asymptotes, break the path into separate segments. Do not draw through an asymptote.

#### Coordinate Plane Standards

```svg
<svg viewBox="-200 -150 400 300">
    <!-- Grid lines (minor and major) -->
    <!-- Axes with arrow markers -->
    <!-- Tick marks at regular intervals with numeric labels -->
    <!-- Function curve -->
    <!-- Key points marked with filled circles -->
    <!-- Labels for key values -->
</svg>
```

Scale guidance:
- Coordinate plane: 20-25px per unit
- Unit circle: radius of 120px in a 320x320 viewBox
- Polar graphs: concentric circles at 30px intervals

### Quadrant Color Convention

Use these colors consistently across ALL diagrams in ALL presentations:

```css
--q1-color: #4ade80;  /* Green  -- Quadrant I   */
--q2-color: #22d3ee;  /* Cyan   -- Quadrant II  */
--q3-color: #f472b6;  /* Pink   -- Quadrant III */
--q4-color: #fbbf24;  /* Gold   -- Quadrant IV  */
```

These must not change between presentations or between diagrams within a presentation.

### Triangle Side Color Convention

For right triangles on the coordinate plane:
- **x-side** (horizontal): cyan
- **y-side** (vertical): pink
- **r-side** (hypotenuse): green

### Common Math Reference Values

Agents must use these exact values. Do not recalculate from scratch and risk rounding errors -- use these as the source of truth for special angles.

**Special Angle Values:**

| Degrees | Radians | sin | cos | tan |
|---------|---------|-----|-----|-----|
| 0 | 0 | 0 | 1 | 0 |
| 30 | pi/6 | 1/2 | sqrt(3)/2 | sqrt(3)/3 |
| 45 | pi/4 | sqrt(2)/2 | sqrt(2)/2 | 1 |
| 60 | pi/3 | sqrt(3)/2 | 1/2 | sqrt(3) |
| 90 | pi/2 | 1 | 0 | undefined |

**Quadrant Sign Rules (ASTC -- All Students Take Calculus):**
- QI: All trig functions positive
- QII: Only sin (and csc) positive
- QIII: Only tan (and cot) positive
- QIV: Only cos (and sec) positive

**Pythagorean Triples:**
- 3-4-5 (and multiples: 6-8-10, 9-12-15, 12-16-20)
- 5-12-13
- 8-15-17
- 7-24-25

**Parent Functions** (know these shapes before graphing transformations):
- Linear: f(x) = x
- Quadratic: f(x) = x^2
- Cubic: f(x) = x^3
- Square root: f(x) = sqrt(x)
- Absolute value: f(x) = |x|
- Exponential: f(x) = e^x or 2^x
- Logarithmic: f(x) = ln(x) or log(x)
- Rational: f(x) = 1/x

**Transformation Rules** (for graphing transformed functions):
- f(x) + k shifts up by k
- f(x - h) shifts right by h
- a * f(x) stretches vertically by factor a
- f(bx) compresses horizontally by factor b
- -f(x) reflects over the x-axis
- f(-x) reflects over the y-axis

**Sequence and Series Formulas:**
- Arithmetic: a_n = a_1 + (n-1)d
- Geometric: a_n = a_1 * r^(n-1)
- Arithmetic sum: S_n = n/2 * (a_1 + a_n)
- Geometric sum: S_n = a_1(1 - r^n) / (1 - r)
- Infinite geometric: S = a_1 / (1 - r) when |r| < 1

**Probability Formulas:**
- P(A or B) = P(A) + P(B) - P(A and B)
- P(A and B) = P(A) * P(B|A)
- Combinations: C(n,r) = n! / (r!(n-r)!)
- Permutations: P(n,r) = n! / (n-r)!
- Binomial: P(x) = C(n,x) * p^x * (1-p)^(n-x)

---

## Math Presentation Patterns

### Click-to-Advance for Worked Examples

For worked examples and problem solutions, use click-to-advance rather than auto-animation. Teachers control when answers appear.

```javascript
setupClickToAdvance(slideId, maxSteps) {
    const slide = document.getElementById(slideId);
    let currentStep = -1;

    slide.addEventListener('click', () => {
        if (currentStep < maxSteps) {
            currentStep++;
            slide.querySelector('.step-' + currentStep)?.classList.add('active');
        }
    });
}
```

```css
.step-box {
    opacity: 0;
    transform: translateX(-20px);
    transition: all 0.6s ease;
}

.step-box.active {
    opacity: 1;
    transform: translateX(0);
}
```

### Math Typography

Use monospace for mathematical expressions:

```css
.math, .formula, .problem-item {
    font-family: 'SF Mono', 'Monaco', 'Consolas', monospace;
}
```

Use Unicode characters for Greek letters and symbols:
- theta: `&theta;` or the literal character
- pi: `&pi;` or the literal character
- sqrt: `&radic;` or the literal character
- Fractions: display as `a/b` (e.g., `sqrt(3)/2`)

### SVG Diagram Templates

These are the standard diagram types used across math presentations. When modifying or creating diagrams, follow these patterns exactly.

**Unit Circle:**
```svg
<svg viewBox="-160 -160 320 320">
    <line class="axis" x1="-150" y1="0" x2="150" y2="0" />
    <line class="axis" x1="0" y1="-150" x2="0" y2="150" />
    <circle cx="0" cy="0" r="120" fill="none" stroke="currentColor" />
    <!-- Angle arc, terminal side, reference line, point on circle -->
</svg>
```

**Coordinate Plane with Triangle:**
```svg
<svg viewBox="-160 -160 320 320">
    <!-- Grid, axes, tick marks -->
    <line class="side-x" ... />  <!-- cyan -->
    <line class="side-y" ... />  <!-- pink -->
    <line class="side-r" ... />  <!-- green -->
    <!-- Right angle marker, reference angle arc, labels -->
</svg>
```

**Function Graph:**
```svg
<svg viewBox="-200 -150 400 300">
    <g class="grid"><!-- Grid lines --></g>
    <line class="axis" x1="-190" y1="0" x2="190" y2="0" />
    <line class="axis" x1="0" y1="-140" x2="0" y2="140" />
    <g class="ticks"><!-- Axis tick marks and labels --></g>
    <path class="function-curve" d="M ... " />
    <!-- Key points, asymptotes if applicable -->
</svg>
```

**Polar Graph:**
```svg
<svg viewBox="-150 -150 300 300">
    <!-- Concentric circles at r=1,2,3... -->
    <!-- Radial lines every 30 or 45 degrees -->
    <!-- Angle labels -->
    <path class="polar-curve" d="M ... " />
</svg>
```

### Math Slide Layout Patterns

**Problem Set:**
```html
<div class="problem-card">
    <div class="problem-grid">
        <div class="problem-item">
            <span class="letter">a)</span>
            <span class="math">sin 30&deg;</span>
        </div>
    </div>
</div>
```

**Worked Example (click-to-advance):**
```html
<div class="steps-container">
    <div class="step-box step-0">
        <p class="step-header">Given</p>
        <p class="step-content">...</p>
    </div>
    <div class="step-box step-1">
        <p class="step-header">Step 1</p>
        <p class="step-content">...</p>
    </div>
</div>
```

**Answer Reveal:**
```html
<div class="answer-grid">
    <div class="answer-item">
        <span class="problem-num">1:</span>
        <span class="answer">QII</span>
        <span class="note">sin+ and tan- only in QII</span>
    </div>
</div>
```

---

## Style Presets Reference

These are the established visual styles. When modifying an existing presentation, identify which style it uses and maintain consistency. When creating new presentations, choose from this list or create a new style that follows the same level of specificity.

### Dark Themes

**Neon Cyber** -- Futuristic, techy, confident. Clash Display + Satoshi. Deep navy background (#0a0f1c), cyan accent (#00ffcc), magenta secondary (#ff00aa). Particle system, neon glow, grid overlay, custom cursor.

**Midnight Executive** -- Premium, trustworthy, corporate. Libre Baskerville + Source Sans 3. Dark slate (#0f172a), blue accent (#3b82f6), gold highlight (#fbbf24). Subtle gradients, thin gold lines, minimal decoration.

**Deep Space** -- Inspiring, vast, visionary. Space Grotesk + DM Sans. Near-black (#030712), indigo accent (#818cf8), purple secondary (#c084fc). Starfield, spotlight effects, floating elements, parallax.

**Terminal Green** -- Developer, hacker, retro-tech. JetBrains Mono throughout. GitHub dark (#0d1117), green accent (#39d353). Scan lines, blinking cursor, ASCII art, typewriter reveals.

### Light Themes

**Paper & Ink** -- Editorial, literary, refined. Cormorant Garamond + Source Serif 4. Off-white (#faf9f7), crimson accent (#c41e3a). Drop caps, pull quotes, paper texture, horizontal rules.

**Swiss Modern** -- Clean, precise, Bauhaus. Archivo + Nunito. White (#ffffff), red accent (#ff3300). Visible grid, asymmetric layouts, bold black type, geometric shapes.

**Soft Pastel** -- Friendly, playful, creative. Nunito throughout. Warm pink-white (#fef3f2), pink accent (#f472b6), purple secondary (#a78bfa). Rounded corners, blob shapes, bouncy animations.

**Warm Editorial** -- Storytelling, photographic, magazine. Playfair Display + Work Sans. Warm white (#fffbf5), amber accent (#b45309). Large images, overlays, Ken Burns effect.

### Specialty Themes

**Brutalist** -- Raw, bold, unconventional. Anton + IBM Plex Mono. Pure white and black only, red accent (#ff0000). Thick borders, chaotic layouts, oversized type, hard cuts.

**Gradient Wave** -- Modern SaaS, energetic. Cabinet Grotesk + Inter (Inter only allowed here). Dark (#0f0f1a), purple-pink gradient mesh. Glassmorphism, floating orbs, smooth curves.

### Math-Specific Themes

**Chalkboard** -- Dark slate (#1a2332), chalk-white text (#f1f5f9), green accent (#4ade80). Subtle grid. Good for projectors and evening classes.

**Graph Paper** -- White with blue grid lines, dark blue text, red accent. Prominent grid pattern. Good for graphing-heavy content.

---

## Code Quality Standards

### Comments

Every major section of CSS and JS must have a block comment explaining what it does and how to modify it:

```css
/* ===========================================
   SECTION NAME
   Brief description of purpose.
   To modify: explain what to change.
   =========================================== */
```

```javascript
/* ===========================================
   COMPONENT NAME
   What it does and why.
   - Key detail 1
   - Key detail 2
   =========================================== */
```

### Performance

- Use `transform` and `opacity` for animations (GPU-composited)
- Use `will-change` sparingly and only on elements that will animate
- Throttle scroll and mousemove handlers
- Reduce particle count or disable canvas effects on mobile
- Prefer CSS transitions over JS animation loops where possible

---

## Anti-Patterns (Avoid These)

These patterns produce generic, unmemorable presentations. Do not use them.

**Fonts to avoid:**
- Inter (except in Gradient Wave style)
- Roboto
- Arial / Helvetica
- System font stacks as display fonts

**Color anti-patterns:**
- Generic indigo (#6366f1) as a primary color
- Purple/violet gradients on white backgrounds
- Generic blue primary buttons
- Equal distribution of accent colors with no hierarchy

**Layout anti-patterns:**
- Centering everything on every slide
- Generic hero with text-left, image-right
- Standard 3-column feature grids
- Rounded rectangle cards with drop shadows

**Animation anti-patterns:**
- Identical timing on all elements (no stagger)
- Linear easing everywhere
- Excessive bounce on serious content
- Animations that serve no communicative purpose

**Effect anti-patterns:**
- Drop shadows without visual intention
- Gratuitous glassmorphism
- Blurs that don't contribute to hierarchy
- Gradients applied without reason

---

## Modification Checklist

Before submitting any change to a presentation, verify:

- [ ] HTML is valid and self-contained (no broken external dependencies)
- [ ] All CSS custom properties are defined in `:root`
- [ ] Keyboard navigation works (arrow keys, space)
- [ ] Touch/swipe works on mobile
- [ ] `prefers-reduced-motion` media query is present
- [ ] All math values are correct (spot-check at least 3)
- [ ] SVG coordinates match intended Cartesian points (remember y-axis inversion)
- [ ] Graph axes have correct labels and tick marks
- [ ] T-table values are verified by plugging into the function
- [ ] Quadrant colors follow the convention (green, cyan, pink, gold)
- [ ] Triangle side colors follow the convention (x=cyan, y=pink, r=green)
- [ ] Click-to-advance works on all worked examples
- [ ] No anti-pattern fonts, colors, or layouts were introduced
- [ ] Code comments are present on all major sections
- [ ] File opens correctly in a browser with no console errors
