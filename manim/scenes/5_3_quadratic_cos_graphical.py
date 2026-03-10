"""
Graphical analysis of 2cos²θ − 7cosθ + 3 = 0 for 0 ≤ θ < 2π.

Shows f(θ) = 2cos²θ − 7cosθ + 3 plotted on [0, 2π], highlights the
x-intercepts at θ = π/3 and θ = 5π/3, and marks cosθ = 3 as impossible.

Render (from the manim/ directory):
    manim -pql scenes/5_3_quadratic_cos_graphical.py QuadraticCosGraphicalAnalysis
    manim -pqh scenes/5_3_quadratic_cos_graphical.py QuadraticCosGraphicalAnalysis
"""

from manim import *
import sys, os

# Allow running from repo root OR from manim/ directory
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *

import numpy as np


def f(theta):
    """f(θ) = 2cos²θ − 7cosθ + 3"""
    c = np.cos(theta)
    return 2 * c**2 - 7 * c + 3


class QuadraticCosGraphicalAnalysis(Scene):
    """
    Animated graphical solution of  2cos²θ − 7cosθ + 3 = 0  on [0, 2π).

    Narrative arc
    ─────────────
    1. Title + algebraic bridge  (factor → cosθ = ½ or cosθ = 3)
    2. Build axes, draw f(θ) = 2cos²θ − 7cosθ + 3
    3. Show y = 0 reference and mark x-intercepts at π/3, 5π/3
    4. Explain cosθ = 3 is impossible (graph never reaches y=0 via that factor)
    5. Solution banner: θ = π/3, 5π/3
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self._phase_intro()
        self._phase_axes()
        self._phase_curve()
        self._phase_x_intercepts()
        self._phase_no_solution()
        self._phase_solution_banner()

    # ── Phase 1 : title + zero-product property walkthrough ─────────────────
    def _phase_intro(self):
        title = MathTex(
            r"\text{Graphical Analysis:}\quad 2\cos^2\!\theta - 7\cos\theta + 3 = 0",
            font_size=32,
            color=TEXT_COLOR,
        ).to_edge(UP, buff=0.25)

        domain = MathTex(
            r"\text{for } 0 \le \theta < 2\pi",
            font_size=24,
            color=TEXT_MUTED,
        ).next_to(title, DOWN, buff=0.15)

        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(domain), run_time=0.5)
        self.wait(0.4)

        # Step 1: u-substitution
        step1 = MathTex(
            r"\text{Let } u = \cos\theta:",
            r"\quad 2u^2 - 7u + 3 = 0",
            font_size=28,
            color=TEXT_COLOR,
        )

        # Step 2: Factor
        step2 = MathTex(
            r"(2u - 1)(u - 3) = 0",
            font_size=28,
            color=TEXT_COLOR,
        )

        # Step 3: Zero-product property header
        zpp_label = Tex(
            r"Zero-Product Property:",
            font_size=24,
            color=HIGHLIGHT,
        )

        # Step 4: Each factor = 0, back-substituted
        factor1 = MathTex(
            r"2\cos\theta - 1 = 0",
            r"\quad\Longrightarrow\quad",
            r"\cos\theta = \tfrac{1}{2}",
            font_size=28,
            color=TEXT_COLOR,
        )
        factor1[2].set_color(Q1_COLOR)

        factor2 = MathTex(
            r"\cos\theta - 3 = 0",
            r"\quad\Longrightarrow\quad",
            r"\cos\theta = 3",
            font_size=28,
            color=TEXT_COLOR,
        )
        factor2[2].set_color(ACCENT_RED)

        steps = VGroup(step1, step2, zpp_label, factor1, factor2)
        steps.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        steps.next_to(domain, DOWN, buff=0.30)

        self.play(Write(step1), run_time=1.0)
        self.play(Write(step2), run_time=0.8)
        self.wait(0.3)
        self.play(Write(zpp_label), run_time=0.6)
        self.play(Write(factor1), run_time=1.0)
        self.play(Write(factor2), run_time=1.0)
        self.wait(0.8)

        # Transition: explain what the graph shows
        graph_note = MathTex(
            r"\text{Graph } f(\theta) = 2\cos^2\!\theta - 7\cos\theta + 3"
            r"\text{ and find where } f(\theta) = 0",
            font_size=24,
            color=ACCENT_TEAL,
        ).next_to(steps, DOWN, buff=0.35)

        self.play(Write(graph_note), run_time=1.2)
        self.wait(1.0)

        # Fade the walkthrough to make room for the graph
        self.play(
            FadeOut(VGroup(steps, domain, graph_note)),
            title.animate.scale(0.85).to_edge(UP, buff=0.12),
            run_time=0.7,
        )
        self.title = title

    # ── Phase 2 : coordinate axes ────────────────────────────────────────────
    def _phase_axes(self):
        # y range: f goes from −2 (at θ=0 and 2π) up to 12 (at θ=π)
        axes = Axes(
            x_range=[0, 2 * PI + 0.2, PI / 2],
            y_range=[-3, 13, 2],
            x_length=9.8,
            y_length=5.4,
            axis_config={
                "color":        AXIS_COLOR,
                "include_tip":  True,
                "tip_length":   0.17,
                "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers":    True,
                "numbers_to_include": [-2, 0, 2, 4, 6, 8, 10, 12],
                "font_size":          16,
            },
        ).shift(DOWN * 0.7)

        # ── θ-axis custom labels ───────────────────────────────────────────
        x_vals = [0,    PI / 2,           PI,    3 * PI / 2,        2 * PI]
        x_strs = [r"0", r"\frac{\pi}{2}", r"\pi", r"\frac{3\pi}{2}", r"2\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=20, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(x_vals, x_strs)
        ])

        theta_lbl = MathTex(r"\theta", font_size=26, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.12)
        y_lbl = MathTex(r"y", font_size=26, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.10)

        self.play(Create(axes), run_time=1.2)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.12),
            Write(theta_lbl), Write(y_lbl),
            run_time=0.9,
        )

        self.axes = axes

    # ── Phase 3 : plot f(θ) ──────────────────────────────────────────────────
    def _phase_curve(self):
        axes = self.axes

        graph = axes.plot(
            f,
            x_range=[0, 2 * PI, 0.01],
            color=ACCENT_TEAL,
            stroke_width=3,
        )

        curve_lbl = MathTex(
            r"f(\theta) = 2\cos^2\!\theta - 7\cos\theta + 3",
            font_size=22,
            color=ACCENT_TEAL,
        ).next_to(axes.c2p(PI, f(PI)), UP, buff=0.2)

        self.play(Create(graph), run_time=2.5)
        self.play(Write(curve_lbl), run_time=0.8)
        self.wait(0.5)

        self.graph = graph

    # ── Phase 4 : y = 0 line + x-intercepts ──────────────────────────────────
    def _phase_x_intercepts(self):
        axes = self.axes

        # horizontal y = 0 reference (thicker segment on x-axis region)
        y0_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(2 * PI, 0),
            color=HIGHLIGHT,
            dash_length=0.16,
            stroke_width=2.5,
        )
        y0_lbl = MathTex(
            r"y = 0", font_size=22, color=HIGHLIGHT
        ).next_to(axes.c2p(2 * PI + 0.05, 0), UR, buff=0.12)

        self.play(Create(y0_line), Write(y0_lbl), run_time=0.9)
        self.wait(0.3)

        # Mark θ = π/3  (QI — green)
        self._mark_solution(
            axes, PI / 3, Q1_COLOR,
            r"\dfrac{\pi}{3}", "QI", UL,
        )

        # Mark θ = 5π/3  (QIV — gold)
        self._mark_solution(
            axes, 5 * PI / 3, Q4_COLOR,
            r"\dfrac{5\pi}{3}", "QIV", UR,
        )
        self.wait(0.5)

    # ── Phase 5 : cosθ = 3 — no solution ─────────────────────────────────────
    def _phase_no_solution(self):
        axes = self.axes

        # Brace / callout: the graph's minimum is −2, it reaches y=0 only twice
        # Show a "cosθ = 3  ✗  no solution" annotation
        no_sol_box = RoundedRectangle(
            corner_radius=0.10,
            width=4.6, height=0.72,
            fill_color="#1c0a0a", fill_opacity=0.92,
            stroke_color=ACCENT_RED, stroke_width=2,
        ).to_corner(UR, buff=0.45)

        no_sol_text = VGroup(
            MathTex(r"\cos\theta = 3", font_size=26, color=ACCENT_RED),
            MathTex(
                r"\text{No solution — } |\!\cos\theta| \le 1",
                font_size=20,
                color=TEXT_MUTED,
            ),
        ).arrange(DOWN, buff=0.08).move_to(no_sol_box)

        self.play(DrawBorderThenFill(no_sol_box), run_time=0.6)
        self.play(Write(no_sol_text), run_time=1.0)
        self.wait(1.0)

    # ── Phase 6 : solution summary banner ────────────────────────────────────
    def _phase_solution_banner(self):
        banner = RoundedRectangle(
            corner_radius=0.14,
            width=7.0, height=0.86,
            fill_color="#0b1d2e", fill_opacity=0.96,
            stroke_color=HIGHLIGHT, stroke_width=2.5,
        ).to_edge(DOWN, buff=0.16)

        sol = MathTex(
            r"\theta = \dfrac{\pi}{3},\quad \dfrac{5\pi}{3}",
            font_size=32,
            color=HIGHLIGHT,
        ).move_to(banner)

        self.play(DrawBorderThenFill(banner), run_time=0.65)
        self.play(Write(sol), run_time=1.0)
        self.wait(2.5)

    # ── helper ───────────────────────────────────────────────────────────────
    def _mark_solution(self, axes, theta, color, theta_str, quad, q_dir):
        """
        Animate one x-intercept:
          • vertical dashed drop-line from curve down to (θ, 0)
          • glowing gold dot at the x-intercept
          • θ-label below the x-axis
          • quadrant tag next to the dot
        """
        y_val = f(theta)  # should be ≈ 0
        pt   = axes.c2p(theta, y_val)
        foot = axes.c2p(theta, 0)

        # vertical trace from a point above to the x-axis to show where curve hits 0
        trace_top = axes.c2p(theta, max(f(theta), 2.0))
        vline = DashedLine(
            trace_top, foot,
            color=color, dash_length=0.10, stroke_width=2.0,
        )
        dot  = Dot(foot, radius=0.11, color=HIGHLIGHT, z_index=5)
        xlbl = MathTex(theta_str, font_size=20, color=HIGHLIGHT).next_to(
            foot, DOWN, buff=0.18)
        qlbl = Tex(quad, font_size=17, color=color).next_to(dot, q_dir, buff=0.09)

        self.play(
            Create(vline),
            FadeIn(dot, scale=1.7),
            Write(xlbl),
            Write(qlbl),
            run_time=0.95,
        )
        self.wait(0.15)
