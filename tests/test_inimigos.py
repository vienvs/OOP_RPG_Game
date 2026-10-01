import unittest
from unittest.mock import Mock
from inimigos import Inimigo
from personagens import Guerreiro


class TestInimigo(unittest.TestCase):
    def test_ataque_do_inimigo(self):
        p = Guerreiro()
        Inimigo().atacar(p, sortear=Mock(return_value=1))
        self.assertEqual(p.vida, 131)

    def test_orc_usa_mesmo_contrato_com_dano_diferente(self):
        from inimigos import Orc
        from batalha import Batalha
        p, orc = Guerreiro(), Orc()
        Batalha(p, orc, Mock(return_value=1)).agir(0)
        self.assertEqual(p.vida, 125)
        self.assertEqual(orc.vida, 73)
        self.assertEqual(orc.simbolo, "O")

    def test_chefe_entra_em_furia_abaixo_de_meia_vida(self):
        from inimigos import Chefe
        chefe, p = Chefe(), Guerreiro()
        chefe.atacar(p, sortear=Mock(return_value=1))
        self.assertEqual(p.vida, 122)
        chefe.receber_dano(80)
        chefe.atacar(p, sortear=Mock(return_value=1))
        self.assertEqual(p.vida, 95)
