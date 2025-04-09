from ec import *
from random import randint


def create_dh_connection(curve: Curve, generator: tuple, order: int, name1: str = "Alice", name2: str = "Bob"):
    crypto_curve = curve.to_crypto_curve(generator, order)
    client1 = DHClient(crypto_curve, name1)
    client2 = DHClient(crypto_curve, name2)
    return client1, client2


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
        self._generate_keys()

    def __str__(self):
        length = 20

        top = f" CLIENT {self.name} "
        top = "+" + top.center(length + 2, "-") + "+"
        bottom = "\n+" + "-" * (length + 2) + "+"

        def row(inside, outside):
            return "\n| " + inside.center(length, " ") + " |  " + outside
        output = top
        output += row("", f"CURVE: {self.curve}")
        output += row(f"PRIVATE: {self._private}", f"PUBLIC: {self.public}")
        output += bottom
        
        return output

    def _generate_keys(self):
        # FIX: is the range correct?
        self._private = randint(2, self.curve.order - 1)  # NOT cryptographically secure
        self.public = self.curve.generator * self._private
    
    def get_shared_key(self, other):
        if not isinstance(other, DHClient): 
            raise ValueError("can only get shared key between two DHClients")
        if not self.curve == other.curve:
            raise ValueError("DHClients must share the same curve and generator")
        key = other.public * self._private

        return key
