from inimigos import Inimigo
from mapa import Mapa
from personagens import Guerreiro, Personagem


class Jogo:
    def __init__(self):
        self.mapa = Mapa()
        self.jogador = Guerreiro()
        self.alvo = Inimigo()
        self.mensagens = ["Treino: 1, 2, 3 atacam. R reinicia."]

    def registrar(self, mensagem):
        self.mensagens.append(mensagem)
        self.mensagens = self.mensagens[-5:]

    def mover(self, dx, dy):
        self.jogador.mover(dx, dy, self.mapa)

    def atacar(self, indice):
        try:
            self.registrar(self.jogador.atacar(self.alvo, indice))
        except ValueError as erro:
            self.registrar(str(erro))

    def reiniciar(self):
        self.__init__()

    def demonstrar_inimigo(self):
        try:
            self.registrar(self.alvo.atacar(self.jogador))
        except ValueError as erro:
            self.registrar(str(erro))
