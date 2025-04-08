import matplotlib.pyplot as plt
from ec import *
from crypto import *
    

curve = Curve(4, 20, 29)
print(curve)


def add_demo():
    p1 = curve.point(5, 22)
    p2 = curve.point(16, 27)
    print(p1, "+", p2, "=", p1 + p2)

def mul_demo():
    x, y = [], []

    p1 = curve.point(5, 22)
    p = p1
    k = 1
    while k < 40:
        p = k * p1
        print(f"{k} * {p1} = {p}")
        x.append(p.x)
        y.append(p.y)
        k += 1

    plt.plot(x, y, "o")
    plt.title(curve)
    plt.show()

def inf_demo():
    p1 = curve.point(5, 22)
    p2 = curve.point(5, 7)
    print(f"{p1} + {p2} = {p1 + p2}")

def crypto_demo():
    crypto_curve = curve.to_crypto_curve((5, 22), 37)
    alice = Client(crypto_curve, "Alice")
    bob = Client(crypto_curve, "Bob")

    print()
    print(alice)
    print(bob)

    k1 = alice.get_shared_key(bob)
    k2 = bob.get_shared_key(alice)
    print(k1, k2)


crypto_demo()
