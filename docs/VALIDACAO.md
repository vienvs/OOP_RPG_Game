# Validação da entrega final

Ambiente: Windows 11, Python 3.12.10, Pygame 2.6.1, pytest 9.1.1 e PyInstaller 6.22.3.

- Suíte final: 56 testes e 17 subtestes aprovados.
- Cada etapa executou pytest, smoke test e git diff --check antes de publicar seu PR.
- Campanhas determinísticas: Guerreiro, Mago e Arqueiro completam o percurso até a vitória.
- Simulação adicional: 100 sementes por classe, 300 partidas; todas encerraram em vitória ou derrota, sem estado preso. Política automática: atacar com maior dano esperado disponível e usar poção com vida menor ou igual a 50. Vitórias: Guerreiro 98/100; Mago 99/100; Arqueiro 100/100. Esses números descrevem essa estratégia e essas sementes, não uma garantia de vitória.
- Interface: eventos de teclado/saída e estados de mapa, batalha, vitória e derrota exercitados com SDL simulado. Capturas de mapa e batalha conferidas visualmente.
- Artes: arquivos de todas as classes/inimigos carregados a partir de outra pasta de trabalho.
- Executável Windows gerado com build.ps1 e executado com --smoke-test fora da pasta do projeto, encerrando com código zero. Tamanho aproximado: 14,9 MB.

A validação gráfica foi automatizada; não houve uma sessão manual completa de jogo. Recomenda-se jogar uma partida interativa antes da apresentação.
