import unittest
from unittest.mock import Mock
from ataques import Golpe
from batalha import Batalha
from inimigos import Inimigo
from itens import PocaoVida
from personagens import Guerreiro, Mago


class TestFluxosBatalha(unittest.TestCase):
    def test_erro_consume_turno(self):
        p, alvo = Guerreiro(), Inimigo()
        sorteio = Mock(side_effect=[100, 1])
        mensagens = Batalha(p, alvo, sorteio).agir(0)
        self.assertIn("errou", mensagens[0])
        self.assertEqual(p.vida, 131)
        self.assertEqual(alvo.vida, 50)
        self.assertEqual(sorteio.call_count, 2)

    def test_mana_insuficiente_nao_contra_ataca(self):
        p, alvo, sorteio = Mago(), Inimigo(), Mock(return_value=1)
        p.gastar_mana(60)
        with self.assertRaises(ValueError):
            Batalha(p, alvo, sorteio).agir(1)
        sorteio.assert_not_called()
        self.assertEqual(p.vida, 110)

    def test_pocao_valida_consume_turno(self):
        p, alvo = Guerreiro(), Inimigo()
        p.receber_dano(60)
        p.inventario = [PocaoVida()]
        Batalha(p, alvo, Mock(return_value=1)).agir(usar_item=True)
        self.assertEqual(p.vida, 121)
        self.assertEqual(p.inventario, [])

    def test_pocao_em_vida_cheia_preserva_turno_e_item(self):
        p, alvo, sorteio = Guerreiro(), Inimigo(), Mock(return_value=1)
        p.inventario = [PocaoVida()]
        with self.assertRaises(ValueError):
            Batalha(p, alvo, sorteio).agir(usar_item=True)
        self.assertEqual(len(p.inventario), 1)
        sorteio.assert_not_called()

    def test_apos_derrota_nao_aceita_novas_acoes(self):
        p, alvo = Guerreiro(), Inimigo()
        p.receber_dano(139)
        p.ataques = [Golpe("Falha", 1, 0)]
        batalha = Batalha(p, alvo, Mock(return_value=1))
        batalha.agir(0)
        self.assertEqual(p.vida, 0)
        self.assertTrue(batalha.finalizada)
        with self.assertRaises(ValueError):
            batalha.agir()
        with self.assertRaises(ValueError):
            Batalha(p, alvo)
