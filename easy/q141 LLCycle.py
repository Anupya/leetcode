# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        first = head
        if not head:
            return False
        second = head.next
        while first != second:
            first = first.next
            if second and second.next:
                second = second.next.next
            else:
                # end of LL
                return False
        # first = second so there must be a circle
        return True