"""
5.5 Example 6 — Half-Angle Quadrant Analysis (CAPSTONE)

Given cos θ = 5/13 where 3π/2 < θ < 2π, find sin(θ/2).

THE key pedagogical scene. θ is in QIV but θ/2 is in QII.
Students' #1 misconception: using θ's quadrant instead of θ/2's
for sign determination. Both arcs shown simultaneously.

3b1b style: dramatic reveal of θ/2 landing in QII, large unit circle,
smooth inequality animation.

Render (from the manim/ directory):
    manim -pql scenes/5_5_half_angle_quadrant_analysis.py HalfAngleQuadrantAnalysis
    manim -pqh scenes/5_5_half_angle_quadrant_analysis.py HalfAngleQuadrantAnalysis
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.helpers import *

THETA = 2 * PI - np.arccos(5 / 13)   # ≈ 5.136 rad, QIV
THETA_HALF = THETA / 2                # ≈ 2.568 rad, QII


class HalfAngleQuadrantAnalysis(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._phase_setup()
        self._phase_key_insight()
        self._phase_formula()
        self._phase_calculate()

    # ── Phase 1: given info + circle + triangle ──────────────────────────────
    def _phase_setup(self):
        given = VGroup(
            MathTex(r"\cos\theta = \tfrac{5}{13}", font_size=30, color=TEXT_PRIMARY),
            MathTex(r"\tfrac{3\pi}{2} < \theta < 2\pi", font_size=26, color=QIV_COLOR),
            MathTex(r"\text{Find: } \sin\!\left(\tfrac{\theta}{2}\right)",
                    font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.2).to_corner(UR, buff=0.5)

        self.play(
            LaggedStart(*[FadeIn(g, shift=LEFT * 0.3) for g in given], lag_ratio=0.15),
            run_time=0.8,
        )
        self.given = given

        # Large unit circle
        self.uc_group, self.axes = build_unit_circle()
        self.play(Create(self.uc_group), run_time=0.9)

        # QIV shade
        q4 = build_quadrant_highlight(self.axes, 4, QIV_COLOR, opacity=0.10)
        self.play(FadeIn(q4), run_time=0.3)
        self.q4 = q4

        # θ arc + dot
        arc_theta = build_angle_arc(
            self.axes, THETA, QIV_COLOR,
            arc_radius=0.25, label_tex=r"\theta", label_font_size=22,
        )
        dot_theta = build_terminal_point(self.axes, THETA, color=QIV_COLOR)
        self.play(Create(arc_theta), FadeIn(dot_theta, scale=1.5), run_time=0.9)

        # Triangle
        tri = build_reference_triangle(
            self.axes,
            x_val=5 / 13, y_val=-12 / 13,
            x_label="5", y_label="-12", r_label="13",
            label_font_size=20,
        )
        self.play(Create(tri), run_time=0.7)

        self.arc_theta = arc_theta
        self.dot_theta = dot_theta
        self.tri = tri
        self.wait(0.5)

    # ── Phase 2: THE KEY — where does θ/2 land? ─────────────────────────────
    def _phase_key_insight(self):
        # Inequality transformation — center stage, below circle
        ineq1 = MathTex(
            r"\tfrac{3\pi}{2}", r"<", r"\theta", r"<", r"2\pi",
            font_size=34, color=QIV_COLOR,
        ).next_to(self.uc_group, DOWN, buff=0.5)

        self.play(Write(ineq1), run_time=0.7)
        self.wait(0.3)

        # Transform: divide by 2
        div_label = MathTex(
            r"\div\, 2", font_size=24, color=TEXT_SECONDARY,
        ).next_to(ineq1, RIGHT, buff=0.3)
        self.play(FadeIn(div_label, shift=LEFT * 0.2), run_time=0.3)

        ineq2 = MathTex(
            r"\tfrac{3\pi}{4}", r"<", r"\tfrac{\theta}{2}", r"<", r"\pi",
            font_size=34, color=QII_COLOR,
        ).move_to(ineq1)

        self.play(
            TransformMatchingTex(ineq1, ineq2),
            FadeOut(div_label),
            run_time=1.0,
        )
        self.wait(0.3)

        # Now the dramatic moment — draw θ/2 arc into QII
        q2 = build_quadrant_highlight(self.axes, 2, QII_COLOR, opacity=0.18)
        self.play(FadeIn(q2), run_time=0.4)

        arc_half = build_angle_arc(
            self.axes, THETA_HALF, QII_COLOR,
            arc_radius=0.45, label_tex=r"\tfrac{\theta}{2}", label_font_size=22,
        )
        dot_half = build_terminal_point(self.axes, THETA_HALF, color=QII_COLOR)

        self.play(
            Create(arc_half),
            FadeIn(dot_half, scale=1.8),
            run_time=1.2,
        )

        # "θ/2 is in QII!" — big, dramatic
        reveal = MathTex(
            r"\tfrac{\theta}{2} \text{ is in QII!}",
            font_size=36, color=QII_COLOR,
        ).next_to(ineq2, DOWN, buff=0.4)

        self.play(Write(reveal), run_time=0.6)

        # Flash
        flash = reveal.copy().set_color(WHITE).set_opacity(0.8)
        self.play(FadeIn(flash, scale=1.15), run_time=0.15)
        self.play(FadeOut(flash), run_time=0.3)

        self.ineq2 = ineq2
        self.reveal = reveal
        self.arc_half = arc_half
        self.dot_half = dot_half
        self.wait(0.5)

    # ── Phase 3: sign → formula ──────────────────────────────────────────────
    def _phase_formula(self):
        sign_note = MathTex(
            r"\sin\text{ is } \textbf{positive} \text{ in QII} \;\Rightarrow\; \text{use } +",
            font_size=26, color=GREEN,
        ).next_to(self.reveal, DOWN, buff=0.3)

        self.play(FadeIn(sign_note, shift=UP * 0.15), run_time=0.5)
        self.wait(0.4)
        self.sign_note = sign_note

    # ── Phase 4: calculate ───────────────────────────────────────────────────
    def _phase_calculate(self):
        # Keep given info visible as context — move to top-right
        self.play(
            self.given.animate.scale(0.8).to_corner(UR, buff=0.35),
            run_time=0.4,
        )

        # Clean up — shrink circle left
        circle_stuff = VGroup(
            self.uc_group, self.arc_theta, self.dot_theta, self.tri,
            self.arc_half, self.dot_half, self.q4,
        )
        self.play(
            circle_stuff.animate.scale(0.45).to_edge(LEFT, buff=0.3).shift(DOWN * 0.3),
            FadeOut(self.ineq2),
            FadeOut(self.reveal), FadeOut(self.sign_note),
            run_time=0.7,
        )

        steps = VGroup(
            MathTex(
                r"\sin\!\left(\tfrac{\theta}{2}\right) = +\sqrt{\dfrac{1 - \cos\theta}{2}}",
                font_size=32, color=FORMULA_COLOR,
            ),
            MathTex(
                r"= \sqrt{\dfrac{1 - \frac{5}{13}}{2}} = \sqrt{\dfrac{\frac{8}{13}}{2}}",
                font_size=30, color=TEXT_PRIMARY,
            ),
            MathTex(
                r"= \sqrt{\dfrac{4}{13}} = \dfrac{2}{\sqrt{13}}",
                font_size=30, color=TEXT_PRIMARY,
            ),
            MathTex(
                r"= \dfrac{2\sqrt{13}}{13}",
                font_size=42, color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(RIGHT * 2.0)

        for step in steps:
            self.play(FadeIn(step, shift=UP * 0.15), run_time=0.55)
            self.wait(0.15)

        box = surround_answer(steps[-1], buff=0.15)
        self.play(Create(box), run_time=0.5)
        self.wait(2.0)
