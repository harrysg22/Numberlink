# board.py
from typing import List, Tuple, Dict

# el tablero es una lista de listas de strings
Board = List[List[str]]
# una posición es un par de enteros (fila, columna)
Pos = Tuple[int, int]
# representa el caracter y la tupla de posiciones de los extremos del flujo para luego cuando
# se vaya leyendo el archivo se vaya llenando el tablero se van guardando las posiciones de los extremos del flujo
# que luego se pasan al solver para reseolver el camino para cada pareja que esta en esa lista
Flow = Tuple[str, Tuple[Pos, Pos]]  # (símbolo, (p1, p2))


def read_board(path: str) -> Tuple[Board, List[Flow]]:
    """
    Lee un archivo de Numberlink.
    Primera línea: R C
    Siguientes R líneas: tablero con espacios y símbolos.
    Devuelve: (board, flows)
    """
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline().strip()
        if not first:
            raise ValueError("Archivo vacío o sin dimensiones en la primera línea")
        parts = first.split()
        if len(parts) != 2:
            raise ValueError("Primera línea debe tener: filas columnas")
        R, C = map(int, parts)

        board: Board = []
        for _ in range(R):
            line = f.readline()
            # Rellenar o recortar para que tenga exactamente C caracteres
            line = line.rstrip("\n")
            if len(line) < C:
                line = line + " " * (C - len(line))
            elif len(line) > C:
                line = line[:C]
            board.append(list(line))

    # Encontrar endpoints de cada símbolo
    endpoints: Dict[str, List[Pos]] = {}
    for r in range(R):
        for c in range(C):
            ch = board[r][c]
            if ch != " ":
                endpoints.setdefault(ch, []).append((r, c))

    # Convertir en lista de flujos (símbolo, (p1, p2))
    flows: List[Flow] = []
    for sym, ps in endpoints.items():
        if len(ps) != 2:
            raise ValueError(f"El símbolo {sym} aparece {len(ps)} veces (debería 2).")
        flows.append((sym, (ps[0], ps[1])))

    return board, flows


def print_board(board: Board) -> None:
    """
    Imprime el tablero. 
    """
    for row in board:
        print("".join(ch if ch != " " else "." for ch in row))


def is_full(board: Board) -> bool:
    """
    Devuelve True si no hay celdas vacías (' ') en el tablero.
    """
    return all(ch != " " for row in board for ch in row)


def manhattan(a: Pos, b: Pos) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])