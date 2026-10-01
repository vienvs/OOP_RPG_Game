import pygame
from recursos import carregar_arte

ARTES = {nome: carregar_arte(nome) for nome in
         ("guerreiro", "mago", "arqueiro", "inimigo", "orc", "chefe")}
ARTE_INIMIGO = {"G": "inimigo", "O": "orc", "B": "chefe"}
from recursos import carregar_arte

ARTES = {nome: carregar_arte(nome) for nome in
         ("guerreiro", "mago", "arqueiro", "inimigo", "orc", "chefe")}
ARTE_INIMIGO = {"G": "inimigo", "O": "orc", "B": "chefe"}

FUNDO = (18, 20, 26)
TEXTO = (228, 231, 238)
VERDE = (122, 224, 170)
VERMELHO = (242, 140, 131)
CELULA = 26


def texto(tela, fonte, mensagem, x, y, cor=TEXTO):
    tela.blit(fonte.render(mensagem, True, cor), (x, y))


def desenhar_arte(tela, fonte, nome, x, y, cor):
    for indice, linha in enumerate(ARTES[nome]):
        texto(tela, fonte, linha, x, y + indice * 24, cor)


def desenhar_arte(tela, fonte, nome, x, y, cor):
    for indice, linha in enumerate(ARTES[nome]):
        texto(tela, fonte, linha, x, y + indice * 24, cor)


def desenhar(tela, fonte, jogo):
    tela.fill(FUNDO)
    texto(tela, fonte, "ASCII RPG | " + jogo.estado.upper(), 24, 18)
    p = jogo.jogador
    if jogo.estado == "mapa":
        for y, linha in enumerate(jogo.mapa.linhas):
            for x, simbolo in enumerate(linha):
                cor = (145, 155, 177) if simbolo == "#" else (65, 73, 91)
                texto(tela, fonte, simbolo, 24 + x * CELULA, 70 + y * CELULA, cor)
        for inimigo in jogo.inimigos:
            retangulo = (24 + inimigo.x * CELULA, 70 + inimigo.y * CELULA, CELULA, CELULA)
            pygame.draw.rect(tela, FUNDO, retangulo)
            texto(tela, fonte, inimigo.simbolo, retangulo[0], retangulo[1], VERMELHO)
        retangulo = (24 + p.x * CELULA, 70 + p.y * CELULA, CELULA, CELULA)
        pygame.draw.rect(tela, FUNDO, retangulo)
        texto(tela, fonte, "@", retangulo[0], retangulo[1], VERDE)
    else:
        texto(tela, fonte, p.nome, 70, 110, VERDE)
        desenhar_arte(tela, fonte, type(p).__name__.lower(), 90, 150, VERDE)
        if jogo.batalha is not None:
            alvo = jogo.batalha.inimigo
            texto(tela, fonte, alvo.nome, 400, 110, VERMELHO)
            desenhar_arte(tela, fonte, ARTE_INIMIGO[alvo.simbolo], 420, 150, VERMELHO)
            texto(tela, fonte, f"Vida {alvo.vida}/{alvo.vida_maxima}", 400, 310)
        texto(tela, fonte, f"Vida {p.vida}/{p.vida_maxima}", 70, 310)
    painel = [type(p).__name__, p.nome, f"Vida {p.vida}/{p.vida_maxima}",
              f"Poções: {len(p.inventario)}", f"Inimigos: {len(jogo.inimigos)}", "",
              "WASD / setas: mover", "1-3: ataque em batalha", "P: usar poção",
              "R: reiniciar", "Novo jogo: F1 / F2 / F3", "Guerreiro / Mago / Arqueiro", "ESC: sair"]
    if hasattr(p, "mana"):
        painel.insert(3, f"Mana {p.mana}/60")
    for i, linha in enumerate(painel):
        texto(tela, fonte, linha, 700, 70 + i * 27)
    if jogo.estado == "mapa":
        texto(tela, fonte, "Derrote G e O. Depois enfrente o chefe B.", 24, 425, VERDE)
    elif jogo.estado == "vitoria":
        texto(tela, fonte, "TORRE LIBERTADA! R: jogar novamente", 24, 385, VERDE)
    elif jogo.estado == "derrota":
        texto(tela, fonte, "VOCE FOI DERROTADO. R: tentar novamente", 24, 385, VERMELHO)
    if jogo.estado == "mapa":
        texto(tela, fonte, "Derrote G e O. Depois enfrente o chefe B.", 24, 425, VERDE)
    elif jogo.estado == "vitoria":
        texto(tela, fonte, "TORRE LIBERTADA! R: jogar novamente", 24, 385, VERDE)
    elif jogo.estado == "derrota":
        texto(tela, fonte, "VOCE FOI DERROTADO. R: tentar novamente", 24, 385, VERMELHO)
    for i, ataque in enumerate(p.ataques):
        texto(tela, fonte, f"[{i + 1}] {ataque}", 24, 455 + i * 27)
    for i, mensagem in enumerate(jogo.mensagens):
        texto(tela, fonte, mensagem, 24, 555 + i * 24)
    pygame.display.flip()
