# from tinyec.ec import SubGroup, Curve
# import matplotlib.pyplot as plt

# field = SubGroup(p=17, g=(15, 13), n=18, h=1)
# curve = Curve(a=0, b=7, field=field, name="p1707")

class Curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    @staticmethod
    def _coefficient(x):
        if x < 0: 
            return f"- {x}"
        else: 
            return f"+ {x}"
    
    def __repr__(self):
        a = self._coefficient(self.a)
        b = self._coefficient(self.b)

        return f"y^2 = x^3 {a}x {b}"
    
    def point(self, x, y):
        return Point(self, x, y)
    
class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y  # TODO: encode as even/odd?

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if not isinstance(other, Point): 
            raise TypeError
        if self == other:
            return self.__mul__(2)

        x1, y1, x2, y2 = self.x, self.y, other.x, other.y

        x3 = ( (y2 - y1) // (x2 - x1) )^2 - x1 - x2
        y3 = ( (y2 - y1) // (x2 - x1) ) * (x1 - x3) - y1
        return self.curve.point(x3, y3)
    
    def __mul__(self, other):
        return "AH"  # TODO

    def __repr__(self):
        return f"({self.x}, {self.y})"


curve = Curve(4, 20, 29)
print(curve)
p1 = curve.point(5, 22)
p2 = curve.point(16, 27)
print(p1, "+", p2, "=", p1 + p2)  # FIX well. it's wrong

# x = []
# y = []
# p = curve.g
# k = 1
# while p.x:
#     p = k * curve.g
#     print(f"{k}G = ({p.x}, {p.y})")
#     x.append(p.x)
#     y.append(p.y)
#     k += 1

# plt.plot(x, y, "o")
# plt.show()