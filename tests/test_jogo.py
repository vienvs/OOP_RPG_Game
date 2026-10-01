import unittest
from jogo import Jogo
from inimigos import Inimigo


class TestExploracao(unittest.TestCase):
    def test_parede_nao_move_inimigos(self):
        jogo = Jogo()
        jogo.jogador.x = 1
        antes = [(i.x, i.y) for i in jogo.inimigos]
        jogo.mover(-1, 0)
        self.assertEqual(antes, [(i.x, i.y) for i in jogo.inimigos])

    def test_passos_aproximam_e_contato_inicia_batalha(self):
        jogo = Jogo()
        jogo.inimigos = [Inimigo(x=5, y=2)]
        jogo.mover(1, 0)
        self.assertEqual(jogo.estado, "batalha")
        self.assertEqual((jogo.jogador.x, jogo.jogador.y), (3, 2))
        self.assertEqual((jogo.inimigos[0].x, jogo.inimigos[0].y), (4, 2))
        jogo.mover(1, 0)
        self.assertEqual(jogo.jogador.x, 3)
