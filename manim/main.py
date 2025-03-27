from manim import *

class EC(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x**3 + 7 - y**2,
            color=BLUE
        )
        plane = NumberPlane()
        self.add(plane)
        self.play(Create(graph))


if __name__ == "__main__":
    with tempconfig({"preview": True}):
        scene = EC()
        scene.render()