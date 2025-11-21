# Numberlink Solver (Python)

Este proyecto implementa utilidades para trabajar con tableros del puzzle **Numberlink** en Python.

El archivo principal es `board.py`, que contiene funciones para:

- Leer un tablero de Numberlink desde un archivo de texto.
- Representar el tablero internamente como una lista de listas de caracteres.
- Detectar las parejas de símbolos (flujos) y sus posiciones.
- Imprimir el tablero de forma legible en consola.
- Comprobar si el tablero está completamente lleno.
- Calcular la distancia Manhattan entre dos posiciones.

## Formato de entrada

Los tableros se leen desde un archivo de texto, por ejemplo `numberlink_00.txt`, con el siguiente formato:

- **Primera línea**: dos enteros `R C` separados por espacio, donde:
  - `R` = número de filas
  - `C` = número de columnas
- **Siguientes R líneas**: el contenido del tablero, con:
  - Espacio en blanco (` `) para celdas vacías.
  - Cualquier otro símbolo (letra, número, etc.) para marcar los extremos de un flujo.
  - Cada símbolo debe aparecer exactamente **2 veces** en el tablero.

Ejemplo de archivo:

5 5
A   A
  B  
  B  
  C  
C    ## Funciones principales (`board.py`)

- `read_board(path: str) -> Tuple[Board, List[Flow]]`  
  Lee un archivo de Numberlink y devuelve:
  - `board`: el tablero como `List[List[str]]`
  - `flows`: lista de flujos, donde cada flujo es `(símbolo, (pos1, pos2))`

- `print_board(board: Board) -> None`  
  Imprime el tablero en consola, sustituyendo las celdas vacías por `.` para visualizarlas mejor.

- `is_full(board: Board) -> bool`  
  Devuelve `True` si no quedan celdas vacías en el tablero.

- `manhattan(a: Pos, b: Pos) -> int`  
  Devuelve la distancia Manhattan entre dos posiciones `(fila, columna)`.

## Requisitos

- Python 3.8 o superior.

No se requieren librerías externas, solo la librería estándar de Python.

## Uso básico

En un intérprete de Python:

from board import read_board, print_board, is_full, manhattan

board, flows = read_board("numberlink_00.txt")
print_board(board)
print("Tablero completo:", is_full(board))
print("Flujos encontrados:", flows)A partir de estas utilidades se puede implementar un **solver** completo para Numberlink que recorra el tablero y conecte cada pareja de símbolos sin cruces.