class Personagem:
    """Guarda o estado do personagem e controla sua movimentação."""

    def __init__(self, nome, x, y, vida=100):
        self.nome = nome
        self.x = x
        self.y = y
        self.vida_maxima = vida
        self.vida = vida

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
