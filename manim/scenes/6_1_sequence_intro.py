"""
Unit 6.1 — Sequence introduction video.

Illustrates the core idea that a sequence is an ordered list, and equivalently
can be viewed as a function whose domain is the positive integers.

Render (from the manim/ directory):
    ../.venv/bin/python -m manim -pql scenes/6_1_sequence_intro.py SequenceAsOrderedFunction
    ../.venv/bin/python -m manim -pqh scenes/6_1_sequence_intro.py SequenceAsOrderedFunction
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
TERM_COLORS = [ACCENT_BLUE, Q1_COLOR, Q3_COLOR, HIGHLIGHT]
ORDER_ALERT = "#ff6b6b"


class SequenceAsOrderedFunction(Scene):
    def construct(self):
        self.camera.background_color = BG_3B1B

        self._build_intro()
        self._show_ordered_terms()
        self._show_order_matters()
        self._transform_to_graph()
        self._show_function_view()

    def _build_intro(self):
        title = Text(
            "What is a sequence?",
            font_size=40,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.35)
        subtitle = Text(
            "An ordered list with positions",
            font_size=24,
            color=TEXT_SECONDARY,
        ).next_to(title, DOWN, buff=0.18)

        self.play(Write(title), FadeIn(subtitle, shift=DOWN * 0.2), run_time=1.1)
        self.wait(0.4)

        self.title = title
        self.subtitle = subtitle

    def _make_term_card(self, value_tex: str, sub_tex: str, color: str) -> VGroup:
        card = RoundedRectangle(
            corner_radius=0.18,
            width=1.55,
            height=1.75,
            stroke_color=color,
            stroke_width=2.6,
            fill_color=color,
            fill_opacity=0.12,
        )
        value = MathTex(value_tex, font_size=40, color=TEXT_PRIMARY)
        index = MathTex(sub_tex, font_size=26, color=color)
        index.next_to(value, DOWN, buff=0.22)
        return VGroup(card, value, index)

    def _show_ordered_terms(self):
        values = ["3", "7", "11", "15"]
        subs = [r"a_1", r"a_2", r"a_3", r"a_4"]
        cards = VGroup(
            *[
                self._make_term_card(value, sub, color)
                for value, sub, color in zip(values, subs, TERM_COLORS)
            ]
        ).arrange(RIGHT, buff=0.45)
        cards.move_to(UP * 0.6)

        ellipsis = MathTex(r"\dots", font_size=42, color=TEXT_SECONDARY)
        ellipsis.next_to(cards, RIGHT, buff=0.25).align_to(cards, UP)

        order_label = Text(
            "Each term has both a value and a position",
            font_size=24,
            color=ACCENT_TEAL,
        ).next_to(cards, DOWN, buff=0.55)

        self.play(
            LaggedStart(*[FadeIn(card, shift=UP * 0.25) for card in cards], lag_ratio=0.18),
            FadeIn(ellipsis, shift=LEFT * 0.15),
            run_time=1.7,
        )
        self.play(Write(order_label), run_time=0.8)
        self.wait(0.6)

        self.cards = cards
        self.ellipsis = ellipsis
        self.order_label = order_label

    def _show_order_matters(self):
        swapped = self.cards.copy()
        swapped[0], swapped[1] = swapped[1], swapped[0]
        swapped.arrange(RIGHT, buff=0.45)
        swapped.next_to(self.order_label, DOWN, buff=0.65)

        caption = Text(
            "Swap the order and you get a different sequence",
            font_size=22,
            color=ORDER_ALERT,
        ).next_to(swapped, DOWN, buff=0.28)
        cross = Cross(swapped, color=ORDER_ALERT, stroke_width=8)

        self.play(TransformFromCopy(self.cards, swapped), run_time=1.0)
        self.play(Create(cross), FadeIn(caption, shift=UP * 0.15), run_time=0.8)
        self.wait(0.55)
        self.play(FadeOut(swapped), FadeOut(cross), FadeOut(caption), run_time=0.5)

    def _transform_to_graph(self):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 16, 4],
            x_length=8.1,
            y_length=4.45,
            axis_config={
                "color": GREY_C,
                "include_tip": True,
                "tip_length": 0.16,
                "stroke_width": 1.8,
            },
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).shift(DOWN * 0.95)
        plane = NumberPlane(
            x_range=[0, 5, 1],
            y_range=[0, 16, 4],
            x_length=8.1,
            y_length=4.45,
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

        x_label = Text("position n", font_size=22, color=ACCENT_BLUE).next_to(axes.x_axis, DOWN, buff=0.28)
        y_label = Text("term value", font_size=22, color=Q1_COLOR).rotate(PI / 2).next_to(axes.y_axis, LEFT, buff=0.38)

        pairs = [(1, 3), (2, 7), (3, 11), (4, 15)]
        guides = VGroup()
        dots = VGroup()
        coord_labels = VGroup()
        for (x_val, y_val), color in zip(pairs, TERM_COLORS):
            point = axes.c2p(x_val, y_val)
            guide = DashedLine(axes.c2p(x_val, 0), point, color=color, dash_length=0.12, stroke_width=2.0)
            dot = Dot(point, radius=0.09, color=color)
            coord = MathTex(fr"({x_val}, {y_val})", font_size=24, color=color).next_to(point, UR, buff=0.12)
            guides.add(guide)
            dots.add(dot)
            coord_labels.add(coord)

        graph_note = Text(
            "A sequence is discrete: only the integer inputs matter",
            font_size=20,
            color=HIGHLIGHT,
        ).next_to(axes, DOWN, buff=0.16)

        self.play(
            FadeOut(self.ellipsis),
            FadeOut(self.order_label),
            self.cards.animate.scale(0.68).move_to(LEFT * 4.25 + UP * 1.88),
            run_time=0.8,
        )
        self.play(FadeIn(plane), Create(axes), Write(x_label), Write(y_label), run_time=1.4)

        card_targets = VGroup()
        for card, dot in zip(self.cards, dots):
            target = card.copy().scale(0.34).move_to(dot.get_center())
            card_targets.add(target)

        self.play(
            LaggedStart(
                *[
                    AnimationGroup(
                        TransformFromCopy(card, target),
                        Create(guide),
                        FadeIn(dot, scale=0.5),
                        FadeIn(coord, shift=UP * 0.12),
                    )
                    for card, target, guide, dot, coord in zip(self.cards, card_targets, guides, dots, coord_labels)
                ],
                lag_ratio=0.22,
            ),
            run_time=2.5,
        )
        self.play(Write(graph_note), run_time=0.75)
        self.wait(0.7)

        self.axes = axes
        self.plane = plane
        self.guides = guides
        self.dots = dots
        self.coord_labels = coord_labels
        self.graph_note = graph_note

    def _show_function_view(self):
        self.play(
            FadeOut(self.cards, shift=UP * 0.1),
            FadeOut(self.subtitle, shift=UP * 0.1),
            FadeOut(self.graph_note, shift=DOWN * 0.1),
            run_time=0.55,
        )

        statement = MathTex(
            r"\text{sequence} \;=\; \text{function on the positive integers}",
            font_size=28,
            color=TEXT_PRIMARY,
        )

        mapping = MathTex(
            r"n \mapsto a_n",
            font_size=36,
            color=ACCENT_TEAL,
        )

        explicit = MathTex(
            r"a_n = 4n - 1",
            font_size=32,
            color=HIGHLIGHT,
        )

        formula_group = VGroup(mapping, explicit).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        formula_group.next_to(self.title, DOWN, buff=0.34).to_edge(RIGHT, buff=0.9)

        formula_panel = RoundedRectangle(
            corner_radius=0.12,
            width=formula_group.width + 0.5,
            height=formula_group.height + 0.34,
            stroke_color=ACCENT_BLUE,
            stroke_width=2.2,
            fill_color="#12122a",
            fill_opacity=0.7,
        ).move_to(formula_group)

        statement_banner = RoundedRectangle(
            corner_radius=0.12,
            width=6.25,
            height=0.62,
            stroke_color=ACCENT_BLUE,
            stroke_width=2.0,
            fill_color="#12122a",
            fill_opacity=0.88,
        ).next_to(self.axes, DOWN, buff=0.18)
        statement.move_to(statement_banner)

        domain_highlight = SurroundingRectangle(
            VGroup(self.axes.x_axis, self.dots),
            color=ACCENT_BLUE,
            buff=0.18,
            stroke_width=2.3,
        )

        self.play(FadeIn(formula_panel), Write(mapping), run_time=0.8)
        self.play(Write(explicit), run_time=0.65)
        self.play(Create(domain_highlight), run_time=0.6)
        self.play(FadeIn(statement_banner), Write(statement), run_time=0.85)
        self.wait(1.6)
