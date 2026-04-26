"""
5.4-ish concept video: amplitude-phase form.

Why a sin(x) + b cos(x) can be written as one shifted sine wave:

    a sin(x) + b cos(x) = R sin(x + theta)

where R = sqrt(a^2 + b^2), R cos(theta) = a, and R sin(theta) = b.

Render from the manim/ directory:
    ../.venv/bin/python -m manim -pql scenes/5_4_amplitude_phase_form.py AmplitudePhaseForm
    ../.venv/bin/python -m manim -pqh scenes/5_4_amplitude_phase_form.py AmplitudePhaseForm
"""

from manim import *
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *


# Consistent role colors for the entire animation.
SCENE_BG = BG_COLOR
PANEL_BG = "#0b1825"
PANEL_STROKE = "#25445f"
SINE_COLOR = ACCENT_BLUE
COS_COLOR = Q3_COLOR
R_COLOR = Q1_COLOR
THETA_COLOR = Q4_COLOR
GUIDE_COLOR = HIGHLIGHT
FINAL_SUMMARY_HOLD = 7.0


class AmplitudePhaseForm(Scene):
    """One polished classroom scene with helper methods for tweakability."""

    def construct(self):
        self.camera.background_color = SCENE_BG

        self._opening_title()
        self._concrete_example()
        self._graph_intuition()
        self._general_algebra()
        self._geometric_interpretation()
        self._find_phase_angle()
        self._return_to_example()
        self._final_summary()

    # ---------------------------------------------------------------------
    # Shared helpers
    # ---------------------------------------------------------------------
    def _clear_scene(self, run_time=0.75):
        """Fade out everything currently on screen."""
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=run_time)

    def _fit(self, mob, max_width=12.4):
        """Keep long equations readable without running off-screen."""
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def _soft_card(self, mob, stroke_color=PANEL_STROKE, buff=0.22):
        """A subdued dark card used for important equations."""
        box = SurroundingRectangle(
            mob,
            color=stroke_color,
            stroke_width=1.7,
            fill_color=PANEL_BG,
            fill_opacity=0.88,
            buff=buff,
            corner_radius=0.08,
        )
        box.set_z_index(mob.z_index - 1)
        return VGroup(box, mob)

    def _color_by_roles(self, mob):
        """Apply the four recurring colors to any MathTex object."""
        mob.set_color_by_tex(r"\sin", SINE_COLOR)
        mob.set_color_by_tex(r"\cos", COS_COLOR)
        mob.set_color_by_tex("R", R_COLOR)
        mob.set_color_by_tex(r"\theta", THETA_COLOR)
        return mob

    def _example_original(self, font_size=50):
        eq = MathTex(
            r"\sqrt{3}", r"\sin x", r"-", r"\cos x",
            font_size=font_size,
            color=TEXT_COLOR,
        )
        eq[0].set_color(SINE_COLOR)
        eq[1].set_color(SINE_COLOR)
        eq[3].set_color(COS_COLOR)
        return eq

    def _example_target(self, font_size=50):
        eq = MathTex(
            r"2", r"\sin", r"\left(x", r"-", r"\frac{\pi}{6}", r"\right)",
            font_size=font_size,
            color=TEXT_COLOR,
        )
        eq[0].set_color(R_COLOR)
        eq[1].set_color(SINE_COLOR)
        eq[3].set_color(THETA_COLOR)
        eq[4].set_color(THETA_COLOR)
        return eq

    def _general_original(self, font_size=46):
        eq = MathTex(
            "a", r"\sin x", "+", "b", r"\cos x",
            font_size=font_size,
            color=TEXT_COLOR,
        )
        eq[0].set_color(SINE_COLOR)
        eq[1].set_color(SINE_COLOR)
        eq[3].set_color(COS_COLOR)
        eq[4].set_color(COS_COLOR)
        return eq

    def _general_target(self, font_size=46):
        eq = MathTex(
            "R", r"\sin", r"\left(x+", r"\theta", r"\right)",
            font_size=font_size,
            color=TEXT_COLOR,
        )
        eq[0].set_color(R_COLOR)
        eq[1].set_color(SINE_COLOR)
        eq[3].set_color(THETA_COLOR)
        return eq

    def _line_label(self, tex, color, font_size=26):
        label = MathTex(tex, font_size=font_size, color=color)
        label.add_background_rectangle(color=SCENE_BG, opacity=0.72, buff=0.08)
        return label

    def _angle_arc(self, axes, angle, radius=0.5, label_tex=r"\theta", color=THETA_COLOR):
        """Create an angle arc centered at the coordinate-plane origin."""
        origin = np.array(axes.c2p(0, 0))
        unit = np.linalg.norm(np.array(axes.c2p(1, 0)) - origin)
        screen_radius = radius * unit

        arc = Arc(
            radius=screen_radius,
            start_angle=0,
            angle=angle,
            arc_center=origin,
            color=color,
            stroke_width=4,
        )
        mid_angle = angle / 2
        label = MathTex(label_tex, font_size=28, color=color)
        label.move_to(
            origin
            + (screen_radius + 0.25)
            * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
        )
        return VGroup(arc, label)

    def _right_angle_marker(self, axes, x_val, y_val, size=0.18):
        """Small square marker at the corner of the reference triangle."""
        x_sign = 1 if x_val >= 0 else -1
        y_sign = 1 if y_val >= 0 else -1
        p0 = axes.c2p(x_val - size * x_sign, 0)
        p1 = axes.c2p(x_val - size * x_sign, size * y_sign)
        p2 = axes.c2p(x_val, size * y_sign)
        return VGroup(
            Line(p0, p1, color=TEXT_MUTED, stroke_width=1.8),
            Line(p1, p2, color=TEXT_MUTED, stroke_width=1.8),
        )

    def _place_segment_label(self, label, start, end, distance=0.24):
        """Place a label near the midpoint of a segment, offset normally."""
        start = np.array(start)
        end = np.array(end)
        direction = end - start
        normal = np.array([-direction[1], direction[0], 0])
        norm = np.linalg.norm(normal)
        if norm == 0:
            normal = UP
        else:
            normal = normal / norm
        label.move_to((start + end) / 2 + distance * normal)
        return label

    # ---------------------------------------------------------------------
    # 1. Opening title
    # ---------------------------------------------------------------------
    def _opening_title(self):
        title = MathTex(
            r"\text{Why does }",
            r"a\sin(x)",
            r"+",
            r"b\cos(x)",
            r"\text{ become one sine wave?}",
            font_size=42,
            color=TEXT_COLOR,
        )
        title[1].set_color(SINE_COLOR)
        title[3].set_color(COS_COLOR)
        self._fit(title, 12.6)

        subtitle = MathTex(
            r"\text{Amplitude--phase form}",
            font_size=30,
            color=TEXT_MUTED,
        ).next_to(title, DOWN, buff=0.34)

        formula = MathTex(
            "a", r"\sin x", "+", "b", r"\cos x", "=",
            "R", r"\sin", r"\left(x+", r"\theta", r"\right)",
            font_size=38,
            color=TEXT_COLOR,
        )
        formula[0].set_color(SINE_COLOR)
        formula[1].set_color(SINE_COLOR)
        formula[3].set_color(COS_COLOR)
        formula[4].set_color(COS_COLOR)
        formula[6].set_color(R_COLOR)
        formula[7].set_color(SINE_COLOR)
        formula[9].set_color(THETA_COLOR)
        formula.next_to(subtitle, DOWN, buff=0.65)

        self.play(Write(title), run_time=1.15)
        self.play(FadeIn(subtitle, shift=DOWN * 0.15), run_time=0.75)
        self.play(Write(formula), run_time=1.1)
        self.wait(1.2)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 2. Concrete example
    # ---------------------------------------------------------------------
    def _concrete_example(self):
        header = MathTex(
            r"\text{Start with one exact example}",
            font_size=34,
            color=TEXT_MUTED,
        ).to_edge(UP, buff=0.48)

        original = self._example_original(font_size=58)
        target = self._example_target(font_size=58)
        arrow = MathTex(r"\Longrightarrow", font_size=48, color=TEXT_MUTED)

        row = VGroup(original, arrow, target).arrange(RIGHT, buff=0.48)
        row.move_to(UP * 0.62)
        self._fit(row, 12.2)

        question = MathTex(
            r"\text{Why are these the same?}",
            font_size=40,
            color=GUIDE_COLOR,
        ).next_to(row, DOWN, buff=0.72)

        original_card = self._soft_card(original, stroke_color=SINE_COLOR)
        target_card = self._soft_card(target, stroke_color=R_COLOR)

        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(original_card, shift=UP * 0.2), run_time=0.85)
        self.wait(0.35)
        self.play(Write(arrow), run_time=0.45)
        self.play(FadeIn(target_card, shift=UP * 0.2), run_time=0.85)
        self.play(Write(question), run_time=0.75)
        self.wait(1.25)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 3. Graph intuition
    # ---------------------------------------------------------------------
    def _graph_intuition(self):
        title = MathTex(
            r"\text{Graph first: do the waves actually match?}",
            font_size=34,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.34)

        axes = Axes(
            x_range=[-PI, 2 * PI, PI / 2],
            y_range=[-2.6, 2.6, 1],
            x_length=10.6,
            y_length=4.75,
            axis_config={
                "color": AXIS_COLOR,
                "include_tip": True,
                "tip_length": 0.14,
                "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-2, -1, 1, 2],
                "font_size": 20,
                "decimal_number_config": {"num_decimal_places": 0},
            },
        ).move_to(DOWN * 0.45)

        x_ticks = [-PI, 0, PI, 2 * PI]
        x_labels_tex = [r"-\pi", r"0", r"\pi", r"2\pi"]
        x_labels = VGroup(
            *[
                MathTex(tex, font_size=22, color=TICK_COLOR).next_to(
                    axes.c2p(value, 0), DOWN, buff=0.18
                )
                for value, tex in zip(x_ticks, x_labels_tex)
            ]
        )
        axis_labels = VGroup(
            MathTex(r"x", font_size=24, color=AXIS_COLOR).next_to(
                axes.x_axis.get_right(), RIGHT, buff=0.08
            ),
            MathTex(r"y", font_size=24, color=AXIS_COLOR).next_to(
                axes.y_axis.get_top(), UP, buff=0.08
            ),
        )

        def f(x):
            return np.sqrt(3) * np.sin(x) - np.cos(x)

        original_curve = axes.plot(
            f,
            x_range=[-PI, 2 * PI],
            color=SINE_COLOR,
            stroke_width=6,
            use_smoothing=True,
        )
        original_curve.set_stroke(opacity=0.78)
        original_curve.set_fill(opacity=0)

        target_curve = axes.plot(
            lambda x: 2 * np.sin(x - PI / 6),
            x_range=[-PI, 2 * PI],
            color=R_COLOR,
            stroke_width=3.3,
            use_smoothing=True,
        )
        target_curve.set_fill(opacity=0)

        original_label = self._example_original(font_size=28)
        original_label.next_to(axes, UP, buff=0.12).to_edge(LEFT, buff=0.78)
        target_label = self._example_target(font_size=28)
        equals_label = MathTex(r"=", font_size=28, color=TEXT_MUTED)
        overlay_label = VGroup(original_label, equals_label, target_label).arrange(
            RIGHT, buff=0.18
        )
        overlay_label.next_to(title, DOWN, buff=0.22)

        # A small wave cue: cosine is sine shifted left by pi/2.
        cue_axes = Axes(
            x_range=[0, 2 * PI, PI],
            y_range=[-1.25, 1.25, 1],
            x_length=2.55,
            y_length=1.1,
            axis_config={"stroke_opacity": 0, "include_tip": False},
        )
        cue_sin = cue_axes.plot(
            lambda t: np.sin(t),
            x_range=[0, 2 * PI],
            color=SINE_COLOR,
            stroke_width=2,
        )
        cue_cos = cue_axes.plot(
            lambda t: np.cos(t),
            x_range=[0, 2 * PI],
            color=COS_COLOR,
            stroke_width=2,
        )
        shift_arrow = Arrow(
            cue_axes.c2p(PI / 2, 1.08),
            cue_axes.c2p(0.08, 1.08),
            buff=0,
            color=THETA_COLOR,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.18,
        )
        shift_label = MathTex(
            r"\frac{\pi}{2}\text{ shift}",
            font_size=18,
            color=THETA_COLOR,
        ).next_to(shift_arrow, UP, buff=0.04)
        cue_eq = MathTex(
            r"\cos x", r"=", r"\sin", r"\left(x+\frac{\pi}{2}\right)",
            font_size=24,
            color=TEXT_COLOR,
        )
        cue_eq[0].set_color(COS_COLOR)
        cue_eq[2].set_color(SINE_COLOR)
        cue_eq[3].set_color(THETA_COLOR)
        cue_eq.next_to(cue_axes, DOWN, buff=0.05)
        cue = VGroup(cue_axes, cue_sin, cue_cos, shift_arrow, shift_label, cue_eq)
        cue.to_corner(UR, buff=0.42)

        self.play(Write(title), run_time=0.75)
        self.play(Create(axes), FadeIn(x_labels), FadeIn(axis_labels), run_time=1.0)
        self.play(Create(original_curve), FadeIn(original_label), run_time=1.25)
        self.wait(0.35)
        self.play(Create(target_curve), FadeIn(target_label), Write(equals_label), run_time=1.25)
        self.play(FadeIn(cue, shift=LEFT * 0.12), run_time=0.9)
        self.wait(0.65)

        # Moving guide line: the same x-value lands on the same y-value.
        x_tracker = ValueTracker(-0.55)

        guide = always_redraw(
            lambda: DashedLine(
                axes.c2p(x_tracker.get_value(), 0),
                axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
                dash_length=0.09,
                color=GUIDE_COLOR,
                stroke_width=2.2,
            )
        )
        outer_dot = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
                radius=0.105,
                color=SINE_COLOR,
            )
        )
        inner_dot = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
                radius=0.055,
                color=R_COLOR,
            )
        )
        same_y_label = MathTex(
            r"\text{same } y",
            font_size=22,
            color=GUIDE_COLOR,
        )
        same_y_label.add_updater(
            lambda mob: mob.next_to(
                axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
                UP if f(x_tracker.get_value()) >= 0 else DOWN,
                buff=0.16,
            )
        )

        self.play(FadeIn(guide), FadeIn(outer_dot), FadeIn(inner_dot), FadeIn(same_y_label), run_time=0.45)
        self.play(x_tracker.animate.set_value(2.7), run_time=3.0, rate_func=smooth)
        self.wait(0.9)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 4. General algebra setup and coefficient matching
    # ---------------------------------------------------------------------
    def _general_algebra(self):
        title = MathTex(
            r"\text{Now match the algebra}",
            font_size=34,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.36)

        original = self._general_original(font_size=44)
        target = self._general_target(font_size=44)
        arrow = MathTex(r"\stackrel{?}{=}", font_size=38, color=TEXT_MUTED)
        setup = VGroup(original, arrow, target).arrange(RIGHT, buff=0.36)
        setup.next_to(title, DOWN, buff=0.38)

        identity = MathTex(
            r"\sin(x+\theta)", "=",
            r"\sin x", r"\cos", r"\theta", "+",
            r"\cos x", r"\sin", r"\theta",
            font_size=34,
            color=TEXT_COLOR,
        )
        identity[0].set_color(SINE_COLOR)
        identity[2].set_color(SINE_COLOR)
        identity[3].set_color(COS_COLOR)
        identity[4].set_color(THETA_COLOR)
        identity[6].set_color(COS_COLOR)
        identity[7].set_color(SINE_COLOR)
        identity[8].set_color(THETA_COLOR)
        identity.next_to(setup, DOWN, buff=0.48)

        expanded = MathTex(
            r"R", r"\sin(x+\theta)", "=",
            r"R\cos\theta", r"\sin x", "+",
            r"R\sin\theta", r"\cos x",
            font_size=34,
            color=TEXT_COLOR,
        )
        self._color_by_roles(expanded)
        expanded.next_to(identity, DOWN, buff=0.48)

        match_a = MathTex(
            r"R\cos\theta", r"\longleftrightarrow", "a",
            font_size=36,
            color=TEXT_COLOR,
        )
        self._color_by_roles(match_a)
        match_a[2].set_color(SINE_COLOR)

        match_b = MathTex(
            r"R\sin\theta", r"\longleftrightarrow", "b",
            font_size=36,
            color=TEXT_COLOR,
        )
        self._color_by_roles(match_b)
        match_b[2].set_color(COS_COLOR)

        matches = VGroup(match_a, match_b).arrange(RIGHT, buff=1.0)
        matches.next_to(expanded, DOWN, buff=0.68)

        box_a = SurroundingRectangle(expanded[3], color=SINE_COLOR, buff=0.11, stroke_width=2.4)
        box_b = SurroundingRectangle(expanded[6], color=COS_COLOR, buff=0.11, stroke_width=2.4)
        original_a_box = SurroundingRectangle(original[0], color=SINE_COLOR, buff=0.10, stroke_width=2.4)
        original_b_box = SurroundingRectangle(original[3], color=COS_COLOR, buff=0.10, stroke_width=2.4)

        aha = MathTex(
            r"\text{Choose } R \text{ and } \theta \text{ so these coefficients match.}",
            font_size=28,
            color=GUIDE_COLOR,
        )
        self._color_by_roles(aha)
        aha.next_to(matches, DOWN, buff=0.42)

        self.play(Write(title), run_time=0.65)
        self.play(FadeIn(original, shift=UP * 0.15), run_time=0.55)
        self.play(Write(arrow), FadeIn(target, shift=UP * 0.15), run_time=0.8)
        self.wait(0.35)
        self.play(Write(identity), run_time=1.25)
        self.wait(0.35)
        self.play(Write(expanded), run_time=1.2)
        self.play(Create(box_a), Create(box_b), Create(original_a_box), Create(original_b_box), run_time=0.65)
        self.play(FadeIn(matches, shift=UP * 0.15), run_time=0.8)
        self.play(Write(aha), run_time=0.8)
        self.wait(1.25)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 5. Geometric interpretation
    # ---------------------------------------------------------------------
    def _geometric_interpretation(self):
        title = MathTex(
            r"\text{Geometry: } (a,b) \text{ is one vector}",
            font_size=34,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.36)
        title.set_color_by_tex("a", SINE_COLOR)
        title.set_color_by_tex("b", COS_COLOR)

        plane = NumberPlane(
            x_range=[-0.6, 3.7, 1],
            y_range=[-0.6, 2.8, 1],
            x_length=5.65,
            y_length=4.45,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.42,
            },
            faded_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 0.7,
                "stroke_opacity": 0.22,
            },
            axis_config={
                "color": AXIS_COLOR,
                "stroke_width": 1.8,
                "include_tip": True,
                "tip_length": 0.13,
            },
        ).to_edge(LEFT, buff=0.72).shift(DOWN * 0.32)

        a_val = 2.6
        b_val = 1.65
        origin = plane.c2p(0, 0)
        point = plane.c2p(a_val, b_val)
        foot = plane.c2p(a_val, 0)
        theta = np.arctan2(b_val, a_val)

        x_leg = Line(origin, foot, color=SINE_COLOR, stroke_width=4.2)
        y_leg = Line(foot, point, color=COS_COLOR, stroke_width=4.2)
        vector = Arrow(
            origin,
            point,
            buff=0,
            color=R_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        endpoint = Dot(point, radius=0.075, color=R_COLOR)
        right_angle = self._right_angle_marker(plane, a_val, b_val)
        angle = self._angle_arc(plane, theta, radius=0.46, label_tex=r"\theta")

        a_label = MathTex("a", font_size=30, color=SINE_COLOR).next_to(x_leg, DOWN, buff=0.16)
        b_label = MathTex("b", font_size=30, color=COS_COLOR).next_to(y_leg, RIGHT, buff=0.14)
        r_label = MathTex("R", font_size=32, color=R_COLOR)
        self._place_segment_label(r_label, origin, point, distance=0.34)
        point_label = MathTex(r"(a,b)", font_size=28, color=TEXT_COLOR).next_to(point, UR, buff=0.13)
        point_label.set_color_by_tex("a", SINE_COLOR)
        point_label.set_color_by_tex("b", COS_COLOR)

        diagram = VGroup(
            plane, x_leg, y_leg, vector, endpoint, right_angle,
            angle, a_label, b_label, r_label, point_label,
        )

        length_eq = MathTex(
            "R", "=", r"\sqrt{", "a", "^2", "+", "b", "^2", "}",
            font_size=36,
            color=TEXT_COLOR,
        )
        length_eq[0].set_color(R_COLOR)
        length_eq[3].set_color(SINE_COLOR)
        length_eq[6].set_color(COS_COLOR)

        x_component = MathTex(
            "a", "=", "R", r"\cos\theta",
            font_size=36,
            color=TEXT_COLOR,
        )
        x_component[0].set_color(SINE_COLOR)
        self._color_by_roles(x_component)
        x_component[0].set_color(SINE_COLOR)

        y_component = MathTex(
            "b", "=", "R", r"\sin\theta",
            font_size=36,
            color=TEXT_COLOR,
        )
        y_component[0].set_color(COS_COLOR)
        self._color_by_roles(y_component)
        y_component[0].set_color(COS_COLOR)

        angle_rule = MathTex(
            r"(\cos\theta,\sin\theta)", "=",
            r"\left(\frac{a}{R},\frac{b}{R}\right)",
            font_size=32,
            color=TEXT_COLOR,
        )
        angle_rule[0].set_color(THETA_COLOR)

        polar_note = MathTex(
            r"\text{This is rectangular-to-polar thinking.}",
            font_size=28,
            color=GUIDE_COLOR,
        )

        equations = VGroup(length_eq, x_component, y_component, angle_rule, polar_note).arrange(
            DOWN, aligned_edge=LEFT, buff=0.32
        )
        equations.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.08)
        equations_card = self._soft_card(equations, stroke_color=R_COLOR, buff=0.3)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(plane), run_time=0.75)
        self.play(Create(x_leg), FadeIn(a_label), run_time=0.55)
        self.play(Create(y_leg), FadeIn(b_label), Create(right_angle), run_time=0.55)
        self.play(GrowArrow(vector), FadeIn(endpoint), FadeIn(r_label), FadeIn(point_label), run_time=0.85)
        self.play(Create(angle), run_time=0.65)
        self.wait(0.35)
        self.play(FadeIn(equations_card, shift=LEFT * 0.18), run_time=0.85)
        self.play(Indicate(length_eq[0], color=R_COLOR), Indicate(vector, color=R_COLOR), run_time=0.9)
        self.play(Indicate(x_component, color=SINE_COLOR), Indicate(x_leg, color=SINE_COLOR), run_time=0.8)
        self.play(Indicate(y_component, color=COS_COLOR), Indicate(y_leg, color=COS_COLOR), run_time=0.8)
        self.play(Indicate(angle_rule, color=THETA_COLOR), Indicate(angle, color=THETA_COLOR), run_time=0.9)
        self.wait(1.25)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 6. Find the phase angle without guessing
    # ---------------------------------------------------------------------
    def _find_phase_angle(self):
        title = MathTex(
            r"\text{How do we find the phase angle?}",
            font_size=34,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.36)

        plane = NumberPlane(
            x_range=[-0.35, 2.35, 1],
            y_range=[-1.45, 0.75, 1],
            x_length=5.45,
            y_length=3.65,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.42,
            },
            faded_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 0.7,
                "stroke_opacity": 0.22,
            },
            axis_config={
                "color": AXIS_COLOR,
                "stroke_width": 1.8,
                "include_tip": True,
                "tip_length": 0.13,
            },
        ).to_edge(LEFT, buff=0.78).shift(DOWN * 0.38)

        a_val = np.sqrt(3)
        b_val = -1
        origin = plane.c2p(0, 0)
        point = plane.c2p(a_val, b_val)
        foot = plane.c2p(a_val, 0)

        x_leg = Line(origin, foot, color=SINE_COLOR, stroke_width=4.2)
        y_leg = Line(foot, point, color=COS_COLOR, stroke_width=4.2)
        vector = Arrow(
            origin,
            point,
            buff=0,
            color=R_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        right_angle = self._right_angle_marker(plane, a_val, b_val)
        theta_arc = self._angle_arc(plane, -PI / 6, radius=0.52, label_tex=r"\theta")

        x_label = MathTex(r"a=\sqrt{3}", font_size=28, color=SINE_COLOR).next_to(
            x_leg, UP, buff=0.15
        )
        y_label = MathTex(r"b=-1", font_size=28, color=COS_COLOR).next_to(
            y_leg, RIGHT, buff=0.13
        )
        point_label = MathTex(
            r"(\sqrt{3},-1)",
            font_size=27,
            color=TEXT_COLOR,
        ).next_to(point, DR, buff=0.14)
        point_label.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        point_label.set_color_by_tex("-1", COS_COLOR)

        reference_arc = Arc(
            radius=0.72,
            start_angle=-PI / 6,
            angle=PI / 6,
            arc_center=origin,
            color=GUIDE_COLOR,
            stroke_width=3,
        )
        alpha_label = MathTex(r"\alpha", font_size=26, color=GUIDE_COLOR)
        alpha_label.move_to(origin + np.array([0.78, -0.18, 0]))

        setup = MathTex(
            r"(a,b)=\left(\sqrt{3},-1\right)",
            font_size=30,
            color=TEXT_COLOR,
        )
        setup.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        setup.set_color_by_tex("-1", COS_COLOR)

        unit_point = MathTex(
            "R=2", r"\quad\Rightarrow\quad",
            r"\left(\frac{a}{R},\frac{b}{R}\right)", "=",
            r"\left(\frac{\sqrt{3}}{2},-\frac{1}{2}\right)",
            font_size=26,
            color=TEXT_COLOR,
        )
        self._color_by_roles(unit_point)
        unit_point.set_color_by_tex("2", R_COLOR)
        unit_point.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        unit_point.set_color_by_tex(r"-\frac{1}{2}", COS_COLOR)

        trig_point = MathTex(
            r"(\cos\theta,\sin\theta)", "=",
            r"\left(\frac{\sqrt{3}}{2},-\frac{1}{2}\right)",
            font_size=28,
            color=TEXT_COLOR,
        )
        self._color_by_roles(trig_point)
        trig_point.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        trig_point.set_color_by_tex(r"-\frac{1}{2}", COS_COLOR)

        quadrant = MathTex(
            r"\cos\theta", r">0,\quad", r"\sin\theta", r"<0",
            r"\quad\Longrightarrow\quad",
            r"\text{Quadrant IV}",
            font_size=28,
            color=TEXT_COLOR,
        )
        quadrant[0].set_color(COS_COLOR)
        quadrant[2].set_color(SINE_COLOR)
        quadrant[5].set_color(THETA_COLOR)

        reference = MathTex(
            r"\frac{\sqrt{3}}{2},\ \frac{1}{2}",
            r"\quad\Longrightarrow\quad",
            r"\text{reference angle } \frac{\pi}{6}",
            font_size=26,
            color=TEXT_COLOR,
        )
        reference[0].set_color(GUIDE_COLOR)
        reference[2].set_color(GUIDE_COLOR)

        exact_note = MathTex(
            r"\theta=-\frac{\pi}{6}",
            font_size=32,
            color=TEXT_COLOR,
        )
        exact_note.set_color_by_tex(r"\theta", THETA_COLOR)
        exact_note.set_color_by_tex(r"-\frac{\pi}{6}", THETA_COLOR)

        negative_note = MathTex(
            r"\text{Negative because the vector is below the } x\text{-axis.}",
            font_size=22,
            color=GUIDE_COLOR,
        )

        steps = VGroup(setup, unit_point, trig_point, quadrant, reference, exact_note, negative_note).arrange(
            DOWN, aligned_edge=LEFT, buff=0.22
        )
        steps.to_edge(RIGHT, buff=0.52).shift(DOWN * 0.12)
        steps_card = self._soft_card(steps, stroke_color=THETA_COLOR, buff=0.24)

        self.play(Write(title), run_time=0.65)
        self.play(FadeIn(plane), run_time=0.65)
        self.play(Create(x_leg), FadeIn(x_label), run_time=0.55)
        self.play(Create(y_leg), Create(right_angle), FadeIn(y_label), run_time=0.55)
        self.play(GrowArrow(vector), FadeIn(point_label), run_time=0.8)
        self.play(Create(theta_arc), run_time=0.7)
        self.wait(0.25)
        self.play(FadeIn(steps_card, shift=LEFT * 0.18), run_time=0.75)
        self.play(Indicate(unit_point, color=R_COLOR), run_time=0.8)
        self.play(Indicate(trig_point, color=THETA_COLOR), run_time=0.8)
        self.play(Indicate(quadrant, color=THETA_COLOR), Indicate(vector, color=THETA_COLOR), run_time=0.8)
        self.play(Create(reference_arc), FadeIn(alpha_label), run_time=0.65)
        self.play(Indicate(reference, color=GUIDE_COLOR), run_time=0.85)
        self.play(Indicate(exact_note, color=THETA_COLOR), Indicate(theta_arc, color=THETA_COLOR), run_time=0.85)
        self.wait(1.35)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 7. Return to the example
    # ---------------------------------------------------------------------
    def _return_to_example(self):
        title = MathTex(
            r"\text{Back to } \sqrt{3}\sin x-\cos x",
            font_size=34,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.36)
        title.set_color_by_tex(r"\sin", SINE_COLOR)
        title.set_color_by_tex(r"\cos", COS_COLOR)

        plane = NumberPlane(
            x_range=[-0.35, 2.35, 1],
            y_range=[-1.45, 0.75, 1],
            x_length=5.5,
            y_length=3.65,
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.42,
            },
            faded_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 0.7,
                "stroke_opacity": 0.22,
            },
            axis_config={
                "color": AXIS_COLOR,
                "stroke_width": 1.8,
                "include_tip": True,
                "tip_length": 0.13,
            },
        ).to_edge(LEFT, buff=0.78).shift(DOWN * 0.35)

        a_val = np.sqrt(3)
        b_val = -1
        origin = plane.c2p(0, 0)
        point = plane.c2p(a_val, b_val)
        foot = plane.c2p(a_val, 0)

        x_leg = Line(origin, foot, color=SINE_COLOR, stroke_width=4.2)
        y_leg = Line(foot, point, color=COS_COLOR, stroke_width=4.2)
        vector = Arrow(
            origin,
            point,
            buff=0,
            color=R_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        endpoint = Dot(point, radius=0.075, color=R_COLOR)
        right_angle = self._right_angle_marker(plane, a_val, b_val)
        angle = self._angle_arc(plane, -PI / 6, radius=0.52, label_tex=r"-\frac{\pi}{6}")

        x_label = MathTex(r"\sqrt{3}", font_size=30, color=SINE_COLOR).next_to(
            x_leg, UP, buff=0.15
        )
        y_label = MathTex(r"-1", font_size=30, color=COS_COLOR).next_to(
            y_leg, RIGHT, buff=0.13
        )
        r_label = MathTex("2", font_size=32, color=R_COLOR)
        self._place_segment_label(r_label, origin, point, distance=0.34)
        point_label = MathTex(
            r"\left(\sqrt{3},-1\right)",
            font_size=27,
            color=TEXT_COLOR,
        ).next_to(point, DR, buff=0.14)
        point_label.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        point_label.set_color_by_tex("-1", COS_COLOR)

        diagram = VGroup(
            plane, x_leg, y_leg, vector, endpoint,
            right_angle, angle, x_label, y_label, r_label, point_label,
        )

        coeffs = MathTex(
            r"(a,b)=\left(\sqrt{3},-1\right)",
            font_size=34,
            color=TEXT_COLOR,
        )
        coeffs.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        coeffs.set_color_by_tex("-1", COS_COLOR)

        r_calc = MathTex(
            r"R=\sqrt{(\sqrt{3})^2+(-1)^2}=2",
            font_size=34,
            color=TEXT_COLOR,
        )
        self._color_by_roles(r_calc)
        r_calc.set_color_by_tex("2", R_COLOR)

        theta_components = MathTex(
            r"\cos\theta=\frac{\sqrt{3}}{2},\qquad",
            r"\sin\theta=-\frac{1}{2}",
            font_size=28,
            color=TEXT_COLOR,
        )
        self._color_by_roles(theta_components)
        theta_components.set_color_by_tex(r"\sqrt{3}", SINE_COLOR)
        theta_components.set_color_by_tex(r"-\frac{1}{2}", COS_COLOR)

        theta_calc = MathTex(
            r"\text{QIV gives }", r"\theta=-\frac{\pi}{6}",
            font_size=28,
            color=TEXT_COLOR,
        )
        theta_calc[1].set_color(THETA_COLOR)

        rebuild = MathTex(
            r"\sqrt{3}", r"\sin x", "-", r"\cos x", "=",
            "2", r"\sin", r"\left(x", r"-\frac{\pi}{6}", r"\right)",
            font_size=34,
            color=TEXT_COLOR,
        )
        rebuild[0].set_color(SINE_COLOR)
        rebuild[1].set_color(SINE_COLOR)
        rebuild[3].set_color(COS_COLOR)
        rebuild[5].set_color(R_COLOR)
        rebuild[6].set_color(SINE_COLOR)
        rebuild[8].set_color(THETA_COLOR)

        stack = VGroup(coeffs, r_calc, theta_components, theta_calc, rebuild).arrange(
            DOWN, aligned_edge=LEFT, buff=0.32
        )
        stack.to_edge(RIGHT, buff=0.64).shift(DOWN * 0.06)
        stack_card = self._soft_card(stack, stroke_color=THETA_COLOR, buff=0.28)

        final_box = SurroundingRectangle(rebuild, color=GUIDE_COLOR, buff=0.16, stroke_width=2.4)

        self.play(Write(title), run_time=0.65)
        self.play(FadeIn(plane), run_time=0.65)
        self.play(Create(x_leg), FadeIn(x_label), run_time=0.5)
        self.play(Create(y_leg), FadeIn(y_label), Create(right_angle), run_time=0.5)
        self.play(GrowArrow(vector), FadeIn(endpoint), FadeIn(r_label), FadeIn(point_label), run_time=0.85)
        self.play(Create(angle), run_time=0.7)
        self.wait(0.35)
        self.play(FadeIn(stack_card, shift=LEFT * 0.18), run_time=0.85)
        self.play(Indicate(r_calc, color=R_COLOR), Indicate(vector, color=R_COLOR), run_time=0.9)
        self.play(Indicate(theta_components, color=THETA_COLOR), run_time=0.8)
        self.play(Indicate(theta_calc, color=THETA_COLOR), Indicate(angle, color=THETA_COLOR), run_time=0.85)
        self.play(Create(final_box), run_time=0.55)
        self.wait(1.35)
        self._clear_scene()

    # ---------------------------------------------------------------------
    # 8. Final summary
    # ---------------------------------------------------------------------
    def _final_summary(self):
        title = MathTex(
            r"\text{The whole idea}",
            font_size=38,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.62)

        line1 = MathTex(
            r"\text{The coefficients }", "a", r"\text{ and }", "b",
            r"\text{ are the components of one vector.}",
            font_size=30,
            color=TEXT_COLOR,
        )
        line1[1].set_color(SINE_COLOR)
        line1[3].set_color(COS_COLOR)

        line2 = MathTex(
            r"\text{That vector has magnitude }", "R",
            r"\text{ and angle }", r"\theta", r"\text{.}",
            font_size=30,
            color=TEXT_COLOR,
        )
        line2[1].set_color(R_COLOR)
        line2[3].set_color(THETA_COLOR)

        line3 = MathTex(
            r"\text{The angle addition formula turns those components}"
            r"\text{ into one shifted sine wave.}",
            font_size=30,
            color=TEXT_COLOR,
        )
        line3.set_color_by_tex(r"\sin", SINE_COLOR)

        summary = VGroup(line1, line2, line3).arrange(DOWN, buff=0.34)
        for line in summary:
            self._fit(line, 11.6)
        summary.move_to(UP * 0.25)

        formula = MathTex(
            "a", r"\sin x", "+", "b", r"\cos x", "=",
            "R", r"\sin", r"\left(x+", r"\theta", r"\right)",
            font_size=42,
            color=TEXT_COLOR,
        )
        formula[0].set_color(SINE_COLOR)
        formula[1].set_color(SINE_COLOR)
        formula[3].set_color(COS_COLOR)
        formula[4].set_color(COS_COLOR)
        formula[6].set_color(R_COLOR)
        formula[7].set_color(SINE_COLOR)
        formula[9].set_color(THETA_COLOR)
        formula.next_to(summary, DOWN, buff=0.62)
        formula_card = self._soft_card(formula, stroke_color=GUIDE_COLOR, buff=0.25)

        conditions_top = MathTex(
            "R", "=", r"\sqrt{", "a", "^2", "+", "b", "^2", "}",
            r",\qquad", r"(\cos\theta,\sin\theta)", "=",
            r"\left(\frac{a}{R},\frac{b}{R}\right)",
            font_size=26,
            color=TEXT_MUTED,
        )
        conditions_top[0].set_color(R_COLOR)
        conditions_top[3].set_color(SINE_COLOR)
        conditions_top[6].set_color(COS_COLOR)
        conditions_top[10].set_color(THETA_COLOR)

        conditions_bottom = MathTex(
            "R", r"\cos", r"\theta", "=", "a",
            r",\qquad", "R", r"\sin", r"\theta", "=", "b",
            font_size=26,
            color=TEXT_MUTED,
        )
        conditions_bottom[0].set_color(R_COLOR)
        conditions_bottom[1].set_color(COS_COLOR)
        conditions_bottom[2].set_color(THETA_COLOR)
        conditions_bottom[4].set_color(SINE_COLOR)
        conditions_bottom[6].set_color(R_COLOR)
        conditions_bottom[7].set_color(SINE_COLOR)
        conditions_bottom[8].set_color(THETA_COLOR)
        conditions_bottom[10].set_color(COS_COLOR)

        conditions = VGroup(conditions_top, conditions_bottom).arrange(DOWN, buff=0.16)
        conditions.next_to(formula_card, DOWN, buff=0.36)

        self.play(Write(title), run_time=0.75)
        self.play(LaggedStart(*[FadeIn(line, shift=UP * 0.15) for line in summary], lag_ratio=0.28), run_time=1.8)
        self.play(FadeIn(formula_card, shift=UP * 0.2), run_time=0.9)
        self.play(Write(conditions), run_time=0.9)
        # Hold the completed summary long enough for classroom narration.
        self.wait(FINAL_SUMMARY_HOLD)
