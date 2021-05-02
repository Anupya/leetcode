# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return None
        
        tortoise = head
        hare = head.next
        
        # find a cycle
        while tortoise and hare and hare.next and tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next.next
        
        # no cycle
        if not tortoise or not hare or not hare.next:
            return None
        
        start = head
        
        # hare started at head.next so we have to start 1 node ahead
        tortoise = tortoise.next
        
        while tortoise != start:
            start = start.next
            tortoise = tortoise.next
        
        return start
        