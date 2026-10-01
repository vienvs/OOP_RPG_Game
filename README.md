# OOP RPG Game — A Torre ASCII

RPG por turnos em uma janela Pygame, criado em Python para a disciplina de Programação Orientada a Objetos. Explore o mapa, derrote o Goblin e o Orc e enfrente o Guardião da torre. Cada personagem tem três ataques; precisão, mana e poções fazem parte das decisões do combate.

## Jogar pelo código — Windows / Python 3.12

No terminal, na raiz deste repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe src/main.py
```

Se o ambiente já existe e as dependências estão instaladas, execute apenas o último comando. Não é necessário ativar a venv. O ponto de entrada é `src/main.py`.

## Controles

| Tecla | Ação |
|---|---|
| WASD ou setas | Andar uma casa; sem diagonal |
| 1, 2, 3 | Selecionar um dos três ataques durante batalha |
| P | Usar uma poção; também funciona fora de batalha |
| F1 / F2 / F3 | Começar **nova partida** com Guerreiro / Mago / Arqueiro |
| R | Reiniciar com a classe atual |
| ESC ou X da janela | Sair |

Você começa como Guerreiro. `@` é o jogador, `#` parede, `.` chão, `G` Goblin, `O` Orc e `B` chefe. A janela mede 1100 × 720 pixels.

## Regras

- Cada passo válido faz os inimigos avançarem uma casa por um caminho livre. Bater em parede não gasta turno. Inimigos não atravessam paredes nem outros inimigos.
- Contato horizontal/vertical inicia batalha; diagonal não. Tentar entrar na casa de um inimigo inicia combate sem sobreposição. A exploração fica parada durante a batalha.
- Acerto: sorteio inteiro entre 1 e 100, com `sorteio <= precisão`. Precisão 0 sempre erra e 100 sempre acerta. Os ataques têm dano fixo; o sorteio decide se acertam.
- Um ataque válido, acertando ou errando, permite resposta do inimigo. Um derrotado não contra-ataca. Índice inválido, falta de mana, falta de poção ou vida cheia não passam o turno.
- Magia consome mana mesmo quando erra. Cajado não custa mana. Só Mago possui mana.
- Cada partida começa com três poções de 50 de vida. A cura respeita o máximo; poção não ressuscita. O item só sai do inventário após sucesso. Em batalha, beber poção permite contra-ataque; no mapa não movimenta inimigos.
- Vitória comum remove o inimigo, concede uma poção e permite descanso: até +20 de vida; Mago também recupera até +30 de mana, limitado a 60. Isso mantém as três classes viáveis ao longo da campanha.
- O chefe fica parado e protegido enquanto houver guardas. Após derrotá-los, ele persegue o jogador. Com metade da vida ou menos, troca a lâmina pela fúria.
- Vida zero: derrota. Derrotar o chefe: vitória final. F1/F2/F3 ou R começam outra partida; não há salvamento.

## Classes e ataques

Formato: **dano / precisão / custo de mana**. Ataques físicos não usam mana.

| Classe | Vida | Ataque 1 | Ataque 2 | Ataque 3 |
|---|---:|---|---|---|
| Guerreiro | 140 | Corte rápido: 12 / 95% | Espadada: 24 / 80% | Golpe pesado: 40 / 55% |
| Mago | 110 | Cajado: 12 / 95% | Raio: 30 / 90% / 8 | Tempestade: 45 / 70% / 14 |
| Arqueiro | 120 | Tiro rápido: 16 / 95% | Tiro preciso: 25 / 85% | Flecha pesada: 38 / 65% |

| Inimigo | Vida | Ataque |
|---|---:|---|
| Goblin | 50 | Arranhão: 9 / 75% |
| Orc | 85 | Machadada: 15 / 80% |
| Guardião | 160 | Lâmina: 18 / 80%; fúria a partir de 80 de vida: 27 / 65% |

## Testar

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe src/main.py --smoke-test
```

Os testes são escritos com `unittest` e `Mock`, como nas aulas, e executados por `pytest`, conforme o roteiro. Cobrem regras e casos inválidos, turnos, caminhos, ocupação, interface e campanha das três classes. A campanha usa sorteio controlado para reproduzir resultados; não garante vitória em todas as partidas aleatórias.

`--smoke-test` abre uma tela simulada, desenha três quadros e encerra. A suíte também simula teclado e renderiza os estados do jogo. Confira manualmente WASD, ataques, poções e fechamento ao apresentar o projeto.

## Gerar o executável Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

O script executa os testes e gera `dist/OOP_RPG_Game.exe`, incluindo as artes. O ajuste de política vale apenas para esse processo; não modifica a configuração permanente do computador. Alternativa direta:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --windowed --name OOP_RPG_Game --add-data "src/artes:artes" src/main.py
```

Depois, abra `dist/OOP_RPG_Game.exe`. O executável contém o interpretador e as dependências, portanto não requer instalar Python no computador de destino Windows. O binário não é versionado no Git; pode ser reconstruído pelo script.

## Artes ASCII

Edite `src/artes/guerreiro.txt`, `mago.txt`, `arqueiro.txt`, `inimigo.txt`, `orc.txt` e `chefe.txt`. Use UTF-8, até 24 caracteres por linha e até 6 linhas, sem tabulações. O desenho usa fonte monoespaçada. As barras invertidas nos `.txt` são escritas normalmente, sem duplicação.

O carregamento usa o caminho de `recursos.py`, não a pasta atual do terminal. Depois de alterar as artes, gere novamente o executável.

## Estrutura e estudo

```text
src/
  main.py          janela, eventos e laço principal
  interface.py     desenho do mapa, combate e painel
  jogo.py          exploração e transições de estado
  mapa.py          casas permitidas e busca de caminho
  personagens.py   Personagem, Guerreiro, Mago, Arqueiro
  ataques.py       Ataque, Golpe, Magia
  inimigos.py      Inimigo, Orc, Chefe
  itens.py         Item, PocaoVida
  batalha.py       ações e resposta do inimigo
  recursos.py     leitura das artes
  artes/           arquivos de texto
tests/             testes automatizados
docs/              arquitetura e histórico de desenvolvimento
build.ps1          geração do executável
```

Veja [POO, SOLID e decisões](docs/ARQUITETURA.md) e [histórico por issue/PR](docs/DESENVOLVIMENTO.md).

## Referências de infraestrutura

- [Pygame — documentação oficial](https://www.pygame.org/docs/)
- [pytest executando unittest](https://docs.pytest.org/en/stable/how-to/unittest.html)
- [PyInstaller — localização de arquivos no executável](https://www.pyinstaller.org/en/stable/runtime-information.html)

As regras utilizam os conceitos das aulas fornecidas. Pygame, pytest e PyInstaller são infraestrutura adicional para janela, execução dos testes e distribuição.
