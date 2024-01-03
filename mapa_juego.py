import os
from typing import List, Tuple
from readchar import readkey, key

# import readchar

# key = readchar.readkey()

def convertir_a_matriz(laberinto: str) -> List[List[str]]:
    lineas = laberinto.split("\n")
    matriz_laberinto = [list(linea) for linea in lineas]
    return matriz_laberinto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa: List[List[str]]):
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]):
    px, py = inicio
    mapa[px][py] = 'P' 

  

    while (px, py) != final:
        limpiar_pantalla()
        mostrar_mapa(mapa)
        

        movimiento = input("Mueve al personaje (WASD): ")
        nueva_px, nueva_py = px, py

        #movimiento = readkey()
        if movimiento == 'w':
            nueva_px -= 1
        elif movimiento == 's':
            nueva_px += 1
        elif movimiento == 'a':
            nueva_py -= 1
        elif movimiento == 'd':
            nueva_py += 1

        if (
            0 <= nueva_px < len(mapa) and
            0 <= nueva_py < len(mapa[0]) and
            mapa[nueva_px][nueva_py] != '#'
        ):
            mapa[px][py] = '.'
            px, py = nueva_px, nueva_py
            mapa[px][py] = 'P'

# def main_loop(mapa: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]):
#     px, py = inicio
#     mapa[px][py] = 'P' 

#     while (px, py) != final:
#         limpiar_pantalla()
#         mostrar_mapa(mapa)

#         movimiento = input("Mueve al personaje (↑ ↓ ← →): ")



#         nueva_px, nueva_py = px, py 
#         if movimiento == key.UP:
#             nueva_px -= 1
#         elif movimiento == key.DOWN:
#             nueva_px += 1
#         elif movimiento == key.LEFT:
#             nueva_py -= 1
#         elif movimiento == key.RIGHT:
#             nueva_py += 1

#         if (
#             0 <= nueva_px < len(mapa) and
#             0 <= nueva_py < len(mapa[0]) and
#             mapa[nueva_px][nueva_py] != '#'
#         ):
#             mapa[px][py] = '.'
#             px, py = nueva_px, nueva_py
#             mapa[px][py] = 'P'
 
if __name__ == "__main__":
    laberinto =    """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

    mapa_laberinto = convertir_a_matriz(laberinto)
    inicio = (0, 0)
    final = (len(mapa_laberinto) - 1, len(mapa_laberinto[0]) - 1)

    main_loop(mapa_laberinto, inicio, final)