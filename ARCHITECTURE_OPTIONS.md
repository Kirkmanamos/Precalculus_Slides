# Architecture Options for the Precalculus Slides Site

> A weighing of options for evolving the current HTML-deck architecture.
> **No decision made.** This document captures the tradeoffs so a choice
> can be made later when the prompting need is clearer.

---

## What "5.5 standard" actually means

Concretely, it's the architecture established in `5.5-double-half-angle.html`
and canonicalized in `6.7-conditional-probability.html` (per `AGENTS.md`).
The fixed elements:

- Single self-contained HTML file per deck (no build step, GitHub-Pages-friendly)
- Links shared `assets/slides-core.css` + `assets/slides-core.js`
- KaTeX for all math, Source Sans 3 for type
- Fixed 28px base font; horizontal slide transitions via `position: absolute; inset: 0`
- `display: none / block` step reveals with `id="slide-N-step-M"` (not max-height or opacity)
- A specific component vocabulary: `.slide-body`, `.steps-area`,
  `.step-box` (teal/green/dark/orange variants), `.info-card`,
  `.formula-row`, `.cards-grid`, `.problem-statement`, `.body-lead`,
  `.note-box`, `.diagram-shell`

It's a **convention**, not a framework. It works because every deck agrees
to follow it.

---

## How modular is the current setup, honestly

| Dimension | Current state |
|---|---|
| Visual tokens (colors, type) | One file: `slides-core.css :root`. Change once, propagates. ✓ |
| Components (card, formula row, step) | Shared in `slides-core.css`. Add a new variant → all decks can use it. ✓ |
| **Page shell** (head, progress bar, nav dots, scripts) | **Duplicated in every HTML file.** Change the shell → edit 40+ files. ✗ |
| Slide layouts (concept, example, reference) | Hand-authored in each file. No template. Repetition is intentional, but verbose. ✗ |
| Per-deck SVG diagrams | Inline. No reuse. Each triangle, unit circle, sine curve hand-coded. ✗ |
| Dark mode / alternate themes | No infrastructure. Colors hard-coded. ✗ |

The system is **good at theming colors centrally**, but **bad at structural
change** (page shell, shared diagrams, alternate themes).

---

## What kind of change are you actually trying to absorb?

The right option depends on this more than anything else:

| Anticipated change | Best-suited option |
|---|---|
| Re-skin all decks (dark mode, print mode, projector mode, school rebrand) | **A** (theme tokens) |
| Add a feature to every deck (bookmarks, embedded mode, accessibility tweaks) | **B** or **C** |
| New slide layout used across decks (e.g., a poll slide, a video slide) | **B**, **C**, or **D** |
| Quick A/B test of two different visual treatments | **A** |
| Total redesign of the deck experience | **C** or **D** |
| Authoring speed (build the next 20 decks faster) | **B** or **C** |
| Hand-off to a collaborator who doesn't know HTML | **C** or **D** |

If the change you anticipate isn't yet clear, **A is the "buys you time" option** —
minimal commitment, real flexibility return.

---

## The four options

### A — Theme tokens (CSS custom properties + `[data-theme]`)

Extract every color/spacing/typography value in `slides-core.css` into CSS
variables and add a `data-theme` attribute switch. Re-skin all 40+ decks
instantly (dark mode, print mode, school rebrand, etc.). No structural
changes, no build step, near-zero risk.

- **Setup cost:** 2–3 hours
- **Build step:** None
- **Doesn't fix:** HTML duplication, hand-coded diagrams

### B — Web Components (custom elements like `<concept-slide>`, `<example-slide>`)

Define the recurring slide patterns as native browser custom elements in
`slides-core.js`. Decks become declarative — content + slot attributes
instead of 40 lines of HTML per slide. Still zero-build,
GitHub-Pages-friendly. Each new deck shrinks ~70%. Existing decks keep
working; migration is opt-in per deck.

- **Setup cost:** 1–2 days for foundation
- **Build step:** None
- **Risk note:** KaTeX auto-render does not enter shadow DOM. Either use
  light DOM (no shadow) or render KaTeX per-component manually.
- **Doesn't fix:** Hand-coded diagrams

### C — Templated build (Eleventy / Astro / Hugo)

Move the page shell and slide layouts into templates; deck content
becomes Markdown/MDX or JSON. One template change ripples to every deck.
Adds an `npm run build` step (source → static HTML). Breaks the "open
the .html and edit" workflow — you edit source files, rebuild, refresh.
Existing 40+ decks need migration.

- **Setup cost:** 1–2 days + per-deck migration
- **Build step:** Yes
- **Adds dependencies:** Eleventy/Astro + plugins
- **Reversibility:** Hard once invested

### D — Migrate to Slidev (Vue-based, already prototyped)

Use the existing Slidev/Vue setup (two prototypes already live in
`slidev/`) as the production stack. Vue components, Markdown content,
runtime theming, native dark mode, hot reload. Loses single-file
portability. Each existing deck would need a full rewrite, but the
per-deck experience is much richer afterward.

- **Setup cost:** Days + per-deck rewrite
- **Build step:** Yes (Vite/Slidev dev server)
- **Adds dependencies:** Slidev + Vue + plugins
- **Reversibility:** Hard once invested

---

## Side-by-side comparison

| | A — Theme tokens | B — Web Components | C — Templated build | D — Slidev |
|---|---|---|---|---|
| **Setup cost** | 2–3 hrs | 1–2 days for foundation | 1–2 days + per-deck migration | Days + per-deck rewrite |
| **Build step** | None | None | Yes (npm run build) | Yes (Vite/Slidev dev server) |
| **GitHub Pages friendly** | ✓ unchanged | ✓ unchanged | ✓ (deploy `dist/`) | ✓ (deploy `dist/`) |
| **"Open .html and edit" works** | ✓ | ✓ (slot syntax) | ✗ (edit source, rebuild) | ✗ (edit .md, rebuild) |
| **Fixes HTML duplication** | ✗ | Partially (shell components) | ✓ | ✓ |
| **Existing 40+ decks keep working** | ✓ instantly | ✓ unchanged; opt-in upgrade | Need migration | Need rewrite |
| **Reversibility** | Trivial | Per-deck | Hard once invested | Hard once invested |
| **Hot reload while authoring** | No (already works without) | No | Yes | Yes |
| **Native dark mode** | Easy to add | Easy to add | Easy | Built in |
| **Adds dependencies to maintain** | None | None | Eleventy/Astro + deps | Slidev + Vue + deps |
| **Per-deck file size** | Same | ~70% smaller | Source much smaller; output similar | Source much smaller; output similar |
| **Risk of breaking existing work** | Near zero | Low (additive) | Medium | Medium-high |

---

## Three hybrids worth knowing about

These aren't on the original menu but are arguably the most defensible
middle paths:

- **A + a single `<deck-shell>` web component.** Just *one* component that
  wraps the head bits + progress bar + nav. Every new deck loses ~30% of
  its boilerplate; existing decks ignore it. Buys ~80% of B's value for
  ~20% of B's cost.

- **A + GraphBuilder-style helpers for SVG diagrams.** Theme tokens for
  visuals, plus a JS library for the recurring SVG diagrams (unit
  circles, sine waves, triangles, parabolas). Doesn't touch the deck
  architecture but eats the *actual* cost — most of which is in the
  hand-coded SVGs, not the HTML shell.

- **A now, B later.** Do the theme refactor first (cheap, useful
  immediately). Revisit Web Components once you've felt the duplication
  pain a few more times and know exactly which components matter.

---

## One thing none of these fix

The hand-coded SVG diagrams. The unit circle on 4.4 is ~150 lines of SVG;
the four-quadrant reference angle on 4.5 is another ~80; the sine/cosine
curves on 4.6 are 33-point polylines. **Templating the HTML doesn't
shrink these.** The only things that do:

1. A JS chart helper (you already have `GraphBuilder` for rational
   functions in Unit 2 — extend it to trig)
2. Generate diagrams from Manim and import as static SVG/PNG (already
   in the plan per `CLAUDE.md`)
3. Use a chart library (Chart.js, D3, Plot) — but most are oriented at
   data viz, not labeled-geometry teaching diagrams

This is worth weighing separately from the architecture question,
because **most of the per-deck cost is the math content + diagrams, not
the shell.** The shell is a fixed ~20% overhead; everything else is
unavoidable mathematical authoring.

---

## Honest read

The current setup is **good** for what it does — stable delivery,
single-file portability, GitHub-Pages-friendly, no JS framework debt.
It's **bad** at exactly two things: shell duplication and quick
re-themings.

- **A** is the cheapest fix and addresses re-theming completely.
- **B** addresses both in a low-risk way but takes a real chunk of time.
- **C** and **D** are big bets — only worth it if you're planning a major
  content expansion or handing the system to someone who can't read HTML.

---

*Authored 2026-05-12 during the Unit 4 rebuild conversation.*
