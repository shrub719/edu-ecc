import matplotlib.pyplot as pl
import math


def coefficient(x):
    if x < 0: 
        return f"- {x}"
    else: 
        return f"+ {x}"

def inverse(x, m):
    g = math.gcd(x, m) 
    if (g != 1):
        raise ValueError(f"inverse of {x} does not exist mod {m}")
    else:  
        # modulo inverse is b^(m-2) mod m - ??!??!?!
        return pow(x, m - 2, m)
    # TODO: use euclid algorithm

def divide(a, b, m):
    a = a % m
    inv = inverse(b, m)
    return (inv * a) % m


class Curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
    
    def __repr__(self):
        a = coefficient(self.a)
        b = coefficient(self.b)

        return f"y^2 = x^3 {a}x {b}"
    
    def point(self, x, y):
        p = self.p
        y_side = y**2 % p
        x_side = (x**3 + self.a * x + self.b) % p
        if y_side != x_side:
            raise ValueError(f"point ({x}, {y}) does not exist on curve {self}")
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
            raise TypeError("points can only be added to other points")
        if self == other:
            return self.double()

        x1, y1, x2, y2 = self.x, self.y, other.x, other.y

        x3 = self.div((y2 - y1), (x2 - x1))**2 - x1 - x2
        y3 = self.div((y2 - y1), (x2 - x1)) * (x1 - x3) - y1

        x3 = x3 % self.curve.p
        y3 = y3 % self.curve.p

        return self.curve.point(x3, y3)
    
    def __mul__(self, scalar: int):
        if not isinstance(scalar, int): 
            raise TypeError("points must be multiplied by an integer scalar")
        
        product = self
        for i in range(scalar-1):
            product = product + self
        
        return product

    __rmul__ = __mul__

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def double(self):
        x1, y1 = self.x, self.y
        a = self.curve.a

        x3 = self.div((3*x1**2 + a), (2*y1))**2 - 2*x1
        y3 = self.div((3*x1**2 + a), (2*y1)) * (x1 - x3) - y1

        x3 = x3 % self.curve.p
        y3 = y3 % self.curve.p

        return self.curve.point(x3, y3)
    
    def div(self, a, b):
        return divide(a, b, self.curve.p)


curve = Curve(4, 20, 29)
print(curve)

p1 = curve.point(5, 22)
p2 = curve.point(16, 27)
print(p1, "+", p2, "=", p1 + p2)


# TODO: add point at infinity

x, y = [], []

p = p1
k = 1
while k < 37:
    p = k * p1
    print(f"{k} * {p2} = {p}")
    x.append(p.x)
    y.append(p.y)
    k += 1

pl.plot(x, y, "o")
pl.show()