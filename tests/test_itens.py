import unittest
from itens import PocaoVida
from personagens import Guerreiro


class TestPocao(unittest.TestCase):
    def test_cura_limitada(self):
        p = Guerreiro()
        p.receber_dano(20)
        PocaoVida().usar(p)
        self.assertEqual(p.vida, 140)

    def test_nao_cura_cheio_nem_morto(self):
        p = Guerreiro()
        with self.assertRaises(ValueError):
            PocaoVida().usar(p)
        p.receber_dano(140)
        with self.assertRaises(ValueError):
            PocaoVida().usar(p)
