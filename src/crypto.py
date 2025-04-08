from ec import *
from random import randint

class Curve(Curve):
    def to_crypto_curve(self, generator: tuple, order: int):
        return CryptoCurve(self.a, self.b, self.p, generator, order)
    

class CryptoCurve(Curve):
    def __init__(self, a: int, b: int, p: int, generator: tuple, order: int):
        Curve.__init__(self, a, b, p)
        if not is_coordinate(generator): raise ValueError("generator must be a valid coordinate")
        self.generator = self.point(generator[0], generator[1])
        self.order = order


class Client:
    def __init__(self, curve: CryptoCurve, name):
        self.curve = curve
        self.name = name
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
        output += bottom
        
        return output

    def _generate_keys(self):
        # FIX: is the range correct?
        self._private = randint(2, self.curve.order - 1)  # NOT cryptographically secure
        self.public = self.curve.generator * self._private
    
    def get_shared_key(self, other, quiet=False):
        if not isinstance(other, Client): 
            raise ValueError("can only get shared key between two Clients")
        if not self.curve == other.curve:
            raise ValueError("Clients must share the same curve and generator")
        key = other.public * self._private

        if not quiet:
            print("sharing key :)")

        return key
