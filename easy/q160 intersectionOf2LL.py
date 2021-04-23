# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None and headB is None:
            return null
        
        ha = headA
        hb = headB
        while ha is not hb:
            # make the shorter one traverse the length of the longer one once it reaches the end
            # this will make length diff irrelevant because in second traversal
            # they read the nodes that have same distance from the end of headA/headB
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        
        return ha # gets here if both lists reached the end or found the intersection
        