# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cur1 = l1
        cur2 = l2
        carryOver = 0
    
        result = ListNode()
        final = result
        while cur1 or cur2:
            addition = 0
            if cur1:
                addition += cur1.val
            if cur2:
                addition += cur2.val
               
            if addition + carryOver > 9:
                onesDigit = int(str(addition + carryOver)[1]) # ones digit
                carryOver = 1
                result.val = onesDigit
                   
            else:
                result.val = addition + carryOver
                carryOver = 0
            
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            if cur1 or cur2:
                result.next = ListNode()
                result = result.next
                
        
        if carryOver:
            result.next = ListNode(1)
            
        return final
                
            
        