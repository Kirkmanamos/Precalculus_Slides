"""
Graphical analysis of  2sin²x + 3cos x - 3 = 0  — all solutions.

Narrative arc
─────────────
1. Title + equation + "All Solutions" statement
2. Algebra steps: Pythagorean substitution → simplify → factor → ZPP
   • Case 1 (green): cos x = 1/2
   • Case 2 (blue):  cos x = 1
   • Bridge → fade algebra and transition to graphs
3. cos x = 1/2 graph (green border, full scene)
   • y = cos x over [0, 2π], dashed y = 1/2 reference
   • Intersections at π/3 (QI) and 5π/3 (QIV)
   • General solution box
4. cos x = 1/2 shrinks to left thumbnail
5. cos x = 1 graph (blue border, full scene)
   • y = cos x over [0, 4π], dashed y = 1 reference
   • Intersections at 0, 2π, 4π
   • General solution box
6. cos x = 1 shrinks to right thumbnail
7. ✓ labels above both + final combined solution banner

Render (from the manim/ directory):
    manim -pql scenes/5_3_pyth_sub_graphical.py PythSubGraphicalAnalysis
    manim -pqh scenes/5_3_pyth_sub_graphical.py PythSubGraphicalAnalysis
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *


class PythSubGraphicalAnalysis(Scene):
    """
    Full narrative: algebra steps → two-graph verification → solution.

    Layout constants
    ────────────────
    SMALL         thumbnail scale factor
    COS_HALF_POS  center of left thumbnail  (cos x = 1/2)
    COS_ONE_POS   center of right thumbnail (cos x = 1)
    FULL_CTR      center of full-scene graph
    """

    SMALL        = 0.65
    COS_HALF_POS = LEFT  * 3.85 + DOWN * 0.25
    COS_ONE_POS  = RIGHT * 3.85 + DOWN * 0.25
    FULL_CTR     = DOWN  * 0.75

    def construct(self):
        self.camera.background_color = BG_COLOR
        self._phase_intro()
        self._phase_math_steps()
        self._phase_cos_half_panel()
        self._phase_cos_one_panel()
        self._phase_banner()

    # ── Phase 1 : title + "All Solutions" statement ─────────────────────────
    def _phase_intro(self):
        title = MathTex(
            r"\text{Graphical Analysis:}\quad"
            r"2\sin^2\!x + 3\cos x - 3 = 0",
            font_size=34, color=TEXT_COLOR,
        ).to_edge(UP, buff=0.28)

        subtitle = MathTex(
            r"\text{Find: }\textbf{all solutions}"
            r"\text{ --- no domain restriction on }x",
            font_size=26, color=ACCENT_BLUE,
        ).next_to(title, DOWN, buff=0.20)
        sub_box = SurroundingRectangle(
            subtitle, color=ACCENT_BLUE, stroke_width=1.5,
            fill_color="#050f1e", fill_opacity=0.50,
            buff=0.13, corner_radius=0.08,
        )

        title.set_z_index(10)
        self.play(Write(title), run_time=1.1)
        self.play(Write(subtitle), run_time=0.9)
        self.play(Create(sub_box), run_time=0.40)
        self.wait(1.5)

        self.title    = title
        self.subtitle = VGroup(sub_box, subtitle)

    # ── Phase 2 : algebra steps ─────────────────────────────────────────────
    def _phase_math_steps(self):
        """
        Four algebra rows, then zero-product-property split, bridge line.
        Everything fades out at the end, leaving only self.title.
        """

        # ── four algebra steps ──────────────────────────────────────────
        s0 = MathTex(
            r"2\sin^2\!x + 3\cos x - 3 = 0",
            font_size=34, color=TEXT_COLOR,
        )
        s1 = MathTex(
            r"2(1 - \cos^2\!x) + 3\cos x - 3 = 0",
            font_size=34, color=TEXT_COLOR,
        )
        s2 = MathTex(
            r"2\cos^2\!x - 3\cos x + 1 = 0",
            font_size=34, color=TEXT_COLOR,
        )
        s3 = MathTex(
            r"(2\cos x - 1)(\cos x - 1) = 0",
            font_size=34, color=TEXT_COLOR,
        )

        ann0 = Tex(r"original equation",              font_size=21, color=TEXT_MUTED)
        ann1 = Tex(r"$\sin^2\!x = 1 - \cos^2\!x$",  font_size=21, color=TEXT_MUTED)
        ann2 = Tex(r"expand, simplify",               font_size=21, color=TEXT_MUTED)
        ann3 = Tex(r"factor",                          font_size=21, color=TEXT_MUTED)

        steps_col = VGroup(s0, s1, s2, s3).arrange(
            DOWN, buff=0.45, aligned_edge=LEFT,
        )
        steps_col.next_to(self.subtitle, DOWN, buff=0.35).to_edge(LEFT, buff=1.0)

        for step, ann in [(s0, ann0), (s1, ann1), (s2, ann2), (s3, ann3)]:
            ann.next_to(step, RIGHT, buff=0.45)

        # Small down-arrows between steps
        arr1 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s0.get_bottom() + s1.get_top()) / 2
        )
        arr2 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s1.get_bottom() + s2.get_top()) / 2
        )
        arr3 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s2.get_bottom() + s3.get_top()) / 2
        )

        # ── zero product property split ─────────────────────────────────
        zpp_lbl = Tex(
            r"\textbf{Zero Product Property:}",
            font_size=25, color=TEXT_MUTED,
        )
        case1 = MathTex(r"\cos x = \tfrac{1}{2}", font_size=32, color=Q1_COLOR)
        or_tx = Tex(r"\textbf{or}",               font_size=25, color=TEXT_MUTED)
        case2 = MathTex(r"\cos x = 1",            font_size=32, color=ACCENT_BLUE)
        cases_row = VGroup(case1, or_tx, case2).arrange(RIGHT, buff=0.50)

        zpp_grp = VGroup(zpp_lbl, cases_row).arrange(DOWN, buff=0.20)
        zpp_grp.next_to(s3, DOWN, buff=0.35).shift(RIGHT * 0.60)

        # ── bridge text ─────────────────────────────────────────────────
        bridge = Tex(
            r"Now let's verify each case graphically $\longrightarrow$",
            font_size=24, color=HIGHLIGHT,
        ).to_edge(DOWN, buff=0.38)

        # ── animate step by step ───────────────────────────────────────
        self.play(FadeIn(s0, shift=RIGHT * 0.1), FadeIn(ann0), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr1), run_time=0.25)
        self.play(FadeIn(s1, shift=RIGHT * 0.1), FadeIn(ann1), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr2), run_time=0.25)
        self.play(FadeIn(s2, shift=RIGHT * 0.1), FadeIn(ann2), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr3), run_time=0.25)
        self.play(FadeIn(s3, shift=RIGHT * 0.1), FadeIn(ann3), run_time=0.70)
        self.wait(0.35)

        self.play(Write(zpp_lbl), run_time=0.50)
        self.play(
            LaggedStart(Write(case1), Write(or_tx), Write(case2), lag_ratio=0.25),
            run_time=1.0,
        )
        self.wait(0.25)

        self.play(Write(bridge), run_time=0.65)
        self.wait(0.6)

        # Fade out everything except self.title
        self.play(
            FadeOut(VGroup(
                self.subtitle,
                s0, s1, s2, s3,
                ann0, ann1, ann2, ann3,
                arr1, arr2, arr3,
                zpp_grp, bridge,
            )),
            run_time=0.85,
        )

    # ── Phase 3 : cos x = 1/2 graph ────────────────────────────────────────
    def _phase_cos_half_panel(self):
        # ── build axes ──────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 2 * PI + 0.2, PI / 2],
            y_range=[-1.3, 1.5, 0.5],
            x_length=9.6,
            y_length=5.0,
            axis_config={
                "color": AXIS_COLOR, "include_tip": True,
                "tip_length": 0.16, "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-1, 1],
                "font_size": 22,
            },
        ).move_to(self.FULL_CTR)

        # graph chrome
        border = SurroundingRectangle(
            axes, color=Q1_COLOR, stroke_width=2.0,
            fill_color="#030e08", fill_opacity=0.55,
            buff=0.25, corner_radius=0.12,
        )
        graph_lbl = MathTex(
            r"\text{Case 1: }\cos x = \tfrac{1}{2}",
            font_size=34, color=Q1_COLOR,
        ).next_to(border, UP, buff=0.10)

        # x-tick labels
        xv = [0, PI / 2, PI, 3 * PI / 2, 2 * PI]
        xs = [r"0", r"\tfrac{\pi}{2}", r"\pi",
              r"\tfrac{3\pi}{2}", r"2\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=21, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(xv, xs)
        ])
        xe = MathTex(r"x", font_size=25, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.09)
        ye = MathTex(r"y", font_size=25, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.08)

        # y = cos x
        cos_curve = axes.plot(
            lambda x: np.cos(x),
            x_range=[0, 2 * PI],
            color=ACCENT_TEAL, stroke_width=3,
        )
        cos_lbl = MathTex(r"y = \cos x", font_size=25, color=ACCENT_TEAL).next_to(
            axes.c2p(PI / 6, np.cos(PI / 6)), UR, buff=0.14)

        # dashed y = 1/2 reference
        ref_line = DashedLine(
            axes.c2p(0, 0.5), axes.c2p(2 * PI, 0.5),
            color=HIGHLIGHT, dash_length=0.15, stroke_width=2.0,
        )
        ref_lbl = MathTex(
            r"y = \tfrac{1}{2}", font_size=24, color=HIGHLIGHT,
        ).next_to(axes.c2p(2 * PI * 0.88, 0.5), UR, buff=0.08)

        # ── animate graph ───────────────────────────────────────────────
        self.play(FadeIn(border), Write(graph_lbl), Create(axes), run_time=1.1)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.09),
            Write(xe), Write(ye), run_time=0.85,
        )
        self.play(Create(cos_curve), Write(cos_lbl), run_time=1.2)
        self.wait(0.2)
        self.play(Create(ref_line), Write(ref_lbl), run_time=0.80)
        self.wait(0.3)

        # ── mark intersections ──────────────────────────────────────────
        # π/3 → QI (green)
        pt1  = axes.c2p(PI / 3, 0.5)
        dot1 = Dot(pt1, radius=0.12, color=Q1_COLOR)
        lbl1 = MathTex(
            r"\tfrac{\pi}{3}", font_size=24, color=Q1_COLOR,
        ).next_to(pt1, DOWN, buff=0.22)
        qtag1 = Tex(r"QI", font_size=18, color=Q1_COLOR).next_to(dot1, UP, buff=0.09)

        # 5π/3 → QIV (gold)
        pt2  = axes.c2p(5 * PI / 3, 0.5)
        dot2 = Dot(pt2, radius=0.12, color=Q4_COLOR)
        lbl2 = MathTex(
            r"\tfrac{5\pi}{3}", font_size=24, color=Q4_COLOR,
        ).next_to(pt2, DOWN, buff=0.22)
        qtag2 = Tex(r"QIV", font_size=18, color=Q4_COLOR).next_to(dot2, UP, buff=0.09)

        self.play(FadeIn(dot1, scale=1.7), Write(lbl1), Write(qtag1), run_time=0.75)
        self.wait(0.15)
        self.play(FadeIn(dot2, scale=1.7), Write(lbl2), Write(qtag2), run_time=0.75)
        self.wait(0.35)

        # ── general solution box ────────────────────────────────────────
        gen_sol = MathTex(
            r"x = \tfrac{\pi}{3} + 2\pi n,\; "
            r"x = \tfrac{5\pi}{3} + 2\pi n",
            font_size=24, color=HIGHLIGHT,
        ).move_to(axes.c2p(PI, -0.80))
        gen_box = SurroundingRectangle(
            gen_sol, color=HIGHLIGHT, stroke_width=1.5,
            fill_color="#181000", fill_opacity=0.60,
            buff=0.12, corner_radius=0.08,
        )
        self.play(DrawBorderThenFill(gen_box), Write(gen_sol), run_time=0.90)
        self.wait(0.85)

        # ── pack & shrink to left thumbnail ─────────────────────────────
        self.cos_half_vg = VGroup(
            border, graph_lbl, axes, x_lbls, xe, ye,
            cos_curve, cos_lbl,
            ref_line, ref_lbl,
            dot1, lbl1, qtag1,
            dot2, lbl2, qtag2,
            gen_box, gen_sol,
        )
        self.play(
            self.cos_half_vg.animate.scale(self.SMALL).move_to(self.COS_HALF_POS),
            run_time=1.3,
        )
        self.wait(0.3)

    # ── Phase 4 : cos x = 1 graph ──────────────────────────────────────────
    def _phase_cos_one_panel(self):
        # Dark scrim covers cos-half thumbnail
        scrim = Rectangle(
            width=16, height=10,
            fill_color=BG_COLOR, fill_opacity=0.95,
            stroke_width=0,
        )
        self.play(FadeIn(scrim), run_time=0.35)
        self.scrim = scrim

        # ── build axes ──────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 4 * PI + 0.3, PI],
            y_range=[-1.3, 1.5, 0.5],
            x_length=9.6,
            y_length=5.0,
            axis_config={
                "color": AXIS_COLOR, "include_tip": True,
                "tip_length": 0.16, "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-1, 1],
                "font_size": 22,
            },
        ).move_to(self.FULL_CTR)

        # graph chrome
        border = SurroundingRectangle(
            axes, color=ACCENT_BLUE, stroke_width=2.0,
            fill_color="#050812", fill_opacity=0.55,
            buff=0.25, corner_radius=0.12,
        )
        graph_lbl = MathTex(
            r"\text{Case 2: }\cos x = 1",
            font_size=34, color=ACCENT_BLUE,
        ).next_to(border, UP, buff=0.10)

        # x-tick labels
        xv = [0, PI, 2 * PI, 3 * PI, 4 * PI]
        xs = [r"0", r"\pi", r"2\pi", r"3\pi", r"4\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=21, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(xv, xs)
        ])
        xe = MathTex(r"x", font_size=25, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.09)
        ye = MathTex(r"y", font_size=25, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.08)

        # y = cos x
        cos_curve = axes.plot(
            lambda x: np.cos(x),
            x_range=[0, 4 * PI],
            color=ACCENT_TEAL, stroke_width=3,
        )
        cos_lbl = MathTex(r"y = \cos x", font_size=25, color=ACCENT_TEAL).next_to(
            axes.c2p(PI / 4, np.cos(PI / 4)), UR, buff=0.14)

        # dashed y = 1 reference
        ref_line = DashedLine(
            axes.c2p(0, 1), axes.c2p(4 * PI, 1),
            color=ACCENT_BLUE, dash_length=0.15, stroke_width=2.0,
        )
        ref_lbl = MathTex(
            r"y = 1", font_size=24, color=ACCENT_BLUE,
        ).next_to(axes.c2p(4 * PI * 0.88, 1), UR, buff=0.08)

        # ── animate graph ───────────────────────────────────────────────
        self.play(FadeIn(border), Write(graph_lbl), Create(axes), run_time=1.0)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.09),
            Write(xe), Write(ye), run_time=0.80,
        )
        self.play(Create(cos_curve), Write(cos_lbl), run_time=1.2)
        self.wait(0.2)
        self.play(Create(ref_line), Write(ref_lbl), run_time=0.80)
        self.wait(0.3)

        # ── mark intersections at 0, 2π, 4π ────────────────────────────
        sol_mobs = []
        for x_val, lbl_s, ntag_s in [
            (0,        r"0",       r"n = 0"),
            (2 * PI,   r"2\pi",   r"n = 1"),
            (4 * PI,   r"4\pi",   r"n = 2"),
        ]:
            pt   = axes.c2p(x_val, 1)
            dot  = Dot(pt, radius=0.12, color=ACCENT_BLUE)
            xlbl = MathTex(lbl_s, font_size=24, color=ACCENT_BLUE).next_to(
                pt, DOWN, buff=0.22)
            ntag = Tex(ntag_s, font_size=18, color=ACCENT_BLUE).next_to(
                dot, UP, buff=0.09)
            self.play(
                FadeIn(dot, scale=1.7), Write(xlbl), Write(ntag), run_time=0.75,
            )
            self.wait(0.10)
            sol_mobs.extend([dot, xlbl, ntag])

        self.wait(0.35)

        # ── general solution box ────────────────────────────────────────
        gen_sol = MathTex(
            r"x = 2\pi n, \quad n \in \mathbb{Z}",
            font_size=26, color=HIGHLIGHT,
        ).move_to(axes.c2p(2 * PI, -0.80))
        gen_box = SurroundingRectangle(
            gen_sol, color=HIGHLIGHT, stroke_width=1.5,
            fill_color="#181000", fill_opacity=0.60,
            buff=0.12, corner_radius=0.08,
        )
        self.play(DrawBorderThenFill(gen_box), Write(gen_sol), run_time=0.90)
        self.wait(0.85)

        # ── pack & shrink to right thumbnail ────────────────────────────
        self.cos_one_vg = VGroup(
            border, graph_lbl, axes, x_lbls, xe, ye,
            cos_curve, cos_lbl,
            ref_line, ref_lbl,
            *sol_mobs,
            gen_box, gen_sol,
        )
        self.play(
            self.cos_one_vg.animate.scale(self.SMALL).move_to(self.COS_ONE_POS),
            FadeOut(self.scrim),       # reveal cos-half thumbnail underneath
            run_time=1.2,
        )
        self.wait(0.5)

    # ── Phase 5 : solution banner ───────────────────────────────────────────
    def _phase_banner(self):
        lbl_a = MathTex(
            r"\checkmark\;\cos x = \tfrac{1}{2}", font_size=28, color=Q1_COLOR,
        ).next_to(self.cos_half_vg, UP, buff=0.12)
        lbl_b = MathTex(
            r"\checkmark\;\cos x = 1", font_size=28, color=ACCENT_BLUE,
        ).next_to(self.cos_one_vg, UP, buff=0.12)

        self.play(Write(lbl_a), Write(lbl_b), run_time=0.70)
        self.wait(0.4)

        banner = RoundedRectangle(
            corner_radius=0.14,
            width=11.5, height=0.95,
            fill_color="#0b1d2e", fill_opacity=0.97,
            stroke_color=HIGHLIGHT, stroke_width=2.5,
        ).to_edge(DOWN, buff=0.18)

        sol = MathTex(
            r"x = \tfrac{\pi}{3} + 2\pi n,\quad "
            r"x = \tfrac{5\pi}{3} + 2\pi n,\quad "
            r"x = 2\pi n",
            font_size=34, color=HIGHLIGHT,
        ).move_to(banner)

        self.play(DrawBorderThenFill(banner), run_time=0.60)
        self.play(Write(sol), run_time=1.25)
        self.wait(2.5)
