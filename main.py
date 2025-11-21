# main.py
import sys
from board import read_board, print_board
from solver import solve_numberlink


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_tablero>")
        print("Ejemplo: python main.py numberlink_00.txt")
        return

    path = sys.argv[1]
    board, flows = read_board(path)

    print("Tablero inicial:")
    print_board(board)
    print()

    solved = solve_numberlink(board, flows)

    if solved:
        print("¡Solución encontrada!")
        print_board(board)
    else:
        print("No se encontró solución que llene todas las celdas.")


if __name__ == "__main__":
    main()