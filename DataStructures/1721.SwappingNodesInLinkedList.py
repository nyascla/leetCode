from typing import Optional

'''
LISTAS ENLAZADAS
    problema muy basico
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    pass

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