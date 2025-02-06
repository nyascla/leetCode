from typing import Optional
'''
Encontrar la mitad, invertir la lista en una mitad e iterar con dos punteros
Encontrar la mited
dos punteros fast slow fast aumenta += 2 slow += 1
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pass

if __name__ == "__main__":
    head = [5, 4, 2, 1]
    sol = Solution().pairSum(head)
    print(sol)

'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''