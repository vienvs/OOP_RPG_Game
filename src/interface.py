import pygame

FUNDO = (18, 20, 26)
TEXTO = (228, 231, 238)
VERDE = (122, 224, 170)
VERMELHO = (242, 140, 131)
CELULA = 26


def texto(tela, fonte, mensagem, x, y, cor=TEXTO):
    tela.blit(fonte.render(mensagem, True, cor), (x, y))


def desenhar(tela, fonte, jogo):
    tela.fill(FUNDO)
    texto(tela, fonte, "ASCII RPG | Treinamento", 24, 18)
    for y, linha in enumerate(jogo.mapa.linhas):
        for x, simbolo in enumerate(linha):
            if (x, y) != (jogo.jogador.x, jogo.jogador.y):
                cor = (145, 155, 177) if simbolo == "#" else (65, 73, 91)
                texto(tela, fonte, simbolo, 24 + x * CELULA, 70 + y * CELULA, cor)
    p = jogo.jogador
    texto(tela, fonte, "@", 24 + p.x * CELULA, 70 + p.y * CELULA, VERDE)
    painel = [type(p).__name__, p.nome, f"Vida {p.vida}/{p.vida_maxima}",
              "", jogo.alvo.nome, f"Vida {jogo.alvo.vida}/{jogo.alvo.vida_maxima}",
              "", "WASD / setas: mover", "1-3: atacar; E: inimigo", "F1 Guerreiro / F2 Mago", "R: reiniciar", "ESC: sair"]
    if hasattr(p, "mana"):
        painel.insert(3, f"Mana {p.mana}/60")
    for i, linha in enumerate(painel):
        texto(tela, fonte, linha, 700, 70 + i * 27)
    for i, ataque in enumerate(p.ataques):
        texto(tela, fonte, f"[{i + 1}] {ataque}", 24, 455 + i * 27)
    for i, mensagem in enumerate(jogo.mensagens):
        texto(tela, fonte, mensagem, 24, 555 + i * 24)
    pygame.display.flip()
