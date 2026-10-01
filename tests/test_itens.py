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

    def test_consumo_so_apos_sucesso(self):
        p = Guerreiro()
        p.inventario = [PocaoVida()]
        with self.assertRaises(ValueError):
            p.usar_item()
        self.assertEqual(len(p.inventario), 1)
        p.receber_dano(60)
        p.usar_item()
        self.assertEqual(p.vida, 130)
        self.assertEqual(p.inventario, [])
        with self.assertRaises(ValueError):
            p.usar_item()
