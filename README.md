# OOP RPG Game

RPG ASCII em Python para a disciplina de Programação Orientada a Objetos.
Base atual: mapa, janela e movimentação. As funcionalidades entram por issues e PRs individuais.

## Executar (Windows, Python 3.12)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe src/main.py
```

WASD/setas movem uma casa. Paredes bloqueiam. ESC fecha.

## Verificar

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe src/main.py --smoke-test
```

O segundo comando desenha três quadros usando SDL simulado e encerra. Não substitui jogar manualmente.
Testes usam `unittest` das aulas, executado por `pytest` conforme o roteiro.

## Organização

`src/personagens.py`: estado e comportamento. `src/mapa.py`: cenário.
`src/main.py`: janela e teclado. A interface usa Pygame; as regras de POO não dependem dele.

Projeto individual. O proprietário autorizou PRs sem revisor externo; os testes devem passar antes do merge.
