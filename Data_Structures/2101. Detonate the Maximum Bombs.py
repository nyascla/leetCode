'''
Dado una lista de bombas (x, y, radio)
Cada bomba tiene un radio de explosion
Si en el radio de explosion de una bomba hay otra, esta explotara

Si solo se puede detonar una bomba manualmente
Cual es el numero maximo de bombas que se pueden explotar
'''
from typing import List
import collections
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Devuelve si una bomba detona otra
        def punto_en_circunferencia(x, y, a, b, r):
            distancia_cuadrada = (x - a) ** 2 + (y - b) ** 2

            return distancia_cuadrada <= r ** 2

        # key: bomba
        # value: todas las bombas que estan en su radio
        dic = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue

                a, b, r = bombs[i]
                x, y, _ = bombs[j]
                if punto_en_circunferencia(x, y, a, b, r):
                    dic[i].append(j)
        # para cada bomba
        # recorrido en profundidad
        res = 0
        for index in range(len(bombs)):
            stack = [index]
            visitados = [index]

            while stack:
                node = stack.pop(0)

                for colateral in dic[node]:
                    if colateral not in visitados:
                        visitados.append(colateral)
                        stack.append(colateral)

            res = max(res, len(visitados))

        return res

if __name__ == "__main__":
    bombs = [[2,1,3],[6,1,4]]
    sol = Solution().maximumDetonation(bombs)

'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.


'''
# Array
# Math
# Depth-First Search
# Breadth-First Search
# Graph
# Geometry
