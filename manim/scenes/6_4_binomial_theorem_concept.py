from manim import *
from itertools import combinations


class ChooseTwoYsFromSix(Scene):
    def make_factor_row(self, y_positions, scale_factor=1.0):
        """
        Build a row showing 6 factors of (x+y), with the chosen 'y' positions
        highlighted in yellow and all other positions shown as x.
        """
        cells = VGroup()
        for i in range(6):
            symbol = MathTex("y" if i in y_positions else "x")
            symbol.scale(1.0 * scale_factor)
            if i in y_positions:
                highlight = Circle(radius=0.34 * scale_factor)
                highlight.set_fill(YELLOW, opacity=0.45)
                highlight.set_stroke(YELLOW, width=0)
                symbol.set_color(BLACK)
                cell = VGroup(highlight, symbol)
            else:
                symbol.set_color(BLUE_D)
                cell = symbol
            cells.add(cell)

        row = VGroup()
        for cell in cells:
            left = MathTex("(").scale(1.15 * scale_factor)
            right = MathTex(")").scale(1.15 * scale_factor)
            group = VGroup(left, cell, right).arrange(RIGHT, buff=0.04 * scale_factor)
            row.add(group)

        row.arrange(RIGHT, buff=0.12 * scale_factor)
        return row

    def make_position_labels(self, scale_factor=1.0):
        labels = VGroup(*[
            Text(str(i + 1), font_size=int(22 * scale_factor)) for i in range(6)
        ])
        labels.arrange(RIGHT, buff=0.88 * scale_factor)
        return labels

    def construct(self):
        title = MathTex(r"\text{Choosing 2 } y\text{'s from 6 factors of } (x+y)")
        title.scale(0.9)
        title.to_edge(UP)

        subtitle = Text("Each arrangement is a choice of which 2 factors contribute y", font_size=30)
        subtitle.next_to(title, DOWN, buff=0.25)

        self.play(Write(title), FadeIn(subtitle, shift=DOWN))
        self.wait(0.8)

        # Intro: show generic 6-factor product with positions labeled
        generic_row = self.make_factor_row(set(), scale_factor=1.0)
        generic_row.set_color(BLUE_D)
        generic_row.move_to(ORIGIN + UP * 1.0)

        labels = VGroup(*[Text(str(i + 1), font_size=24) for i in range(6)])
        for label, group in zip(labels, generic_row):
            label.next_to(group, UP, buff=0.18)

        prompt = Text("Pick exactly 2 positions for y", font_size=32)
        prompt.next_to(generic_row, DOWN, buff=0.6)

        self.play(FadeIn(generic_row), FadeIn(labels), Write(prompt))
        self.wait(1.0)

        # Show one example becoming highlighted
        example_positions = {1, 4}
        example_row = self.make_factor_row(example_positions, scale_factor=1.0)
        example_row.move_to(generic_row)

        choose_text = MathTex(r"\text{Example: choose positions } 2 \text{ and } 5")
        choose_text.next_to(prompt, DOWN, buff=0.35)

        self.play(Transform(generic_row, example_row), Write(choose_text))
        self.wait(1.0)

        self.play(
            FadeOut(labels),
            FadeOut(prompt),
            FadeOut(choose_text),
            generic_row.animate.scale(0.9).to_edge(UP).shift(DOWN * 1.2),
        )

        # Build all 15 combinations in a 5x3 grid
        all_pairs = list(combinations(range(6), 2))
        rows = VGroup(*[self.make_factor_row(set(pair), scale_factor=0.62) for pair in all_pairs])
        rows.arrange_in_grid(rows=5, cols=3, buff=(0.35, 0.45))
        rows.move_to(ORIGIN + DOWN * 0.2)

        pair_labels = VGroup()
        for pair, row in zip(all_pairs, rows):
            lab = Text(f"({pair[0] + 1}, {pair[1] + 1})", font_size=20)
            lab.next_to(row, DOWN, buff=0.08)
            pair_labels.add(lab)

        grid_group = VGroup(rows, pair_labels)

        self.play(LaggedStart(*[FadeIn(row, scale=0.92) for row in rows], lag_ratio=0.06, run_time=2.8))
        self.play(LaggedStart(*[FadeIn(lab, shift=UP * 0.1) for lab in pair_labels], lag_ratio=0.04, run_time=1.6))
        self.wait(1.2)

        # Count them
        total_box = SurroundingRectangle(grid_group, color=WHITE, buff=0.2)
        total_text = MathTex(r"\binom{6}{2} = 15")
        total_text.scale(1.05)
        total_text.next_to(grid_group, DOWN, buff=0.45)

        explanation = VGroup(
            MathTex(r"\text{Choose which 2 of the 6 factors contribute } y"),
            MathTex(r"\text{The other 4 factors contribute } x"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        explanation.scale(0.72)
        explanation.next_to(total_text, DOWN, buff=0.25)

        self.play(Create(total_box), Write(total_text))
        self.play(FadeIn(explanation, shift=UP * 0.15))
        self.wait(2)

        # Final emphasis on one resulting term
        final_statement = MathTex(r"\text{So the coefficient of } x^4y^2 \text{ in } (x+y)^6 \text{ is } 15")
        final_statement.scale(0.85)
        final_statement.to_edge(DOWN)
        self.play(Write(final_statement))
        self.wait(2)
