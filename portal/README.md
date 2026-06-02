# Course Portal

The student-facing front door for the Precalculus & Trigonometry slides.
Built with **Astro + Tailwind CSS + KaTeX**, deployed to GitHub Pages.

It is overlaid on top of the existing slide decks at the repo root, so every
slide URL (e.g. `/Precalculus_Slides/4.3-trig-functions-unit-circle.html`)
keeps working unchanged. The portal becomes the site's `index.html` and adds
`/upcoming` and `/resources`.

## Local development

```bash
cd portal
npm install        # first time only
npm run dev        # live preview at http://localhost:4321/Precalculus_Slides
npm run build      # production build into portal/dist
npm run preview    # serve the production build locally
```

## How to update the site (no HTML required)

Everything students see is driven by JSON data files. **You never edit
components to add content.**

### Add or change a unit / topic / slide link — `src/data/units.json`

Each unit is one object. Each topic lists its resources. A resource is:

```json
{ "type": "slides", "title": "Slides 4.3", "href": "4.3-trig-functions-unit-circle.html" }
```

- `href` is either a **bare deck filename** at the repo root (the
  `/Precalculus_Slides` base path is added automatically) **or a full
  `https://...` URL** (e.g. a YouTube video).
- `type` controls the icon + label. Allowed values:
  `slides`, `notes`, `video`, `key`, `worksheet`, `activity`, `playground`,
  `reference`. (Defined in `src/data/types.ts`.)
- `duration` is optional, e.g. `"32:18"` for a video.

To add a brand-new unit, append another object to the array. To add notes,
worksheets, videos, or answer keys later, just add more resources to a topic —
the row icons and "open in new tab" behavior are automatic.

### Add an upcoming assignment — `src/data/assignments.json`

```json
{ "due": "2026-06-09", "title": "Unit 5 Quiz", "unit": "Unit 5", "note": "Covers 5.1–5.5.", "href": "5.4-graphs-other-trig-functions.html" }
```

- `due` is `YYYY-MM-DD`. Past-due items hide automatically; the list sorts
  soonest-first.
- `unit`, `note`, and `href` are all optional.

### Edit resources / formulas — `src/pages/resources.astro`

Tool links and the KaTeX formula reference live at the top of that file.

## Writing math (LaTeX)

Two ways, both rendered at **build time** (no client JS, fast):

1. In any Markdown content: write `$\sin^2\theta + \cos^2\theta = 1$` (inline)
   or `$$ ... $$` (display).
2. In an `.astro` page: `<Katex math="\\frac{a}{b}" />` or
   `<Katex math="..." display />`. See `src/components/Katex.astro`.

## Embedding video / Manim / custom HTML inline

Drop an iframe in any `.astro` page or Markdown file:

```html
<iframe src="/Precalculus_Slides/8.2-polar-graphs.html"
        class="aspect-video w-full rounded-lg border" loading="lazy"></iframe>
```

(Same-origin, so your interactive decks and Manim outputs embed cleanly.)

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the
portal, overlays it on the slide decks, and publishes to GitHub Pages.
**One-time setup:** repo **Settings → Pages → Source → "GitHub Actions"**.
