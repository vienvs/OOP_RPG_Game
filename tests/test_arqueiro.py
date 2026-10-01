import unittest
from unittest.mock import Mock
from personagens import Arqueiro
from inimigos import Inimigo
from batalha import Batalha
from jogo import Jogo


class TestArqueiro(unittest.TestCase):
    def test_substitui_personagem_na_batalha(self):
        p, alvo = Arqueiro(), Inimigo()
        Batalha(p, alvo, Mock(return_value=1)).agir(1)
        self.assertEqual(alvo.vida, 25)
        self.assertEqual(p.vida, 111)
        self.assertEqual(len(p.ataques), 3)

    def test_troca_inicia_partida_nova(self):
        jogo = Jogo()
        jogo.escolher_classe(Arqueiro)
        self.assertIsInstance(jogo.jogador, Arqueiro)
        self.assertEqual(len(jogo.jogador.inventario), 3)
