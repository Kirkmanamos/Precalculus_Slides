---
theme: default
title: "4.9 — Inverse Trig Functions"
info: "Precalculus 4.9 — Inverse Trigonometric Functions"
layout: cover
class: hero-slide
drawings:
  persist: false
transition: fade-out
mdc: true
---

<div class="hero-shell">
  <div class="eyebrow">Section 4.9</div>
  <h1>Inverse Trig<br>Functions</h1>
  <p class="hero-subtitle">Finding angles from ratios — <strong>arcsin</strong>, <strong>arccos</strong>, and <strong>arctan</strong>.</p>
  <div class="hero-goals">
    <div class="goal">
      <div class="goal-label">Understand</div>
      <div class="goal-text">Why domain restrictions are required for inverses to exist</div>
    </div>
    <div class="goal">
      <div class="goal-label">Compute</div>
      <div class="goal-text">Exact values for special angles using principal ranges</div>
    </div>
    <div class="goal">
      <div class="goal-label">Evaluate</div>
      <div class="goal-text">Compositions like arcsin(sin θ) using principal range rules</div>
    </div>
  </div>
</div>

---
layout: two-cols
class: panel-slide
---

<div class="panel-box">
  <div class="eyebrow">Recall</div>
  <h2 class="panel-title">How trig functions work</h2>
  <div class="concept-card">
    <h3>Trig Function</h3>
    <p style="font-size:0.84rem; margin-bottom:0.5rem; color:var(--deck-text-muted);">Start with an angle — get a ratio.</p>
    <div class="flow-row">
      <div class="flow-pill">angle θ</div>
      <div class="flow-arrow">→</div>
      <div class="flow-pill">ratio</div>
    </div>
    <p style="font-size:0.82rem; margin-top:0.5rem; color:var(--deck-text-muted);">e.g. sin(π/6) = ½</p>
  </div>
  <div class="concept-card" style="margin-top:0.7rem;" v-click>
    <h3>Inverse Trig Function</h3>
    <p style="font-size:0.84rem; margin-bottom:0.5rem; color:var(--deck-text-muted);">Start with a ratio — get back an angle.</p>
    <div class="flow-row">
      <div class="flow-pill">ratio</div>
      <div class="flow-arrow">→</div>
      <div class="flow-pill">angle θ</div>
    </div>
    <p style="font-size:0.82rem; margin-top:0.5rem; color:var(--deck-text-muted);">e.g. arcsin(½) = π/6</p>
  </div>
</div>

::right::

<div class="panel-box">
  <div class="eyebrow">Key Shift</div>
  <h2 class="panel-title">What changes with inverses?</h2>
  <v-clicks>

  - The output is now an **angle**, not a ratio.
  - We need a **restricted domain** so the original function is one-to-one.
  - Both $\arcsin(x)$ and $\sin^{-1}(x)$ mean the same thing.
  - **Caution:** $\sin^{-1}(x)$ means inverse sine, **not** $\dfrac{1}{\sin(x)}$. The $-1$ is not an exponent.

  </v-clicks>
</div>

---
class: panel-slide
---

<div class="panel-box" style="max-width: 720px; margin: 0 auto;">
  <div class="eyebrow">The Problem</div>
  <h2 class="panel-title">Why can't we invert sine everywhere on ℝ?</h2>
  <p>For a function to have an inverse, it must be <strong>one-to-one</strong> — each output from exactly one input. Sine is not.</p>
  <div class="reveal-grid" style="margin-top: 0.9rem;"><RevealCard>
<template #prompt>Does y = sin(x) pass the Horizontal Line Test?</template>
<template #answer>No — the line y = 0 crosses the sine curve at x = 0, π, −π, … Many inputs share the same output, so sine is not one-to-one on ℝ.</template>
</RevealCard>
<RevealCard>
<template #prompt>Which interval do we restrict sine to?</template>
<template #answer>[−π/2, π/2] — sine is strictly increasing on this window and covers every output in [−1, 1] exactly once.</template>
</RevealCard>
<RevealCard>
<template #prompt>What does the restriction give us?</template>
<template #answer>A one-to-one function. Its inverse arcsin(x) maps each x ∈ [−1, 1] to exactly one angle in [−π/2, π/2].</template>
</RevealCard>
  </div>
</div>

---
layout: two-cols
class: panel-slide
---

<div class="panel-box">
  <div class="eyebrow">Definition</div>
  <h2 class="panel-title">y = arcsin(x)</h2>
  <div class="work-card problem" style="margin-top:0.65rem;">
    <div class="label">Formal Definition</div>
    <p style="margin:0.3rem 0 0;">y = arcsin(x) means sin(y) = x,<br>where y is the unique angle in [−π/2, π/2].</p>
  </div>
  <div class="principal-range" style="margin-top: 0.75rem;">
    <div class="range-line">Input (domain): x ∈ [−1, 1]</div>
    <div class="range-line">Output (range): y ∈ [−π/2, π/2]</div>
    <div class="range-line">Output is always an <strong>angle in radians</strong>.</div>
  </div>
</div>

::right::

<div class="panel-box">
  <div class="eyebrow">Properties</div>
  <h2 class="panel-title">Click each to explore</h2>
  <div class="reveal-col"><RevealCard>
<template #prompt>What values of x are allowed as input?</template>
<template #answer>Domain: −1 ≤ x ≤ 1. Only ratios that sine can produce — values outside this interval have no inverse sine.</template>
</RevealCard>
<RevealCard>
<template #prompt>What angles can arcsin(x) output?</template>
<template #answer>Range: −π/2 ≤ arcsin(x) ≤ π/2. This is the principal range — approximately −90° to 90°.</template>
</RevealCard>
<RevealCard>
<template #prompt>What is arcsin(1), and why?</template>
<template #answer>arcsin(1) = π/2, because sin(π/2) = 1 and π/2 lies in the principal range.</template>
</RevealCard>
  </div>
</div>

---
class: panel-slide
---

<div class="panel-box explorer-panel">
  <div class="eyebrow">Explore</div>
  <h2 class="panel-title" style="margin-bottom:0.3rem;">Graph of y = arcsin(x)</h2>
  <p style="margin-bottom:0.65rem; font-size:0.88rem;">Drag the slider to any input value. Watch the output angle update in real time.</p>
  <ArcsinGraphDemo />
</div>

<!--
Presenter notes
Anchor points: (−1, −π/2), (0, 0), (1, π/2)
Ask students: "What do you predict arcsin(½) equals?" before pressing the preset.
Emphasize: the output is always in [−π/2, π/2].
-->

---
class: panel-slide
---

<div class="panel-box" style="max-width: 680px; margin: 0 auto;">
  <div class="eyebrow">Worked Example</div>
  <h2 class="panel-title">Find arcsin(−½) exactly.</h2>
  <div class="work-card problem" style="margin-top:0.65rem;">
    <div class="label">Goal</div>
    <p style="margin:0.25rem 0 0;">Find θ ∈ [−π/2, π/2] such that sin(θ) = −½.</p>
  </div>
  <div class="step-list" style="margin-top:0.55rem;">
  <v-clicks>

  - **Reference angle:** $\sin(\pi/6) = 1/2$, so the reference angle is $\pi/6$.
  - **Sign & quadrant:** We need $\sin(\theta) < 0$. In $[-\pi/2,\, \pi/2]$, negative sine means $\theta < 0$.
  - **Choose the angle:** $\theta = -\pi/6$ gives $\sin(-\pi/6) = -1/2$. ✓
  - **Answer:** $\arcsin(-1/2) = -\pi/6$

  </v-clicks>
  </div>
</div>

---
layout: two-cols
class: panel-slide
---

<div class="panel-box">
  <div class="eyebrow">Worked Example — Composition</div>
  <h2 class="panel-title">Evaluate arcsin(sin π/3) exactly.</h2>
  <div class="work-card problem" style="margin-top:0.65rem;">
    <div class="label">Goal</div>
    <div class="math-big">arcsin(sin π/3) = ?</div>
  </div>
  <div class="step-list" style="margin-top:0.5rem;">
  <v-clicks>

  - **Check the inner angle:** Is $\pi/3$ in the principal range $[-\pi/2,\, \pi/2]$?
  - **Verify:** Yes — $-\pi/2 \le \pi/3 \le \pi/2$.
  - **Conclude:** Since $\pi/3$ is already in the principal range, the composition returns it unchanged.
  - **Answer:** $\arcsin(\sin(\pi/3)) = \pi/3$

  </v-clicks>
  </div>
</div>

::right::

<div class="panel-box" v-click>
  <div class="eyebrow">Watch Out</div>
  <h2 class="panel-title">When composition does <em>not</em> simplify</h2>
  <p style="font-size:0.88rem;">The shortcut arcsin(sin θ) = θ only works when θ is <strong>already in the principal range</strong>.</p>
  <div style="margin-top:0.8rem;"><RevealCard>
<template #prompt>What is arcsin(sin(2π/3))?</template>
<template #answer>2π/3 is outside [−π/2, π/2], so the answer is NOT 2π/3. Since sin(2π/3) = √3/2 and arcsin(√3/2) = π/3, the answer is π/3.</template>
</RevealCard>
  </div>
  <div class="summary-card" style="margin-top:0.75rem;">
    <div class="label">Rule</div>
    <p>arcsin(sin θ) = θ <strong>if and only if</strong> θ ∈ [−π/2, π/2].</p>
  </div>
</div>
