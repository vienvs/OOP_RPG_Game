import unittest
from mapa import Mapa
from personagens import Personagem


class TestMapa(unittest.TestCase):
    def test_movimento_e_parede(self):
        jogador = Personagem("Arthur", 2, 2)
        mapa = Mapa()
        self.assertTrue(jogador.mover(-1, 0, mapa))
        self.assertFalse(jogador.mover(-1, 0, mapa))
        self.assertEqual((jogador.x, jogador.y), (1, 2))

    def test_limites_e_diagonal(self):
        mapa = Mapa()
        for x, y in [(-1, 1), (1, -1), (24, 1), (1, 14)]:
            self.assertFalse(mapa.pode_caminhar(x, y))
        jogador = Personagem("Arthur", 2, 2)
        self.assertFalse(jogador.mover(1, 1, mapa))
        self.assertEqual((jogador.x, jogador.y), (2, 2))
