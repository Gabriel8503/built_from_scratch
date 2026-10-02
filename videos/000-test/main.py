from manim import *


class TestScene(Scene):
    def construct(self):
        circle = Circle()
        text = Text("Built From Scratch")

        self.play(Create(circle))
        self.play(Write(text))
        self.wait()
