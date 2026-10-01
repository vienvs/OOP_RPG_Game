class Mapa:
    """Representa o cenário: # é parede e . é chão."""

    def __init__(self):
        self.linhas = [
            "########################",
            "#......................#",
            "#......................#",
            "#......######..........#",
            "#......#....#..........#",
            "#......#....#..........#",
            "#......##.###..........#",
            "#......................#",
            "#.................####.#",
            "#.................#..#.#",
            "#.................##.#.#",
            "#......................#",
            "#......................#",
            "########################",
        ]

    def pode_caminhar(self, x, y):
        # Validar antes de indexar evita erro e índices negativos do Python.
        if y < 0 or y >= len(self.linhas):
            return False
        if x < 0 or x >= len(self.linhas[y]):
            return False
        return self.linhas[y][x] == "."

    def proximo_passo(self, inicio, destino, ocupadas):
        # Busca em largura: encontra um caminho curto sem atravessar paredes.
        fila = [(inicio, None)]
        visitadas = {inicio}
        while fila:
            (x, y), primeiro = fila.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                vizinha = (x + dx, y + dy)
                if vizinha in visitadas or vizinha in ocupadas:
                    continue
                if not self.pode_caminhar(*vizinha):
                    continue
                passo = primeiro if primeiro is not None else vizinha
                if vizinha == destino:
                    return passo
                visitadas.add(vizinha)
                fila.append((vizinha, passo))
        return inicio
