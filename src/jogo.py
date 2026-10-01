from batalha import Batalha
from inimigos import Inimigo
from itens import PocaoVida
from mapa import Mapa
from personagens import Guerreiro


class Jogo:
    def __init__(self, classe=Guerreiro):
        self.mapa = Mapa()
        self.jogador = classe()
        self.jogador.inventario = [PocaoVida() for _ in range(3)]
        self.inimigos = [Inimigo(x=10, y=2), Inimigo(x=17, y=11)]
        self.batalha = None
        self.estado = "mapa"
        self.mensagens = ["Explore. Inimigos se aproximam a cada passo."]

    def registrar(self, mensagem):
        self.mensagens.append(mensagem)
        self.mensagens = self.mensagens[-5:]

    def adjacente(self, inimigo):
        return abs(self.jogador.x - inimigo.x) + abs(self.jogador.y - inimigo.y) == 1

    def iniciar_batalha(self, inimigo):
        self.batalha = Batalha(self.jogador, inimigo)
        self.estado = "batalha"
        self.registrar(f"{inimigo.nome} encontrou você. Escolha 1, 2, 3 ou P.")

    def mover(self, dx, dy):
        if self.estado != "mapa" or abs(dx) + abs(dy) != 1:
            return
        destino = self.jogador.x + dx, self.jogador.y + dy
        for inimigo in self.inimigos:
            if (inimigo.x, inimigo.y) == destino:
                self.iniciar_batalha(inimigo)
                return
        if not self.jogador.mover(dx, dy, self.mapa):
            return
        for inimigo in self.inimigos:
            if self.adjacente(inimigo):
                self.iniciar_batalha(inimigo)
                return
        for inimigo in self.inimigos:
            ocupadas = {(outro.x, outro.y) for outro in self.inimigos if outro is not inimigo}
            inimigo.x, inimigo.y = self.mapa.proximo_passo(
                (inimigo.x, inimigo.y), (self.jogador.x, self.jogador.y), ocupadas)
            if self.adjacente(inimigo):
                self.iniciar_batalha(inimigo)
                return

    def atacar(self, indice):
        if self.estado != "batalha":
            return
        self.acao_batalha(indice)

    def usar_item(self):
        if self.estado == "batalha":
            self.acao_batalha(usar_item=True)
        elif self.estado == "mapa":
            try:
                self.registrar(self.jogador.usar_item())
            except ValueError as erro:
                self.registrar(str(erro))

    def acao_batalha(self, indice=0, usar_item=False):
        try:
            for mensagem in self.batalha.agir(indice, usar_item):
                self.registrar(mensagem)
        except ValueError as erro:
            self.registrar(str(erro))
        self.verificar_resultado()

    def verificar_resultado(self):
        if self.batalha.finalizada:
            self.estado = "encerrado"
            self.registrar("Combate encerrado. R inicia outro jogo.")

    def reiniciar(self):
        self.__init__(type(self.jogador))

    def escolher_classe(self, classe):
        self.__init__(classe)
