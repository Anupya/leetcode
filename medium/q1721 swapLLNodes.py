# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        if not head.next:
            return head
        
        p, h1, h2 = head, None, None
        
        while p:
            k -= 1
            
            if h2:
                h2 = h2.next
            
            if k == 0:
                h1 = p
                h2 = head
            
            p = p.next
            
        
        h1.val, h2.val = h2.val, h1.val
        return head
    
        