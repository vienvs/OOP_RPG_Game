from abc import ABC, abstractmethod


class Ataque(ABC):
    def __init__(self, nome, dano, precisao):
        if not isinstance(dano, int) or isinstance(dano, bool) or dano < 0:
            raise ValueError("Dano deve ser inteiro não negativo.")
        if not isinstance(precisao, int) or isinstance(precisao, bool) or not 0 <= precisao <= 100:
            raise ValueError("Precisão deve ser um inteiro entre 0 e 100.")
        self.nome = nome
        self.dano = dano
        self.precisao = precisao

    def __str__(self):
        return f"{self.nome}: {self.dano} dano / {self.precisao}%"

    @abstractmethod
    def executar(self, atacante, alvo, sortear):
        pass


class Golpe(Ataque):
    def executar(self, atacante, alvo, sortear):
        if sortear(1, 100) > self.precisao:
            return f"{atacante.nome} errou {self.nome}."
        dano = alvo.receber_dano(self.dano)
        return f"{atacante.nome}: {self.nome} causou {dano} de dano."


class Magia(Golpe):
    def __init__(self, nome, dano, precisao, custo):
        super().__init__(nome, dano, precisao)
        if not isinstance(custo, int) or isinstance(custo, bool) or custo <= 0:
            raise ValueError("Custo deve ser um inteiro positivo.")
        self.custo = custo

    def executar(self, atacante, alvo, sortear):
        atacante.gastar_mana(self.custo)
        return super().executar(atacante, alvo, sortear)

    def __str__(self):
        return super().__str__() + f" / {self.custo} mana"
