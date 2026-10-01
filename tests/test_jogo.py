import unittest
from jogo import Jogo
from inimigos import Inimigo


class TestExploracao(unittest.TestCase):
    def test_parede_nao_move_inimigos(self):
        jogo = Jogo()
        jogo.jogador.x = 1
        antes = [(i.x, i.y) for i in jogo.inimigos]
        jogo.mover(-1, 0)
        self.assertEqual(antes, [(i.x, i.y) for i in jogo.inimigos])

    def test_passos_aproximam_e_contato_inicia_batalha(self):
        jogo = Jogo()
        jogo.inimigos = [Inimigo(x=5, y=2)]
        jogo.mover(1, 0)
        self.assertEqual(jogo.estado, "batalha")
        self.assertEqual((jogo.jogador.x, jogo.jogador.y), (3, 2))
        self.assertEqual((jogo.inimigos[0].x, jogo.inimigos[0].y), (4, 2))
        jogo.mover(1, 0)
        self.assertEqual(jogo.jogador.x, 3)

    def test_vitoria_remove_alvo_e_retorna_mapa(self):
        jogo = Jogo()
        alvo = jogo.inimigos[0]
        jogo.iniciar_batalha(alvo)
        alvo.receber_dano(alvo.vida)
        jogo.verificar_resultado()
        self.assertEqual(jogo.estado, "mapa")
        self.assertNotIn(alvo, jogo.inimigos)
        self.assertIsNone(jogo.batalha)

    def test_ultimo_inimigo_encerra_e_reinicio_restaura(self):
        jogo = Jogo()
        jogo.inimigos = jogo.inimigos[:1]
        alvo = jogo.inimigos[0]
        jogo.iniciar_batalha(alvo)
        alvo.receber_dano(alvo.vida)
        jogo.verificar_resultado()
        self.assertEqual(jogo.estado, "vitoria")
        jogo.reiniciar()
        self.assertEqual(jogo.estado, "mapa")
        self.assertEqual(jogo.jogador.vida, jogo.jogador.vida_maxima)

    def test_derrota_impede_exploracao(self):
        jogo = Jogo()
        jogo.iniciar_batalha(jogo.inimigos[0])
        jogo.jogador.receber_dano(999)
        jogo.verificar_resultado()
        jogo.mover(1, 0)
        self.assertEqual(jogo.estado, "derrota")
        self.assertEqual(jogo.jogador.x, 2)

    def test_descanso_apos_vitoria_recupera_recursos(self):
        from personagens import Mago
        jogo = Jogo(Mago)
        jogo.jogador.receber_dano(50)
        jogo.jogador.gastar_mana(50)
        alvo = jogo.inimigos[0]
        jogo.iniciar_batalha(alvo)
        alvo.receber_dano(alvo.vida)
        jogo.verificar_resultado()
        self.assertEqual(jogo.jogador.vida, 80)
        self.assertEqual(jogo.jogador.mana, 40)

    def test_chefe_bloqueado_ate_derrotar_guardas(self):
        from inimigos import Chefe
        jogo = Jogo()
        chefe = next(i for i in jogo.inimigos if isinstance(i, Chefe))
        jogo.iniciar_batalha(chefe)
        self.assertEqual(jogo.estado, "mapa")
        jogo.inimigos = [chefe]
        jogo.iniciar_batalha(chefe)
        self.assertEqual(jogo.estado, "batalha")
        chefe.receber_dano(chefe.vida)
        jogo.verificar_resultado()
        self.assertEqual(jogo.estado, "vitoria")

    def test_chefe_protegido_nao_paralisa_os_guardas(self):
        jogo = Jogo()
        jogo.jogador.x, jogo.jogador.y = 20, 12
        guarda = jogo.inimigos[0]
        antes = guarda.x, guarda.y
        jogo.mover(1, 0)
        self.assertEqual(jogo.estado, "mapa")
        self.assertNotEqual((guarda.x, guarda.y), antes)
