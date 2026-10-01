import unittest
from unittest.mock import Mock
from personagens import Mago, Guerreiro


class TestMago(unittest.TestCase):
    def test_cajado_e_tres_ataques(self):
        mago, alvo = Mago(), Guerreiro()
        mago.atacar(alvo, 0, Mock(return_value=1))
        self.assertEqual(alvo.vida, 128)
        self.assertEqual(len(mago.ataques), 3)

    def test_magia_gasta_mana_mesmo_errando(self):
        p, alvo = Mago(), Guerreiro()
        p.atacar(alvo, 1, Mock(return_value=100))
        self.assertEqual(p.mana, 52)
        self.assertEqual(alvo.vida, 140)

    def test_sem_mana_nao_sorteia_nem_altera_alvo(self):
        p, alvo = Mago(), Guerreiro()
        p.gastar_mana(60)
        sorteio = Mock()
        with self.assertRaises(ValueError):
            p.atacar(alvo, 1, sorteio)
        sorteio.assert_not_called()
        self.assertEqual(alvo.vida, 140)
        self.assertEqual(p.mana, 0)
