---
name: source-to-html-math-deck
description: Convert source material (PowerPoint, PDF, LaTeX teacher notes, or bare concepts) into a HoffMath Classroom HTML slide deck that links the shared assets/slides-core.css and assets/slides-core.js. Faithful to source pedagogy, but not limited by it — expand worked examples into step-reveal cards, convert dense prose into fill-in-blank concept slides, and add interactivity (sliders, modals, SVG manipulatives) where the concept benefits. Every deck follows the 6.7-conditional-probability.html canonical reference.
---

# Source → HTML Math Deck (HoffMath Classroom)

This skill converts lesson source material (`.pptx`, `.pdf`, `.tex` teacher notes, or a raw concept outline) into a single self-contained HTML file that plugs into this repo's shared slide engine. The canonical reference is `6.7-conditional-probability.html`; every new deck should match its structure.

---

## Core Philosophy

1. **Faithful to pedagogy, not to layout.** The source defines *what is taught* and *in what order*. It does **not** define slide count, visual design, or pacing. If a PPT jams six equations onto one slide, the HTML deck breaks them into six step-reveal cards — that's a feature, not infidelity.

2. **Teacher-controlled reveals, always.** No auto-animation of answers. Steps appear only when the teacher clicks/presses space. Every worked example uses `data-steps="N"` with `.step-box.visible`-gated reveal.

3. **Mathematical rigor is non-negotiable.** Every coordinate, intermediate algebra line, table value, and final answer must be correct. Verify by recomputing — don't trust OCR or image extraction.

4. **Expand and enhance.** When a concept would benefit from interactivity (a slider, a clickable modal derivation, a responsive SVG), build it. See 6.3's Ratio Playground and formula-button modals for reference.

5. **No copyright marks.** Older decks shipped with "Hoff Math" footers; new decks omit them entirely.

6. **One file per deck, shared assets.** Every `.html` file links `assets/slides-core.css` and `assets/slides-core.js`. No npm, no build step. Deck-specific CSS goes in a small `<style>` block after the link; deck-specific JS goes after `SlidesCore.init(...)`.

---

## Phase 0 — Detect Input Mode

Determine what the user has before scaffolding:

- **Mode A — From scratch:** only a topic name or objective. Ask via AskUserQuestion what the section number is, what the main concepts are, and whether there's a textbook reference. Then proceed to Phase 1.
- **Mode B — `.tex` teacher notes:** the most structured source. Headings define slide boundaries; `\blank{}` macros map to fill-in-blank patterns; `\begin{align}` blocks become worked-example steps. Read the full file before writing any HTML.
- **Mode C — `.pptx` or `.pdf` export:** extract slide-by-slide. Use `pdftotext` for PDFs, or ask the user to export the PPT to PDF first if no direct `.pptx` parser is available. Discard slide numbers, footers, decorative borders. Extract text + equations + figures.
- **Mode D — Hybrid (PPT + teacher notes):** treat teacher notes as authoritative for structure, PPT as the source for examples/figures that didn't make it into the notes.

Always confirm the target filename (e.g. `7.2-some-topic.html`) and the section numbers for the section-nav before writing code.

---

## Phase 1 — Content Inventory

Before scaffolding the HTML, build a content outline in a comment or scratch doc. For each source chapter/section, categorize:

### Extract verbatim
- **Problem statements** for worked examples
- **Definitions** and vocabulary
- **Formulas** and key identities
- **Fill-in-blank prompts** (from `.tex` `\blank{}` macros or PPT underscores)
- **Figures / SVGs / diagrams** — re-author as inline SVG where possible

### Discard
- Slide numbers, headers, footers from source
- Copyright marks, logos, decorative borders
- Speaker notes (unless they reveal hidden step structure)
- Redundant "agenda" or "what we'll cover" slides

### Expand or restructure
- **Dense algebra blocks** → one `.step-box` per logical move (substitute, factor, simplify, solve)
- **Multi-part definitions** → `.cards-grid` of `.info-card` elements (2 or 3 columns)
- **Formula tables** → `.formula-grid` with `.formula-row` + `.fn-label` + `.fn-eq-stack`
- **Derivations** → optional `.card-modal` behind a clickable `.info-card.clickable` (see 6.3)
- **Interactive concepts** → sliders in an `.explorer` grid (see 6.3 Ratio Playground)

---

## Phase 2 — Scaffold the Deck

Every deck follows the skeleton below. Copy it as the starting point, then fill in slides.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X.X — Topic Name</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600;700&display=swap">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <link rel="stylesheet" href="assets/slides-core.css">
    <!-- Optional: deck-specific CSS only -->
</head>
<body>
    <div class="slides-wrapper">
        <div class="progress-bar"><div id="progressBar"></div></div>
        <div class="nav-dots" id="navDots"></div>
        <div class="click-hint" id="clickHint"></div>

        <!-- Slides go here -->
        <section class="slide" id="slide-0"> ... </section>
        <section class="slide" id="slide-1"> ... </section>
        <!-- etc. -->
    </div>

    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    <script src="assets/slides-core.js"></script>
    <script>
        SlidesCore.init({
            sectionTargets: [
                { label: 'Overview', slideId: 'slide-0' },
                { label: 'Basics',   slideId: 'slide-1' },
                // ... typically 5–8 labels, each mapping to a section-start slideId
            ]
        });
        // Deck-specific JS (modals, explorers, playground init) goes here.
    </script>
</body>
</html>
```

**Section-nav labels should match the teaching arc**, not every slide. 5–8 chips is typical. Look at 6.6 and 6.7 for good examples.

---

## Phase 3 — Per-Slide Construction

Work through slides in order. Each slide type has an established pattern.

### Title slide (slide-0)
Navy background, centered. Section label + main title + one-sentence objective + `.identity-chips` row of keywords.

```html
<section class="slide title-slide" id="slide-0">
    <div class="slide-body center-layout">
        <div class="section-label">6.7 · Probability</div>
        <h1 class="deck-title">Conditional Probability</h1>
        <p class="deck-subtitle">Updating probability when you already know something.</p>
        <div class="identity-chips">
            <span class="chip">P(A | B)</span>
            <span class="chip">independence</span>
            <span class="chip">two-way tables</span>
        </div>
    </div>
</section>
```

### Concept / Definition slide
Grid background. `.slide-header` with a colored label (`.concept-label`, `.ref-label`) and title. Body contains `.cards-grid` (2 or 3 columns of `.info-card`) or `.notes-list` with fill-in-blanks.

**Fill-in-blank pattern** (maps to `\blank{}` in teacher notes):
```html
<span class="fb">
    <span class="fb-blank">________</span>
    <span class="fb-answer">geometric</span>
</span>
```
Answer is hidden by default; a step-reveal flips a parent element to `.visible` to show all `.fb-answer`s within.

### Reference / Formula slide
Grid background. `.formula-grid` of `.formula-row` elements, color-coded by category (`.teal`, `.green`, `.orange`, `.navy`). Each row has `.fn-label` (uppercase, 0.6em) + `.fn-eq-stack` (centered display math).

### Worked example slide
The workhorse. Grid background. `.slide-header` with `.example-label` + title. `.problem-statement` navy-light banner with the problem. Then `.steps-area` containing N hidden `.step-box` cards.

```html
<section class="slide" id="slide-4" data-steps="4">
    <div class="slide-header">
        <span class="example-label">Example 2</span>
        <h2 class="slide-title">Find the probability of drawing a red card given it's a face card</h2>
    </div>
    <div class="slide-body top-layout">
        <div class="problem-statement">\[ P(\text{red} \mid \text{face}) = \text{?} \]</div>
        <div class="steps-area">
            <div class="step step-box teal" id="slide-4-step-0">
                <div class="step-label">Step 1 · Identify the reduced sample space</div>
                <div class="step-math">Face cards: J, Q, K of each suit — 12 cards total.</div>
            </div>
            <div class="step step-box" id="slide-4-step-1">
                <div class="step-label">Step 2 · Count favorable outcomes</div>
                <div class="step-math">\[\text{Red face cards} = 6\]</div>
            </div>
            <div class="step step-box green" id="slide-4-step-2">
                <div class="step-label">Step 3 · Divide</div>
                <div class="step-math">\[P(\text{red} \mid \text{face}) = \frac{6}{12} = \frac{1}{2}\]</div>
            </div>
            <div class="step step-box dark" id="slide-4-step-3">
                <div class="step-label">Step 4 · Interpret</div>
                <div class="step-math">Half of face cards are red — same as for the full deck.</div>
            </div>
        </div>
    </div>
</section>
```

**Color discipline within a worked example:**
- **Teal** — set-up / identify / organize
- **Blue** (default) — substitution / intermediate algebra
- **Green** — final computational answer
- **Orange** — warning / special case / key insight
- **Dark (navy)** — emphatic result, interpretation, or second final answer

**Annotations** — attach an explanation beside a step's math by adding `<span class="annotation">because…</span>` inside `.step-math`. The shared JS auto-wraps the math in `.step-eq` and lays the two out flexbox-style.

### Interactive slides (modal, explorer)
See 6.3 for modal patterns (`.card-modal` + `.derivation-steps`) and the Ratio Playground (`.explorer` grid + range sliders + live SVG chart). Deck-specific JS for these goes inside the `SlidesCore.init` block's follow-up script.

### Review / Summary slide
Grid background. `.cards-grid` of take-aways, one card per key idea. Color-coded to mirror the worked-example step colors.

---

## Phase 4 — Verify

Before declaring the deck done:

1. **Open in a preview server** (`npx serve .` or the `preview_start` MCP tool).
2. **Advance through every slide** with space/right-arrow. Every step should reveal cleanly; no clipped KaTeX, no layout shifts.
3. **Test bidirectional nav** — left-arrow should retreat through steps, not jump slides.
4. **Test section-nav chips** — all chips should jump to the right slide, and the active chip should update.
5. **Spot-check math on a phone-width viewport** (400px). KaTeX display math should scroll horizontally rather than overflow.
6. **Check console for KaTeX render errors** — a stray unmatched brace `}` will silently fail to render a formula.
7. **Update `CLAUDE.md` curriculum table** and add a `CHANGELOG.md` entry.

---

## Architectural Invariants (never break these)

- Fixed base font `28px` on `html, body`. Never `clamp()`. All other sizes are `em` relative to this.
- Steps toggle **`display: none` ↔ `display: block`** only. Never `opacity`, never `max-height`, never animated collapse.
- Slide containers use **`.slides-wrapper > .slide`**. Slides are absolutely positioned; transitions are horizontal `translateX` (handled by the shared JS).
- **IDs**: `id="slide-N"` on each slide; `id="slide-N-step-M"` on each hidden step inside.
- **KaTeX**: `\(inline\)` and `\[display\]`. No HTML entities (`&pi;`), no Unicode math glyphs, no monospace approximations.
- Deck-specific JS runs **after** `SlidesCore.init()`. Don't reach into `SlidesCore` internals; append buttons and wire event listeners to the existing DOM instead (see 6.3's formula-button injection).
- SVG y-axis is inverted vs. Cartesian. Always plot `(x · scale, −y · scale)`.

---

## Gotchas (tried and failed)

- **`max-height` collapse for steps** → clips tall fractions. Fails silently on different screens.
- **`opacity: 0/1` transitions for steps** → invisible steps still occupy layout space.
- **Nested `em` sizing** → `0.75em` inside `0.72em` inside 28px = 15px. Keep nesting shallow.
- **Running deck-specific JS inside `SlidesCore.init`'s class** → when `slides-core.js` gets updated, your deck-specific init is lost. Always put deck-specific init in the *follow-up* script block, not inside the class.
- **Legacy decks** (pre-5.5, pre-shared-assets) use scroll-snap + opacity steps + HTML-entity math. Do not restyle them incrementally — rebuild to the current standard instead.
- **KaTeX unmatched braces** fail silently. If a formula doesn't render, check for stray `}` or missing `\left` / `\right` pairs.
- **Forgetting the KaTeX JS CDN** → you can include `katex.min.css` but still see `\(...\)` as literal text. You need *both* `katex.min.js` *and* `contrib/auto-render.min.js` before `slides-core.js`. If `katexRendered` is 0 in preview, this is the cause.
- **`text-transform: uppercase` on a parent containing KaTeX math** → the uppercase transform mangles rendered math. Keep `.step-label` uppercase-only on its text; never nest `\(...\)` inside uppercase-transformed parents (prefer plain-text step labels when math is unavoidable there).
- **KaTeX delimiters inside SVG `<text>`** → auto-render does not walk into SVG. Inside SVG use plain-text + `<tspan font-style="italic">f</tspan>` for italic, and `<tspan dy="-3" font-size="8">−1</tspan>` for superscripts. Don't write `\(f^{-1}\)` inside an SVG label.
- **Unicode superscript minus `⁻`** — renders but often invisible in many fonts. Always use `<tspan dy="-3" font-size="8">−1</tspan>` (note the U+2212 minus, not a hyphen) for the "f-inverse" look inside SVG.
- **`.fb` wrapped in a separate `.step` div** → the fill-in never reveals. The `.fb` span **itself** carries `id="slide-N-step-M"`. The `.fb-answer` inside becomes visible via the sibling-selector rule when `.fb.visible` is toggled.
- **`<td class="step">` with `display:block` from `.step.visible`** → shatters the table layout. Tables and SVG groups need their own reveal classes — see "Table-cell and SVG-group reveals" below.

---

## Table-cell and SVG-group reveals (Unit 1 pattern)

The default `.step { display: none; } .step.visible { display: block; }` works for `<div>` children but **breaks** `<td>` (should be `table-cell`) and `<g>` SVG groups (should stay `inline`). When you need a table answer column or an SVG curve to reveal mid-example:

```css
/* Table cells — use visibility to preserve grid layout */
.ans-cell.ans-hide { visibility: hidden; }
.ans-cell.ans-hide.visible { visibility: visible; animation: stepReveal 0.4s ease both; }

/* SVG groups — use opacity to preserve the inline layout context */
g.svg-step { opacity: 0; }
g.svg-step.visible { opacity: 1; transition: opacity 0.35s ease; }
```

```html
<td class="ans-cell ans-hide" id="slide-8-step-3">\(-3\)</td>
...
<g class="svg-step" id="slide-8-step-4">
    <polyline points="40,140 100,70 160,140" stroke="#ea580c" stroke-width="2.5" fill="none"/>
</g>
```

The engine still adds `.visible` to `#slide-8-step-3`; the CSS above makes the reveal behave correctly for the element type.

---

## Paired reveals (table rows, graph points)

When two or more elements should reveal on the *same* click (e.g. the floor column and the ceiling column of a Floor/Ceiling table, or five consecutive table rows that all map to one conceptual step), give the primary element the real step id and the followers synthetic ids (`-3b`, `-3c`, …). Link them with a `MutationObserver`:

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const pairs = [
        ['slide-8-step-3', ['slide-8-step-3b', 'slide-8-step-3c', 'slide-8-step-3d']],
    ];
    pairs.forEach(([primaryId, followerIds]) => {
        const primary = document.getElementById(primaryId);
        if (!primary) return;
        const followers = followerIds.map(id => document.getElementById(id)).filter(Boolean);
        const obs = new MutationObserver(() => {
            const on = primary.classList.contains('visible');
            followers.forEach(f => f.classList.toggle('visible', on));
        });
        obs.observe(primary, { attributes: true, attributeFilter: ['class'] });
    });
});
```

This lets `data-steps="N"` stay honest (N = number of teacher clicks) while reducing visual bookkeeping.

---

## Unit 1 worked-example palettes

Unit 1 canonized a few recurring pedagogical motifs. Use these as-is when the same concept appears elsewhere.

### Four-operation color arc (arithmetic examples)
- **Teal** → set up the expression or combine the two functions
- **Blue** → distribute, simplify, intermediate algebra
- **Green** → evaluate at a specific value, or collect the domain
- **Navy (dark)** → final answer, with label text in `color: #fbbf24`

### D.R.S. palette (transformations)
- **Orange** `#ea580c` → **D**ilate (shrink/stretch)
- **Blue**  `#2563eb` → **R**eflect
- **Green** `#16a34a` → **S**hift
- Dark navy → emphatic conclusion ("Apply in this order, always.")

```css
.drs-step.d { border-color: #ea580c; background: #fff7ed; }
.drs-step.r { border-color: #2563eb; background: #eff6ff; }
.drs-step.s { border-color: #16a34a; background: #ecfdf5; }
```

### Parent-function gallery (6-card grid)
A 3×2 grid of `.parent-card`, each with a mini-SVG of the parent graph and a KaTeX label. Use when a unit hinges on recognizing a shape (Unit 1.5 gallery: `x`, `x²`, `x³`, `|x|`, `√x`, `∛x`).

### Mapping-diagram SVG (inverse functions, piecewise, relations)
Two labelled ellipses connected by a forward-arrow above and a return-arrow below. Labels use `<tspan>` italic for function names, `<tspan dy="-3" font-size="8">−1</tspan>` for inverse exponent. Do not attempt KaTeX inside the SVG.

---

## Source-extraction recipe (PPT + PDF)

Unit 1 was extracted from `~/Desktop/precalculus/Unit 1 - Function Analysis/original_notes/`. Standard pattern per section:

1. Run `python3` with `python-pptx` against the TEACHER `.pptx` to dump slide-by-slide text. Most per-slide text is sparse — most of the pedagogy lives in pictures/math shapes that python-pptx doesn't expose.
2. Use the `Read` tool on the STUDENT `.pdf` (pages 1–20) to get the actual worked-example problem statements and the exact fill-in-blank blanks that students see.
3. Trust the PDF for problem *statements* and the PPT for *narrative order* (section headings, "Order matters!", etc.).
4. **Always recompute every worked example** before writing it into a step-box. OCR from either source is unreliable for signs, exponents, and radicals.

---

## Verification recipe (preview loop)

After writing a new deck:

1. `mcp__Claude_Preview__preview_start` with name `dev` (from `.claude/launch.json` → `npx serve .`).
2. `preview_eval`: navigate via `window.location.href = 'http://localhost:3000/X.Y-name.html'`, wait ~2.5s, expect a navigation error (that's fine).
3. `preview_eval`: read `{ slideCount, chipCount, katexRendered, katexErr, title }`. Sanity check: `katexErr === 0`, `katexRendered` > 50 for a typical deck, `chipCount` matches the `sectionTargets` length, `slideCount` matches the `.slide` count you wrote.
4. Force-activate tricky slides with `document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'))` and `getElementById('slide-N').classList.add('active')`, then screenshot.
5. For reveal-heavy slides, programmatically add `.visible` to every step id to verify the fully-revealed state before committing.

---

## Component Vocabulary Cheat-Sheet

| Component | Purpose | Color variants |
|---|---|---|
| `.step-box` | Worked-example step card | default (blue), `.teal`, `.green`, `.orange`, `.dark` |
| `.info-card` | Definition, tip, key concept | same + `.navy` |
| `.formula-row` | Reference-card row | same |
| `.problem-statement` | Navy-light banner holding the example problem | — |
| `.notes-list` | Bulleted concept list (often with fill-in-blanks) | — |
| `.cards-grid` / `.cards-grid-3` | Responsive grid of info-cards | — |
| `.fb` / `.fb-blank` / `.fb-answer` | Fill-in-blank pattern | — |
| `.identity-chips` + `.chip` | Keyword chips on title slides | — |
| `.card-modal` + `.derivation-steps` | Clickable modal with step-by-step derivation | — |
| `.formula-button` | Floating "Formulas" FAB → opens reference modal | — |
| `.explorer` + `.explorer-control` | Interactive slider playground (6.3 pattern) | — |
| `.annotation` | Inline explanation beside step math | — |
| `.ans-cell.ans-hide` | Revealable table cell answer (visibility-based) | — |
| `g.svg-step` | Revealable SVG group (opacity-based) | — |
| `.drs-step` | Dilate/Reflect/Shift step card | `.d` orange, `.r` blue, `.s` green |
| `.parent-card` | Mini-SVG parent-function gallery tile | — |
| `.flavor-card` | Three-flavor transformation card (translation/reflection/dilation) | `.trans`, `.refl`, `.dil` |
| `.ll-card` | One-to-one / horizontal-line-test card | `.yes` green, `.no` red |
| `.point-tbl` | Key-points table for graph transformations | — |

When in doubt, open `6.7-conditional-probability.html` and copy the pattern. When adding interactivity, open `6.3-geometric-sequences.html` — it has the most advanced patterns (modals, explorer, formula-button).

---

## What This Skill Does **Not** Do

- It does not auto-parse `.tex` into HTML deterministically. Every conversion is a judgment call about what to extract, discard, and expand.
- It does not guarantee 1:1 slide parity with the source. A 15-slide PPT may become a 20-slide HTML deck, or vice versa.
- It does not build the shared assets. `assets/slides-core.css` and `assets/slides-core.js` are the source of truth and should only be edited when a change benefits *every* deck.
