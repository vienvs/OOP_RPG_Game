from random import randint
from ataques import Golpe
from personagens import Personagem


class Inimigo(Personagem):
    def __init__(self, nome="Goblin", x=8, y=2, vida=50):
        super().__init__(nome, x, y, vida)
        self.simbolo = "G"
        self.ataques = [Golpe("Arranhao", 9, 75)]


class Orc(Inimigo):
    def __init__(self, x=17, y=11):
        super().__init__("Orc", x, y, 85)
        self.simbolo = "O"
        self.ataques = [Golpe("Machadada", 15, 80)]


class Chefe(Inimigo):
    def __init__(self, x=21, y=11):
        super().__init__("Guardião da torre", x, y, 160)
        self.simbolo = "B"
        self.ataques = [Golpe("Lamina", 18, 80), Golpe("Furia", 27, 65)]

    def atacar(self, alvo, indice=0, sortear=randint):
        # A mesma operação ganha uma regra própria: fúria abaixo de meia vida.
        escolha = 1 if self.vida <= self.vida_maxima // 2 else 0
        return super().atacar(alvo, escolha, sortear)
