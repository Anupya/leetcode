# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any path.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def maxPathSum(self, root: TreeNode) -> int:
        maxPath = float('-inf')
        
        def maxPathSumHelper(root):
            nonlocal maxPath
            if root is None:
                return 0

            # if the gains are going down, we don't count it
            left = max(maxPathSumHelper(root.left), 0)
            right = max(maxPathSumHelper(root.right), 0) 

            maxGain = left + right + root.val
            maxPath = max(maxPath, maxGain)

            return root.val + max(left, right)
    
        maxPathSumHelper(root)
        return maxPath
