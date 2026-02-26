---
theme: default
title: Precalculus Prototype (Slidev)
info: A styled Slidev prototype deck for trig and sinusoidal modeling lessons.
drawings:
  persist: false
transition: fade-out
mdc: true
defaults:
  layout: center
---

---
layout: cover
class: hero-slide
---

# Precalculus Slides
## Slidev Prototype

**Focus:** exact trig values, sinusoidal modeling, and teacher-friendly pacing

<div class="hero-meta">
  <span>Prototype deck</span>
  <span>Dark math theme</span>
  <span>Click-reveal ready</span>
</div>

---
layout: two-cols
class: panel-slide
---

# Special Angles

Use exact values, not decimals, for the standard reference set.

<div class="formula-card">
  <div class="formula-label">Reference Rule</div>
  <div class="formula-text">

Use $1/2$, $\frac{\sqrt{2}}{2}$, $\frac{\sqrt{3}}{2}$ when conventional.

  </div>
</div>

<div class="quadrant-legend">
  <span class="q q1">QI</span>
  <span class="q q2">QII</span>
  <span class="q q3">QIII</span>
  <span class="q q4">QIV</span>
</div>

::right::

<div class="table-card" markdown="1">

| $\theta$ | $\sin \theta$ | $\cos \theta$ | $\tan \theta$ |
| :--- | :--- | :--- | :--- |
| $0^\circ$ | $0$ | $1$ | $0$ |
| $30^\circ$ | $1/2$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| $45^\circ$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $60^\circ$ | $\frac{\sqrt{3}}{2}$ | $1/2$ | $\sqrt{3}$ |
| $90^\circ$ | $1$ | $0$ | undefined |

</div>

---
class: panel-slide
---

# Sine Modeling (Parameters)

<div class="formula-card wide">
  <div class="formula-label">General Form</div>
  <div class="formula-text">

$$y = a \sin(b(x - h)) + k$$

  </div>
</div>

<div class="parameter-grid">
  <div class="metric">
    <div class="metric-label">Amplitude</div>
    <div class="metric-value">

$|a|$

  </div>
  </div>
  <div class="metric">
    <div class="metric-label">Period</div>
    <div class="metric-value">

$\frac{2\pi}{|b|}$

  </div>
  </div>
  <div class="metric">
    <div class="metric-label">Phase Shift</div>
    <div class="metric-value">

$h$

  </div>
  </div>
  <div class="metric">
    <div class="metric-label">Midline</div>
    <div class="metric-value">

$y = k$

  </div>
  </div>
</div>

<div class="example-strip">

  <span class="label">Example</span>
  <span>$y = 2 \sin\left(x - \frac{\pi}{2}\right) - 1$</span>
  <span>Amplitude = $2$</span>
  <span>Period = $2\pi$</span>
  <span>Shift right $\frac{\pi}{2}$</span>
  <span>Midline $y = -1$</span>

</div>

---
layout: two-cols
class: panel-slide
---

# Exact Checkpoints

For one period of $y = 2 \sin\left(x - \frac{\pi}{2}\right) - 1$, use quarter-period checkpoints.

<div class="table-card">
  <table class="exact-table">
    <thead>
      <tr>
        <th>$x$</th>
        <th>$\sin\left(x - \frac{\pi}{2}\right)$</th>
        <th>$y$</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>$\frac{\pi}{2}$</td><td>$0$</td><td>$-1$</td></tr>
      <tr><td>$\pi$</td><td>$1$</td><td>$1$</td></tr>
      <tr><td>$\frac{3\pi}{2}$</td><td>$0$</td><td>$-1$</td></tr>
      <tr><td>$2\pi$</td><td>$-1$</td><td>$-3$</td></tr>
      <tr><td>$\frac{5\pi}{2}$</td><td>$0$</td><td>$-1$</td></tr>
    </tbody>
  </table>
</div>

::right::

<div class="graph-card">
  <svg viewBox="0 0 360 240" class="checkpoint-plot" role="img" aria-label="Checkpoint plot for y equals 2 sine of x minus pi over 2 minus 1">
    <defs>
      <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 Z" fill="currentColor" />
      </marker>
    </defs>

    <!-- Grid -->
    <g class="grid">
      <line x1="40" y1="30" x2="40" y2="210" />
      <line x1="100" y1="30" x2="100" y2="210" />
      <line x1="160" y1="30" x2="160" y2="210" />
      <line x1="220" y1="30" x2="220" y2="210" />
      <line x1="280" y1="30" x2="280" y2="210" />
      <line x1="340" y1="30" x2="340" y2="210" />

      <line x1="40" y1="40" x2="340" y2="40" />
      <line x1="40" y1="85" x2="340" y2="85" />
      <line x1="40" y1="130" x2="340" y2="130" />
      <line x1="40" y1="175" x2="340" y2="175" />
      <line x1="40" y1="220" x2="340" y2="220" />
    </g>

    <!-- Axes (y=0 at 85, left axis x=40) -->
    <line class="axis" x1="40" y1="85" x2="348" y2="85" marker-end="url(#arrow)" />
    <line class="axis" x1="40" y1="228" x2="40" y2="24" marker-end="url(#arrow)" />

    <!-- Midline y=-1 -->
    <line class="midline" x1="40" y1="130" x2="340" y2="130" />

    <!-- Checkpoints (scale: quarter-period = 60px, 1 unit = 45px) -->
    <!-- y_px = 85 - 45*y -->
    <polyline class="checkpoint-line" points="40,130 100,40 160,130 220,220 280,130" />

    <g class="points">
      <circle cx="40" cy="130" r="5" />
      <circle cx="100" cy="40" r="5" />
      <circle cx="160" cy="130" r="5" />
      <circle cx="220" cy="220" r="5" />
      <circle cx="280" cy="130" r="5" />
    </g>

    <g class="labels">
      <text x="38" y="78" text-anchor="end">0</text>
      <text x="38" y="123" text-anchor="end">-1</text>
      <text x="38" y="168" text-anchor="end">-2</text>
      <text x="38" y="213" text-anchor="end">-3</text>
      <text x="40" y="104" text-anchor="middle">π/2</text>
      <text x="100" y="104" text-anchor="middle">π</text>
      <text x="160" y="104" text-anchor="middle">3π/2</text>
      <text x="220" y="104" text-anchor="middle">2π</text>
      <text x="280" y="104" text-anchor="middle">5π/2</text>
    </g>
  </svg>
  <p class="graph-caption">Checkpoint plot for sketching. Connect with a smooth sinusoid in class.</p>
</div>

---
class: panel-slide reveal-slide
---

# Teacher Pacing (Click Reveal)

Use stepwise reveals for worked examples so answers do not appear too early.

<div class="step-stack">
  <div class="step-card">
    <div class="step-tag">Given</div>
    <div class="text-center my-2">

$$y = 3 \sin(2x) + 4$$

  </div>
  </div>

  <v-click>
    <div class="step-card">
      <div class="step-tag">Step 1</div>

Amplitude = $3$

  </div>
  </v-click>

  <v-click>
    <div class="step-card">
      <div class="step-tag">Step 2</div>

Period = $\frac{2\pi}{2} = \pi$

  </div>
  </v-click>

  <v-click>
    <div class="step-card">
      <div class="step-tag">Step 3</div>

Midline $y = 4$

  </div>
  </v-click>
</div>

<v-clicks>

- Click to reveal one step at a time during instruction.
- Keep symbolic forms exact until the context requires approximations.
- Reuse this structure for tangent, rational, and transformation lessons.

</v-clicks>

---
class: hero-slide
---

# Next Build

1. Pick a unit (Trig, Rational, Sequences, Probability)
2. Duplicate this folder
3. Replace prototype content with lesson-specific slides
4. Add speaker notes and activity prompts

<div class="hero-meta">
  <span class="math">slidev/precalculus-prototype</span>
  <span>ready to customize</span>
</div>

<!--
Speaker note:
This deck is a style and workflow prototype, not a finished lesson.
-->
