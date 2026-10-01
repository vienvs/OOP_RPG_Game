from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def usar(self, alvo):
        pass


class PocaoVida(Item):
    def __init__(self, cura=50):
        if not isinstance(cura, int) or isinstance(cura, bool) or cura <= 0:
            raise ValueError("Cura deve ser um inteiro positivo.")
        self.cura = cura

    def usar(self, alvo):
        recuperado = alvo.curar(self.cura)
        return f"{alvo.nome} recuperou {recuperado} de vida."
