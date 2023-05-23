'''
Programacion dinamica

    Subestructuras óptimas - se pueden usar soluciones óptimas de subproblemas para encontrar la solución óptima
        1. Dividir el problema en subproblemas más pequeños.
        2. Resolver estos problemas de manera óptima usando este proceso de tres pasos recursivamente.
        3. Usar estas soluciones óptimas para construir una solución óptima al problema original.
    
    Subproblemas superpuestos - se usa un mismo subproblema para resolver diferentes problemas
        sucesión de Fibonacci (F3 = F1 + F2 y F4 = F2 + F3) calcular cada término supone calcular F2. Como para calcular F5 hacen falta tanto F3 como F4

    Parecido: 
        Similar a LCS(long common subsecuence)
    
    Solucion recursiva (Subestructura optimas)
        i = index array1
        j = index array2
        Arbol binario - En cada nivel avanzamos a la derecha 
        subarbol izquirdo avanzamos i
        subarbol derecho avanzamos j
    
    Subproblema (Subproblemas superpuestos)
        Dibujando el arbol se vee que muchos subarboles son iguales

'''
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        def df(i, j):
            if i == len(nums1) or j == len(nums1):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + df(i + 1, j + 1)
            else:
                dp[(i, j)] = max(df(i + 1, j), df(i, j + 1))

        dp = {}
        df(0,0)


if __name__ == "__main__":
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    sol = Solution().maxUncrossedLines(nums1, nums2)

'''
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.
'''