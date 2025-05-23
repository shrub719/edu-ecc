import matplotlib.pyplot as plt
import networkx as nx
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

    dh_mesh_connect(alice, bob, charlie)

    show_clients(alice, bob, charlie)

    G = nx.Graph()
    dh_mesh_nx_graph(G, alice, bob, charlie)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def ecdh_mesh_demo():
    n = 50

    crypto_curve = curve.to_crypto_curve((5, 22), 37)
    clients = [DHClient(crypto_curve, str(i)) for i in range(n)]
    show_clients(*clients)

    dh_mesh_connect(*clients)
    show_clients(*clients)
    
    G = nx.Graph()
    dh_mesh_nx_graph(G, *clients)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


def big_demo():
    x, y = [], []
    big = Curve(0, 7, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
    g = big.point(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
    k = 1
    while k <= 1000:
        g = k * g
        x.append(g.x)
        y.append(g.y)
        k += 1

    plt.plot(x, y, "o")
    plt.title(big)
    plt.show()

big_demo()
