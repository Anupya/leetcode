'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSum(self, root):
        if not root:
            return 0
        
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        
        return left + right + root.val
    
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.findTilt(root.left)
        right = self.findTilt(root.right)
        
        leftSum = self.getSum(root.left)
        rightSum = self.getSum(root.right)
        
        tilt = abs(leftSum-rightSum)
        
        return left + right + tilt
        
        
        