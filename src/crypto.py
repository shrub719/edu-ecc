from ec import *
from random import randint

class Client:
    def __init__(self, curve: Curve, generator: tuple, order: int):
        self.curve = curve
        if not is_coordinate(generator): raise ValueError("generator must be a valid coordinate")
        self.generator = self.curve.point(generator[0], generator[1])
        self.generate_keys(order)

    def generate_keys(self, order: int):
        # FIX: is the range correct?
        self.__private = randint(2, order-1)  # NOT cryptographically secure
        self.public = self.generator * self.__private
    
    def get_shared_key(self, other):
        if not isinstance(other, Client): raise ValueError("can only get shared key between two Clients")
        key = other.public * self.__private
        return key
