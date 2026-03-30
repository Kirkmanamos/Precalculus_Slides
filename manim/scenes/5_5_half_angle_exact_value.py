"""
5.5 Example 4 — Half-Angle Exact Value: cos 165°

Shows 165° = 330°/2 on a large unit circle, builds the reference triangle
for 330°, determines sign from 165° being in QII, applies the formula.

3b1b style: big circle, contextual labels, smooth reveals.

Render (from the manim/ directory):
    manim -pql scenes/5_5_half_angle_exact_value.py HalfAngleExactValue
    manim -pqh scenes/5_5_half_angle_exact_value.py HalfAngleExactValue
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.helpers import *

DEG165 = 165 * DEGREES
DEG330 = 330 * DEGREES


class HalfAngleExactValue(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._phase_setup()
        self._phase_connection()
        self._phase_triangle()
        self._phase_sign()
        self._phase_calculate()

    # ── Phase 1: unit circle + 165° ──────────────────────────────────────────
    def _phase_setup(self):
        # Question
        question = MathTex(
            r"\cos 165° = \;?",
            font_size=44, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.5)
        self.play(Write(question), run_time=0.7)
        self.question = question

        # Big circle
        self.uc_group, self.axes = build_unit_circle()
        self.play(Create(self.uc_group), run_time=0.9)

        # QII shade + 165° arc
        q2 = build_quadrant_highlight(self.axes, 2, QII_COLOR, opacity=0.10)
        self.play(FadeIn(q2), run_time=0.3)

        arc_165 = build_angle_arc(
            self.axes, DEG165, QII_COLOR,
            arc_radius=0.32, label_tex=r"165°", label_font_size=22,
        )
        dot_165 = build_terminal_point(self.axes, DEG165, color=QII_COLOR)

        self.play(Create(arc_165), run_time=0.8)
        self.play(FadeIn(dot_165, scale=1.5), run_time=0.4)
        self.arc_165 = arc_165
        self.dot_165 = dot_165
        self.wait(0.4)

    # ── Phase 2: 165° = 330°/2 ───────────────────────────────────────────────
    def _phase_connection(self):
        # Draw 330° arc in QIV
        arc_330 = build_angle_arc(
            self.axes, DEG330, QIV_COLOR,
            arc_radius=0.22, label_tex=r"330°", label_font_size=18,
        )
        dot_330 = build_terminal_point(self.axes, DEG330, color=QIV_COLOR, radius=0.07)

        self.play(Create(arc_330), FadeIn(dot_330), run_time=0.8)

        # Key equation
        key = MathTex(
            r"165°", r"=", r"\dfrac{330°}{2}",
            font_size=38, color=YELLOW,
        ).to_corner(UR, buff=0.5)

        self.play(Write(key), run_time=0.7)
        self.key_eq = key
        self.wait(0.5)

    # ── Phase 3: reference triangle for 330° ─────────────────────────────────
    def _phase_triangle(self):
        cos330 = np.cos(DEG330)
        sin330 = np.sin(DEG330)

        tri = build_reference_triangle(
            self.axes,
            x_val=cos330, y_val=sin330,
            x_label=r"\frac{\sqrt{3}}{2}",
            y_label=r"-\frac{1}{2}",
            r_label="1",
            label_font_size=20,
        )
        self.play(Create(tri), run_time=0.8)

        # cos 330° value
        cos_val = MathTex(
            r"\cos 330° = \dfrac{\sqrt{3}}{2}",
            font_size=28, color=SIDE_A_COLOR,
        ).next_to(self.uc_group, DOWN, buff=0.4)

        self.play(FadeIn(cos_val, shift=UP * 0.2), run_time=0.5)
        self.cos_val = cos_val
        self.wait(0.5)

    # ── Phase 4: sign determination ──────────────────────────────────────────
    def _phase_sign(self):
        # Flash QII
        flash = build_quadrant_highlight(self.axes, 2, QII_COLOR, opacity=0.3)
        self.play(FadeIn(flash), run_time=0.2)
        self.play(FadeOut(flash), run_time=0.3)

        sign_note = VGroup(
            MathTex(r"165° \in \text{QII}", font_size=26, color=QII_COLOR),
            MathTex(r"\Rightarrow\;\cos\text{ is } \textbf{negative}",
                    font_size=26, color=RED),
        ).arrange(DOWN, buff=0.2).next_to(self.key_eq, DOWN, buff=0.5)

        self.play(
            LaggedStart(*[FadeIn(s, shift=LEFT * 0.2) for s in sign_note], lag_ratio=0.2),
            run_time=0.7,
        )
        self.wait(0.5)
        self.sign_note = sign_note

    # ── Phase 5: calculate ───────────────────────────────────────────────────
    def _phase_calculate(self):
        # Keep question + key eq visible as context in top-right
        context = VGroup(
            self.question.copy().scale(0.7),
            self.key_eq.copy().scale(0.7),
        ).arrange(DOWN, buff=0.1, aligned_edge=RIGHT).to_corner(UR, buff=0.35)

        # Shrink circle to left
        circle_stuff = VGroup(self.uc_group, self.arc_165, self.dot_165, self.cos_val)
        self.play(
            circle_stuff.animate.scale(0.5).to_edge(LEFT, buff=0.3).shift(DOWN * 0.3),
            FadeOut(self.sign_note),
            FadeOut(self.question), FadeOut(self.key_eq),
            FadeIn(context),
            run_time=0.7,
        )
        self.context = context

        # Calculation chain — right side
        steps = VGroup(
            MathTex(
                r"\cos 165° = -\sqrt{\dfrac{1 + \cos 330°}{2}}",
                font_size=32, color=FORMULA_COLOR,
            ),
            MathTex(
                r"= -\sqrt{\dfrac{1 + \frac{\sqrt{3}}{2}}{2}}",
                font_size=32, color=TEXT_PRIMARY,
            ),
            MathTex(
                r"= -\sqrt{\dfrac{2 + \sqrt{3}}{4}}",
                font_size=32, color=TEXT_PRIMARY,
            ),
            MathTex(
                r"= -\dfrac{\sqrt{2 + \sqrt{3}}}{2}",
                font_size=40, color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(RIGHT * 2.0)

        for step in steps:
            self.play(FadeIn(step, shift=UP * 0.15), run_time=0.55)
            self.wait(0.2)

        # Box the answer
        box = surround_answer(steps[-1], buff=0.15)
        self.play(Create(box), run_time=0.5)
        self.wait(2.0)
