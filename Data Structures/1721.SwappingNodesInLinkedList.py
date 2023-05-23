from typing import Optional

'''
Intercambia los valores del elemento X desde el inicio y el elemento X desde el final

Al encontrar el elemento X
    Iteramos con DOS punteros, uno desde el inicio y otro desde X
    Cuando el punto desde X llega al final
    El otro puntero estara junto X elementos antes del final 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        for x in range(1,k):
            left = left.next

        right = head
        end = left
        while end.next:
            right = right.next
            end = end.next

        left.val, right.val = right.val, left.val

        return head


'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
'''