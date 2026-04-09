# Unit 6 Sequence Videos

## Overview
- **Topic**: What a sequence is, and how convergent and divergent infinite sequences behave
- **Hook**: Why does order matter, and what does it really mean for an infinite list to "approach" a number?
- **Target Audience**: High school precalculus / algebra 2 students
- **Estimated Length**: 2 short videos, each about 35-60 seconds
- **Key Insight**: A sequence is a function on the positive integers, so each term has a position; convergence means the dots eventually cluster near one value, while divergence means they never settle there

## Video 1: Sequence as an Ordered Function
- Start with a colorful ordered list such as `3, 7, 11, 15, ...`
- Label each term with `a_1, a_2, a_3, a_4`
- Briefly swap the first two terms to show that a different order creates a different sequence
- Transform the ordered list into discrete plotted points `(1, 3), (2, 7), (3, 11), (4, 15)` on default Cartesian axes
- End with the summary statement: "A sequence is an ordered list, or equivalently a function whose domain is the positive integers."

## Video 2: Convergent vs Divergent Infinite Sequences
- Use the classic convergent example `a_n = 1/n`
- Use the classic divergent example `b_n = (-1)^n`
- Plot both on default Cartesian axes with only discrete dots, not continuous curves
- Add a highlighted horizontal band around the limit line `y = 0`
- Show that the `1/n` dots eventually stay inside the band, while the `(-1)^n` dots keep jumping out forever
- Close with a short note that divergence can also happen by growing without bound, such as `c_n = n`

## Visual Style
- Dark 3Blue1Brown-inspired background with bright cyan, green, pink, gold, and blue accents
- Clean typography, default Manim axes/grid objects, and smooth transformations
- Visual continuity preferred over hard cuts

## Implementation Notes
- Use `Scene` from ManimCE
- Keep the graphs discrete with dots and vertical guides
- Use `LaggedStart`, `TransformMatchingTex`, and `ReplacementTransform` for pacing
- Render from the `manim/` directory using the project virtual environment
