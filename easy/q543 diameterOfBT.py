'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        dLeft = 1 + self.maxDepth(root.left)
        dRight = 1 + self.maxDepth(root.right)
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        
        pathLength = dLeft + dRight - 2
        
        if left >= right and left > pathLength:
            return left
        elif right >= left and right > pathLength:
            return right
        else:
            return pathLength
