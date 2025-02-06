'''
El problema consiste en encontrar el camino mas corto entre
dos grupos de "1" que estan en una matriz de "0"

Recorrer Grafos

    SOLUCION
        encontrar la primera insla
    Ejecutar un DFS cuando encontremos la primera casilla de un insla
    buscamos en profundidad y guardamos en un conjunto todas las casillas de esa insla
    para cada iteracion mirados los 4 lados de la casilla
    llegamos a un nodo bueno, añadimos a visitados y miramos sus 4 esquinas,
    es un nodo bueno añadimos y miramos sus 4 esquinas
    no es un modo bueno return y seguimos desde el anterior nodo bueno mirando
    las 3 esquinas que faltas

        encontrar el camino mas corto entre la primera isla y la segundo
    Para ello utilizar BFS, algoritmo tipico para encontrar la distancia en grafos no dirigidos
    iteraremos el grafo por capas de vecinos hasta encontrar el primer nodo de la otra isla
'''

from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def invalid(r, c) -> bool:
            return r >= N or r < 0 or c >= N or c < 0


        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visited):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            capa = 0
            stack = []
            stack += visited

            while stack:
                for x in range(len(stack)):
                    r, c = stack.pop(0)

                    for dr, dc in directions:
                        newR, newC = r + dr, c + dc
                        if invalid(newR, newC) or (newR, newC) in visited:
                            continue
                        if grid[newR][newC]:
                            return capa
                        visited.add((newR, newC))
                        stack.append((newR, newC))
                capa += 1
            return -1

        visited = set()
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()

        return -1
'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Array
Depth-First Search
Breadth-First Search
Matrix
'''