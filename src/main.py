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
    charlie = DHClient(crypto_curve, "Charlie")

    show_clients(alice, bob)
    # input()

    dh_mesh_connect(alice, bob, charlie)

    show_clients(alice, bob, charlie)
    dh_mesh_show(alice, bob, charlie)
    # input()

def ecdh_mesh_demo():
    crypto_curve = curve.to_crypto_curve((5, 22), 37)
    clients = [DHClient(crypto_curve, str(i)) for i in range(10)]
    show_clients(*clients)

    dh_mesh_connect(*clients)
    show_clients(*clients)
    dh_mesh_show(*clients)


ecdh_demo()
ecdh_mesh_demo()
