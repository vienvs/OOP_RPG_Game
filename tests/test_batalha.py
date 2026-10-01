import unittest
from unittest.mock import Mock
from batalha import Batalha
from personagens import Guerreiro
from inimigos import Inimigo


class TestTurnos(unittest.TestCase):
    def test_inimigo_responde_a_um_ataque(self):
        p, inimigo = Guerreiro(), Inimigo()
        mensagens = Batalha(p, inimigo, Mock(return_value=1)).agir(0)
        self.assertEqual(len(mensagens), 2)
        self.assertEqual(inimigo.vida, 38)
        self.assertEqual(p.vida, 131)

    def test_derrotado_nao_contra_ataca(self):
        p, inimigo = Guerreiro(), Inimigo()
        inimigo.receber_dano(49)
        batalha = Batalha(p, inimigo, Mock(return_value=1))
        self.assertEqual(len(batalha.agir()), 1)
        self.assertTrue(batalha.finalizada)
        self.assertEqual(p.vida, 140)

    def test_item_invalido_nao_passa_turno(self):
        p, inimigo = Guerreiro(), Inimigo()
        sorteio = Mock(return_value=1)
        with self.assertRaises(ValueError):
            Batalha(p, inimigo, sorteio).agir(usar_item=True)
        sorteio.assert_not_called()
