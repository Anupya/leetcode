# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return None
        
        # store ll in list
        listify = []
        while head:
            listify.append(head.val)
            head = head.next
        
        # reverse
        listify = list(reversed(listify))
        
        oghead = ListNode()
        head = oghead
        
        # make new listnode
        for x in range(0, len(listify)):
            head.val = listify[x]
            if x < len(listify)-1: # not the last elem
                head.next = ListNode()
            head = head.next
        
        return oghead
            