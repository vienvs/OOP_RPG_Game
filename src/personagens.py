from random import randint
from ataques import Golpe, Magia


class Personagem:
    """Guarda o estado do personagem e controla sua movimentação."""

    def __init__(self, nome, x, y, vida=100):
        self.inventario = []
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

    def usar_item(self, indice=0):
        if not isinstance(indice, int) or isinstance(indice, bool) or not 0 <= indice < len(self.inventario):
            raise ValueError("Nenhuma poção disponível.")
        mensagem = self.inventario[indice].usar(self)
        self.inventario.pop(indice)
        return mensagem

    def descansar(self):
        if not self.esta_vivo():
            raise ValueError("Personagens derrotados não podem descansar.")
        self._vida = min(self.vida_maxima, self.vida + 20)

    def curar(self, quantidade):
        if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade <= 0:
            raise ValueError("Cura deve ser um inteiro positivo.")
        if not self.esta_vivo():
            raise ValueError("Poção não ressuscita personagens.")
        recuperado = min(quantidade, self.vida_maxima - self.vida)
        if recuperado == 0:
            raise ValueError("Vida já está cheia.")
        self._vida += recuperado
        return recuperado

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


class Mago(Personagem):
    def __init__(self, nome="Merlin", x=2, y=2):
        super().__init__(nome, x, y, 110)
        self._mana = 60
        self.ataques = [Golpe("Cajado", 12, 95),
                        Magia("Raio", 30, 90, 8),
                        Magia("Tempestade", 45, 70, 14)]

    @property
    def mana(self):
        return self._mana

    def descansar(self):
        super().descansar()
        self._mana = min(60, self.mana + 30)

    def gastar_mana(self, custo):
        if not isinstance(custo, int) or isinstance(custo, bool) or custo < 0:
            raise ValueError("Custo de mana inválido.")
        if custo > self._mana:
            raise ValueError("Mana insuficiente. Use o cajado.")
        self._mana -= custo
