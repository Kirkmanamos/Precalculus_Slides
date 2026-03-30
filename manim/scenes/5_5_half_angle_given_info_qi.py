"""
5.5 Example 5 — Half-Angle from Given Information (Quadrant I)

Given sin x = 2/5 where 0 < x < π/2, find cos(x/2).

3b1b style: big unit circle with triangle, organic equation positioning,
smooth quadrant analysis.

Render (from the manim/ directory):
    manim -pql scenes/5_5_half_angle_given_info_qi.py HalfAngleGivenInfoQI
    manim -pqh scenes/5_5_half_angle_given_info_qi.py HalfAngleGivenInfoQI
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.helpers import *

ANGLE_X = np.arcsin(2 / 5)  # ≈ 0.4115 rad


class HalfAngleGivenInfoQI(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._phase_setup()
        self._phase_triangle()
        self._phase_quadrant()
        self._phase_calculate()

    # ── Phase 1: given info + circle ─────────────────────────────────────────
    def _phase_setup(self):
        given = VGroup(
            MathTex(r"\sin x = \tfrac{2}{5}", font_size=32, color=TEXT_PRIMARY),
            MathTex(r"0 < x < \tfrac{\pi}{2}", font_size=26, color=QI_COLOR),
            MathTex(r"\text{Find: } \cos\!\left(\tfrac{x}{2}\right)",
                    font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.25).to_corner(UR, buff=0.5)

        self.play(
            LaggedStart(*[FadeIn(g, shift=LEFT * 0.3) for g in given], lag_ratio=0.15),
            run_time=0.8,
        )
        self.given = given

        self.uc_group, self.axes = build_unit_circle()
        self.play(Create(self.uc_group), run_time=0.9)

        # QI shade
        q1 = build_quadrant_highlight(self.axes, 1, QI_COLOR, opacity=0.08)
        self.play(FadeIn(q1), run_time=0.3)

        # Angle arc + dot
        arc = build_angle_arc(
            self.axes, ANGLE_X, QI_COLOR,
            arc_radius=0.35, label_tex=r"x", label_font_size=24,
        )
        dot = build_terminal_point(self.axes, ANGLE_X, color=QI_COLOR)
        self.play(Create(arc), FadeIn(dot, scale=1.5), run_time=0.8)
        self.arc = arc
        self.dot = dot
        self.wait(0.3)

    # ── Phase 2: triangle + cos x ────────────────────────────────────────────
    def _phase_triangle(self):
        cos_x = np.sqrt(21) / 5
        sin_x = 2 / 5

        tri = build_reference_triangle(
            self.axes,
            x_val=cos_x, y_val=sin_x,
            x_label=r"\sqrt{21}", y_label="2", r_label="5",
            label_font_size=22,
        )

        self.play(Create(tri.x_leg), run_time=0.4)
        self.play(Create(tri.y_leg), run_time=0.4)
        self.play(Create(tri.hyp), run_time=0.4)
        self.play(
            Create(tri.right_angle_mark),
            *[FadeIn(lbl) for lbl in [tri.x_lbl, tri.y_lbl, tri.r_lbl] if lbl],
            run_time=0.5,
        )
        self.tri = tri

        # cos x value — below circle
        cos_eq = MathTex(
            r"\cos x = \dfrac{\sqrt{21}}{5}",
            font_size=30, color=SIDE_A_COLOR,
        ).next_to(self.uc_group, DOWN, buff=0.45)

        self.play(Write(cos_eq), run_time=0.6)
        self.cos_eq = cos_eq
        self.wait(0.5)

    # ── Phase 3: quadrant of x/2 ────────────────────────────────────────────
    def _phase_quadrant(self):
        # Show x/2 arc
        arc_half = build_angle_arc(
            self.axes, ANGLE_X / 2, TEAL,
            arc_radius=0.55, label_tex=r"\tfrac{x}{2}", label_font_size=20,
        )
        self.play(Create(arc_half), run_time=0.6)

        # Quadrant reasoning — below cos eq
        reasoning = VGroup(
            MathTex(r"0 < \tfrac{x}{2} < \tfrac{\pi}{4}",
                    font_size=26, color=TEAL),
            MathTex(r"\Rightarrow\;\cos\text{ is } \textbf{positive}",
                    font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.2).next_to(self.cos_eq, DOWN, buff=0.4)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.15) for r in reasoning], lag_ratio=0.2),
            run_time=0.7,
        )
        self.wait(0.5)
        self.reasoning = reasoning

    # ── Phase 4: calculate ───────────────────────────────────────────────────
    def _phase_calculate(self):
        # Keep given info visible as context — move to top-right
        self.play(
            self.given.animate.scale(0.8).to_corner(UR, buff=0.35),
            run_time=0.4,
        )

        # Clean up — shrink circle left
        circle_stuff = VGroup(
            self.uc_group, self.arc, self.dot, self.tri, self.cos_eq, self.reasoning
        )
        self.play(
            circle_stuff.animate.scale(0.45).to_edge(LEFT, buff=0.3).shift(DOWN * 0.3),
            run_time=0.7,
        )

        steps = VGroup(
            MathTex(
                r"\cos\!\left(\tfrac{x}{2}\right) = +\sqrt{\dfrac{1 + \cos x}{2}}",
                font_size=32, color=FORMULA_COLOR,
            ),
            MathTex(
                r"= \sqrt{\dfrac{1 + \frac{\sqrt{21}}{5}}{2}}",
                font_size=30, color=TEXT_PRIMARY,
            ),
            MathTex(
                r"= \sqrt{\dfrac{5 + \sqrt{21}}{10}}",
                font_size=38, color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(RIGHT * 2.0)

        for step in steps:
            self.play(FadeIn(step, shift=UP * 0.15), run_time=0.55)
            self.wait(0.2)

        box = surround_answer(steps[-1], buff=0.15)
        self.play(Create(box), run_time=0.5)
        self.wait(2.0)
