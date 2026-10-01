# Histórico de desenvolvimento

Uma issue → uma funcionalidade → uma branch → um PR para main. A etapa 0 prepara a base; as demais seguem as 15 ações do chat.

O repositório inicial continha RPG_Game/main.py vazio, sem testes. Foi executado antes das alterações; pytest inicialmente informou ausência de testes. O ponto de entrada foi organizado em src/main.py.

**Trabalho individual:** o proprietário autorizou seguir sem revisor externo. Não houve autoaprovação registrada como revisão independente. Cada PR foi validado com testes e smoke test antes do merge.

| Etapa | Issue | PR | Entrega |
|---|---|---|---|
| 0 | [#16](https://github.com/vienvs/OOP_RPG_Game/issues/16) | [#17](https://github.com/vienvs/OOP_RPG_Game/pull/17) | Preparar base executável, mapa e ambiente de testes |
| 1 | [#1](https://github.com/vienvs/OOP_RPG_Game/issues/1) | [#18](https://github.com/vienvs/OOP_RPG_Game/pull/18) | Implementar receber_dano() |
| 2 | [#2](https://github.com/vienvs/OOP_RPG_Game/issues/2) | [#19](https://github.com/vienvs/OOP_RPG_Game/pull/19) | Implementar ataque do Guerreiro |
| 3 | [#3](https://github.com/vienvs/OOP_RPG_Game/issues/3) | [#20](https://github.com/vienvs/OOP_RPG_Game/pull/20) | Implementar ataque do Inimigo |
| 4 | [#4](https://github.com/vienvs/OOP_RPG_Game/issues/4) | [#21](https://github.com/vienvs/OOP_RPG_Game/pull/21) | Implementar ataque do Mago |
| 5 | [#5](https://github.com/vienvs/OOP_RPG_Game/issues/5) | [#22](https://github.com/vienvs/OOP_RPG_Game/pull/22) | Implementar magia do Mago |
| 6 | [#6](https://github.com/vienvs/OOP_RPG_Game/issues/6) | [#23](https://github.com/vienvs/OOP_RPG_Game/pull/23) | Criar Poção de Vida |
| 7 | [#7](https://github.com/vienvs/OOP_RPG_Game/issues/7) | [#24](https://github.com/vienvs/OOP_RPG_Game/pull/24) | Implementar uso de itens |
| 8 | [#8](https://github.com/vienvs/OOP_RPG_Game/issues/8) | [#25](https://github.com/vienvs/OOP_RPG_Game/pull/25) | Implementar turno do inimigo |
| 9 | [#9](https://github.com/vienvs/OOP_RPG_Game/issues/9) | [#26](https://github.com/vienvs/OOP_RPG_Game/pull/26) | Implementar condição de vitória |
| 10 | [#10](https://github.com/vienvs/OOP_RPG_Game/issues/10) | [#27](https://github.com/vienvs/OOP_RPG_Game/pull/27) | Criar classe Arqueiro |
| 11 | [#11](https://github.com/vienvs/OOP_RPG_Game/issues/11) | [#28](https://github.com/vienvs/OOP_RPG_Game/pull/28) | Criar novo tipo de inimigo |
| 12 | [#12](https://github.com/vienvs/OOP_RPG_Game/issues/12) | [#29](https://github.com/vienvs/OOP_RPG_Game/pull/29) | Criar chefe final |
| 13 | [#13](https://github.com/vienvs/OOP_RPG_Game/issues/13) | [#30](https://github.com/vienvs/OOP_RPG_Game/pull/30) | Criar testes para Personagem |
| 14 | [#14](https://github.com/vienvs/OOP_RPG_Game/issues/14) | [#31](https://github.com/vienvs/OOP_RPG_Game/pull/31) | Criar testes para Batalha |
| 15 | [#15](https://github.com/vienvs/OOP_RPG_Game/issues/15) | [localizar PR da etapa](https://github.com/vienvs/OOP_RPG_Game/pulls?q=is%3Apr+%22Etapa+15%22) | Melhorar documentação e gerar executável |

## Estudar versões anteriores

Use `git log --oneline --graph --all` para ver implementações e merges. As branches `feature/...` foram preservadas para consulta. O diff de cada PR mostra somente sua etapa.

As etapas iniciais de ataques possuíam uma tela de treinamento. A etapa 8 substituiu os controles provisórios pela exploração e batalha integradas. As etapas 13 e 14 ampliaram os testes que já acompanhavam as funcionalidades.

Para consultar uma versão sem alterar arquivos atuais, use o GitHub e escolha a branch desejada. Para executar uma versão local, termine ou registre mudanças pendentes antes de trocar de branch; atualize as dependências da versão escolhida.

## Critério de conclusão

Cada etapa executa `python -m pytest -q`, `python src/main.py --smoke-test` e `git diff --check`. O PR registra o resultado daquele momento. A etapa final inclui artes, documentação, testes dos recursos e empacotamento Windows.

Os testes gráficos utilizam SDL simulado. A simulação de campanha controla o sorteio; a execução interativa continua importante para conferir a experiência de jogo.

- Etapa 15: implementação e testes registrados no PR correspondente à issue #15.
