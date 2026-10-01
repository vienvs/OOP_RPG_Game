import unittest
from unittest.mock import Mock
from personagens import Mago, Guerreiro


class TestMago(unittest.TestCase):
    def test_cajado_e_tres_ataques(self):
        mago, alvo = Mago(), Guerreiro()
        mago.atacar(alvo, 0, Mock(return_value=1))
        self.assertEqual(alvo.vida, 128)
        self.assertEqual(len(mago.ataques), 3)
