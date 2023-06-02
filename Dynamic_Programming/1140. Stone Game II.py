'''
Problema
    Juego entre A y B el problema consiste en maximizar los puntos de A
    El juego consiste en conseguir el mayor numero de piedras
    las piedras estan en pilas (varias pilas)
    en cada tueno se pueden coger todas las piedras de las X primeras pilas
Las restricciones
    En cada turno puedos pillar X piedras (1 <= X <= 2M)
    M es una constante que empieza en 1 en cada turno se modifica (M = max(M, X))
    ambos juegos de forma obtima

Solucion
Primera idea: arbol de decisiones
para los dos jugadores
    A maximizaremos
    B minimizaremos
    los dos juegan optimo su partida
info de caba nivel del arbol
    De quien es el turno
    En que indice estamos
    la M
En cada nivel
    devolver el maximo de piedras posibles para A
    devolver el minimo de piedras posible para B
    un for de mire todas las posibles decisiones
    max() o min() devuelve el valor al nivel inferior

'''
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def dfs(alice, i, m):
            if i >= len(piles):
                # cuando llega al final del arbol de decisiones devuelve 0 y empiezan los calculos
                return 0
            if (alice, i, m) in dp:
                return dp[(alice, i, m)]

            # res maniene el mejor resultado en el nivel, despues pasa a una capa inferior
            # si es ALICE el objetivo es maximizar
            # si es BOB el objetivo es minimizar
            res = 0 if alice else float("inf")
            total = 0
            # todas las opciones en este turno
            for x in range(1, (2 * m) + 1):
                # fuera de rango
                if (i + x - 1) >= len(piles):
                    break
                # suma las piedras de todas las posibles opciones
                # desde pillar 1 piedra a 2M piedras
                total += piles[i + x - 1]
                if alice:
                    # pregunta por el mejor resultado en capas superiores
                    # suma el total de esta ronda al mejor acumulado
                    # res mantiene el mejor valor de este turno
                    res = max(res, total + dfs(not alice, i + x, max(x, m)))
                else:
                    res = min(res, dfs(not alice, i + x, max(x, m)))

            # el mejor valor de este turno
            dp[(alice, i, m)] = res
            return res

        dp = {}

        return dfs(True, 0, 1)

if __name__ == "__main__":
    piles = [2, 7, 9, 4, 4]
    sol = Solution().stoneGameII(piles)
'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Array
Math
Dynamic Programming
Game Theory
'''