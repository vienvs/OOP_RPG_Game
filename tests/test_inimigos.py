import unittest
from unittest.mock import Mock
from inimigos import Inimigo
from personagens import Guerreiro


class TestInimigo(unittest.TestCase):
    def test_ataque_do_inimigo(self):
        p = Guerreiro()
        Inimigo().atacar(p, sortear=Mock(return_value=1))
        self.assertEqual(p.vida, 131)
