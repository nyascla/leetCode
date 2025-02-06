'''
Algoritmo de buscada en grafos
    En una matriz cuadrada de 0 y 1
    Encuentra un camino despejado (todos 0)
    Desde una casilla te puedes mover en las 8 direcciones
    No puedes repetir nodos visitados

'''
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        size = len(grid) -1
        if grid[size][size] == 1:
            return -1
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

        stack = []
        visited = []

        stack.append((0, 0, 1))
        visited.append((0,0))
        def is_valid(x, y):
            return x < len(grid) and x >= 0 and y < len(grid) and y >= 0

        while stack:
            nx,ny,d = stack.pop(0)

            if (nx, ny) == (size, size):
                return d

            for dx,dy in directions:
                x = nx + dx
                y = ny + dy
                if not is_valid(x,y):
                    continue
                if (x,y) in visited:
                    continue
                if grid[x][y] == 1:
                    continue

                stack.append((x,y, d + 1))
                visited.append((x,y))

        return -1

if __name__ == "__main__":
    # grid = [[0,1],[1,0]]
    # grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid = [
        [0,1,1,0,0,0],
        [0,1,0,1,1,0],
        [0,1,1,0,1,0],
        [0,0,0,1,1,0],
        [1,1,1,1,1,0],
        [1,1,1,1,1,0]
    ]
    sol = Solution().shortestPathBinaryMatrix(grid)
    print(sol)

'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''