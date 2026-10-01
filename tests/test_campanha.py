import unittest
from unittest.mock import Mock
from jogo import Jogo
from personagens import Guerreiro, Mago, Arqueiro


class TestCampanha(unittest.TestCase):
    def test_campanha_completa_com_cada_classe(self):
        for classe in [Guerreiro, Mago, Arqueiro]:
            with self.subTest(classe=classe.__name__):
                jogo = Jogo(classe)
                for _ in range(400):
                    if jogo.estado in ("vitoria", "derrota"):
                        break
                    if jogo.estado == "mapa":
                        alvo = jogo.inimigos[0]
                        pos = jogo.jogador.x, jogo.jogador.y
                        passo = jogo.mapa.proximo_passo(pos, (alvo.x, alvo.y), set())
                        jogo.mover(passo[0] - pos[0], passo[1] - pos[1])
                    else:
                        jogo.batalha.sortear = Mock(return_value=1)
                        p = jogo.jogador
                        if p.vida <= 50 and p.inventario:
                            jogo.usar_item()
                        else:
                            opcoes = [(i, a) for i, a in enumerate(p.ataques)
                                      if getattr(a, "custo", 0) <= getattr(p, "mana", 0)]
                            # Escolher dano real, pois este teste fixa todos os acertos.
                            indice = max(opcoes, key=lambda par: par[1].dano)[0]
                            jogo.atacar(indice)
                self.assertEqual(jogo.estado, "vitoria")
                self.assertEqual(jogo.inimigos, [])
