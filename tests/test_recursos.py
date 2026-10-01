import os
from pathlib import Path
import tempfile
import unittest
from recursos import carregar_arte


class TestRecursos(unittest.TestCase):
    def test_artes_independem_da_pasta_atual(self):
        anterior = Path.cwd()
        try:
            with tempfile.TemporaryDirectory() as pasta:
                os.chdir(pasta)
                for nome in ['guerreiro', 'mago', 'arqueiro', 'inimigo', 'orc', 'chefe']:
                    linhas = carregar_arte(nome)
                    self.assertGreaterEqual(len(linhas), 4)
                    self.assertTrue(all(len(linha) <= 24 for linha in linhas))
                os.chdir(anterior)
        finally:
            os.chdir(anterior)
