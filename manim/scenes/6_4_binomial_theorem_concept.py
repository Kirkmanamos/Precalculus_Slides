"""
Unit 6.4 — The Binomial Theorem: why the coefficient counts choices.

Walks the viewer from the multiplication itself to the combination count.
The goal is that a student who has never seen Pascal's Triangle ends up
understanding that the coefficient of x^4 y^2 in (x+y)^6 *is literally*
the number of ways to pick which 2 of the 6 factors contribute y.

Render (from the manim/ directory):
    ../.venv/bin/python -m manim -pql scenes/6_4_binomial_theorem_concept.py CountingY2TermsInBinomial
    ../.venv/bin/python -m manim -pqh scenes/6_4_binomial_theorem_concept.py CountingY2TermsInBinomial
"""

from manim import *
from itertools import combinations
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *


X_COLOR = ACCENT_BLUE
Y_COLOR = HIGHLIGHT


def make_factor(choice=None, scale=1.0):
    """
    One (x+y) factor. `choice` in {None, 'x', 'y'} controls which letter is
    emphasized. None = neutral (both shown, same weight).
    """
    left = MathTex("(").scale(1.1 * scale)
    x = MathTex("x").scale(1.0 * scale)
    plus = MathTex("+").scale(1.0 * scale)
    y = MathTex("y").scale(1.0 * scale)
    right = MathTex(")").scale(1.1 * scale)

    if choice == "x":
        x.set_color(X_COLOR)
        y.set_opacity(0.25)
        plus.set_opacity(0.35)
    elif choice == "y":
        y.set_color(Y_COLOR)
        x.set_opacity(0.25)
        plus.set_opacity(0.35)

    inner = VGroup(x, plus, y).arrange(RIGHT, buff=0.06 * scale)
    factor = VGroup(left, inner, right).arrange(RIGHT, buff=0.04 * scale)
    factor.choice = choice
    factor.x_sym = x
    factor.y_sym = y
    return factor


def make_factor_row(choices, scale=1.0, buff=0.14):
    """choices: list of six entries, each None / 'x' / 'y'."""
    row = VGroup(*[make_factor(c, scale=scale) for c in choices])
    row.arrange(RIGHT, buff=buff * scale)
    return row


def make_chosen_row(y_positions, scale=1.0, buff=0.14):
    """For the grid at the end: six factors with chosen 'y' positions highlighted."""
    choices = ["y" if i in y_positions else "x" for i in range(6)]
    return make_factor_row(choices, scale=scale, buff=buff)


class CountingY2TermsInBinomial(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        self._act_setup()
        self._act_first_path()
        self._act_second_path()
        self._act_question()
        self._act_count_pairs()
        self._act_show_all_fifteen()
        self._act_conclude()

    # ---------- Act 1: six factors, six choices ----------
    def _act_setup(self):
        title = Text("Where do coefficients come from?",
                     font=FONT_DISPLAY, color=TEXT_COLOR, weight=BOLD)
        title.scale(0.85).to_edge(UP, buff=0.5)

        compact = MathTex("(x+y)^6", color=TEXT_COLOR).scale(1.4)
        compact.next_to(title, DOWN, buff=0.55)

        self.play(Write(title))
        self.play(FadeIn(compact, shift=DOWN * 0.2))
        self.wait(0.6)

        equals = MathTex("=", color=TEXT_COLOR).scale(1.2)
        neutral_row = make_factor_row([None] * 6, scale=0.8, buff=0.1)
        expanded = VGroup(compact.copy(), equals, neutral_row).arrange(RIGHT, buff=0.3)
        expanded.move_to(compact).shift(DOWN * 0.1)

        self.play(
            Transform(compact, expanded[0]),
            FadeIn(equals, shift=RIGHT * 0.2),
            FadeIn(neutral_row, shift=RIGHT * 0.3),
        )
        self.wait(0.5)

        caption = Text("6 factors. Each one: choose x or y.",
                       font=FONT_BODY, color=TEXT_MUTED)
        caption.scale(0.6).next_to(neutral_row, DOWN, buff=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1))
        self.wait(1.4)

        self._title = title
        self._compact = compact
        self._equals = equals
        self._neutral_row = neutral_row
        self._caption = caption

    # ---------- Act 2: one multiplication path ----------
    def _act_first_path(self):
        self.play(FadeOut(self._caption))

        pattern_a = ["x", "x", "y", "x", "y", "x"]
        chosen_a = make_factor_row(pattern_a, scale=0.8, buff=0.1)
        chosen_a.move_to(self._neutral_row)

        prompt = Text("One way to multiply: pick one letter from each factor.",
                      font=FONT_BODY, color=TEXT_MUTED)
        prompt.scale(0.6).next_to(chosen_a, DOWN, buff=0.55)

        self.play(FadeIn(prompt, shift=UP * 0.1))
        self.play(Transform(self._neutral_row, chosen_a), run_time=1.4)
        self.wait(0.6)

        product_syms = VGroup(*[MathTex(c, color=(X_COLOR if c == "x" else Y_COLOR))
                                .scale(1.1) for c in pattern_a])
        dots = [MathTex(r"\cdot", color=TEXT_MUTED).scale(0.9) for _ in range(5)]
        product = VGroup(product_syms[0])
        for d, s in zip(dots, product_syms[1:]):
            product.add(d, s)
        product.arrange(RIGHT, buff=0.12).next_to(prompt, DOWN, buff=0.55)

        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.1) for m in product],
                              lag_ratio=0.08, run_time=1.4))
        self.wait(0.5)

        combined = MathTex("x^4", "y^2").next_to(product, DOWN, buff=0.45).scale(1.3)
        combined[0].set_color(X_COLOR)
        combined[1].set_color(Y_COLOR)

        arrow = MathTex(r"\Rightarrow", color=TEXT_COLOR).scale(1.0)
        arrow.next_to(product, DOWN, buff=0.2)
        self.play(FadeIn(arrow), FadeIn(combined, shift=DOWN * 0.1))
        self.wait(1.3)

        self._path_a_group = VGroup(prompt, product, arrow, combined)
        self._current_row = self._neutral_row  # transformed in place

    # ---------- Act 3: same term, different story ----------
    def _act_second_path(self):
        reset_caption = Text("Same term, different choices.",
                             font=FONT_BODY, color=TEXT_MUTED).scale(0.6)
        reset_caption.move_to(self._path_a_group[0])

        self.play(
            FadeOut(self._path_a_group[1]),
            FadeOut(self._path_a_group[2]),
            FadeOut(self._path_a_group[3]),
            Transform(self._path_a_group[0], reset_caption),
        )

        pattern_b = ["y", "x", "x", "x", "x", "y"]
        chosen_b = make_factor_row(pattern_b, scale=0.8, buff=0.1)
        chosen_b.move_to(self._current_row)

        self.play(Transform(self._current_row, chosen_b), run_time=1.2)
        self.wait(0.4)

        product_syms = VGroup(*[MathTex(c, color=(X_COLOR if c == "x" else Y_COLOR))
                                .scale(1.1) for c in pattern_b])
        dots = [MathTex(r"\cdot", color=TEXT_MUTED).scale(0.9) for _ in range(5)]
        product = VGroup(product_syms[0])
        for d, s in zip(dots, product_syms[1:]):
            product.add(d, s)
        product.arrange(RIGHT, buff=0.12).next_to(self._path_a_group[0], DOWN, buff=0.55)

        combined = MathTex("x^4", "y^2").scale(1.3)
        combined[0].set_color(X_COLOR)
        combined[1].set_color(Y_COLOR)
        arrow = MathTex(r"\Rightarrow", color=TEXT_COLOR).scale(1.0)
        arrow.next_to(product, DOWN, buff=0.2)
        combined.next_to(arrow, DOWN, buff=0.2)

        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.1) for m in product],
                              lag_ratio=0.06, run_time=1.0))
        self.play(FadeIn(arrow), FadeIn(combined, shift=DOWN * 0.1))
        self.wait(1.6)

        self._second_group = VGroup(product, arrow, combined)
        self._reset_caption = self._path_a_group[0]

    # ---------- Act 4: pose the question ----------
    def _act_question(self):
        self.play(
            FadeOut(self._second_group),
            FadeOut(self._reset_caption),
        )

        question = Text(
            "How many of these pre-combined terms equal x^4 y^2 ?",
            font=FONT_BODY, color=TEXT_COLOR,
        ).scale(0.65)
        question.next_to(self._current_row, DOWN, buff=0.55)

        sub = Text(
            "= how many ways to pick which 2 factors give y",
            font=FONT_BODY, color=ACCENT_TEAL,
        ).scale(0.55)
        sub.next_to(question, DOWN, buff=0.2)

        self.play(Write(question))
        self.wait(0.5)
        self.play(FadeIn(sub, shift=UP * 0.1))
        self.wait(1.4)

        self._question = question
        self._sub = sub

    # ---------- Act 5: clear for the grid ----------
    def _act_count_pairs(self):
        self.play(
            FadeOut(self._question),
            FadeOut(self._sub),
            FadeOut(self._current_row),
            FadeOut(self._equals),
            self._compact.animate.scale(0.8).to_corner(UL, buff=0.6),
            self._title.animate.set_opacity(0.0),
        )

    # ---------- Act 6: show all 15 arrangements ----------
    def _act_show_all_fifteen(self):
        pairs = list(combinations(range(6), 2))
        rows = VGroup(*[make_chosen_row(set(p), scale=0.46, buff=0.08) for p in pairs])
        rows.arrange_in_grid(rows=5, cols=3, buff=(0.45, 0.35))
        rows.move_to(ORIGIN).shift(DOWN * 0.2)

        labels = VGroup()
        for p, r in zip(pairs, rows):
            lab = Text(f"y in {p[0]+1}, {p[1]+1}",
                       font=FONT_BODY, color=TEXT_MUTED).scale(0.32)
            lab.next_to(r, DOWN, buff=0.1)
            labels.add(lab)

        header = Text("Every arrangement of two y's among six factors:",
                      font=FONT_BODY, color=TEXT_COLOR).scale(0.55)
        header.to_edge(UP, buff=0.6)

        self.play(FadeIn(header, shift=DOWN * 0.1))
        self.play(LaggedStart(*[FadeIn(r, scale=0.92) for r in rows],
                              lag_ratio=0.08, run_time=2.6))
        self.play(LaggedStart(*[FadeIn(l) for l in labels],
                              lag_ratio=0.04, run_time=1.2))
        self.wait(0.6)

        counter = MathTex(r"\text{count} = ", "15", color=TEXT_COLOR).scale(0.9)
        counter[1].set_color(HIGHLIGHT)
        counter.to_edge(DOWN, buff=0.6)
        self.play(Write(counter))
        self.wait(1.2)

        self._grid = VGroup(rows, labels)
        self._grid_header = header
        self._counter = counter

    # ---------- Act 7: land the binomial coefficient ----------
    def _act_conclude(self):
        self.play(
            FadeOut(self._grid),
            FadeOut(self._grid_header),
            FadeOut(self._compact),
            self._counter.animate.move_to(UP * 1.8).scale(1.0),
        )

        identity = MathTex(
            r"\binom{6}{2}", "=", "15",
            color=TEXT_COLOR,
        ).scale(1.6)
        identity[0].set_color(ACCENT_TEAL)
        identity[2].set_color(HIGHLIGHT)
        identity.move_to(ORIGIN + UP * 0.3)

        gloss = Text(
            '"choose which 2 of the 6 factors contribute y"',
            font=FONT_BODY, color=TEXT_MUTED,
        ).scale(0.55)
        gloss.next_to(identity, DOWN, buff=0.45)

        self.play(FadeOut(self._counter), Write(identity))
        self.play(FadeIn(gloss, shift=UP * 0.1))
        self.wait(1.0)

        coef_line = MathTex(
            r"\text{coefficient of }", "x^4 y^2", r"\text{ in }", "(x+y)^6", r" = ", r"\binom{6}{2}", r" = ", "15",
            color=TEXT_COLOR,
        ).scale(0.85)
        coef_line[1].set_color(TEXT_COLOR)
        coef_line[1][0:2].set_color(X_COLOR)
        coef_line[1][2:].set_color(Y_COLOR)
        coef_line[5].set_color(ACCENT_TEAL)
        coef_line[7].set_color(HIGHLIGHT)
        coef_line.next_to(gloss, DOWN, buff=0.7)

        self.play(Write(coef_line))
        self.wait(2.5)
