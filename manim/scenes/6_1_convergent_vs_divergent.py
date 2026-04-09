"""
Unit 6.1 — Convergent vs divergent infinite sequences.

Contrasts the classic convergent sequence a_n = 1/n with the classic divergent
sequence b_n = (-1)^n using discrete graphs and a highlighted band around y = 0.

Render (from the manim/ directory):
    ../.venv/bin/python -m manim -pql scenes/6_1_convergent_vs_divergent.py ConvergentVsDivergentSequences
    ../.venv/bin/python -m manim -pqh scenes/6_1_convergent_vs_divergent.py ConvergentVsDivergentSequences
"""

from manim import *
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *


BG_3B1B = "#1C1C2E"
TEXT_PRIMARY = WHITE
TEXT_SECONDARY = GREY_B
GRID_SOFT = "#2A4058"
CONVERGENT_COLOR = Q1_COLOR
DIVERGENT_COLOR = Q3_COLOR
BAND_COLOR = HIGHLIGHT
ORDER_ALERT = ACCENT_RED


class ConvergentVsDivergentSequences(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._intro()
        self._build_axes()
        self._plot_convergent_sequence()
        self._plot_divergent_sequence()
        self._compare()
        self._close()

    def _intro(self):
        title = Text(
            "Convergent vs Divergent Infinite Sequences",
            font_size=34,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.28)
        subtitle = Text(
            "Do the dots settle near one number?",
            font_size=22,
            color=TEXT_SECONDARY,
        ).next_to(title, DOWN, buff=0.18)

        self.play(Write(title), FadeIn(subtitle, shift=DOWN * 0.2), run_time=1.0)
        self.wait(0.4)

        self.title = title
        self.subtitle = subtitle

    def _make_panel(self, title_text: str, color: str, x_shift: float) -> tuple[VGroup, Axes, NumberPlane]:
        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[-1.4, 1.4, 0.5],
            x_length=5.25,
            y_length=3.9,
            axis_config={
                "color": GREY_C,
                "include_tip": True,
                "tip_length": 0.15,
                "stroke_width": 1.7,
            },
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).shift(x_shift * RIGHT + DOWN * 0.65)

        plane = NumberPlane(
            x_range=[0, 9, 1],
            y_range=[-1.4, 1.4, 0.5],
            x_length=5.25,
            y_length=3.9,
            background_line_style={
                "stroke_color": GRID_SOFT,
                "stroke_width": 1,
                "stroke_opacity": 0.45,
            },
            axis_config={"stroke_opacity": 0},
            faded_line_style={
                "stroke_color": GRID_SOFT,
                "stroke_width": 0.7,
                "stroke_opacity": 0.22,
            },
        ).move_to(axes)

        label = Text(title_text, font_size=24, color=color).next_to(axes, UP, buff=0.25)
        panel_box = SurroundingRectangle(
            VGroup(axes, label),
            color=color,
            buff=0.22,
            corner_radius=0.12,
            stroke_width=2.2,
        )

        group = VGroup(plane, axes, label, panel_box)
        return group, axes, plane

    def _build_axes(self):
        left_group, left_axes, left_plane = self._make_panel("Convergent Example", CONVERGENT_COLOR, -3.25)
        right_group, right_axes, right_plane = self._make_panel("Divergent Example", DIVERGENT_COLOR, 3.25)

        left_formula = MathTex(r"a_n = \frac{1}{n}", font_size=34, color=CONVERGENT_COLOR).next_to(left_group, DOWN, buff=0.16)
        right_formula = MathTex(r"b_n = (-1)^n", font_size=34, color=DIVERGENT_COLOR).next_to(right_group, DOWN, buff=0.16)

        self.play(
            FadeIn(left_plane),
            Create(left_axes),
            FadeIn(right_plane),
            Create(right_axes),
            run_time=1.3,
        )
        self.play(
            Write(left_group[2]),
            Create(left_group[3]),
            Write(right_group[2]),
            Create(right_group[3]),
            Write(left_formula),
            Write(right_formula),
            run_time=1.0,
        )

        self.left_axes = left_axes
        self.right_axes = right_axes
        self.left_formula = left_formula
        self.right_formula = right_formula

    def _plot_convergent_sequence(self):
        points = []
        labels = []
        guides = []
        for n in range(1, 9):
            y_val = 1 / n
            point = self.left_axes.c2p(n, y_val)
            dot = Dot(point, radius=0.075, color=CONVERGENT_COLOR)
            guide = DashedLine(self.left_axes.c2p(n, 0), point, color=CONVERGENT_COLOR, dash_length=0.1, stroke_width=1.7)
            if n <= 4:
                label = MathTex(fr"\frac{{1}}{{{n}}}", font_size=22, color=CONVERGENT_COLOR).next_to(point, UR, buff=0.1)
            else:
                label = MathTex(fr"a_{{{n}}}", font_size=18, color=TEXT_SECONDARY).next_to(point, UP, buff=0.08)
            points.append(dot)
            labels.append(label)
            guides.append(guide)

        limit_line = DashedLine(
            self.left_axes.c2p(0, 0),
            self.left_axes.c2p(8.8, 0),
            color=BAND_COLOR,
            dash_length=0.15,
            stroke_width=2.4,
        )
        limit_label = MathTex(r"y = 0", font_size=24, color=BAND_COLOR).next_to(limit_line, LEFT, buff=0.15)

        self.play(Create(limit_line), Write(limit_label), run_time=0.8)
        self.play(
            LaggedStart(
                *[
                    AnimationGroup(Create(guide), FadeIn(dot, scale=0.6), FadeIn(label, shift=UP * 0.08))
                    for guide, dot, label in zip(guides, points, labels)
                ],
                lag_ratio=0.16,
            ),
            run_time=2.4,
        )

        band = Rectangle(
            width=self.left_axes.x_length,
            height=0.62,
            stroke_color=BAND_COLOR,
            stroke_width=2.0,
            fill_color=BAND_COLOR,
            fill_opacity=0.12,
        ).move_to(self.left_axes.c2p(4.4, 0))
        band_text = Text(
            "Eventually inside this band",
            font_size=20,
            color=BAND_COLOR,
        ).next_to(band, UP, buff=0.12)

        self.play(FadeIn(band), FadeIn(band_text, shift=UP * 0.1), run_time=0.9)
        self.wait(0.5)

        self.left_points = VGroup(*points)
        self.left_band = band
        self.left_band_text = band_text

    def _plot_divergent_sequence(self):
        points = []
        labels = []
        guides = []
        for n in range(1, 9):
            y_val = -1 if n % 2 == 1 else 1
            point = self.right_axes.c2p(n, y_val)
            dot = Dot(point, radius=0.075, color=DIVERGENT_COLOR)
            guide = DashedLine(self.right_axes.c2p(n, 0), point, color=DIVERGENT_COLOR, dash_length=0.1, stroke_width=1.7)
            if n <= 4:
                label = MathTex(str(y_val), font_size=22, color=DIVERGENT_COLOR).next_to(point, RIGHT if y_val > 0 else LEFT, buff=0.1)
            else:
                label = MathTex(fr"b_{{{n}}}", font_size=18, color=TEXT_SECONDARY).next_to(point, RIGHT, buff=0.08)
            points.append(dot)
            labels.append(label)
            guides.append(guide)

        center_line = DashedLine(
            self.right_axes.c2p(0, 0),
            self.right_axes.c2p(8.8, 0),
            color=BAND_COLOR,
            dash_length=0.15,
            stroke_width=2.4,
        )
        center_label = MathTex(r"y = 0", font_size=24, color=BAND_COLOR).next_to(center_line, LEFT, buff=0.15)

        self.play(Create(center_line), Write(center_label), run_time=0.8)
        self.play(
            LaggedStart(
                *[
                    AnimationGroup(Create(guide), FadeIn(dot, scale=0.6), FadeIn(label, shift=UP * 0.08))
                    for guide, dot, label in zip(guides, points, labels)
                ],
                lag_ratio=0.16,
            ),
            run_time=2.4,
        )

        band = Rectangle(
            width=self.right_axes.x_length,
            height=0.62,
            stroke_color=BAND_COLOR,
            stroke_width=2.0,
            fill_color=BAND_COLOR,
            fill_opacity=0.12,
        ).move_to(self.right_axes.c2p(4.4, 0))
        band_text = Text(
            "Keeps escaping the band",
            font_size=20,
            color=ORDER_ALERT,
        ).next_to(band, DOWN, buff=0.12)

        escape_marks = VGroup(
            Arrow(band.get_top() + UP * 0.05, self.right_points_target(2), buff=0.04, color=ORDER_ALERT, stroke_width=5),
            Arrow(band.get_bottom() + DOWN * 0.05, self.right_points_target(1), buff=0.04, color=ORDER_ALERT, stroke_width=5),
        )

        self.play(FadeIn(band), FadeIn(band_text, shift=DOWN * 0.1), run_time=0.9)
        self.play(GrowArrow(escape_marks[0]), GrowArrow(escape_marks[1]), run_time=0.7)
        self.wait(0.5)

        self.right_points = VGroup(*points)
        self.right_band = band
        self.right_band_text = band_text
        self.escape_marks = escape_marks

    def right_points_target(self, n: int) -> np.ndarray:
        y_val = -1 if n % 2 == 1 else 1
        return self.right_axes.c2p(n, y_val)

    def _compare(self):
        converge_text = Text(
            "Convergent: the terms approach one number",
            font_size=22,
            color=CONVERGENT_COLOR,
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 3.05)
        diverge_text = Text(
            "Divergent: the terms never settle at one number",
            font_size=22,
            color=DIVERGENT_COLOR,
        ).to_edge(RIGHT, buff=0.6).shift(DOWN * 3.05)

        self.play(Write(converge_text), Write(diverge_text), run_time=1.0)
        self.wait(0.6)

        self.converge_text = converge_text
        self.diverge_text = diverge_text

    def _close(self):
        note = Text(
            "Another classic divergent example is c_n = n, which grows without bound.",
            font_size=20,
            color=TEXT_SECONDARY,
        ).to_edge(DOWN, buff=0.22)

        banner = RoundedRectangle(
            corner_radius=0.14,
            width=8.8,
            height=0.82,
            fill_color="#12122a",
            fill_opacity=0.95,
            stroke_color=ACCENT_BLUE,
            stroke_width=2.4,
        ).next_to(self.subtitle, DOWN, buff=0.35)
        summary = Text(
            "Convergence means the dots settle down.",
            font_size=24,
            color=TEXT_PRIMARY,
        ).move_to(banner)

        self.play(FadeIn(banner), Write(summary), run_time=0.9)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(1.8)
