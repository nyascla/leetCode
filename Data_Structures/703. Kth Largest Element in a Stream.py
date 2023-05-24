'''
Clase que almacena una lista con un
metodo add q anyade un valor y devuelve el X valor mas grande

Monticulo

    Min heap de tamanyo X
    ya que en el problema no se borran valores si hay un min heap de tamnanyo X este
    siempre devolvera el X numero mas grande en tiempo O(1)
'''

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Tree
Design
Binary Search Tree
Heap (Priority Queue)
Binary Tree
Data Stream
'''