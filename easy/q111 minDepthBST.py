'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        q = deque([(root, 1)])
        
        # leaf node = both children are null
        while q:
            top, depth = q.popleft()
            
            # is top a leaf
            if top != None and top.left == None and top.right == None:
                return depth
            
            if top.left:
                q.append((top.left, depth+1))
            if top.right:
                q.append((top.right, depth+1))
        
        
            
        