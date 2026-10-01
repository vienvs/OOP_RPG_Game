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
