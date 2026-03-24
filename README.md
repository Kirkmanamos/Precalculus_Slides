# Precalculus Slides

> This repo contains the slides for a precalculus course. Each slide deck is a standalone, interactive web application (HTML) that can be opened locally in a browser.

[Precalculus Slides (GitHub Pages)](https://kirkmanamos.github.io/Precalculus_Slides/)

## Status
- Unit 4 and Unit 5 HTML slide decks now include a first-pass mobile phone layout patch.
- Desktop and projector presentation behavior remains intact.

## Python / uv
- This repo uses `uv` for Python environment management.
- Python is pinned by [`.python-version`](/Users/kirkmanamos/Documents/GitHub/precalculus_slides/.python-version) and dependencies are defined in [`pyproject.toml`](/Users/kirkmanamos/Documents/GitHub/precalculus_slides/pyproject.toml).
- Create or update the project environment with `uv sync`.
- Activate it with `source .venv/bin/activate`.
- Prefer `uv run ...` and `uv pip ... --python .venv/bin/python` over plain `pip`.

## Unit 3: Rational Functions
- [Rational Features](RationalFeatures.html)
- [Rational Graphing](RationalGraphing.html)

## Unit 4: Intro to Trigonometry
- [Review of sections 4.1 - 4.5](trig-review.html)
- [Spaghetti Trig Activity](Spaghetti_Trig_Slides.html)
- [4.6 Graphs of Sine and Cosine](4.6-graphs-sine-cosine.html)
- [4.6b Graphs of Sine and Cosine (Part 2)](4.6b-graphs-sine-cosine-part2.html)
- [4.7 Modeling with Sine and Cosine](4.7-modeling-sine-cosine.html)
- [4.8 Graphs of Other Trig Functions](4.8-graphs-other-trig-functions.html)
- [4.9 Inverse Trig Functions](4.9-inverse-trig-functions.html)

## Unit 5: Analytic Trigonometry
- [5.1 Using Fundamental Identities](5.1-fundamental-identities.html)
- [5.2 Verifying Trig Identities](5.2-verifying-trig-identities.html)
- [5.3 Solving Trig Equations](5.3-solving-trig-equations.html)
- [5.4 Sum and Difference Identities](5.4-sum-and-difference.html)
- [5.5 Double & Half Angle Identities](5.5-double-half-angle.html)
