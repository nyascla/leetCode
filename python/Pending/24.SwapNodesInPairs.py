from typing import Optional

'''
Problemas que se pueden dividir en casos más pequeños: Algunos problemas se pueden resolver dividiéndolos en casos más pequeños del mismo tipo. Cada caso más pequeño se resuelve de la misma manera utilizando la misma lógica. Un ejemplo clásico es el algoritmo de ordenamiento recursivo "Quicksort".

Estructuras de datos recursivas: Si estás trabajando con estructuras de datos recursivas como árboles o listas enlazadas, es común utilizar la recursión para recorrer o procesar los elementos de la estructura. Por ejemplo, recorrer un árbol binario o encontrar un elemento en una lista enlazada.

Backtracking (retroceso): Algunos problemas requieren explorar todas las posibles soluciones o combinaciones. En estos casos, la recursión puede ser utilizada para probar todas las opciones de forma exhaustiva y realizar un retroceso cuando se alcanza una solución incorrecta. El algoritmo de "N-queens" (reinas) es un ejemplo común de un problema resuelto mediante backtracking recursivo.

Problemas con estructuras recursivas: Algunos problemas están inherentemente definidos de forma recursiva. Por ejemplo, cálculos matemáticos como el factorial o la secuencia de Fibonacci se definen en función de sí mismos, por lo que se pueden resolver de manera natural utilizando recursión.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
'''