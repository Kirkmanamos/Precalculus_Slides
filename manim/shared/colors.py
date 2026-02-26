"""
Shared color and font constants for all Manim scenes in this project.

Always import at the top of every scene file:
    from shared.colors import *

These values are deliberately synchronized with the Slidev/HTML palette defined
in CONVENTIONS.md. Do not change them here without updating CONVENTIONS.md.
"""

# ---------------------------------------------------------------------------
# Quadrant Colors (ASTC — All Students Take Calculus)
# ---------------------------------------------------------------------------
Q1_COLOR = "#4ade80"    # Quadrant I   — All positive   — Green
Q2_COLOR = "#22d3ee"    # Quadrant II  — sin positive    — Cyan
Q3_COLOR = "#f472b6"    # Quadrant III — tan positive    — Pink
Q4_COLOR = "#fbbf24"    # Quadrant IV  — cos positive    — Gold/Amber

# ---------------------------------------------------------------------------
# Right Triangle Side Colors
# ---------------------------------------------------------------------------
X_SIDE = Q2_COLOR       # Horizontal leg — Cyan
Y_SIDE = Q3_COLOR       # Vertical leg   — Pink
R_SIDE = Q1_COLOR       # Hypotenuse     — Green

# ---------------------------------------------------------------------------
# Background and Text
# ---------------------------------------------------------------------------
BG_COLOR      = "#071018"   # Slide background (dark)
TEXT_COLOR    = "#eef6ff"   # Primary text
TEXT_MUTED    = "#a8bfd0"   # Secondary / muted text
ACCENT_TEAL   = "#5eead4"   # Primary accent
ACCENT_BLUE   = "#93c5fd"   # Secondary accent
ACCENT_RED    = "#fca5a5"   # Tertiary accent / error highlight

# ---------------------------------------------------------------------------
# Axis and Grid
# ---------------------------------------------------------------------------
AXIS_COLOR    = "#a8bfd0"   # Axis lines
GRID_COLOR    = "#1a2d40"   # Grid lines (subtle)
TICK_COLOR    = "#a8bfd0"   # Tick mark labels

# ---------------------------------------------------------------------------
# Highlight / Emphasis
# ---------------------------------------------------------------------------
HIGHLIGHT     = "#fbbf24"   # Call-out color (gold, used sparingly)
CORRECT       = Q1_COLOR    # Correct / positive emphasis
INCORRECT     = Q3_COLOR    # Incorrect / negative emphasis

# ---------------------------------------------------------------------------
# Typography (use with Manim Text objects)
# ---------------------------------------------------------------------------
FONT_DISPLAY  = "Space Grotesk"   # Headings and titles
FONT_BODY     = "IBM Plex Sans"   # Body text and labels
FONT_MONO     = "IBM Plex Mono"   # Code and mathematical expressions

# ---------------------------------------------------------------------------
# Quick usage reference
# ---------------------------------------------------------------------------
#
# from manim import *
# from shared.colors import *
#
# class MyScene(Scene):
#     def construct(self):
#         self.camera.background_color = BG_COLOR
#
#         title = Text("Inverse Sine", font=FONT_DISPLAY, color=TEXT_COLOR)
#         circle = Circle(color=Q1_COLOR, fill_opacity=0.2)
#         x_leg = Line(color=X_SIDE)
#         y_leg = Line(color=Y_SIDE)
#         hyp   = Line(color=R_SIDE)
