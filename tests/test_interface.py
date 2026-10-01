import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
import unittest
import pygame
from jogo import Jogo
from interface import desenhar
from main import processar_eventos
from personagens import Arqueiro


class TestInterface(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.tela = pygame.display.set_mode((1100, 720))
        self.fonte = pygame.font.SysFont("consolas", 20)
        pygame.event.clear()

    def tearDown(self):
        pygame.quit()

    def test_teclas_e_fechamento(self):
        jogo = Jogo()
        for tecla, posicao in [(pygame.K_s, (2, 3)), (pygame.K_DOWN, (2, 4)),
                               (pygame.K_a, (1, 4)), (pygame.K_RIGHT, (2, 4))]:
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=tecla))
            self.assertTrue(processar_eventos(jogo))
            self.assertEqual((jogo.jogador.x, jogo.jogador.y), posicao)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_F3))
        processar_eventos(jogo)
        self.assertIsInstance(jogo.jogador, Arqueiro)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
        self.assertFalse(processar_eventos(jogo))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        self.assertFalse(processar_eventos(jogo))

    def test_desenha_mapa_batalha_e_finais(self):
        jogo = Jogo()
        desenhar(self.tela, self.fonte, jogo)
        jogo.iniciar_batalha(jogo.inimigos[0])
        for estado in ['batalha', 'vitoria', 'derrota']:
            jogo.estado = estado
            desenhar(self.tela, self.fonte, jogo)
