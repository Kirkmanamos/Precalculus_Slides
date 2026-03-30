"""
5.5 Example 2 — Solving a Double-Angle Equation

Solve  2cos x + sin(2x) = 0  where 0 ≤ x < 2π.

3b1b style: equation transforms center stage, unit circle for solutions,
organic layout with contextual annotations.

Render (from the manim/ directory):
    manim -pql scenes/5_5_double_angle_equation.py DoubleAngleEquation
    manim -pqh scenes/5_5_double_angle_equation.py DoubleAngleEquation
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.helpers import *


class DoubleAngleEquation(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._phase_equation()
        self._phase_substitute()
        self._phase_factor()
        self._phase_solve()
        self._phase_unit_circle()

    # ── Phase 1: present the equation ────────────────────────────────────────
    def _phase_equation(self):
        self.eq = MathTex(
            r"2\cos x", r"+", r"\sin(2x)", r"= 0",
            font_size=52, color=TEXT_PRIMARY,
        ).move_to(UP * 1.0)

        domain = MathTex(
            r"0 \le x < 2\pi",
            font_size=28, color=TEXT_SECONDARY,
        ).next_to(self.eq, DOWN, buff=0.5)

        self.play(Write(self.eq), run_time=1.0)
        self.play(FadeIn(domain, shift=UP * 0.2), run_time=0.5)
        self.domain = domain
        self.wait(0.5)

    # ── Phase 2: identity substitution ───────────────────────────────────────
    def _phase_substitute(self):
        # Highlight sin(2x)
        self.play(self.eq[2].animate.set_color(YELLOW), run_time=0.4)

        # Show identity
        identity = MathTex(
            r"\sin(2x) = 2\sin x\cos x",
            font_size=28, color=FORMULA_COLOR,
        ).next_to(self.eq, UP, buff=0.6)

        self.play(FadeIn(identity, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.3)

        # Transform equation
        eq2 = MathTex(
            r"2\cos x", r"+", r"2\sin x\cos x", r"= 0",
            font_size=52, color=TEXT_PRIMARY,
        ).move_to(UP * 1.0)
        eq2[2].set_color(YELLOW)

        self.play(
            TransformMatchingTex(self.eq, eq2),
            FadeOut(identity),
            run_time=1.0,
        )
        self.eq = eq2
        self.wait(0.3)

    # ── Phase 3: factor ──────────────────────────────────────────────────────
    def _phase_factor(self):
        factored = MathTex(
            r"2\cos x", r"\big(", r"1 + \sin x", r"\big)", r"= 0",
            font_size=52, color=TEXT_PRIMARY,
        ).move_to(UP * 1.0)

        self.play(TransformMatchingTex(self.eq, factored), run_time=1.0)
        self.eq = factored
        self.wait(0.3)

        # Color the two factors
        self.play(
            factored[0].animate.set_color(GREEN),
            factored[2].animate.set_color(RED),
            run_time=0.5,
        )

    # ── Phase 4: solve each factor ───────────────────────────────────────────
    def _phase_solve(self):
        # Case 1 — left
        case1 = VGroup(
            MathTex(r"\cos x = 0", font_size=34, color=GREEN),
            MathTex(r"x = \dfrac{\pi}{2},\; \dfrac{3\pi}{2}",
                    font_size=30, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to(LEFT * 3.0 + DOWN * 1.5)

        # Case 2 — right
        case2 = VGroup(
            MathTex(r"\sin x = -1", font_size=34, color=RED),
            MathTex(r"x = \dfrac{3\pi}{2}",
                    font_size=30, color=RED),
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 3.0 + DOWN * 1.5)

        # Arrows from factors to cases
        a1 = Arrow(
            self.eq[0].get_bottom(), case1[0].get_top(),
            color=GREEN, stroke_width=2, buff=0.15,
            max_tip_length_to_length_ratio=0.12,
        )
        a2 = Arrow(
            self.eq[2].get_bottom(), case2[0].get_top(),
            color=RED, stroke_width=2, buff=0.15,
            max_tip_length_to_length_ratio=0.12,
        )

        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.5)
        self.play(
            LaggedStart(
                FadeIn(case1[0], shift=UP * 0.2),
                FadeIn(case2[0], shift=UP * 0.2),
                lag_ratio=0.15,
            ),
            run_time=0.6,
        )
        self.play(
            FadeIn(case1[1], shift=UP * 0.15),
            FadeIn(case2[1], shift=UP * 0.15),
            run_time=0.5,
        )
        self.wait(0.5)

        self.case1 = case1
        self.case2 = case2
        self.arrows = VGroup(a1, a2)

    # ── Phase 5: unit circle with factored eq + interval in top-right ────────
    def _phase_unit_circle(self):
        # Fade arrows and cases
        self.play(
            FadeOut(self.arrows),
            FadeOut(self.case1), FadeOut(self.case2),
            run_time=0.4,
        )

        # Build context block: factored eq + interval → top-right
        context = VGroup(
            self.eq.copy().scale(0.55),
            self.domain.copy().scale(0.9),
        ).arrange(DOWN, buff=0.15, aligned_edge=RIGHT).to_corner(UR, buff=0.4)

        self.play(
            FadeOut(self.eq), FadeOut(self.domain),
            FadeIn(context),
            run_time=0.6,
        )
        self.context = context

        # Unit circle — slightly left to leave room for the context block
        uc_group, axes = build_unit_circle()
        self.play(Create(uc_group), run_time=0.8)

        # ── Mark π/2 (top) — GREEN (from cos x = 0) ─────────────────────
        dot1 = build_terminal_point(axes, PI / 2, color=GREEN)
        lbl1 = MathTex(
            r"\tfrac{\pi}{2}", font_size=26, color=GREEN
        ).next_to(dot1, RIGHT, buff=0.25)

        self.play(FadeIn(dot1, scale=1.5), Write(lbl1), run_time=0.6)

        ann1 = MathTex(
            r"\leftarrow \cos x = 0",
            font_size=20, color=GREEN_B,
        ).next_to(lbl1, RIGHT, buff=0.15)
        self.play(FadeIn(ann1, shift=LEFT * 0.2), run_time=0.4)

        # ── Mark 3π/2 (bottom) — both GREEN and RED converge here ────────
        dot2_glow = Dot(
            axes.c2p(0, -1), radius=0.25,
            color=GREEN, fill_opacity=0.2, z_index=4,
        )
        dot2_red = Dot(
            axes.c2p(0, -1), radius=0.14,
            color=RED, fill_opacity=0.3, z_index=4,
        )
        dot2 = Dot(
            axes.c2p(0, -1), radius=0.10,
            color=YELLOW, z_index=5,
        )
        dot2_group = VGroup(dot2_glow, dot2_red, dot2)

        lbl2 = MathTex(
            r"\tfrac{3\pi}{2}", font_size=26, color=YELLOW,
        ).next_to(dot2_group, RIGHT, buff=0.25)

        self.play(FadeIn(dot2_group, scale=1.5), Write(lbl2), run_time=0.6)

        ann2 = VGroup(
            MathTex(r"\leftarrow \cos x = 0", font_size=18, color=GREEN_B),
            MathTex(r"\leftarrow \sin x = -1", font_size=18, color=RED_B),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT).next_to(lbl2, RIGHT, buff=0.15)
        self.play(FadeIn(ann2, shift=LEFT * 0.2), run_time=0.5)

        self.wait(0.4)

        # ── Final answer — underneath the context block in top-right ─────
        answer = MathTex(
            r"x = \dfrac{\pi}{2},\;\; \dfrac{3\pi}{2}",
            font_size=34, color=YELLOW,
        ).next_to(context, DOWN, buff=0.35)
        box = surround_answer(answer, buff=0.12)

        self.play(Write(answer), Create(box), run_time=0.8)
        self.wait(2.0)
