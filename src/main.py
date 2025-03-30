# from tinyec.ec import SubGroup, Curve
# import matplotlib.pyplot as plt

# field = SubGroup(p=17, g=(15, 13), n=18, h=1)
# curve = Curve(a=0, b=7, field=field, name="p1707")

class Curve:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def _coefficient(x):
        if x < 0: return f"- {x}"
        else: return f"+ {x}"
    
    def __repr__(self):
        a = self._coefficient(self.a)
        b = self._coefficient(self.b)
        
        return f"y^2 = x^3 {a}x {b}"

curve = Curve(0, 7)
print(curve)

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