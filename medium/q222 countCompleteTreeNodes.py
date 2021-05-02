# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left, right = 0, 0
        
        if root.left:
            left = self.countNodes(root.left)
        if root.right:
            right = self.countNodes(root.right)
        
        return 1 + left + right
        