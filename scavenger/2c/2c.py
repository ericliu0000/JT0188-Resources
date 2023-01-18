from manim import *

class Animation(Scene): 
    def construct(self):
        a = Triangle().set_color(RED)
        a_t = Text("Blue", color=RED)

        b = Circle(2, GREEN)
        b_t = Text("Green", color=GREEN)

        c = Rectangle(BLUE)
        c_t = Text("Blue", color=BLUE)

        self.play(Create(a), Create(a_t))

        self.wait(2)
        self.play(ReplacementTransform(a, b), ReplacementTransform(a_t, b_t))

        self.wait(2)
        self.play(ReplacementTransform(b, c), ReplacementTransform(b_t, c_t))

        self.wait(2)