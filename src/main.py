import os
import sys
import pygame
from jogo import Jogo
from personagens import Guerreiro, Mago, Arqueiro
from interface import desenhar

MOVIMENTOS = {pygame.K_w: (0, -1), pygame.K_UP: (0, -1),
              pygame.K_s: (0, 1), pygame.K_DOWN: (0, 1),
              pygame.K_a: (-1, 0), pygame.K_LEFT: (-1, 0),
              pygame.K_d: (1, 0), pygame.K_RIGHT: (1, 0)}


def processar_eventos(jogo):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            tecla = evento.key
            if tecla == pygame.K_ESCAPE:
                return False
            if tecla in MOVIMENTOS:
                jogo.mover(*MOVIMENTOS[tecla])
            elif tecla in (pygame.K_1, pygame.K_2, pygame.K_3):
                jogo.atacar(tecla - pygame.K_1)
            elif tecla == pygame.K_F1:
                jogo.escolher_classe(Guerreiro)
            elif tecla == pygame.K_F2:
                jogo.escolher_classe(Mago)
            elif tecla == pygame.K_F3:
                jogo.escolher_classe(Arqueiro)
            elif tecla == pygame.K_p:
                jogo.usar_item()
            elif tecla == pygame.K_r:
                jogo.reiniciar()
    return True


def main(limite_quadros=None):
    pygame.init()
    try:
        tela = pygame.display.set_mode((1100, 720))
        pygame.display.set_caption("ASCII RPG - POO")
        fonte = pygame.font.SysFont("consolas", 20)
        relogio = pygame.time.Clock()
        jogo = Jogo()
        quadros = 0
        while processar_eventos(jogo):
            desenhar(tela, fonte, jogo)
            relogio.tick(60)
            quadros += 1
            if limite_quadros is not None and quadros >= limite_quadros:
                break
    finally:
        pygame.quit()


if __name__ == "__main__":
    teste = "--smoke-test" in sys.argv
    if teste:
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        os.environ["SDL_AUDIODRIVER"] = "dummy"
    main(3 if teste else None)
