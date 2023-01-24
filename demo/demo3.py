from manim import *

class MDemo(Scene):
    def construct(self):
        # Make path and dot objects
        path = VMobject()
        dot = Dot().move_to((-1, -1, 0))
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        # Create four paths in the letter "M"
        cheese = Line((-1, -1, 0), (-1, 2, 0))
        l1 = Line((-1, 2, 0), (0, -1, 0))
        lines = Line((0, -1, 0), (1, 2, 0))
        cheese2 = Line((1, 2, 0), (1, -1.25, 0))
        
        # Create path updater and add to path
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        # Create path and dot objects
        self.play(Create(path), Create(dot))

        # Move 
        self.play(MoveAlongPath(dot, cheese))
        self.play(MoveAlongPath(dot, l1))
        self.play(MoveAlongPath(dot, lines))
        self.play(MoveAlongPath(dot, cheese2))

        # Destroy the dot from the face of the earth
        self.play(Uncreate(dot))

        # Remove the path updater
        path.remove_updater(update_path)

        # Scale the "M" down, and move it down
        self.play(path.animate().scale(0.5).shift(DOWN + LEFT))

        # Do the pixar lamp animation with the "M," but be lazy about it
        # Make a circle object to be the lamp and move it to an okay location
        lamp = Circle(0.5, fill_opacity=1).move_to((-1, 1, 0))
        self.play(Create(lamp))
        self.play(lamp.animate(rate_func=rate_functions.ease_out_bounce).shift(DOWN * 2))

        # Make the lamp bounce on top of the object and end up inside it, then wait a bit
        self.wait(1)

        # New scene! Move everything to the side to make a bar chart with various metrics
        group = Group(path, lamp)
        # self.play(path.animate().shift(LEFT * 4), lamp.animate().shift(LEFT * 4))
        self.play(group.animate().shift(LEFT * 4))

        # Create a bar chart object and populate it with the following metrics:
        # lines: 4
        # hours slept: Probably 3 or something
        # manim: 10
        # yes: 2
        # Then, show it (and the labels) to the screen
        chart = BarChart(
            values = [4, 3, 10, 2],
            bar_names = ["lines", "hours slept", "manim", "yes"],
            y_range = [0, 15, 2],
            y_length = 6,
            x_length = 10,
            x_axis_config={"font_size": 36}
        ).shift(RIGHT * 2)
        c_bar_lbls = chart.get_bar_labels(font_size=48)

        self.play(FadeIn(chart), FadeIn(c_bar_lbls))

        self.wait(3)

        # Break everything apart using Uncreate
        self.play(Unwrite(chart), Unwrite(c_bar_lbls))
        self.play(Uncreate(path))
        self.play(Uncreate(lamp))
