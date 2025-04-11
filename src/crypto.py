from ec import *
from random import randint


def show_clients(*args):
    print()
    for client in args:
        print(client)

def dh_connect(client1, client2):
    client1.generate_shared_key(client2)
    client2.generate_shared_key(client1)

def dh_mesh_connect(*clients):
    i = 0
    for client in clients:
        i += 1
        for other in clients[i:]:
            dh_connect(client, other)

def dh_mesh_nx_graph(graph, *clients):
    for client in clients:
        graph.add_node(client.name)
    for client in clients:
        for name in client.keys:
            graph.add_edge(client.name, name)


class Curve(Curve):
    def to_crypto_curve(self, generator: tuple, order: int):
        return CryptoCurve(self.a, self.b, self.p, generator, order)
    

class CryptoCurve(Curve):
    def __init__(self, a: int, b: int, p: int, generator: tuple, order: int):
        Curve.__init__(self, a, b, p)
        if not is_coordinate(generator): raise ValueError("generator must be a valid coordinate")
        self.generator = self.point(generator[0], generator[1])
        self.order = order


class DHClient:
    def __init__(self, curve: CryptoCurve, name):
        self.curve = curve
        self.name = name
        self.keys = {}
        self._generate_keys()

    def __str__(self):
        length = 20

        top = f" CLIENT {self.name} "
        top = "+" + top.center(length + 2, "-") + "+"
        bottom = "\n+" + "-" * (length + 2) + "+\n"

        def row(inside, outside):
            return "\n| " + inside.center(length, " ") + " |  " + outside
        output = top
        output += row("", f"CURVE: {self.curve}")
        output += row(f"PRIVATE: {self._private}", f"PUBLIC: {self.public}")

        for name in self.keys:
            output += row(f"{name}: {self.keys[name]}", "")

        output += bottom
        
        return output

    def _generate_keys(self):
        # FIX: is the range correct?
        self._private = randint(2, self.curve.order - 1)  # NOT cryptographically secure
        self.public = self.curve.generator * self._private
    
    def generate_shared_key(self, other):
        if not isinstance(other, DHClient): 
            raise ValueError("can only get shared key between two DHClients")
        if not self.curve == other.curve:
            raise ValueError("DHClients must share the same CryptoCurve")
        key = other.public * self._private

        self.keys[other.name] = key
