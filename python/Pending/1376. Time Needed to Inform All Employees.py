'''
El jefe quiere dar una noticia, Esta tiene que pasar por todos los empleados

En la empresa hay N empleados
distribuidos en forma de arbol segun su rango

la informacion pasa del jefe

Devuelve el tiempo que le cuenta a una noticia pasar del jefe a todos los empleados
'''
import collections
from typing import List
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = collections.defaultdict(list)

        for employee in range(n):
            dic[manager[employee]].append(employee)

        stack = [(headID, 0)]
        res = 0
        while stack:
            manager, time = stack.pop(0)
            res = max(res, time)
            for employee in dic[manager]:
                stack.append((employee, time + informTime[manager]))

        return res
'''
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

Tree
Depth-First Search
Breadth-First Search
'''