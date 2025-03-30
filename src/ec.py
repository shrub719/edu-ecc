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

def is_coordinate(x):
    if not isinstance(x, tuple): return False
    if len(x) != 2: return False
    if x == (None, None): return True
    if not (type(x[0]) is int and type(x[1]) is int): return False
    return True


class Curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
    
    def __repr__(self):
        a = coefficient(self.a)
        b = coefficient(self.b)

        return f"y^2 = x^3 {a}x {b} (mod {self.p})"
    
    def implicit(self):  # converts to manim implicit lambda function
        # graph = ImplicitFunction(
        #     lambda x, y: x**3 + 7 - y**2,
        #     color=BLUE
        # )
        def func(x, y):
            return x**3 + self.a * x + self.b * x - y**2
        return func
    
    def point(self, x, y):
        if x == None and y == None:
            return Point(self, x, y)
        
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
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        if is_coordinate(other):
            return self.x == other[0] and self.y == other[1]
        
        return False
        

    def __add__(self, other):
        if not isinstance(other, Point): 
            raise TypeError("points can only be added to other points")
        if self == other:
            return self.double()
        if self == (None, None):
            return other
        if other == (None, None):
            return self

        x1, y1, x2, y2 = self.x, self.y, other.x, other.y

        l = self.div((y2 - y1), (x2 - x1))
        if l == None:
            return self.curve.point(None, None)  # point at infinity

        x3 = l**2 - x1 - x2
        y3 = l * (x1 - x3) - y1

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
        if self == (None, None):
            return self
        
        x1, y1 = self.x, self.y
        a = self.curve.a

        # TODO: test when it's its own inverse
        l = self.div((3*x1**2 + a), (2*y1))
        if l == None:
            return self.curve.point(None, None)  # point at infinity

        x3 = l**2 - 2*x1
        y3 = l * (x1 - x3) - y1

        x3 = x3 % self.curve.p
        y3 = y3 % self.curve.p

        return self.curve.point(x3, y3)
    
    def div(self, a, b):
        try:
            return divide(a, b, self.curve.p)
        except ValueError:
            return
