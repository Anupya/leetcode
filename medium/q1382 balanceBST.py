'''
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBSTtoArr(self, root):
        
        if not root:
            return []
        
        return self.convertBSTtoArr(root.left) + [root.val] + self.convertBSTtoArr(root.right)
    
    def constructBST(self, arr):
        
        if not arr:
            return None
        
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.constructBST(arr[:mid])
        root.right = self.constructBST(arr[mid+1:])
        
        return root
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        arr = self.convertBSTtoArr(root)
        return self.constructBST(arr)
        