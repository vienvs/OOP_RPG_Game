from batalha import Batalha
from inimigos import Inimigo, Orc, Chefe
from itens import PocaoVida
from mapa import Mapa
from personagens import Guerreiro


class Jogo:
    def __init__(self, classe=Guerreiro):
        self.mapa = Mapa()
        self.jogador = classe()
        self.jogador.inventario = [PocaoVida() for _ in range(3)]
        self.inimigos = [Inimigo(x=10, y=2), Orc(x=17, y=11), Chefe()]
        self.batalha = None
        self.estado = "mapa"
        self.mensagens = ["Explore. Inimigos se aproximam a cada passo."]

    def registrar(self, mensagem):
        self.mensagens.append(mensagem)
        self.mensagens = self.mensagens[-5:]

    def adjacente(self, inimigo):
        return abs(self.jogador.x - inimigo.x) + abs(self.jogador.y - inimigo.y) == 1

    def iniciar_batalha(self, inimigo):
        if self.chefe_bloqueado(inimigo):
            self.registrar("Derrote G e O antes de enfrentar o guardião B.")
            return
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
            if self.adjacente(inimigo) and not self.chefe_bloqueado(inimigo):
                self.iniciar_batalha(inimigo)
                return
        for inimigo in self.inimigos:
            if self.chefe_bloqueado(inimigo):
                continue
            ocupadas = {(outro.x, outro.y) for outro in self.inimigos if outro is not inimigo}
            inimigo.x, inimigo.y = self.mapa.proximo_passo(
                (inimigo.x, inimigo.y), (self.jogador.x, self.jogador.y), ocupadas)
            if self.adjacente(inimigo) and not self.chefe_bloqueado(inimigo):
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
        if not self.batalha.finalizada:
            return
        if not self.jogador.esta_vivo():
            self.estado = "derrota"
            self.registrar("Você foi derrotado. R tenta novamente.")
            return
        inimigo = self.batalha.inimigo
        self.inimigos.remove(inimigo)
        self.jogador.inventario.append(PocaoVida())
        self.jogador.descansar()
        self.registrar(f"Vitória sobre {inimigo.nome}! Recebeu uma poção.")
        self.registrar("Descanso: até +20 de vida e, para Mago, +30 de mana.")
        self.batalha = None
        self.estado = "mapa" if self.inimigos else "vitoria"
        if self.estado == "vitoria":
            self.registrar("Torre libertada! Você venceu. R inicia outra partida.")

    def reiniciar(self):
        self.__init__(type(self.jogador))

    def escolher_classe(self, classe):
        self.__init__(classe)

    def chefe_bloqueado(self, inimigo):
        return isinstance(inimigo, Chefe) and len(self.inimigos) > 1
