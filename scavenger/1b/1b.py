from manim import *

class Animation(Scene): 
    def construct(self):
        text = Text("here is some text!")

        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))