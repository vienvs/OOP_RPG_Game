from random import randint
from ataques import Golpe


class Personagem:
    """Guarda o estado do personagem e controla sua movimentação."""

    def __init__(self, nome, x, y, vida=100):
        self.ataques = []
        self.nome = nome
        self.x = x
        self.y = y
        if not isinstance(vida, int) or isinstance(vida, bool) or vida <= 0:
            raise ValueError("A vida máxima deve ser um inteiro positivo.")
        self._vida_maxima = vida
        self._vida = vida

    def mover(self, dx, dy, mapa):
        # Uma ação permite somente um passo horizontal ou vertical.
        if abs(dx) + abs(dy) != 1:
            return False

        novo_x = self.x + dx
        novo_y = self.y + dy

        if not mapa.pode_caminhar(novo_x, novo_y):
            return False

        self.x = novo_x
        self.y = novo_y
        return True

    def esta_vivo(self):
        return self.vida > 0

    @property
    def vida(self):
        return self._vida

    @property
    def vida_maxima(self):
        return self._vida_maxima

    def receber_dano(self, dano):
        if not isinstance(dano, int) or isinstance(dano, bool) or dano < 0:
            raise ValueError("O dano deve ser um inteiro não negativo.")
        dano_real = min(dano, self._vida)
        self._vida -= dano_real
        return dano_real

    def atacar(self, alvo, indice=0, sortear=randint):
        if not self.esta_vivo() or not alvo.esta_vivo():
            raise ValueError("Atacante e alvo precisam estar vivos.")
        if not isinstance(indice, int) or isinstance(indice, bool) or not 0 <= indice < len(self.ataques):
            raise ValueError("Escolha um ataque disponível.")
        return self.ataques[indice].executar(self, alvo, sortear)


class Guerreiro(Personagem):
    def __init__(self, nome="Arthur", x=2, y=2):
        super().__init__(nome, x, y, 140)
        self.ataques = [Golpe("Corte rapido", 12, 95),
                        Golpe("Espadada", 24, 80),
                        Golpe("Golpe pesado", 40, 55)]
