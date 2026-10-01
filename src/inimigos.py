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
