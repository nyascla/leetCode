from typing import List

'''
Un grafo cumple la siguiente caracteristica?
En un grafo no dirigido se pueden separar los nodos en dos conjuntos de modo q todos los vertices conectern nodes de A y B

INTUICON
Recorremos el grafo en anchura - creamos don conjunto A B
ponemos el 0 en A y todos sus adyacentes en B
ahora todos los adyacentes de B tendirian que estar en A si alguno esta en B no cumple las restricciones
si esa condicion no se cumple devolvemos false
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    sol = Solution().isBipartite(graph)
    print(sol)

'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
'''