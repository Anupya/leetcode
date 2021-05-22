'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getAncestors(self, root, val, loa):
        if not root:
            return []

        if root.val == val:
            return loa + [root]
        
        left = self.getAncestors(root.left, val, loa + [root])
        if len(left):
            return left
        
        right = self.getAncestors(root.right, val, loa + [root])
        return right
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        aop = self.getAncestors(root, p.val, [])
        aoq = self.getAncestors(root, q.val, [])

        aopL = [x.val for x in aop]
        aoqL = [x.val for x in aoq]
        
        commonAncestors = set(aopL) & set(aoqL)
        
        # lowest common ancestor appears last in aop
        loa = -1
        for x in commonAncestors:
            if aopL.index(x) > loa:
                loa = aopL.index(x)
        
        return aop[loa]

        
        