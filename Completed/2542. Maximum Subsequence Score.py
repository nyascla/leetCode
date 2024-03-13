'''
DESCRIPCION:
    Dos listas, una constante X
    Devuelve la mayor subsecuencia de tamanyo X de la primera lista
    Maximiza:
    Todos los elementos de la subsecuencia 1 multiplicados por el menor elemento de la subsecuencia 2
    SUBSECUENCIA es un conjunto que puede ser derivado de eliminar alguno o ningun elemento de la lista

#Monticulo

Si realizaramos el problema por fuerza bruta tedriamos q probar     nCk = n! / (k! * (n - k)!)

Si entendemos el problema podemos ver que la clave es la lista2
    Ordenamos las dos listas en base a la lista2
    - podremos formar los subconjuntos del problema de forma muy sencilla

    Empezamos con los K primeros elementos de la lista1 multiplicados por el valor q esta en la posicion K-1 de la lista2
    ahora queda iterar el resto de elementos de la lista2 y ver si hay alguna mejor solucion
        Iteramos:
        se pillara el siguiente valor de la lista2 (sera uno de menor valor ya que esta ordenado)
        se eliminara el menor valor del subconjunto de la lista1 (porque es un subconjunto de tamanyo fijo y se busca maximizar)
        se anyadira al subconjunto el valor de la lista1 correspondiente al nuevo elemento de la lista2

    para mantener una lista de tamanyo fijos con los mayores elementos posibles la solucion optima es utilizar un monticulo
    de esta forma sera O(1) eliminar el menor valor del subconjunto
'''
from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Ordenar las listas respecto a la lista2
        lista = list(zip(nums1, nums2))
        lista = sorted(lista, key=lambda x: x[1], reverse=True)

        # rellear el maxheap con los k primeros elementos
        max_heap, answer = [], 0
        for x in lista[:k]:
            heapq.heappush(max_heap, x[0])

        # Primera posible respuesta
        heap_sum = sum(max_heap)
        answer = heap_sum * lista[k - 1][1]

        # Iterar el resto de posibles respuestas
        for x in lista[k:]:
            heap_sum -= heapq.heappop(max_heap)
            heap_sum += x[0]
            heapq.heappush(max_heap, x[0])

            answer = max(answer, heap_sum * x[1])

        return answer

if __name__ == "__main__":
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    sol = Solution().maxScore(nums1, nums2, k)
'''
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.
'''