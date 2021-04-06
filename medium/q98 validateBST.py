# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTModified(self, root, minNum, maxNum):
        if not root: # empty tree
            return True
        if minNum < root.val and root.val < maxNum:
            left = self.isValidBSTModified(root.left, minNum, root.val)
            right = self.isValidBSTModified(root.right, root.val, maxNum)
            if left and right:
                return True
            else:
                return False
        else:
            return False
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTModified(root, float('-inf'), float('inf'))
    
    