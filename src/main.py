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

def ecdh_demo():
    crypto_curve = curve.to_crypto_curve((5, 22), 37)
    alice = DHClient(crypto_curve, "Alice")
    bob = DHClient(crypto_curve, "Bob")

    show_clients(alice, bob)
    input()

    alice.generate_shared_key(bob)
    bob.generate_shared_key(alice)
    k1, k2 = alice.keys["Bob"], bob.keys["Alice"]

    show_clients(alice, bob)
    input()


ecdh_demo()
