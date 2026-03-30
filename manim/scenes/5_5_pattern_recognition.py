"""
5.5 Example 3 — Pattern Recognition: cos²(5α) − sin²(5α) = cos(10α)

3b1b-style: large centered equations, color-coded pattern matching,
smooth transforms. No rigid panels — text floats organically.

Render (from the manim/ directory):
    manim -pql scenes/5_5_pattern_recognition.py PatternRecognition
    manim -pqh scenes/5_5_pattern_recognition.py PatternRecognition
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.helpers import *


class PatternRecognition(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._phase_setup()
        self._phase_identity()
        self._phase_match()
        self._phase_result()

    # ── Phase 1: present the expression ──────────────────────────────────────
    def _phase_setup(self):
        title = Text(
            "Rewrite using a double-angle identity",
            font_size=28, color=TEXT_SECONDARY,
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.7)
        self.title = title

        # Big, centered expression
        self.expr = MathTex(
            r"\cos^2(5\alpha)", r"-", r"\sin^2(5\alpha)",
            font_size=56, color=TEXT_PRIMARY,
        ).move_to(ORIGIN)

        self.play(Write(self.expr), run_time=1.2)
        self.wait(0.8)

    # ── Phase 2: recall the identity ─────────────────────────────────────────
    def _phase_identity(self):
        # Shift expression up to make room
        self.play(self.expr.animate.shift(UP * 1.0), run_time=0.6)

        # Identity template below
        self.identity = MathTex(
            r"\cos(2u)", r"=", r"\cos^2(u)", r"-", r"\sin^2(u)",
            font_size=40, color=FORMULA_COLOR,
        ).next_to(self.expr, DOWN, buff=1.0)

        box = SurroundingRectangle(
            self.identity, color=FORMULA_COLOR, buff=0.2,
            stroke_width=1.5, corner_radius=0.08,
            fill_color=BLUE, fill_opacity=0.08,
        )

        self.play(
            FadeIn(self.identity, shift=UP * 0.3),
            Create(box),
            run_time=0.9,
        )
        self.identity_box = box
        self.wait(0.6)

    # ── Phase 3: color-match u = 5α ──────────────────────────────────────────
    def _phase_match(self):
        # Color the "u" slots in identity gold
        u_targets = [
            self.identity[0][4],     # u in cos(2u)
            self.identity[2][5],     # u in cos²(u)
            self.identity[4][5],     # u in sin²(u)
        ]
        # Color "5α" in expression gold
        five_alpha_0 = self.expr[0][5:]
        five_alpha_2 = self.expr[2][5:]

        self.play(
            *[m.animate.set_color(YELLOW) for m in u_targets],
            five_alpha_0.animate.set_color(YELLOW),
            five_alpha_2.animate.set_color(YELLOW),
            run_time=0.8,
        )

        # Substitution label
        sub_label = MathTex(
            r"u = 5\alpha", r"\quad\Longrightarrow\quad", r"2u = 10\alpha",
            font_size=36, color=YELLOW,
        ).next_to(self.identity_box, DOWN, buff=0.6)

        self.play(Write(sub_label), run_time=0.8)
        self.wait(0.6)

        self.sub_label = sub_label

    # ── Phase 4: transform to result ─────────────────────────────────────────
    def _phase_result(self):
        result = MathTex(
            r"\cos(10\alpha)",
            font_size=64, color=GREEN,
        ).move_to(ORIGIN)

        # Fade out scaffolding
        self.play(
            FadeOut(self.identity), FadeOut(self.identity_box),
            FadeOut(self.sub_label), FadeOut(self.title),
            run_time=0.5,
        )

        # Transform
        self.play(
            TransformMatchingShapes(self.expr, result),
            run_time=1.4,
        )

        # Answer box
        answer_box = surround_answer(result)
        self.play(Create(answer_box), run_time=0.6)

        # Full equation below
        full = MathTex(
            r"\cos^2(5\alpha) - \sin^2(5\alpha) = \cos(10\alpha)",
            font_size=32, color=TEXT_SECONDARY,
        ).next_to(result, DOWN, buff=0.8)
        self.play(FadeIn(full, shift=UP * 0.2), run_time=0.6)

        self.wait(2.0)
