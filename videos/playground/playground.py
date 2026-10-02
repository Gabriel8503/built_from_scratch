from manim import *

from built_from_scratch.animation.primitives import (
    BFSGrid,
    BFSAxes,
    BFSLabel,
    BFSMathLabel,
    BFSVector,
    BFSHighlight,
)


class Playground(Scene):

    def construct(self):

        # ----------------------------------------------------
        # Background
        # ----------------------------------------------------

        grid = BFSGrid()
        self.add(grid)

        # ----------------------------------------------------
        # Title
        # ----------------------------------------------------

        title = BFSLabel(
            "Built From Scratch",
            font_size=40,
        )

        subtitle = BFSLabel(
            "Mathematics • Engineering • Computation",
            font_size=22,
            color=GRAY_B,
        )

        subtitle.next_to(title, DOWN, buff=0.15)

        self.play(Write(title))
        self.play(FadeIn(subtitle))

        self.wait(1)

        self.play(FadeOut(title))
        self.play(FadeOut(subtitle))

        # ----------------------------------------------------
        # Coordinate system
        # ----------------------------------------------------

        axes = BFSAxes()

        self.play(
            Create(axes),
            run_time=1.5,
        )


        # ----------------------------------------------------
        # Vector
        # ----------------------------------------------------

        vector = BFSVector(
            axes.c2p(0, 0),
            axes.c2p(3, 2),
        )

        label = BFSMathLabel(
            r"\vec{v}",
            font_size=30,
            color=BLUE_C,
        )

        label.next_to(vector.get_end(), UP + RIGHT)

        self.play(
            GrowArrow(vector),
            Write(label),
        )

        # ----------------------------------------------------
        # Highlight
        # ----------------------------------------------------

        highlight = BFSHighlight(vector)

        self.play(
            Create(highlight),
        )

        self.wait(1)

        # ----------------------------------------------------
        # Equation
        # ----------------------------------------------------


        equation = MathTex(
            r"\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}",
            font_size=21,
        )

        equation.move_to(axes.c2p(1,1.75))


        self.play(
            Write(equation),
        )

        self.wait(2)

        self.play(
            FadeOut(highlight),
            FadeOut(vector),
            FadeOut(label),
            FadeOut(axes),
            FadeOut(equation),
        )