from manim import *

class Animation(Scene): 
    def construct(self):
        mobject = Circle(3, color=GREEN_C)
        text = Text("Here is my equation").shift(DOWN * 2)
        equation = MathTex("f(x)").move_to(mobject, UP)
        # equation = Text("f(x)").move_to(mobject, UP)

        self.play(Create(mobject))
        self.play(mobject.animate().shift(LEFT * 3))
        self.play(Write(text))
        self.play(Create(equation))
        self.wait(2)
        self.play(FadeOut(mobject, text, equation))
        self.wait(1)