# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # store val in string
        llValues = ""
        while head:
            llValues += str(head.val)
            head = head.next
        
        if len(llValues) < 2:
            return True
        
        if len(llValues) == 2:
            if llValues[0] == llValues[1]:
                return True
            else:
                return False
        
        # two pointers to start and end and they must be the same
        i = 0
        j = len(llValues) - 1
        while i < j:
            if llValues[i] != llValues[j]:
                return False
            i+=1
            j-=1
        
        return True