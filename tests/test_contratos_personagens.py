import unittest
from unittest.mock import Mock
from ataques import Ataque, Golpe, Magia
from itens import Item, PocaoVida
from personagens import Personagem, Guerreiro, Mago, Arqueiro


class TestContratosPersonagens(unittest.TestCase):
    def test_construtor_rejeita_vida_invalida(self):
        for valor in [0, -1, 2.5, True, "100", None]:
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Personagem("Alvo", 1, 1, valor)

    def test_dano_invalido_preserva_vida(self):
        for valor in [-1, 2.5, True, "10", None]:
            p = Guerreiro()
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    p.receber_dano(valor)
                self.assertEqual(p.vida, 140)

    def test_zero_nao_causa_dano(self):
        p = Guerreiro()
        self.assertEqual(p.receber_dano(0), 0)
        self.assertEqual(p.vida, 140)

    def test_maximo_e_mana_somente_leitura(self):
        p = Mago()
        for atributo in ['vida', 'vida_maxima', 'mana']:
            with self.assertRaises(AttributeError):
                setattr(p, atributo, -1)

    def test_subclasses_respeitam_contrato(self):
        for classe in [Guerreiro, Mago, Arqueiro]:
            with self.subTest(classe=classe.__name__):
                p, alvo = classe(), Guerreiro()
                self.assertIsInstance(p, Personagem)
                self.assertEqual(len(p.ataques), 3)
                self.assertIsInstance(p.atacar(alvo, 0, Mock(return_value=1)), str)
                self.assertLess(alvo.vida, alvo.vida_maxima)
                p.receber_dano(999)
                self.assertFalse(p.esta_vivo())

    def test_ataque_indisponivel_nao_sorteia(self):
        p, alvo, sorteio = Guerreiro(), Guerreiro(), Mock()
        for indice in [-1, 3, True, "1"]:
            with self.assertRaises(ValueError):
                p.atacar(alvo, indice, sorteio)
        sorteio.assert_not_called()

    def test_derrotados_nao_atacam_nem_recebem_novo_ataque(self):
        p, alvo, sorteio = Guerreiro(), Guerreiro(), Mock()
        alvo.receber_dano(999)
        with self.assertRaises(ValueError):
            p.atacar(alvo, sortear=sorteio)
        with self.assertRaises(ValueError):
            alvo.atacar(p, sortear=sorteio)
        sorteio.assert_not_called()

    def test_precisao_e_dano_invalidos(self):
        for precisao in [-1, 101, 1.5, True]:
            with self.assertRaises(ValueError):
                Golpe("Teste", 10, precisao)
        for dano in [-1, 1.5, True]:
            with self.assertRaises(ValueError):
                Golpe("Teste", dano, 80)

    def test_mana_exata_e_falha_sem_efeitos(self):
        p, alvo = Mago(), Guerreiro()
        p.gastar_mana(52)
        p.atacar(alvo, 1, Mock(return_value=1))
        self.assertEqual(p.mana, 0)
        vida = alvo.vida
        with self.assertRaises(ValueError):
            p.atacar(alvo, 1, Mock(return_value=1))
        self.assertEqual(alvo.vida, vida)
        for custo in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                p.gastar_mana(custo)
        self.assertEqual(p.mana, 0)

    def test_abstracoes_nao_instanciaveis(self):
        with self.assertRaises(TypeError):
            Ataque("Teste", 10, 80)
        with self.assertRaises(TypeError):
            Item()

    def test_inventarios_e_ataques_nao_compartilham_listas(self):
        a, b = Guerreiro(), Guerreiro()
        a.inventario.append(PocaoVida())
        a.ataques.pop()
        self.assertEqual(b.inventario, [])
        self.assertEqual(len(b.ataques), 3)

    def test_cura_e_custo_invalidos(self):
        p = Guerreiro()
        p.receber_dano(40)
        for valor in [0, -1, True, 2.5]:
            with self.assertRaises(ValueError):
                p.curar(valor)
            with self.assertRaises(ValueError):
                PocaoVida(valor)
            with self.assertRaises(ValueError):
                Magia("Teste", 20, 90, valor)
        self.assertEqual(p.vida, 100)
