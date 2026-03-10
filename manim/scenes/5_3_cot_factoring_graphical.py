"""
Graphical analysis of  cot x · cos²x = 2cot x  — all solutions.

Narrative arc
─────────────
1. Title + equation + "All Solutions" statement  (held on screen)
2. Algebra steps: original → subtract → factor → zero product property
   • Color-coded cases: Case 1 (green) vs Case 2 (red)
   • Warning: don't divide by cot x
   • Bridge → fade algebra and transition to graphs
3. Cot graph (green border, full scene) — Case 1: cot x = 0
   • y = cot x over [0, 3π], zeros at π/2, 3π/2, 5π/2
   • "cot x = cos x / sin x = 0 ⟹ cos x = 0" annotation
   • General solution box: x = π/2 + πn, n ∈ ℤ
4. Cot graph shrinks to left thumbnail
5. Cos² graph (red border, full scene) — Case 2: cos²x = 2  (impossible)
   • y = cos²x vs y = 2; ceiling at y = 1
   • "No intersection!" + proof stamp
6. Cos² graph shrinks to right thumbnail
7. ✓/✗ labels above thumbnails + final solution banner

Render (from the manim/ directory):
    manim -pql scenes/5_3_cot_factoring_graphical.py CotFactoringGraphicalAnalysis
    manim -pqh scenes/5_3_cot_factoring_graphical.py CotFactoringGraphicalAnalysis
"""

from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from shared.colors import *

# ── constants ─────────────────────────────────────────────────────────────────
# EPS = gap on each side of cot asymptotes.  At EPS = 0.25 the max
# |cot| value is ≈ 3.9, safely inside the axes y_range [-4, 4].
# No np.clip needed → no flatline near asymptotes.
EPS    = 0.25
ASYM_C = "#3d5a73"      # muted blue-grey for asymptote dashes


def _cot(x):
    """Plain cot(x).  EPS keeps the x_range far enough from asymptotes."""
    return np.cos(x) / np.sin(x)


class CotFactoringGraphicalAnalysis(Scene):
    """
    Full narrative: algebra steps → two-graph verification → solution.

    Layout constants
    ────────────────
    SMALL      thumbnail scale factor
    COT_THUMB  center of left thumbnail
    COS_THUMB  center of right thumbnail
    FULL_CTR   center of full-scene graph
    """

    SMALL     = 0.55                          # larger thumbnails on final screen
    COT_THUMB = LEFT  * 3.65 + DOWN * 0.55    # spread wider to fit bigger thumbs
    COS_THUMB = RIGHT * 3.50 + DOWN * 0.55
    FULL_CTR  = DOWN  * 0.75

    def construct(self):
        self.camera.background_color = BG_COLOR
        self._phase_intro()
        self._phase_math_steps()
        self._phase_cot_panel()
        self._phase_cos2_panel()
        self._phase_banner()

    # ── Phase 1 : title + "All Solutions" statement ───────────────────────────
    def _phase_intro(self):
        title = MathTex(
            r"\text{Graphical Analysis:}\quad \cot x\cos^2\!x = 2\cot x",
            font_size=34, color=TEXT_COLOR,
        ).to_edge(UP, buff=0.28)

        subtitle = MathTex(
            r"\text{Find: }\textbf{all solutions}\text{ --- no domain restriction on }x",
            font_size=26, color=ACCENT_BLUE,
        ).next_to(title, DOWN, buff=0.20)
        sub_box = SurroundingRectangle(
            subtitle, color=ACCENT_BLUE, stroke_width=1.5,
            fill_color="#050f1e", fill_opacity=0.50,
            buff=0.13, corner_radius=0.08,
        )

        title.set_z_index(10)                   # stays above scrim in cos² phase
        self.play(Write(title), run_time=1.1)
        self.play(Write(subtitle), run_time=0.9)
        self.play(Create(sub_box), run_time=0.40)
        self.wait(1.5)

        self.title    = title
        self.subtitle = VGroup(sub_box, subtitle)

    # ── Phase 2 : algebra steps ───────────────────────────────────────────────
    def _phase_math_steps(self):
        """
        Three visible algebra steps, each with a right-side annotation.
        Then the zero-product-property split, a warning box, and a bridge line.
        Everything fades out at the end, leaving only self.title.
        """

        # ── three algebra steps ───────────────────────────────────────────
        s0 = MathTex(
            r"\cot x\cos^2\!x = 2\cot x",
            font_size=34, color=TEXT_COLOR,
        )
        s1 = MathTex(
            r"\cot x\cos^2\!x - 2\cot x = 0",
            font_size=34, color=TEXT_COLOR,
        )
        s2 = MathTex(
            r"\cot x\,(\cos^2\!x - 2) = 0",
            font_size=34, color=TEXT_COLOR,
        )

        ann0 = Tex(r"original equation",   font_size=21, color=TEXT_MUTED)
        ann1 = Tex(r"subtract $2\cot x$",  font_size=21, color=TEXT_MUTED)
        ann2 = Tex(r"factor out $\cot x$", font_size=21, color=TEXT_MUTED)

        # Stack equations in a column; position annotations to their right
        steps_col = VGroup(s0, s1, s2).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        steps_col.next_to(self.subtitle, DOWN, buff=0.40).to_edge(LEFT, buff=1.0)

        for step, ann in [(s0, ann0), (s1, ann1), (s2, ann2)]:
            ann.next_to(step, RIGHT, buff=0.45)

        # Small down-arrows between steps
        arr1 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s0.get_bottom() + s1.get_top()) / 2
        )
        arr2 = MathTex(r"\Downarrow", font_size=24, color=TEXT_MUTED).move_to(
            (s1.get_bottom() + s2.get_top()) / 2
        )

        # ── zero product property split ───────────────────────────────────
        zpp_lbl = Tex(r"\textbf{Zero Product Property:}", font_size=25, color=TEXT_MUTED)

        case1 = MathTex(r"\cot x = 0",        font_size=32, color=Q1_COLOR)
        or_tx = Tex(r"\textbf{or}",            font_size=25, color=TEXT_MUTED)
        case2 = MathTex(r"\cos^2\!x - 2 = 0", font_size=32, color=ACCENT_RED)
        cases_row = VGroup(case1, or_tx, case2).arrange(RIGHT, buff=0.50)

        zpp_grp = VGroup(zpp_lbl, cases_row).arrange(DOWN, buff=0.20)
        zpp_grp.next_to(s2, DOWN, buff=0.40).shift(RIGHT * 0.60)

        # ── warning box ───────────────────────────────────────────────────
        warn_tex = Tex(
            r"\textbf{[!] Do NOT divide by }$\cot x$\textbf{ --- that erases Case\,1!}",
            font_size=21, color=ACCENT_RED,
        )
        warn_box = SurroundingRectangle(
            warn_tex, color=ACCENT_RED, stroke_width=1.5,
            fill_color="#160404", fill_opacity=0.55,
            buff=0.13, corner_radius=0.08,
        )
        warn_grp = VGroup(warn_box, warn_tex)
        warn_tex.move_to(warn_box)
        warn_grp.next_to(zpp_grp, DOWN, buff=0.28)

        # ── bridge text ───────────────────────────────────────────────────
        bridge = Tex(
            r"Now let's verify each case graphically $\longrightarrow$",
            font_size=24, color=HIGHLIGHT,
        ).to_edge(DOWN, buff=0.38)

        # ── animate step by step ─────────────────────────────────────────
        self.play(FadeIn(s0, shift=RIGHT * 0.1), FadeIn(ann0), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr1), run_time=0.25)
        self.play(FadeIn(s1, shift=RIGHT * 0.1), FadeIn(ann1), run_time=0.70)
        self.wait(0.20)

        self.play(Write(arr2), run_time=0.25)
        self.play(FadeIn(s2, shift=RIGHT * 0.1), FadeIn(ann2), run_time=0.70)
        self.wait(0.35)

        self.play(Write(zpp_lbl), run_time=0.50)
        self.play(
            LaggedStart(Write(case1), Write(or_tx), Write(case2), lag_ratio=0.25),
            run_time=1.0,
        )
        self.wait(0.25)

        self.play(FadeIn(warn_grp, shift=UP * 0.08), run_time=0.60)
        self.wait(1.1)

        self.play(Write(bridge), run_time=0.65)
        self.wait(0.6)

        # Fade out everything except self.title
        self.play(
            FadeOut(VGroup(
                self.subtitle,
                s0, s1, s2,
                ann0, ann1, ann2,
                arr1, arr2,
                zpp_grp, warn_grp,
                bridge,
            )),
            run_time=0.85,
        )

    # ── Phase 3 : cot x = 0 graph ────────────────────────────────────────────
    def _phase_cot_panel(self):
        # ── build axes ────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 3 * PI + 0.2, PI / 2],
            y_range=[-4, 4, 1],
            x_length=9.6,
            y_length=4.8,
            axis_config={
                "color": AXIS_COLOR, "include_tip": True,
                "tip_length": 0.16, "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [-3, -2, -1, 1, 2, 3],
                "font_size": 22,
            },
        ).move_to(self.FULL_CTR)

        # graph chrome — simplified label (no "Panel A")
        border = SurroundingRectangle(
            axes, color=Q1_COLOR, stroke_width=2.0,
            fill_color="#030e08", fill_opacity=0.55,
            buff=0.25, corner_radius=0.12,
        )
        graph_lbl = MathTex(
            r"\text{Case 1: }\cot x = 0",
            font_size=28, color=Q1_COLOR,
        ).next_to(border, UP, buff=0.10)

        # x-tick labels
        xv = [0, PI/2, PI, 3*PI/2, 2*PI, 5*PI/2, 3*PI]
        xs = [r"0", r"\tfrac{\pi}{2}", r"\pi", r"\tfrac{3\pi}{2}",
              r"2\pi", r"\tfrac{5\pi}{2}", r"3\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=21, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(xv, xs)
        ])
        xe = MathTex(r"x", font_size=25, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.09)
        ye = MathTex(r"y", font_size=25, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.08)

        # asymptotes at x = π and x = 2π
        ak = dict(color=ASYM_C, dash_length=0.12, stroke_width=1.4)
        a1  = DashedLine(axes.c2p(PI,   -3.85), axes.c2p(PI,   3.85), **ak)
        a2  = DashedLine(axes.c2p(2*PI, -3.85), axes.c2p(2*PI, 3.85), **ak)
        al1 = MathTex(r"x=\pi",  font_size=18, color=ASYM_C).next_to(
            axes.c2p(PI,   3.85), UP, buff=0.05)
        al2 = MathTex(r"x=2\pi", font_size=18, color=ASYM_C).next_to(
            axes.c2p(2*PI, 3.85), UP, buff=0.05)

        # cot x — three branches (EPS=0.25 keeps values within y_range)
        bk = dict(color=ACCENT_TEAL, stroke_width=3)
        b1 = axes.plot(_cot, x_range=[0 + EPS,    PI - EPS,    0.01], **bk)
        b2 = axes.plot(_cot, x_range=[PI + EPS,   2*PI - EPS,  0.01], **bk)
        b3 = axes.plot(_cot, x_range=[2*PI + EPS, 3*PI - EPS,  0.01], **bk)
        c_lbl = MathTex(r"y = \cot x", font_size=25, color=ACCENT_TEAL).next_to(
            axes.c2p(PI * 0.30, _cot(PI * 0.30)), UR, buff=0.14)

        # y = 0 reference line
        ref = axes.plot(lambda x: 0, x_range=[0, 3*PI],
                        color=Q1_COLOR, stroke_width=2.8)
        ref_lbl = MathTex(r"y = 0", font_size=23, color=Q1_COLOR).next_to(
            axes.c2p(0.2, 0), UL, buff=0.12)

        # ── animate graph ────────────────────────────────────────────────
        self.play(FadeIn(border), Write(graph_lbl), Create(axes), run_time=1.1)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.09),
            Write(xe), Write(ye), run_time=0.85,
        )
        self.play(
            LaggedStart(
                AnimationGroup(Create(a1), Create(a2)),
                AnimationGroup(Write(al1), Write(al2)),
                lag_ratio=0.30,
            ), run_time=0.80,
        )
        self.play(
            LaggedStart(Create(b1), Create(b2), Create(b3), lag_ratio=0.20),
            run_time=2.2,
        )
        self.play(Write(c_lbl), run_time=0.55)
        self.wait(0.3)
        self.play(Create(ref), Write(ref_lbl), run_time=0.90)
        self.wait(0.3)

        # ── annotation: why cot x = 0 ────────────────────────────────────
        annot = MathTex(
            r"\cot x = \dfrac{\cos x}{\sin x} = 0"
            r"\;\Longrightarrow\; \cos x = 0",
            font_size=24, color=Q1_COLOR,
        ).next_to(axes.c2p(3*PI/2, -2.6), DOWN, buff=0.22)

        self.play(Write(annot), run_time=1.0)
        self.wait(0.3)

        # ── mark zeros at π/2, 3π/2, 5π/2 ───────────────────────────────
        zero_mobs = []
        for x_val, lbl_s, ntag_s in [
            (PI / 2,   r"\tfrac{\pi}{2}",  r"n = 0"),
            (3*PI/2,   r"\tfrac{3\pi}{2}", r"n = 1"),
            (5*PI/2,   r"\tfrac{5\pi}{2}", r"n = 2"),
        ]:
            pt   = axes.c2p(x_val, 0)
            dot  = Dot(pt, radius=0.12, color=HIGHLIGHT, z_index=5)
            xlbl = MathTex(lbl_s, font_size=24, color=HIGHLIGHT).next_to(pt, DOWN, buff=0.22)
            ntag = Tex(ntag_s, font_size=18, color=Q1_COLOR).next_to(dot, UP, buff=0.09)
            self.play(FadeIn(dot, scale=1.7), Write(xlbl), Write(ntag), run_time=0.75)
            self.wait(0.10)
            zero_mobs.extend([dot, xlbl, ntag])

        self.wait(0.35)

        # ── general solution box inside graph ─────────────────────────────
        gen_sol = MathTex(
            r"x = \dfrac{\pi}{2} + \pi n,\quad n \in \mathbb{Z}",
            font_size=26, color=HIGHLIGHT,
        ).move_to(axes.c2p(3*PI/2, 3.0))
        gen_box = SurroundingRectangle(
            gen_sol, color=HIGHLIGHT, stroke_width=1.5,
            fill_color="#181000", fill_opacity=0.60,
            buff=0.12, corner_radius=0.08,
        )
        self.play(DrawBorderThenFill(gen_box), Write(gen_sol), run_time=0.90)
        self.wait(0.85)

        # ── pack & shrink to left thumbnail ──────────────────────────────
        self.cot_vg = VGroup(
            border, graph_lbl, axes, x_lbls, xe, ye,
            a1, a2, al1, al2,
            b1, b2, b3, c_lbl,
            ref, ref_lbl,
            annot,
            *zero_mobs,
            gen_box, gen_sol,
        )
        self.play(
            self.cot_vg.animate.scale(self.SMALL).move_to(self.COT_THUMB),
            run_time=1.3,
        )
        self.wait(0.3)

    # ── Phase 4 : cos²x = 2 graph (impossible) ───────────────────────────────
    def _phase_cos2_panel(self):
        # Dark scrim covers cot thumbnail so it doesn't bleed through
        scrim = Rectangle(
            width=16, height=10,
            fill_color=BG_COLOR, fill_opacity=0.95,
            stroke_width=0,
        )
        self.play(FadeIn(scrim), run_time=0.35)
        self.scrim = scrim      # keep reference for banner phase

        # ── build axes ────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 2 * PI + 0.2, PI / 2],
            y_range=[-0.3, 2.8, 1],
            x_length=8.5,
            y_length=4.8,
            axis_config={
                "color": AXIS_COLOR, "include_tip": True,
                "tip_length": 0.15, "stroke_width": 1.8,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [1, 2],
                "font_size": 22,
            },
        ).move_to(self.FULL_CTR)

        # graph chrome — simplified label (no "Panel B")
        border = SurroundingRectangle(
            axes, color=ACCENT_RED, stroke_width=2.0,
            fill_color="#100505", fill_opacity=0.55,
            buff=0.25, corner_radius=0.12,
        )
        graph_lbl = MathTex(
            r"\text{Case 2: }\cos^2\!x = 2\;?",
            font_size=28, color=ACCENT_RED,
        ).next_to(border, UP, buff=0.10)

        # x-tick labels
        xv = [0, PI/2, PI, 3*PI/2, 2*PI]
        xs = [r"0", r"\tfrac{\pi}{2}", r"\pi", r"\tfrac{3\pi}{2}", r"2\pi"]
        x_lbls = VGroup(*[
            MathTex(s, font_size=21, color=TICK_COLOR)
              .next_to(axes.c2p(v, 0), DOWN, buff=0.22)
            for v, s in zip(xv, xs)
        ])
        xe = MathTex(r"x", font_size=25, color=AXIS_COLOR).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.09)
        ye = MathTex(r"y", font_size=25, color=AXIS_COLOR).next_to(
            axes.y_axis.get_top(), UP, buff=0.08)

        # y = cos²x
        cos2 = axes.plot(
            lambda x: np.cos(x) ** 2,
            x_range=[0, 2 * PI],
            color=ACCENT_BLUE, stroke_width=3,
        )
        cos2_lbl = MathTex(r"y = \cos^2\!x", font_size=25, color=ACCENT_BLUE).next_to(
            axes.c2p(PI / 4, np.cos(PI / 4) ** 2), UR, buff=0.14)

        # dashed ceiling at y = 1 (max of cos²x)
        ceil1 = DashedLine(
            axes.c2p(0, 1), axes.c2p(2 * PI, 1),
            color=ACCENT_TEAL, dash_length=0.15, stroke_width=1.6,
        )
        ceil1_lbl = MathTex(r"\max = 1", font_size=22, color=ACCENT_TEAL).next_to(
            axes.c2p(2 * PI * 0.84, 1), DR, buff=0.07)

        # y = 2 (impossible target)
        y2_graph = axes.plot(lambda x: 2.0, x_range=[0, 2 * PI],
                             color=ACCENT_RED, stroke_width=2.8)
        y2_lbl = MathTex(r"y = 2\;\text{(target)}", font_size=24, color=ACCENT_RED).next_to(
            axes.c2p(2 * PI * 0.72, 2.0), UR, buff=0.08)

        # "No intersection" stamp
        no_sol = VGroup(
            Tex(r"\textbf{No intersection!}", font_size=30, color=ACCENT_RED),
            MathTex(
                r"|\cos x| \le 1 \;\Rightarrow\; \cos^2\!x \le 1 < 2",
                font_size=24, color=ACCENT_RED,
            ),
        ).arrange(DOWN, buff=0.16).move_to(axes.c2p(PI, 1.50))

        # ── animate graph ────────────────────────────────────────────────
        self.play(FadeIn(border), Write(graph_lbl), Create(axes), run_time=1.0)
        self.play(
            LaggedStart(*[Write(l) for l in x_lbls], lag_ratio=0.09),
            Write(xe), Write(ye), run_time=0.80,
        )
        self.play(Create(cos2), Write(cos2_lbl), run_time=1.0)
        self.play(Create(ceil1), Write(ceil1_lbl), run_time=0.70)
        self.wait(0.2)
        self.play(Create(y2_graph), Write(y2_lbl), run_time=0.80)
        self.wait(0.3)
        self.play(Write(no_sol), run_time=0.90)
        self.wait(0.85)

        # ── pack & shrink to right thumbnail ──────────────────────────────
        self.cos_vg = VGroup(
            border, graph_lbl, axes, x_lbls, xe, ye,
            cos2, cos2_lbl,
            ceil1, ceil1_lbl,
            y2_graph, y2_lbl,
            no_sol,
        )
        self.play(
            self.cos_vg.animate.scale(self.SMALL).move_to(self.COS_THUMB),
            FadeOut(self.scrim),       # reveal cot thumbnail underneath
            run_time=1.2,
        )
        self.wait(0.5)

    # ── Phase 5 : solution banner ─────────────────────────────────────────────
    def _phase_banner(self):
        lbl_a = MathTex(
            r"\checkmark\;\cot x = 0", font_size=20, color=Q1_COLOR
        ).next_to(self.cot_vg, UP, buff=0.12)
        lbl_b = MathTex(
            r"\times\;\cos^2\!x = 2", font_size=20, color=ACCENT_RED
        ).next_to(self.cos_vg, UP, buff=0.12)

        self.play(Write(lbl_a), Write(lbl_b), run_time=0.70)
        self.wait(0.4)

        banner = RoundedRectangle(
            corner_radius=0.14,
            width=8.2, height=0.95,
            fill_color="#0b1d2e", fill_opacity=0.97,
            stroke_color=HIGHLIGHT, stroke_width=2.5,
        ).to_edge(DOWN, buff=0.18)

        sol = MathTex(
            r"x = \dfrac{\pi}{2} + \pi n, \quad n \in \mathbb{Z}",
            font_size=38, color=HIGHLIGHT,
        ).move_to(banner)

        self.play(DrawBorderThenFill(banner), run_time=0.60)
        self.play(Write(sol), run_time=1.25)
        self.wait(2.5)
