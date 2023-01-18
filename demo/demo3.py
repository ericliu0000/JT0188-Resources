from manim import *

class MDemo(Scene):
    def construct(self):
        # Make path and dot objects
        path = VMobject()
        dot = Dot().move_to((-2, -1, 0))
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        # Make the path a foreground object to make it look (and feel!) cooler
        self.add_foreground_mobjects(path)

        # Create four paths in the letter "M"
        l1 = Line((-2, -1, 0), (-2, 1, 0))
        l2 = Line((-2, 1, 0), (0, -1, 0))
        l3 = Line((0, -1, 0), (2, 1, 0))
        l4 = Line((2, 1, 0), (2, -1, 0))

        # Create path updater and add to path
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        # Create path and dot objects
        self.play(Create(path), Create(dot))

        # Move 
        self.play(MoveAlongPath(dot, l1))
        self.play(MoveAlongPath(dot, l2))
        self.play(MoveAlongPath(dot, l3))
        self.play(MoveAlongPath(dot, l4))

        # Destroy the dot from the face of the earth
        self.play(Uncreate(dot))

        # Remove the path updater
        path.remove_updater(update_path)

        # Scale the "M" down, and move it down
        self.play(path.animate().scale(0.5).shift(DOWN))

        # Do the pixar lamp animation with the "M," but be lazy about it
        # Make a circle object to be the lamp and move it to an okay location
        lamp = Circle(1, fill_opacity=1).move_to((0, 2, 0))
        self.play(Create(lamp))

        # Make the lamp bounce on top of the object and end up inside it, then wait a bit
        self.play(lamp.animate(run_time=3, rate_func=rate_functions.ease_out_bounce).shift(DOWN * 2.5))
        self.wait(2)

        # New scene! Move everything to the side to make a bar chart with various metrics
        lamp_path = Group(lamp, path)
        self.play(lamp_path.animate().shift(LEFT * 5))

        # Create a bar chart object and populate it with the following metrics:
        # lines: 4
        # hours slept: Probably 3 or something
        # manim: 10
        # yes: 2
        # Then, show it (and the labels) to the screen

        chart = BarChart(
            values=[4, 3, 10, 2],
            bar_names=["lines", "hours slept", "manim", "yes"],
            y_range=[0, 10, 1],
            y_length=6,
            x_length=8,
            x_axis_config={"font_size": 36},
        ).shift(RIGHT * 2)

        c_bar_lbls = chart.get_bar_labels(font_size=36)
        self.play(Create(chart), Create(c_bar_lbls))

        self.wait(3)

        # Break everything apart using Uncreate
        self.play(Uncreate(chart), Uncreate(c_bar_lbls))
        self.play(Uncreate(path))
        self.play(Uncreate(lamp))

        self.wait(0.5)