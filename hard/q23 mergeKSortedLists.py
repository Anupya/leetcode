# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not len(lists):
            return None
        
        # if all LL in lists are empty
        if all(x == None for x in lists):
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        # merge 2 sorted LL
        elif len(lists) == 2:
            p1 = lists[0]
            p2 = lists[1]
            final = ListNode()
            answer = final
            while p1 and p2:
                if p1.val > p2.val:
                    final.val = p2.val
                    p2 = p2.next
                else:
                    final.val = p1.val
                    p1 = p1.next
                
                final.next = ListNode()
                final = final.next

            while p1:
                final.val = p1.val
                p1 = p1.next
                if p1: 
                    final.next = ListNode()
                    final = final.next
            
            while p2:
                final.val = p2.val
                p2 = p2.next
                if p2: 
                    final.next = ListNode()
                    final = final.next
            
            return answer
            
        else:
            mid = int(len(lists)/2)
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            newL = [left, right]
            return self.mergeKLists(newL)
            
        