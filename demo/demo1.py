from manim import *


'''
Either one of ``"spring"`` (the default), ``"circular"``, ``"kamada_kawai"``,
``"planar"``, ``"random"``, ``"shell"``, ``"spectral"``, ``"spiral"``, ``"tree"``, and ``"partite"``

'''
# class name


class Example1(Scene):
    def construct(self):

        # create a path graph of 6 vertices, with circular layout
        g = Graph([0, 1, 2, 3, 4, 5], [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], 
                layout="spring")
        # create a path graph of 6 vertices, with spring layout
        g2 = Graph([0, 1, 2, 3, 4, 5], [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], 
                layout="circular")

        # g3 = Graph(list(range(50)), [(i, i + 1) for i in range(50)])

        # draw the graph
        self.play(Create(g))

        # highlight each vertex
        for i in range(6):
            self.play(Indicate(g.vertices[i], color=BLUE, radius=5, run_time=2))
            self.wait(0.2)

        # wait for 2 seconds
        self.wait(2)
        # draw the graph
        self.play(ReplacementTransform(g, g2))
        # wait for 2 seconds
        self.wait(2)
        for i in range(6):
            self.play(Indicate(g.vertices[i], color=RED, radius=5))
            self.wait(0.05)
        self.wait(2)
