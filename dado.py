import random

class Dado:
    def __init__(self, numero_caras:int):
        self.numero_caras = numero_caras

    def tirada(self) -> int:
        return random.randint(1, self.numero_caras)
