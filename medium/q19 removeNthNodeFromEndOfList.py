"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        start = head

        # find the n-1 node from start
        end = start
        for i in range(n):
            end = end.next

        while end and end.next:
            start = start.next
            end = end.next

        # start is the n-1th node from the end of the list
        if head == start and not end: # remove first node
            return head.next
        elif start.next:
            start.next = start.next.next
        else:
            start.next = None

        return head
