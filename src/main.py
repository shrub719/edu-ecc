from tinyec.ec import SubGroup, Curve
from manim import *  # TODO: install manim, doesn't work on mb

class EC(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x ** 3 + 3 - y**2,
            color=BLUE
        )
        self.add(NumberPlane(), graph)


field = SubGroup(p=17, g=(15, 13), n=18, h=1)
curve = Curve(a=0, b=7, field=field, name="p1707")

print(curve)

for k in range(25):
    p = k * curve.g
    print(f"{k}G = ({p.x}, {p.y})")