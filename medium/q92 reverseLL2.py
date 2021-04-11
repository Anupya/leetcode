# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        return prev
    
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        index = 1
        curr = head
        revbeforestart = None
        revstart = None
        revend = None
        revafterend = None
        
        # Find values of above pointers
        while curr and index <= right:
            if index < left:
                revbeforestart = curr
            
            if index == left:
                revstart = curr
                
            if index == right:
                revend = curr
                revafterend = curr.next
            
            index+=1
            curr = curr.next
        
        revend.next = None
        revend = self.reverseList(revstart)
        
        # if starting position was not head
        if (revbeforestart):
            revbeforestart.next = revend
        else:
            head = revend
        
        revstart.next = revafterend
        
        return head
        