from manim import *

class Animation(Scene): 
    def construct(self):
        shape = Circle(radius=2, color=ORANGE)

        self.play(Create(shape))
        self.wait(3)
        self.play(FadeOut(shape))