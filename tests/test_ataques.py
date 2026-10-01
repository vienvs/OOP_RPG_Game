import unittest
from unittest.mock import Mock
from ataques import Golpe
from personagens import Guerreiro, Personagem


class TestAtaques(unittest.TestCase):
    def test_guerreiro_tem_tres_opcoes(self):
        guerreiro = Guerreiro()
        alvo = Personagem("Alvo", 1, 1)
        sorteio = Mock(return_value=80)
        guerreiro.atacar(alvo, 1, sorteio)
        self.assertEqual(alvo.vida, 76)
        sorteio.assert_called_once_with(1, 100)
        self.assertEqual(len(guerreiro.ataques), 3)

    def test_erro_nao_causa_dano(self):
        p, alvo = Guerreiro(), Guerreiro()
        p.atacar(alvo, 2, Mock(return_value=100))
        self.assertEqual(alvo.vida, alvo.vida_maxima)

    def test_extremos_precisao(self):
        p, alvo = Guerreiro(), Guerreiro()
        p.ataques = [Golpe("Nunca", 10, 0), Golpe("Sempre", 10, 100)]
        p.atacar(alvo, 0, Mock(return_value=1))
        self.assertEqual(alvo.vida, 140)
        p.atacar(alvo, 1, Mock(return_value=100))
        self.assertEqual(alvo.vida, 130)
