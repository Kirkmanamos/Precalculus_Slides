---
name: panel-layout
description: Lessons for multi-graph layouts and discontinuous function plotting
metadata:
  tags: panel, thumbnail, graph, discontinuous, asymptote, scrim, readability
---

# Multi-Graph Layout Gotchas

## SurroundingRectangle Does NOT Clip

`SurroundingRectangle` is visual decoration only. Curves that exceed the axes
`y_range` will render outside the border. The only way to keep content inside
a panel border is to keep the plotted values within the axes range.

## Scrim Pattern for Layered Content

When a full-size graph overlaps a shrunken thumbnail behind it, semi-transparent
borders let the thumbnail bleed through. Fix: fade in a full-scene rectangle
matching `BG_COLOR` before showing the overlapping content, then fade it out
when you want both visible again.

Set `title.set_z_index(10)` so persistent elements stay above the scrim.
Avoid `z_index` on dots/markers — they will poke through the scrim.

## Readability at Reduced Scale

When content will be scaled down (thumbnails, insets), start with larger font
sizes than you think you need. A label at `font_size=20` becomes ~13pt at
0.65× scale — barely readable at 1080p. Prioritize readability over aesthetics
at full size; the content spends more screen time as a thumbnail.

## Discontinuous Functions (tan, cot, csc, sec)

### Use EPS gaps, not np.clip

`np.clip` clamps values to a flat ceiling near asymptotes — it creates visible
flatlines. Instead, increase `EPS` (the x_range gap from each asymptote) so
the function value naturally stays within the axes `y_range`:

```python
EPS = 0.25   # cot(0.25) ≈ 3.9, inside y_range [-4, 4]

b1 = axes.plot(_cot, x_range=[0 + EPS,    PI - EPS,    0.01], ...)
b2 = axes.plot(_cot, x_range=[PI + EPS,   2*PI - EPS,  0.01], ...)
```

### Don't duplicate the x-axis

The x-axis IS the y = 0 line. Adding a separate reference line at y = 0 just
creates visual clutter and can make the axis look doubled or offset.

## LaTeX: No Unicode in Tex/MathTex

Characters like ⚠, ✓, ✗ crash LaTeX compilation. Use ASCII or LaTeX commands:

```python
# BAD:  Tex(r"\textbf{⚠ Warning}")       — crashes
# GOOD: Tex(r"\textbf{[!] Warning}")      — works
# GOOD: MathTex(r"\checkmark\;\cot x")    — LaTeX command for ✓
# GOOD: MathTex(r"\times\;\cos^2 x")      — LaTeX command for ✗
```
