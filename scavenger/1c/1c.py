from manim import *

class Animation(Scene): 
    def construct(self):
        image_a = ImageMobject("1ca.jpg")
        image_b = ImageMobject("1cb.png").set_opacity(0.4)
        text = Text("dish washer", color=BLUE)

        self.play(FadeIn(image_a), Create(text))
        self.wait(1)
        self.play(FadeIn(image_b))
        self.wait(3)

        self.play(FadeOut(image_a, image_b, text))