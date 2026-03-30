"""
5.5 Example 1 — Double-Angle with Given Information

Find sin(2θ), cos(2θ), tan(2θ) given cos θ = 5/13 where 3π/2 < θ < 2π.

3b1b style: large unit circle dominates, triangle built organically,
formula steps float contextually. Smooth transforms between steps.

Render (from the manim/ directory):
    manim -pql scenes/5_5_double_angle_given_info.py DoubleAngleGivenInfo
    manim -pqh scenes/5_5_double_angle_given_info.py DoubleAngleGivenInfo
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.helpers import *

THETA = 2 * PI - np.arccos(5 / 13)  # ≈ 5.136 rad, QIV


class DoubleAngleGivenInfo(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._phase_setup()
        self._phase_triangle()
        self._phase_sin2theta()
        self._phase_cos2theta()
        self._phase_tan2theta()

    # ── Phase 1: unit circle + given info ────────────────────────────────────
    def _phase_setup(self):
        # Given info — top right, understated
        given = VGroup(
            MathTex(r"\cos\theta = \tfrac{5}{13}", font_size=30, color=TEXT_PRIMARY),
            MathTex(r"\tfrac{3\pi}{2} < \theta < 2\pi", font_size=26, color=QIV_COLOR),
        ).arrange(DOWN, buff=0.2).to_corner(UR, buff=0.5)

        self.play(FadeIn(given, shift=LEFT * 0.3), run_time=0.7)
        self.given = given

        # Big unit circle (slightly left)
        self.uc_group, self.axes = build_unit_circle()
        self.play(Create(self.uc_group), run_time=1.0)

        # QIV shade
        q4 = build_quadrant_highlight(self.axes, 4, QIV_COLOR, opacity=0.10)
        self.play(FadeIn(q4), run_time=0.3)

        # Sweep angle arc
        arc = build_angle_arc(
            self.axes, THETA, QIV_COLOR,
            arc_radius=0.28, label_tex=r"\theta", label_font_size=22,
        )
        dot = build_terminal_point(self.axes, THETA, color=QIV_COLOR)

        self.play(Create(arc), run_time=1.0)
        self.play(FadeIn(dot, scale=1.5), run_time=0.4)
        self.arc = arc
        self.dot = dot
        self.wait(0.4)

    # ── Phase 2: reference triangle ──────────────────────────────────────────
    def _phase_triangle(self):
        tri = build_reference_triangle(
            self.axes,
            x_val=5 / 13, y_val=-12 / 13,
            x_label="5", y_label="-12", r_label="13",
            label_font_size=22,
        )

        # Animate sides one at a time
        self.play(Create(tri.x_leg), run_time=0.5)
        self.play(Create(tri.y_leg), run_time=0.5)
        self.play(Create(tri.hyp), run_time=0.5)
        self.play(
            Create(tri.right_angle_mark),
            *[FadeIn(lbl) for lbl in [tri.x_lbl, tri.y_lbl, tri.r_lbl] if lbl],
            run_time=0.5,
        )
        self.tri = tri

        # Trig values — float below the circle
        trig_vals = VGroup(
            MathTex(r"\sin\theta = -\tfrac{12}{13}", font_size=28, color=SIDE_B_COLOR),
            MathTex(r"\cos\theta = \tfrac{5}{13}", font_size=28, color=SIDE_A_COLOR),
            MathTex(r"\tan\theta = -\tfrac{12}{5}", font_size=28, color=TEXT_SECONDARY),
        ).arrange(RIGHT, buff=0.6).next_to(self.uc_group, DOWN, buff=0.5)

        self.play(
            LaggedStart(*[FadeIn(v, shift=UP * 0.2) for v in trig_vals], lag_ratio=0.15),
            run_time=0.9,
        )
        self.trig_vals = trig_vals
        self.wait(0.6)

    # ── Phase 3: sin(2θ) ─────────────────────────────────────────────────────
    def _phase_sin2theta(self):
        # Fade trig vals, but KEEP given info — move it to top-right as context
        self.play(FadeOut(self.trig_vals), run_time=0.4)
        self.play(
            self.given.animate.scale(0.8).to_corner(UR, buff=0.35),
            run_time=0.5,
        )

        # Shrink circle to make room for equations
        uc_all = VGroup(self.uc_group, self.arc, self.dot, self.tri)
        self.play(
            uc_all.animate.scale(0.55).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2),
            run_time=0.8,
        )

        # Formula + computation — right side, organic
        formula = MathTex(
            r"\sin(2\theta)", r"=", r"2\sin\theta\cos\theta",
            font_size=36, color=FORMULA_COLOR,
        ).move_to([2.5, 2.2, 0])

        sub = MathTex(
            r"= 2\!\left(-\tfrac{12}{13}\right)\!\left(\tfrac{5}{13}\right)",
            font_size=32, color=TEXT_PRIMARY,
        ).next_to(formula, DOWN, buff=0.4, aligned_edge=LEFT)

        result = MathTex(
            r"= -\dfrac{120}{169}",
            font_size=38, color=YELLOW,
        ).next_to(sub, DOWN, buff=0.4, aligned_edge=LEFT)

        self.play(Write(formula), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.6)
        self.play(Write(result), run_time=0.6)
        self.wait(0.4)

        self.sin_group = VGroup(formula, sub, result)

    # ── Phase 4: cos(2θ) ─────────────────────────────────────────────────────
    def _phase_cos2theta(self):
        # Shift sin result up and fade sub-steps
        self.play(
            self.sin_group[1].animate.set_opacity(0.3),
            run_time=0.3,
        )

        formula = MathTex(
            r"\cos(2\theta)", r"=", r"2\cos^2\!\theta - 1",
            font_size=36, color=FORMULA_COLOR,
        ).next_to(self.sin_group, DOWN, buff=0.6, aligned_edge=LEFT)

        sub = MathTex(
            r"= 2\!\left(\tfrac{5}{13}\right)^{\!2} - 1",
            font_size=32, color=TEXT_PRIMARY,
        ).next_to(formula, DOWN, buff=0.35, aligned_edge=LEFT)

        result = MathTex(
            r"= -\dfrac{119}{169}",
            font_size=38, color=YELLOW,
        ).next_to(sub, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(formula), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.5)
        self.play(Write(result), run_time=0.6)
        self.wait(0.4)

        self.cos_group = VGroup(formula, sub, result)

    # ── Phase 5: tan(2θ) + answer ────────────────────────────────────────────
    def _phase_tan2theta(self):
        # Fade sub-steps of cos
        self.play(
            self.cos_group[1].animate.set_opacity(0.3),
            run_time=0.3,
        )

        formula = MathTex(
            r"\tan(2\theta)", r"=", r"\dfrac{\sin(2\theta)}{\cos(2\theta)}",
            font_size=34, color=FORMULA_COLOR,
        ).next_to(self.cos_group, DOWN, buff=0.5, aligned_edge=LEFT)

        result = MathTex(
            r"= \dfrac{120}{119}",
            font_size=38, color=YELLOW,
        ).next_to(formula, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(formula), run_time=0.7)
        self.play(Write(result), run_time=0.6)

        # Box the three yellow answers
        answers = VGroup(
            self.sin_group[2], self.cos_group[2], result
        )
        for ans in answers:
            box = surround_answer(ans, buff=0.12)
            self.play(Create(box), run_time=0.25)

        self.wait(2.0)
