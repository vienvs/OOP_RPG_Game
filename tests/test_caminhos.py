import unittest
from mapa import Mapa
from jogo import Jogo
from inimigos import Inimigo


class TestCaminhos(unittest.TestCase):
    def test_contorna_parede(self):
        mapa = Mapa()
        mapa.linhas = ["#######", "#..#..#", "#..#..#", "#.....#", "#######"]
        atual, destino = (1, 1), (5, 1)
        for _ in range(10):
            seguinte = mapa.proximo_passo(atual, destino, set())
            self.assertTrue(mapa.pode_caminhar(*seguinte))
            self.assertEqual(abs(atual[0] - seguinte[0]) + abs(atual[1] - seguinte[1]), 1)
            atual = seguinte
            if atual == destino:
                break
        self.assertEqual(atual, destino)

    def test_sem_caminho_fica_parado(self):
        mapa = Mapa()
        mapa.linhas = ["#####", "#.#.#", "#####"]
        self.assertEqual(mapa.proximo_passo((1, 1), (3, 1), set()), (1, 1))

    def test_ocupacao_bloqueia(self):
        mapa = Mapa()
        passo = mapa.proximo_passo((2, 2), (5, 2), {(3, 2)})
        self.assertNotEqual(passo, (3, 2))

    def test_colisao_nao_sobrepoe_personagens(self):
        jogo = Jogo()
        jogo.inimigos = [Inimigo(x=3, y=2)]
        jogo.mover(1, 0)
        self.assertEqual(jogo.estado, "batalha")
        self.assertEqual(jogo.jogador.x, 2)

    def test_diagonal_nao_inicia_contato(self):
        jogo = Jogo()
        self.assertFalse(jogo.adjacente(Inimigo(x=3, y=3)))
