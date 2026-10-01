import os
import sys

import pygame

from mapa import Mapa
from personagens import Personagem


LARGURA = 1000
ALTURA = 600
CELULA = 28
ORIGEM_X = 24
ORIGEM_Y = 96
FPS = 60

FUNDO = (18, 20, 26)
TEXTO = (228, 231, 238)
PAREDE = (147, 159, 181)
CHAO = (65, 73, 91)
JOGADOR = (122, 224, 170)

# Cada tecla corresponde a um deslocamento (coluna, linha).
MOVIMENTOS = {
    pygame.K_w: (0, -1),
    pygame.K_UP: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_DOWN: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_LEFT: (-1, 0),
    pygame.K_d: (1, 0),
    pygame.K_RIGHT: (1, 0),
}


def processar_eventos(jogador, mapa):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return False
            if evento.key in MOVIMENTOS:
                dx, dy = MOVIMENTOS[evento.key]
                jogador.mover(dx, dy, mapa)
    return True


def desenhar_simbolo(tela, fonte, simbolo, cor, x, y):
    imagem = fonte.render(simbolo, True, cor)
    # Centralizar o caractere mantém a grade alinhada em qualquer fonte.
    destino = imagem.get_rect(
        center=(ORIGEM_X + x * CELULA + CELULA // 2,
                ORIGEM_Y + y * CELULA + CELULA // 2)
    )
    tela.blit(imagem, destino)


def desenhar(tela, fonte_mapa, fonte_ui, jogador, mapa):
    tela.fill(FUNDO)
    titulo = fonte_ui.render("ASCII RPG | Etapa 0: exploracao", True, TEXTO)
    tela.blit(titulo, (ORIGEM_X, 30))

    for y, linha in enumerate(mapa.linhas):
        for x, simbolo in enumerate(linha):
            # Não desenhar o chão por baixo do personagem.
            if (x, y) == (jogador.x, jogador.y):
                continue
            cor = PAREDE if simbolo == "#" else CHAO
            desenhar_simbolo(tela, fonte_mapa, simbolo, cor, x, y)

    desenhar_simbolo(tela, fonte_mapa, "@", JOGADOR, jogador.x, jogador.y)

    painel = [
        "PERSONAGEM",
        jogador.nome,
        f"Vida: {jogador.vida}/{jogador.vida_maxima}",
        f"Posicao: {jogador.x}, {jogador.y}",
        "",
        "LEGENDA",
        "@  Voce",
        "#  Parede",
        ".  Chao",
        "",
        "CONTROLES",
        "WASD ou setas: mover",
        "ESC: sair",
    ]
    for indice, linha in enumerate(painel):
        texto = fonte_ui.render(linha, True, TEXTO)
        tela.blit(texto, (732, 96 + indice * 28))

    dica = fonte_ui.render("Explore o mapa. Cada tecla move uma casa.", True, TEXTO)
    tela.blit(dica, (ORIGEM_X, 530))
    pygame.display.flip()


def main(limite_quadros=None):
    pygame.init()
    try:
        tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("ASCII RPG - POO")
        relogio = pygame.time.Clock()
        fonte_mapa = pygame.font.SysFont("consolas", 26)
        fonte_ui = pygame.font.SysFont("consolas", 20)
        mapa = Mapa()
        jogador = Personagem("Arthur", 2, 2)

        quadros = 0
        while processar_eventos(jogador, mapa):
            desenhar(tela, fonte_mapa, fonte_ui, jogador, mapa)
            relogio.tick(FPS)
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
