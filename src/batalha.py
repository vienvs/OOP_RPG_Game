from random import randint


class Batalha:
    """Alterna ações. Não conhece janela, teclado ou classes concretas."""

    def __init__(self, jogador, inimigo, sortear=randint):
        if not jogador.esta_vivo() or not inimigo.esta_vivo():
            raise ValueError("Não é possível iniciar batalha com derrotados.")
        self.jogador = jogador
        self.inimigo = inimigo
        self.sortear = sortear

    @property
    def finalizada(self):
        return not self.jogador.esta_vivo() or not self.inimigo.esta_vivo()

    def agir(self, indice=0, usar_item=False):
        if self.finalizada:
            raise ValueError("A batalha terminou.")
        if usar_item:
            mensagem = self.jogador.usar_item()
        else:
            mensagem = self.jogador.atacar(self.inimigo, indice, self.sortear)
        mensagens = [mensagem]
        if not self.finalizada:
            mensagens.append(self.turno_inimigo())
        return mensagens

    def turno_inimigo(self):
        if self.finalizada:
            return ""
        return self.inimigo.atacar(self.jogador, sortear=self.sortear)
