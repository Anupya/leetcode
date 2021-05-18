'''
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins and there are n coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another. (A move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def distributeCoins(self, root: TreeNode) -> int:
        
        # intuition = count how many moves the excess is making
        self.ans = 0
        
        def excess(root):
            if not root:
                return 0
            
            left = excess(root.left)
            right = excess(root.right)
            
            self.ans += abs(left) + abs(right)
            
            # carry over moves throughout rest of the tree
            return root.val + left + right - 1
        
        excess(root)
        return self.ans
            
            
        
        