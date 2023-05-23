from collections import defaultdict
from typing import List

'''
Entendiendo el problema como muchos arboles (porque sabemos que es un grafo sin ciclos)
    Todos los nodos raiz son la solucion
    
'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for desde,hasta in edges:
            dic[hasta].append(desde)

        sol = []
        for x in range(n):
            if x not in dic:
                sol.append(x)

        return sol

'''
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
'''
