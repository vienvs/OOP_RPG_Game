from pathlib import Path

# __file__ também aponta para os arquivos extraídos pelo PyInstaller.
PASTA_ARTES = Path(__file__).resolve().parent / "artes"


def carregar_arte(nome):
    with open(PASTA_ARTES / (nome + ".txt"), encoding="utf-8") as arquivo:
        return arquivo.read().splitlines()
