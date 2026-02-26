---
theme: default
title: "4.9 Inverse Trig Functions (Slidev Prototype)"
info: "Prototype subset conversion of the 4.9 inverse trig deck with click-to-reveal and an interactive arcsin demo."
drawings:
  persist: false
transition: fade-out
mdc: true
---

---
layout: cover
class: hero-slide
---

<div class="hero-shell">
  <div class="hero-tag">Section 4.9 Prototype</div>
  <h1>Inverse Trig Functions</h1>
  <p class="hero-subtitle">Slidev experiment: KaTeX math, click-to-reveal solutions, and interactive graph exploration</p>

  <div class="hero-goals">
    <div class="goal">
      <div class="goal-label">Prototype Scope</div>
      <div class="goal-text">Subset conversion (5-6 slides)</div>
    </div>
    <div class="goal">
      <div class="goal-label">Interaction</div>
      <div class="goal-text">Reveal steps + simple math demo</div>
    </div>
    <div class="goal">
      <div class="goal-label">Math Rendering</div>
      <div class="goal-text">KaTeX + SVG diagrams</div>
    </div>
  </div>

  <div class="tag-row">
    <span class="tag">Dark/Light Toggle</span>
    <span class="tag">Teacher-paced reveals</span>
    <span class="tag">Future Manim-ready pipeline</span>
  </div>
</div>

---
layout: two-cols
class: panel-slide
---

<div class="panel-box">
  <div class="eyebrow">Recall</div>
  <h2 class="panel-title">How trig vs inverse trig behaves</h2>
  <p>Think of the inverse trig function as reversing the input/output roles.</p>

  <div class="concept-grid">
    <div class="concept-card">
      <h3>Trig Function</h3>
      <div class="flow-row">
        <div class="flow-pill">angle</div>
        <div class="flow-arrow">→</div>
        <div class="flow-pill">ratio</div>
      </div>
    </div>

    <div class="concept-card" v-click>
      <h3>Inverse Trig Function</h3>
      <div class="flow-row">
        <div class="flow-pill">ratio</div>
        <div class="flow-arrow">→</div>
        <div class="flow-pill">angle</div>
      </div>
    </div>
  </div>

  <div class="hint-chip">Space / click to reveal steps</div>
</div>

::right::

<div class="panel-box">
  <div class="eyebrow">Key Ideas</div>
  <h2 class="panel-title">What changes with inverses?</h2>

  <v-clicks>

  - The output is an **angle**, not a side ratio.
  - We must use a **restricted domain** on the original trig function to make it one-to-one.
  - For this prototype, we focus on **$\arcsin(x)$** and its principal range.
  - Both notations are common: **$\arcsin(x)$** and **$\sin^{-1}(x)$**.

  </v-clicks>

  <div class="summary-card" v-click>
    <div class="label">Caution</div>
    <p><strong>$\sin^{-1}(x)$</strong> means inverse sine, not <strong>$\dfrac{1}{\sin(x)}$</strong>.</p>
  </div>
</div>

---
layout: two-cols
class: panel-slide
---

## Inverse Sine: Definition, Domain, Range

To define an inverse, we restrict the sine function to the interval
$[-\pi/2,\pi/2]$ so it is one-to-one.

<v-clicks>

- Notation: $y=\arcsin(x)$ or $y=\sin^{-1}(x)$
- Domain: $-1 \le x \le 1$
- Range (principal values): $-\pi/2 \le \arcsin(x) \le \pi/2$
- The output of inverse sine is an angle in radians.

</v-clicks>

::right::

## Visual Strategy (Prototype)

Use the interactive graph on the next slide to model the full idea:

1. Graph the restricted sine function on $[-\pi/2,\pi/2]$.
2. Reflect across the line $y=x$.
3. Read $\arcsin(x)$ as the output angle in the principal range.

<v-clicks>

- Common mistake: choosing an angle outside the principal range
- Teacher move: ask "What interval must the answer come from?"
- Then verify on the interactive graph with a slider input

</v-clicks>

---

# Example 1 Prototype

Use the slider to explore the graph of `y = arcsin(x)` and verify that outputs stay in the principal range.

<ArcsinGraphDemo />

## Anchor Points

- `(-1, -pi/2)`
- `(0, 0)`
- `(1, pi/2)`

## Teacher Prompt

- Ask students to predict `arcsin(1/2)` before using the preset button.
- Emphasize that the output is an angle (in radians).

---
class: panel-slide
---

## Worked Example: `arcsin(-1/2)`

Teacher-paced reveal prototype using Slidev fragments.

<v-clicks>

- Find an angle whose sine is `-1/2`.
- Reference angle is `pi/6` because `sin(pi/6) = 1/2`.
- Use the principal range `[-pi/2, pi/2]`, so choose the angle `-pi/6`.
- Therefore, `arcsin(-1/2) = -pi/6`.

</v-clicks>

<div class="summary-card" style="margin-top: 0.75rem;">
  <div class="label">Range Check</div>
  <p><code>sin(-pi/6) = -1/2</code> and <code>-pi/6</code> is in <code>[-pi/2, pi/2]</code>.</p>
</div>

---
layout: two-cols
class: panel-slide
---

<div class="panel-box">
  <div class="eyebrow">Composition Example</div>
  <h2 class="panel-title">Evaluate arcsin(sin(π/3)) exactly</h2>

  <div class="work-card problem">
    <div class="label">Goal</div>
    <div class="math-big">arcsin(sin(π/3))</div>
  </div>

  <div class="step-row">
    <div class="step-chip" v-click>
      <div class="step-chip__title">Step 1</div>
      <p>Check whether pi/3 lies in the principal range of arcsin: [-pi/2, pi/2].</p>
    </div>
    <div class="step-chip" v-click>
      <div class="step-chip__title">Step 2</div>
      <p>Yes, because -pi/2 <= pi/3 <= pi/2.</p>
    </div>
    <div class="step-chip" v-click>
      <div class="step-chip__title">Step 3</div>
      <p>Since the input angle is already in the inverse sine range, the composition returns the same angle.</p>
    </div>
  </div>

  <div class="answer-banner" v-click>
    arcsin(sin(pi/3)) = pi/3
  </div>
</div>

::right::

<div class="panel-box">
  <div class="eyebrow">Prototype Success Check</div>
  <h2 class="panel-title">What this experiment proves</h2>

  <div class="success-list">
    <div class="success-item" v-click>KaTeX renders inverse trig notation and exact values cleanly.</div>
    <div class="success-item" v-click>Click-to-reveal steps work for teacher-paced examples.</div>
    <div class="success-item" v-click>Vue components can support interactive math demos inside Slidev.</div>
    <div class="success-item" v-click>Dark/light mode can be handled at the deck level without duplicating slides.</div>
  </div>

  <div class="summary-card" style="margin-top: 0.75rem;" v-click>
    <div class="label">Next Phase (Later)</div>
    <p>Add Manim-generated assets/videos for graph animations and worked-example visuals.</p>
  </div>
</div>
