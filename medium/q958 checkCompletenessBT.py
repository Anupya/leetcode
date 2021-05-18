'''
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        queue = collections.deque([root])
        
        # BFS on tree
        
        while queue:
            top = queue.popleft()
            
            # we should only reach a null if there are no more non-null nodes left in queue
            if top == None:

                while queue:
                    top = queue.popleft()
                    if top != None:
                        return False
                
                return True
                
            queue.append(top.left)
            queue.append(top.right)
        
        