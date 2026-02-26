<template>
  <div class="arcsin-demo">
    <div class="arcsin-demo__controls">
      <label class="arcsin-demo__label" for="arcsin-x-range">Choose an input value in the domain [-1, 1]</label>
      <input
        id="arcsin-x-range"
        v-model.number="xValue"
        class="arcsin-demo__range"
        type="range"
        min="-1"
        max="1"
        step="0.01"
        @input="clampX"
      >
      <div class="arcsin-demo__row">
        <label class="arcsin-demo__small-label" for="arcsin-x-number">x</label>
        <input
          id="arcsin-x-number"
          v-model.number="xValue"
          class="arcsin-demo__number"
          type="number"
          min="-1"
          max="1"
          step="0.01"
          @change="clampX"
        >
        <div class="arcsin-demo__presets">
          <button
            v-for="preset in presets"
            :key="preset.label"
            type="button"
            class="arcsin-demo__preset"
            @click="setPreset(preset.value)"
          >
            {{ preset.label }}
          </button>
        </div>
      </div>
    </div>

    <div class="arcsin-demo__layout">
      <div class="arcsin-demo__plot">
        <svg
          viewBox="0 0 420 300"
          role="img"
          aria-label="Interactive graph of y equals arcsine of x with a movable point"
        >
          <defs>
            <marker id="axis-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="currentColor" />
            </marker>
          </defs>

          <g class="demo-grid">
            <line v-for="tick in xTicks" :key="`x-grid-${tick.label}`" :x1="sx(tick.value)" y1="28" :x2="sx(tick.value)" y2="262" />
            <line v-for="tick in yTicks" :key="`y-grid-${tick.label}`" x1="40" :y1="sy(tick.value)" x2="392" :y2="sy(tick.value)" />
          </g>

          <g class="demo-axes">
            <line x1="40" :y1="sy(0)" x2="397" :y2="sy(0)" marker-end="url(#axis-arrow)" />
            <line x1="40" y1="266" x2="40" y2="23" marker-end="url(#axis-arrow)" />
          </g>

          <line class="demo-ref-line" x1="40" :y1="pointY" :x2="pointX" :y2="pointY" />
          <line class="demo-ref-line" :x1="pointX" y1="sy(0)" :x2="pointX" :y2="pointY" />

          <path class="demo-curve" :d="curvePath" />

          <g class="demo-point">
            <circle :cx="pointX" :cy="pointY" r="6" />
          </g>

          <g class="demo-ticks">
            <g v-for="tick in xTicks" :key="`x-tick-${tick.label}`">
              <line :x1="sx(tick.value)" :y1="sy(0) - 5" :x2="sx(tick.value)" :y2="sy(0) + 5" />
              <text :x="sx(tick.value)" y="287" text-anchor="middle">{{ tick.label }}</text>
            </g>
            <g v-for="tick in yTicks" :key="`y-tick-${tick.label}`">
              <line x1="35" :y1="sy(tick.value)" x2="45" :y2="sy(tick.value)" />
              <text x="29" :y="sy(tick.value) + 4" text-anchor="end">{{ tick.label }}</text>
            </g>
          </g>

          <text x="401" :y="sy(0) - 10" class="demo-axis-label">x</text>
          <text x="48" y="24" class="demo-axis-label">y</text>

          <text :x="Math.min(pointX + 10, 360)" :y="Math.max(pointY - 10, 30)" class="demo-point-label">
            ({{ xCompact }}, {{ yCompact }})
          </text>
        </svg>
      </div>

      <div class="arcsin-demo__readout">
        <div class="demo-stat">
          <div class="demo-stat__label">Input</div>
          <div class="demo-stat__value">x = {{ xDisplay }}</div>
        </div>
        <div class="demo-stat">
          <div class="demo-stat__label">Output</div>
          <div class="demo-stat__value">arcsin(x) = {{ yDisplay }}</div>
          <div class="demo-stat__sub">≈ {{ yValue.toFixed(4) }} rad ≈ {{ yDegrees.toFixed(2) }}°</div>
        </div>
        <div class="demo-stat">
          <div class="demo-stat__label">Reminders</div>
          <ul class="demo-stat__list">
            <li>Domain: -1 ≤ x ≤ 1</li>
            <li>Range: -π/2 ≤ arcsin(x) ≤ π/2</li>
            <li>Output is an angle in principal range</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

const PI = Math.PI
const X_MIN = -1
const X_MAX = 1
const Y_MIN = -PI / 2
const Y_MAX = PI / 2
const PAD_LEFT = 40
const PAD_RIGHT = 28
const PAD_TOP = 28
const PAD_BOTTOM = 38
const WIDTH = 420
const HEIGHT = 300
const PLOT_WIDTH = WIDTH - PAD_LEFT - PAD_RIGHT
const PLOT_HEIGHT = HEIGHT - PAD_TOP - PAD_BOTTOM

const xValue = ref(-0.5)

const presets = [
  { label: 'x = -1/2', value: -0.5 },
  { label: 'x = 0', value: 0 },
  { label: 'x = 1/2', value: 0.5 },
  { label: 'x = √2/2', value: Math.SQRT1_2 },
]

const xTicks = [
  { value: -1, label: '-1' },
  { value: -0.5, label: '-1/2' },
  { value: 0, label: '0' },
  { value: 0.5, label: '1/2' },
  { value: 1, label: '1' },
]

const yTicks = [
  { value: -PI / 2, label: '-π/2' },
  { value: -PI / 6, label: '-π/6' },
  { value: 0, label: '0' },
  { value: PI / 6, label: 'π/6' },
  { value: PI / 2, label: 'π/2' },
]

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value))
}

function clampX() {
  const numeric = Number(xValue.value)
  xValue.value = Number.isFinite(numeric) ? clamp(numeric, X_MIN, X_MAX) : 0
}

function setPreset(value: number) {
  xValue.value = value
}

function sx(x: number) {
  return PAD_LEFT + ((x - X_MIN) / (X_MAX - X_MIN)) * PLOT_WIDTH
}

function sy(y: number) {
  return PAD_TOP + ((Y_MAX - y) / (Y_MAX - Y_MIN)) * PLOT_HEIGHT
}

function almostEqual(a: number, b: number, tol = 1e-6) {
  return Math.abs(a - b) <= tol
}

function exactXLabel(x: number) {
  const labels = [
    { value: -1, label: '-1' },
    { value: -Math.sqrt(3) / 2, label: '-√3/2' },
    { value: -Math.SQRT1_2, label: '-√2/2' },
    { value: -0.5, label: '-1/2' },
    { value: 0, label: '0' },
    { value: 0.5, label: '1/2' },
    { value: Math.SQRT1_2, label: '√2/2' },
    { value: Math.sqrt(3) / 2, label: '√3/2' },
    { value: 1, label: '1' },
  ]
  return labels.find(item => almostEqual(x, item.value))?.label ?? null
}

function exactAngleLabel(y: number) {
  const labels = [
    { value: -PI / 2, label: '-π/2' },
    { value: -PI / 3, label: '-π/3' },
    { value: -PI / 4, label: '-π/4' },
    { value: -PI / 6, label: '-π/6' },
    { value: 0, label: '0' },
    { value: PI / 6, label: 'π/6' },
    { value: PI / 4, label: 'π/4' },
    { value: PI / 3, label: 'π/3' },
    { value: PI / 2, label: 'π/2' },
  ]
  return labels.find(item => almostEqual(y, item.value, 1e-5))?.label ?? null
}

const yValue = computed(() => Math.asin(clamp(xValue.value, X_MIN, X_MAX)))
const yDegrees = computed(() => (yValue.value * 180) / PI)
const pointX = computed(() => sx(xValue.value))
const pointY = computed(() => sy(yValue.value))

const curvePath = computed(() => {
  const samples = 160
  const parts: string[] = []
  for (let i = 0; i <= samples; i += 1) {
    const x = X_MIN + ((X_MAX - X_MIN) * i) / samples
    const y = Math.asin(x)
    const cmd = i === 0 ? 'M' : 'L'
    parts.push(`${cmd} ${sx(x).toFixed(2)} ${sy(y).toFixed(2)}`)
  }
  return parts.join(' ')
})

const xDisplay = computed(() => exactXLabel(xValue.value) ?? xValue.value.toFixed(3))
const yDisplay = computed(() => exactAngleLabel(yValue.value) ?? `${yValue.value.toFixed(4)} rad`)
const xCompact = computed(() => exactXLabel(xValue.value) ?? xValue.value.toFixed(2))
const yCompact = computed(() => exactAngleLabel(yValue.value) ?? yValue.value.toFixed(2))
</script>

<style scoped>
/* ===========================================
   ARCSIN DEMO LAYOUT
   Interactive graph + controls for principal-value exploration.
   To modify: adjust grid columns and card spacing for density.
   =========================================== */
.arcsin-demo {
  display: grid;
  gap: 0.85rem;
}

.arcsin-demo__controls,
.arcsin-demo__plot,
.arcsin-demo__readout {
  border: 1px solid var(--deck-line);
  border-radius: 16px;
  background: var(--deck-panel-soft);
}

.arcsin-demo__controls {
  padding: 0.85rem;
}

.arcsin-demo__label {
  display: block;
  color: var(--deck-text-primary);
  font-weight: 600;
  margin-bottom: 0.55rem;
}

.arcsin-demo__range {
  width: 100%;
}

.arcsin-demo__row {
  display: flex;
  gap: 0.6rem;
  align-items: center;
  flex-wrap: wrap;
  margin-top: 0.65rem;
}

.arcsin-demo__small-label {
  color: var(--deck-text-muted);
  font-size: 0.85rem;
}

.arcsin-demo__number {
  width: 92px;
  padding: 0.35rem 0.45rem;
  border-radius: 10px;
  border: 1px solid var(--deck-line);
  background: var(--deck-bg-elevated);
  color: var(--deck-text-primary);
}

.arcsin-demo__presets {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.arcsin-demo__preset {
  border: 1px solid var(--deck-line);
  background: var(--deck-bg-elevated);
  color: var(--deck-text-primary);
  border-radius: 999px;
  padding: 0.28rem 0.55rem;
  font-size: 0.8rem;
}

.arcsin-demo__preset:hover {
  border-color: var(--deck-accent);
}

.arcsin-demo__layout {
  display: grid;
  grid-template-columns: 1.35fr 0.9fr;
  gap: 0.85rem;
}

.arcsin-demo__plot {
  padding: 0.5rem;
}

.arcsin-demo__plot svg {
  width: 100%;
  height: auto;
  display: block;
  color: var(--deck-text-muted);
}

.demo-grid line {
  stroke: var(--deck-grid-line);
  stroke-width: 1;
}

.demo-axes line {
  stroke: var(--deck-axis-line);
  stroke-width: 1.7;
}

.demo-ref-line {
  stroke: var(--deck-accent);
  stroke-dasharray: 5 5;
  stroke-width: 1.6;
  opacity: 0.9;
}

.demo-curve {
  fill: none;
  stroke: var(--deck-curve);
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.demo-point circle {
  fill: var(--deck-accent-strong);
  stroke: var(--deck-bg-base);
  stroke-width: 2;
}

.demo-ticks line {
  stroke: var(--deck-axis-line);
  stroke-width: 1.2;
}

.demo-ticks text,
.demo-axis-label,
.demo-point-label {
  fill: var(--deck-text-muted);
  font-size: 12px;
  font-family: var(--deck-font-mono);
}

.demo-point-label {
  fill: var(--deck-text-primary);
  font-weight: 600;
}

.arcsin-demo__readout {
  padding: 0.8rem;
  display: grid;
  gap: 0.65rem;
  align-content: start;
}

.demo-stat {
  border: 1px solid var(--deck-line);
  border-radius: 12px;
  padding: 0.6rem 0.7rem;
  background: var(--deck-bg-elevated);
}

.demo-stat__label {
  color: var(--deck-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.72rem;
  margin-bottom: 0.2rem;
}

.demo-stat__value {
  color: var(--deck-text-primary);
  font-weight: 700;
  line-height: 1.3;
}

.demo-stat__sub {
  color: var(--deck-text-muted);
  font-size: 0.82rem;
  margin-top: 0.2rem;
}

.demo-stat__list {
  margin: 0.25rem 0 0;
  padding-left: 1rem;
  color: var(--deck-text-muted);
  font-size: 0.86rem;
  line-height: 1.35;
}

@media (max-width: 900px) {
  .arcsin-demo__layout {
    grid-template-columns: 1fr;
  }
}
</style>
