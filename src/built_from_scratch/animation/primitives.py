from manim import *

from built_from_scratch.animation.style import (
    BFS_PRIMARY,
    BFS_SECONDARY,
    BFS_ACCENT,
    BFS_HIGHLIGHT,
    BFS_STROKE_WIDTH,
    BFS_GRID_STROKE_WIDTH,
    BFS_GRID_OPACITY,
    BFS_LABEL_SIZE,
)


class BFSGrid(VGroup):
    """Subtle background grid."""

    def __init__(
        self,
        x_range=(-7, 7, 1),
        y_range=(-4, 4, 1),
        **kwargs,
    ):
        super().__init__(**kwargs)

        grid = NumberPlane(
            x_range=x_range,
            y_range=y_range,
            background_line_style={
                "stroke_color": BFS_SECONDARY,
                "stroke_width": BFS_GRID_STROKE_WIDTH,
                "stroke_opacity": BFS_GRID_OPACITY,
            },
            axis_config={
                "stroke_opacity": 0,
            },
        )

        self.add(grid)


class BFSAxes(Axes):
    """Standard Built From Scratch coordinate system."""

    def __init__(
        self,
        x_range=(-5, 5, 1),
        y_range=(-3, 3, 1),
        x_length=10,
        y_length=6,
        **kwargs,
    ):
        super().__init__(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={
                "stroke_color": BFS_PRIMARY,
                "stroke_width": BFS_STROKE_WIDTH,
                "include_ticks": True,
                "include_numbers": False,
            },
            tips=True,
            **kwargs,
        )


class BFSLabel(Text):
    """Standard text label."""

    def __init__(
        self,
        text,
        font_size=BFS_LABEL_SIZE,
        color=BFS_PRIMARY,
        **kwargs,
    ):
        super().__init__(
            text,
            font_size=font_size,
            color=color,
            **kwargs,
        )


class BFSVector(Arrow):
    """Standard vector/arrow."""

    def __init__(
        self,
        start,
        end,
        color=BFS_ACCENT,
        **kwargs,
    ):
        super().__init__(
            start=start,
            end=end,
            color=color,
            stroke_width=BFS_STROKE_WIDTH,
            buff=0,
            **kwargs,
        )


class BFSHighlight(SurroundingRectangle):
    """Highlight an important mathematical object."""

    def __init__(
        self,
        mobject,
        color=BFS_HIGHLIGHT,
        buff=0.15,
        **kwargs,
    ):
        super().__init__(
            mobject,
            color=color,
            stroke_width=BFS_STROKE_WIDTH,
            buff=buff,
            **kwargs,
        )

class BFSMathLabel(MathTex):
    """Standard mathematical label."""

    def __init__(
        self,
        tex,
        font_size=BFS_LABEL_SIZE,
        color=BFS_PRIMARY,
        **kwargs,
    ):
        super().__init__(
            tex,
            font_size=font_size,
            color=color,
            **kwargs,
        )