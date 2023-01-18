from manim import *


class Reduction(Scene):
    def construct(self):
        # Create the sulfur atom (r=0.5, yellow, solid fill)
        s = Circle(0.5, YELLOW_A, fill_opacity=1)

        # Create the electron (r=0.25, blue, solid fill)
        e = Circle(0.25, BLUE_B, fill_opacity=1)

        # Make a copy of the electron
        e2 = e.copy()

        # Group the sulfur atom and both electrons together
        elements = Group(s, e, e2)

        # Create top and bottom text objects styled however you want
        # Top text should say "Oxidation"
        # Bottom text should contain the oxidation reaction of Sulfur
        ox_text = MarkupText("Oxidation", font_size=36, font="IBM Plex Mono", color=WHITE).shift(UP * 2)
        ox_rxn = MarkupText("S<sup>2-</sup> → S + 2e<sup>-</sup>", font_size=36, font="IBM Plex Mono", color=WHITE).shift(DOWN * 2)

        # Create top and bottom text objects styled however you want
        # Top text should say "Reduction"
        # Bottom text should contain the reduction reaction of Sulfur
        red_text = MarkupText("Reduction", font_size=36, font="IBM Plex Mono", color=WHITE).shift(UP * 2)
        red_rxn = MarkupText("S + 2e<sup>-</sup> → S<sup>2-</sup>", font_size=36, font="IBM Plex Mono", color=WHITE).shift(DOWN * 2)

        # Create sulfur object
        self.play(Create(s))

        # Fade in both electrons
        self.play(FadeIn(e, e2))
        
        # Move both electrons down and away from the sulfur atom (one to the left, one to the right) (animation run times = 1 second)
        self.play(e.animate(run_time=1).shift(1 * np.array((3.7, 2.0, 0.0)) + 1 * RIGHT), e2.animate(run_time=1).shift(DOWN + LEFT))

        # Make oxidation text objects, then wait for 3 seconds
        self.play(Create(ox_text), Create(ox_rxn))
        self.wait(3)

        # Uncreate the oxidation text, and animate the full elements group shifting right 10 units (animation run time = 1 second)
        self.play(Uncreate(ox_text), Uncreate(ox_rxn), elements.animate(run_time=1).shift(RIGHT * 10))

        # Shift (do not animate) the elements group left 20 units
        elements.shift(LEFT * 20)

        # Animate the full elements group shifting right 10 units
        self.play(elements.animate(run_time=1).shift(RIGHT * 10))

        # Tip: These animations are the same as the ones above for oxidation; just flipped in many ways
        # Move both electrons up and into the sulfur atom (one to the left, one to the right) (animation run times = 1 second)
        self.play(e.animate(run_time=1).shift(UP + LEFT), e2.animate(run_time=1).shift(UP + RIGHT))

        # Fade out both electrons
        self.play(FadeOut(e, e2))

        # Make reduction text objects, then wait for 3 seconds
        self.play(Create(red_text), Create(red_rxn))
        self.wait(3)

        # Uncreate the reduction text, and animate the full elements group shifting right 10 units (animation run time = 1 second)
        self.play(Uncreate(red_text), Uncreate(red_rxn), elements.animate(run_time=1).shift(RIGHT * 10))
