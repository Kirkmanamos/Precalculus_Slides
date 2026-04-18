# Agents Guide: HTML Slide Presentations

This document is for any AI agent (Claude, Claude Code, ChatGPT, Gemini, Deepseek, Codex, Copilot, or others) working on HTML slide presentations in this repository. Read this entire file before making any modifications.

---

## Core Philosophy

1. **Zero Build Step** -- Every presentation is a single HTML file. No npm, no build tools, no frameworks. Decks share `assets/slides-core.css` and `assets/slides-core.js` via plain `<link>` / `<script src=...>` (works on GitHub Pages). External CDN resources allowed: Google Fonts and **KaTeX**.

2. **HoffMath Classroom Standard** -- All new presentations (and all updates to older ones) must follow the architecture established in `6.7-conditional-probability.html` (canonical for the shared-assets pattern; see also `5.5-double-half-angle.html` for legacy inline-style decks awaiting conversion). See [HTML Architecture](#html-architecture).

3. **KaTeX for All Math** -- Every mathematical expression uses KaTeX via CDN. No HTML entities, no Unicode math, no monospace approximations. See [Math Rendering](#math-rendering).

4. **Mathematical Rigor** -- Every number, coordinate, graph point, table value, and computed result must be mathematically correct. Never approximate. See [Mathematical Accuracy](#mathematical-accuracy).

5. **Production Quality** -- Code must be well-commented, accessible, performant, and responsive on both projectors and laptops.

---

## Rebuild Checklist: Updating Older Presentations

> **Critical**: When asked to update, restyle, or fix an older presentation, **do not patch CSS on top of legacy architecture**. Instead, rebuild it to match the 5.5 standard. Incremental patching fails because the older HTML structure, step system, and math rendering are fundamentally incompatible.

Before modifying any presentation, check if it uses the current architecture:

| Check | Legacy (needs rebuild) | Current standard |
|---|---|---|
| Math rendering | HTML entities (`&theta;`, `&radic;`) or monospace | KaTeX (`\(\theta\)`, `\(\sqrt{}\)`) |
| Step reveals | `opacity` transitions or `data-step` attrs | `display: none/block` with `id="slide-X-step-Y"` |
| Slide model | `scroll-snap-type: y mandatory` (vertical scroll) | `position: absolute; inset: 0` (horizontal transitions) |
| Layout | Fixed pixel padding, no `.slide-body` | Flexbox autoscaling with `.slide-body` + `.steps-area` |
| Step cards | Plain `<div>` or `<p>` tags | `.step-box` cards with `.step-label` + `.step-math` |
| Container | `#slides-container` or bare sections | `.slides-wrapper` |
| Base font | No base set, or `clamp()` | Fixed `font-size: 28px` on `html, body` |

**If 2+ items are "Legacy" → full rebuild required.** Follow these steps:

1. Read the current file to extract all content (slide titles, math, SVGs, examples)
2. Read `5.5-double-half-angle.html` as the architectural reference
3. Rebuild the file from scratch using the 5.5 skeleton below
4. Preserve all SVG graphs, interactive elements, and math content
5. Convert all math to KaTeX LaTeX notation
6. Verify in browser

### Lessons Learned (from 5.5 development)

These are **proven failures** — do not repeat them:

- **`max-height` collapse for steps** → clips KaTeX fractions and tall math. Failed.
- **`opacity: 0/1` transitions for steps** → hidden steps still occupy layout space, pushing content off-screen. Failed.
- **Raised `max-height` ceiling (e.g. 500px)** → still clips unpredictably on different screen sizes. Failed.
- **`clamp()` for base font-size** → inconsistent scaling across devices. Use fixed `28px`.
- **Compounding `em` units in nested elements** → `0.75em` inside `0.72em` inside `28px` = 15px (way too small). Keep nesting shallow.

**What works**: `display: none` → `display: block` with `@keyframes stepReveal`. Steps render at full natural height. Overflow handled by scrollable `.steps-area`.

---

## File Structure

```
presentation-name.html          # Single file — links shared assets/
presentation-name-assets/       # Optional: images extracted from PPT conversions
assets/
    slides-core.css             # Shared baseline CSS (one source of truth)
    slides-core.js              # Shared SlidePresentation engine (window.SlidesCore)
```

Layout, components (info-card, step-box, formula-row, fill-in-blank, etc.), navigation, and the slide engine all live in `assets/`. A deck's HTML file contains only its content plus a small inline `<style>` block for *deck-specific* additions (e.g. `.read-aloud` in 6.1, modal/explorer CSS in 6.3) and a one-line `SlidesCore.init({ sectionTargets: [...] })` call.

When updating shared visuals (colors, typography, info-card style, step-reveal animation, etc.), edit `assets/slides-core.css` once and every deck inherits the change. Only edit a deck's inline `<style>` block when the rule is genuinely unique to that deck.

---

## HTML Architecture

> **Reference implementation: `5.5-double-half-angle.html`**
>
> When in doubt, open that file and copy the pattern exactly.

### Complete Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X.X — Topic Name</title>

    <!-- Font: Source Sans 3 (standard for HoffMath Classroom) -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600;700&display=swap">

    <!-- KaTeX CDN (required for all math) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">

    <style>
        /* ============================================================
           THEME — HoffMath Classroom
           ============================================================ */
        :root {
            --navy:          #1a365d;
            --blue-accent:   #2563eb;
            --green-accent:  #16a34a;
            --teal-accent:   #0891b2;
            --orange-accent: #d97706;
            --red-accent:    #dc2626;
            --grid-line:     #dbeafe;
            --bg-white:      #ffffff;
            --text:          #1e293b;
            --text-muted:    #64748b;
            --blue-light:    #eff6ff;
            --green-light:   #f0fdf4;
            --teal-light:    #f0fdfa;
            --orange-light:  #fffbeb;
            --navy-light:    #e8edf5;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        html, body {
            width: 100%; height: 100%;
            overflow: hidden;
            font-family: 'Source Sans 3', sans-serif;
            font-size: 28px;           /* FIXED — do not use clamp() */
            background: var(--navy);
        }

        /* ============================================================
           SLIDE SHELL — horizontal transition model
           ============================================================ */
        .slides-wrapper {
            width: 100vw; height: 100vh;
            position: relative; overflow: hidden;
        }

        .slide {
            position: absolute; inset: 0;
            display: flex; flex-direction: column;
            padding-top: 5rem; padding-bottom: 3rem;
            padding-left:  max(3rem, calc((100% - 1120px) / 2));
            padding-right: max(3rem, calc((100% - 1120px) / 2));
            opacity: 0; transform: translateX(60px);
            transition: opacity 0.5s ease, transform 0.5s ease;
            pointer-events: none;
        }
        .slide.active    { opacity: 1; transform: translateX(0); pointer-events: all; }
        .slide.exit-left { opacity: 0; transform: translateX(-60px); }

        /* FLEXBOX AUTOSCALING — the key layout mechanism */
        .slide-body {
            flex: 1;
            display: flex; flex-direction: column;
            justify-content: center;
        }
        .slide-body:has(.steps-area) {
            justify-content: flex-start;
            overflow: hidden;
        }

        /* ============================================================
           BACKGROUNDS
           ============================================================ */
        .title-slide {
            background: var(--navy); color: white;
            justify-content: center;
        }
        .grid-bg {
            background-color: var(--bg-white);
            background-image:
                linear-gradient(var(--grid-line) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
            background-size: 30px 30px;
            color: var(--text);
        }

        /* ============================================================
           SLIDE HEADER
           ============================================================ */
        .slide-header {
            display: flex; align-items: center; gap: 1rem;
            margin-bottom: 1.2rem; flex-shrink: 0;
        }
        .slide-title { font-size: 1em; font-weight: 700; color: var(--navy); }

        /* Tags / labels */
        .example-label, .concept-label, .ref-label {
            font-size: 0.6em; font-weight: 700; padding: 0.2em 0.75em;
            border-radius: 6px; letter-spacing: 0.05em;
            text-transform: uppercase; color: white;
        }
        .example-label { background: var(--green-accent); }
        .concept-label { background: var(--teal-accent); }
        .ref-label     { background: var(--navy); }

        /* ============================================================
           PROBLEM STATEMENT
           ============================================================ */
        .problem-statement {
            background: var(--navy-light);
            border-left: 5px solid var(--navy);
            border-radius: 10px; padding: 0.65em 1.2em;
            margin-bottom: 0.9rem; flex-shrink: 0;
            font-weight: 600; color: var(--navy); font-size: 0.9em;
        }
        .problem-statement .katex-display { margin: 0; }

        /* ============================================================
           STEP REVEALS — display:none/block with keyframe animation
           IMPORTANT: Do NOT use opacity or max-height transitions.
           ============================================================ */
        .steps-area {
            display: flex; flex-direction: column;
            overflow-y: auto; flex: 1;
            min-height: 0; padding-bottom: 3.5rem;
        }

        .step { display: none; }
        .step.visible {
            display: block;
            animation: stepReveal 0.4s ease both;
            margin-bottom: 0.4rem;
        }
        .step.visible:last-child { margin-bottom: 0; }

        @keyframes stepReveal {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        /* ============================================================
           STEP-BOX CARDS — labeled cards for worked examples
           ============================================================ */
        .step-box {
            background: var(--blue-light);
            border-left: 4px solid var(--blue-accent);
            border-radius: 10px; padding: 0.45em 1.1em;
        }
        .step-box.teal   { background: var(--teal-light);   border-color: var(--teal-accent); }
        .step-box.green  { background: var(--green-light);  border-color: var(--green-accent); }
        .step-box.orange { background: var(--orange-light); border-color: var(--orange-accent); }
        .step-box.dark   { background: var(--navy); }

        .step-label {
            font-size: 0.58em; font-weight: 700;
            text-transform: uppercase; letter-spacing: 0.08em;
            color: var(--text-muted); margin-bottom: 0.08em;
        }
        .step-box.dark .step-label { color: #93c5fd; }

        .step-math {
            font-size: 0.88em; line-height: 2;
            padding: 0.2em 0; text-align: center;
        }
        .step-box.dark .step-math { color: white; }
        .step-box.dark .katex { color: white; }

        /* Annotation beside equation — applied via JS after KaTeX renders */
        .step-math.has-annotation {
            display: flex; align-items: center;
            gap: 2.5rem; text-align: left;
        }
        .step-eq { flex: 1; text-align: center; }
        .annotation {
            flex: 0 0 36%; color: var(--blue-accent);
            font-size: 0.72em; font-weight: 600; line-height: 1.45;
            text-align: left; border-left: 3px solid #93c5fd;
            padding-left: 1rem;
        }

        /* ============================================================
           NAV / PROGRESS
           ============================================================ */
        .nav-dots {
            position: fixed; right: 1.2rem; top: 50%;
            transform: translateY(-50%);
            display: flex; flex-direction: column;
            gap: 8px; z-index: 100;
        }
        .nav-dot {
            width: 8px; height: 8px; border-radius: 50%;
            background: rgba(255,255,255,0.3);
            border: none; cursor: pointer; transition: all 0.3s;
        }
        .nav-dot.active {
            background: var(--blue-accent);
            transform: scale(1.4);
        }
        .progress-bar {
            position: fixed; top: 0; left: 0; height: 3px;
            background: linear-gradient(90deg, var(--blue-accent), var(--teal-accent));
            transition: width 0.4s ease; z-index: 100;
        }
        .click-hint {
            position: fixed; bottom: 1.5rem; left: 50%;
            transform: translateX(-50%);
            font-size: 0.45em; color: rgba(100,116,139,0.6);
            letter-spacing: 0.1em; text-transform: uppercase;
            animation: pulse 2s ease-in-out infinite; z-index: 100;
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.4; } 50% { opacity: 1; }
        }

        @media (prefers-reduced-motion: reduce) {
            .slide { transition: opacity 0.3s ease; transform: none !important; }
            .step.visible { animation: none; opacity: 1; }
        }
    </style>
</head>
<body>

<!-- Progress bar -->
<div class="progress-bar" id="progressBar"></div>

<!-- Navigation dots -->
<nav class="nav-dots" id="navDots" aria-label="Slide navigation"></nav>

<!-- Click hint -->
<div class="click-hint" id="clickHint">click to advance</div>

<div class="slides-wrapper">

    <!-- ===== TITLE SLIDE ===== -->
    <section class="slide title-slide" id="slide-0">
        <div class="title-section-label">Section X.X</div>
        <h1 class="title-main">Topic Name</h1>
        <p class="title-objective">Objective: ...</p>
    </section>

    <!-- ===== CONCEPT SLIDE (no steps) ===== -->
    <section class="slide grid-bg" id="slide-1">
        <div class="slide-header">
            <span class="concept-label">Concept</span>
            <h2 class="slide-title">Slide Title</h2>
        </div>
        <div class="slide-body">
            <!-- Content fills via flexbox centering -->
            <p>Explanation text with \(\text{inline math}\) here.</p>
        </div>
    </section>

    <!-- ===== WORKED EXAMPLE (with steps) ===== -->
    <section class="slide grid-bg" id="slide-2" data-steps="3">
        <div class="slide-header">
            <span class="example-label">Example 1</span>
            <h2 class="slide-title">Find the exact value</h2>
        </div>
        <div class="slide-body">
            <div class="problem-statement">
                \[\text{Problem statement in display math}\]
            </div>
            <div class="steps-area">
                <!-- Step IDs: slide-{slideId}-step-{0, 1, 2, ...} -->
                <div class="step" id="slide-2-step-0">
                    <div class="step-box teal">
                        <div class="step-label">Identify the formula</div>
                        <div class="step-math">\[\text{Step math here}\]</div>
                    </div>
                </div>
                <div class="step" id="slide-2-step-1">
                    <div class="step-box">
                        <div class="step-label">Substitute</div>
                        <div class="step-math">\[\text{Substitution}\]</div>
                    </div>
                </div>
                <div class="step" id="slide-2-step-2">
                    <div class="step-box green">
                        <div class="step-label">Answer</div>
                        <div class="step-math">\[\text{Final answer}\]</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

</div><!-- end .slides-wrapper -->

<!-- KaTeX (loaded AFTER all HTML, BEFORE the controller) -->
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
    /* Render all LaTeX in the document */
    renderMathInElement(document.body, {
        delimiters: [
            { left: '\\[', right: '\\]', display: true  },
            { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
    });

    /* Move each annotation beside its equation */
    document.querySelectorAll('.step-math').forEach(stepMath => {
        const annotation = stepMath.querySelector('.annotation');
        if (!annotation) return;
        const eqDiv = document.createElement('div');
        eqDiv.className = 'step-eq';
        const before = [];
        for (const node of stepMath.childNodes) {
            if (node === annotation) break;
            before.push(node);
        }
        before.forEach(n => eqDiv.appendChild(n));
        stepMath.insertBefore(eqDiv, annotation);
        stepMath.classList.add('has-annotation');
    });

    /* ===== PRESENTATION CONTROLLER ===== */
    class SlidePresentation {
        constructor() {
            this.slides      = Array.from(document.querySelectorAll('.slide'));
            this.current     = 0;
            this.total       = this.slides.length;
            this.progressBar = document.getElementById('progressBar');
            this.navDotsEl   = document.getElementById('navDots');
            this.clickHint   = document.getElementById('clickHint');
            this._buildNav();
            this._activate(0);
            this._bindEvents();
        }

        _buildNav() {
            this.slides.forEach((_, i) => {
                const dot = document.createElement('button');
                dot.className = 'nav-dot';
                dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
                dot.addEventListener('click', e => {
                    e.stopPropagation(); this._goTo(i);
                });
                this.navDotsEl.appendChild(dot);
            });
            this.dots = Array.from(this.navDotsEl.querySelectorAll('.nav-dot'));
        }

        _sync() {
            this.dots.forEach((d, i) => d.classList.toggle('active', i === this.current));
            this.progressBar.style.width =
                ((this.current + 1) / this.total * 100) + '%';
            const slide = this.slides[this.current];
            const max   = parseInt(slide.dataset.steps || 0);
            const cur   = parseInt(slide.dataset.currentStep ?? -1);
            this.clickHint.textContent =
                cur < max - 1 ? 'click to advance'
                : this.current < this.total - 1 ? 'click for next slide' : '';
        }

        _activate(i) {
            this.slides[i].classList.add('active');
            this._sync();
        }

        _goTo(i) {
            if (i === this.current) return;
            const out = this.slides[this.current];
            out.classList.add('exit-left');
            out.classList.remove('active');
            setTimeout(() => out.classList.remove('exit-left'), 500);
            this.current = i;
            this.slides[i].classList.add('active');
            this._sync();
        }

        /* ID-based step finding: slide-{slideId}-step-{N} */
        _advanceStep(slide) {
            const max = parseInt(slide.dataset.steps || 0);
            let   cur = parseInt(slide.dataset.currentStep ?? -1);
            if (cur < max - 1) {
                cur++;
                slide.dataset.currentStep = cur;
                const el = slide.querySelector(`#${slide.id}-step-${cur}`);
                if (el) {
                    el.classList.add('visible');
                    el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
                this._sync();
                return true;
            }
            return false;
        }

        /* Bidirectional: retreat steps before going to previous slide */
        _retreatStep(slide) {
            let cur = parseInt(slide.dataset.currentStep ?? -1);
            if (cur < 0) return false;
            slide.querySelector(`#${slide.id}-step-${cur}`)?.classList.remove('visible');
            slide.dataset.currentStep = cur - 1;
            this._sync();
            return true;
        }

        _next() {
            if (!this._advanceStep(this.slides[this.current])
                && this.current < this.total - 1)
                this._goTo(this.current + 1);
        }

        _prev() {
            if (!this._retreatStep(this.slides[this.current])
                && this.current > 0)
                this._goTo(this.current - 1);
        }

        _bindEvents() {
            document.addEventListener('keydown', e => {
                if (['ArrowRight','ArrowDown',' '].includes(e.key)) {
                    e.preventDefault(); this._next();
                } else if (['ArrowLeft','ArrowUp'].includes(e.key)) {
                    e.preventDefault(); this._prev();
                }
            });
            document.addEventListener('click', e => {
                if (!e.target.closest('.nav-dot')) this._next();
            });
            let tx = 0;
            document.addEventListener('touchstart', e => {
                tx = e.touches[0].clientX;
            }, { passive: true });
            document.addEventListener('touchend', e => {
                const dx = e.changedTouches[0].clientX - tx;
                if (Math.abs(dx) > 50) dx < 0 ? this._next() : this._prev();
            }, { passive: true });
        }
    }

    new SlidePresentation();
</script>
</body>
</html>
```

---

## Slide Types Reference

### Title Slide

```html
<section class="slide title-slide" id="slide-0">
    <div class="title-section-label">Section X.X</div>
    <h1 class="title-main">Topic Name</h1>
    <p class="title-objective">Objective: description here</p>
</section>
```

### Concept / Definition Slide (no steps)

```html
<section class="slide grid-bg" id="slide-N">
    <div class="slide-header">
        <span class="concept-label">Definition</span>
        <h2 class="slide-title">Title</h2>
    </div>
    <div class="slide-body">
        <!-- Content auto-centers via flexbox -->
    </div>
</section>
```

### Worked Example (with step reveals)

```html
<section class="slide grid-bg" id="slide-N" data-steps="3">
    <div class="slide-header">
        <span class="example-label">Example 1</span>
        <h2 class="slide-title">Description</h2>
    </div>
    <div class="slide-body">
        <div class="problem-statement">\[\text{Problem}\]</div>
        <div class="steps-area">
            <div class="step" id="slide-N-step-0">
                <div class="step-box teal">
                    <div class="step-label">Step description</div>
                    <div class="step-math">\[\text{Math}\]</div>
                </div>
            </div>
            <!-- more steps... -->
        </div>
    </div>
</section>
```

### Formula Reference Card

```html
<section class="slide grid-bg" id="slide-N">
    <div class="slide-header">
        <span class="ref-label">Reference</span>
        <h2 class="slide-title">Formula Name</h2>
    </div>
    <div class="slide-body">
        <div class="formula-grid">
            <div class="formula-row sin-row">
                <div class="fn-label">SIN</div>
                <div class="fn-eq-stack">
                    <div class="step-math">\[\sin(2\theta) = 2\sin\theta\cos\theta\]</div>
                </div>
            </div>
            <!-- more rows... -->
        </div>
    </div>
</section>
```

### Step-Box Color Variants

| Class | Background | Border | Use for |
|---|---|---|---|
| *(default)* | `--blue-light` | `--blue-accent` | General steps, substitutions |
| `.teal` | `--teal-light` | `--teal-accent` | Formula identification, setup |
| `.green` | `--green-light` | `--green-accent` | Final answers, results |
| `.orange` | `--orange-light` | `--orange-accent` | Warnings, special notes |
| `.dark` | `--navy` | none | Highlighted answers on dark bg |

### Annotation Pattern

For steps that need a text explanation beside the math:

```html
<div class="step-math">
    \[\sin(2\theta) = 2 \cdot \frac{4}{5} \cdot \frac{3}{5}\]
    <div class="annotation">Substituting the known values<br>of sin and cos</div>
</div>
```

JS in the controller automatically wraps the math in `.step-eq` and applies `.has-annotation` layout.

---

## Math Rendering

### KaTeX CDN (Required)

Every presentation must load these in `<head>` and `<script>`:

```html
<!-- In <head> -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">

<!-- Before </body>, after all HTML -->
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
    renderMathInElement(document.body, {
        delimiters: [
            { left: '\\[', right: '\\]', display: true  },
            { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
    });
</script>
```

### Delimiter Conventions

| Context | Delimiter | Example |
|---|---|---|
| Display math (centered, block) | `\[ ... \]` | `\[\sin(2\theta) = 2\sin\theta\cos\theta\]` |
| Inline math (within text) | `\( ... \)` | `where \(\theta\) is in QII` |

### Common LaTeX Patterns

```latex
% Fractions
\dfrac{a}{b}              % display-size fraction (use in display math)
\frac{a}{b}               % normal fraction

% Trig
\sin\theta    \cos\theta    \tan\theta
\arcsin(x)    \arccos(x)    \arctan(x)
\csc\theta    \sec\theta    \cot\theta

% Special values
\dfrac{\sqrt{3}}{2}       % √3/2
\dfrac{\sqrt{2}}{2}       % √2/2
\dfrac{\pi}{6}            % π/6

% Plus/minus
\pm                        % ±

% Text within math
\text{where } \theta \text{ is in QII}
```

### Deprecated (Do Not Use)

- HTML entities for math: `&theta;`, `&pi;`, `&radic;`, `&infin;`
- Monospace font for math: `font-family: 'SF Mono', monospace`
- Unicode characters for math: `θ`, `π`, `√`

These are from the legacy system and must be converted to KaTeX when found.

---

## Design Principles

### Typography

The HoffMath Classroom standard uses **Source Sans 3** as the sole font:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600;700&display=swap">
```

Font sizes are all relative to the `28px` base:
- Slide titles: `1em` (28px)
- Labels/tags: `0.6em`
- Step labels: `0.58em`
- Step math: `0.88em`
- Problem statements: `0.9em`
- Title slide heading: `2em`

### Color

All colors defined as CSS custom properties in `:root`. The HoffMath Classroom palette is documented in the skeleton above.

For **quadrant colors** and **triangle side colors**, see `CONVENTIONS.md`.

### Accessibility

- Keyboard navigation: arrow keys, space bar
- Touch/swipe support for mobile
- ARIA labels on navigation dots
- `prefers-reduced-motion` media query
- Sufficient color contrast on both projector and laptop screens

---

## Mathematical Accuracy

**This is non-negotiable.** Every number, coordinate, graph point, table value, and computed result must be mathematically correct.

### Rules

1. **Compute, don't approximate.** sin(30°) = 1/2, not 0.5 displayed as a decimal.
2. **Verify with Pythagorean theorem.** For any right triangle, confirm a² + b² = c².
3. **Check sign conventions.** Quadrant signs matter (ASTC rule).
4. **Use exact values for special angles.** Fractions and radicals, not decimals.
5. **Validate graph coordinates.** Plug coordinates back into the original equation.
6. **Double-check tables.** Verify at least 3 values independently.

### SVG Coordinate System

- SVG y-axis is **inverted** (positive y goes downward)
- Cartesian point `(x, y)` → SVG `(x · scale, -y · scale)`
- Standard scales: 20–25 px/unit for coordinate planes; 120 px radius for unit circle

### Quadrant Color Convention

```css
--q1-color: #4ade80;  /* Green  — Quadrant I   */
--q2-color: #22d3ee;  /* Cyan   — Quadrant II  */
--q3-color: #f472b6;  /* Pink   — Quadrant III */
--q4-color: #fbbf24;  /* Gold   — Quadrant IV  */
```

### Triangle Side Colors

- **x-side** (horizontal): cyan `#22d3ee`
- **y-side** (vertical): pink `#f472b6`
- **r-side** (hypotenuse): green `#4ade80`

### Special Angle Reference

See `CONVENTIONS.md` Section 8 for the complete table. Copy values from there — do not recalculate.

---

## Modification Checklist

Before delivering any change to a presentation:

- [ ] Architecture matches 5.5 standard (not legacy scroll-snap or opacity system)
- [ ] All math uses KaTeX (no HTML entities or Unicode math)
- [ ] Step reveals use `display: none/block` with ID-based steps
- [ ] `.slide-body` flexbox autoscaling is present
- [ ] `.steps-area` with `overflow-y: auto` on worked example slides
- [ ] Step-box cards with `.step-label` + `.step-math` on worked examples
- [ ] All math values are correct (spot-check at least 3)
- [ ] SVG coordinates verified (remember y-axis inversion)
- [ ] Quadrant/triangle colors follow conventions
- [ ] Teacher-controlled reveals on all worked examples (click to advance)
- [ ] Keyboard nav works (arrow keys, space)
- [ ] Touch/swipe works on mobile
- [ ] `prefers-reduced-motion` media query present
- [ ] File opens correctly in browser with no console errors
