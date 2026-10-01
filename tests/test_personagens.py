import unittest
from personagens import Personagem


class TestDano(unittest.TestCase):
    def test_dano_e_limite_zero(self):
        p = Personagem("Arthur", 2, 2)
        self.assertEqual(p.receber_dano(30), 30)
        self.assertEqual(p.vida, 70)
        self.assertEqual(p.receber_dano(150), 70)
        self.assertEqual(p.vida, 0)
        self.assertFalse(p.esta_vivo())

    def test_negativo_nao_altera_estado(self):
        p = Personagem("Arthur", 2, 2)
        with self.assertRaises(ValueError):
            p.receber_dano(-10)
        self.assertEqual(p.vida, 100)

    def test_vida_somente_leitura(self):
        p = Personagem("Arthur", 2, 2)
        with self.assertRaises(AttributeError):
            p.vida = -1
