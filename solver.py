# solver.py
from typing import List, Tuple
from board import Board, Pos, Flow, is_full, manhattan

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha


def solve_numberlink(board: Board, flows: List[Flow]) -> bool:
    """
    Resuelve el puzzle de Numberlink modificando el board IN-PLACE.
    Devuelve True si encontró solución que llena todas las celdas.
    """

    # Heurística simple: ordenar parejas por distancia Manhattan
    flows.sort(key=lambda item: manhattan(item[1][0], item[1][1]))

    R, C = len(board), len(board[0]) if board else 0

    def solve_all(idx: int) -> bool:
        # Si ya tratamos todas las parejas, comprobar que el tablero está lleno
        if idx == len(flows):
            return is_full(board)

        symbol, (start, end) = flows[idx]
        sr, sc = start

        # Desde el start (que ya tiene el símbolo) lanzamos DFS
        return dfs_path(sr, sc, end, symbol, idx)

    def dfs_path(r: int, c: int, end: Pos, symbol: str, flow_idx: int) -> bool:
        # Si llegamos al otro extremo, pasamos a la siguiente pareja
        if (r, c) == end:
            return solve_all(flow_idx + 1)

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue

            # Podemos ir al endpoint final o a una celda vacía
            if (nr, nc) == end:
                # No sobrescribimos el endpoint, solo avanzamos
                if dfs_path(nr, nc, end, symbol, flow_idx):
                    return True
            elif board[nr][nc] == " ":
                # Marcar celda como parte del camino
                board[nr][nc] = symbol
                if dfs_path(nr, nc, end, symbol, flow_idx):
                    return True
                # Backtracking: deshacer
                board[nr][nc] = " "

        # No hay forma de conectar este extremo desde (r,c) que lleve a solución
        return False

    return solve_all(0)