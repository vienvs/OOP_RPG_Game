from ataques import Golpe
from personagens import Personagem


class Inimigo(Personagem):
    def __init__(self, nome="Goblin", x=8, y=2):
        super().__init__(nome, x, y, 50)
        self.simbolo = "G"
        self.ataques = [Golpe("Arranhao", 9, 75)]
