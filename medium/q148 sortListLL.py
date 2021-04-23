# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        # convert to list
        llList = []
        while head:
            llList.append(head.val)
            head = head.next
        
        # sort it
        llList = sorted(llList)
        
        # convert back to LL
        head = ListNode(llList.pop(0))
        final = head
        while len(llList):
            head.next = ListNode(llList.pop(0))
            head = head.next
        
        return final

                    
                
            