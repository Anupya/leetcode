"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        head = root
        while root:
            left = root.left
            rightMost = left

            # find rightmost node of left half
            while rightMost and rightMost.right:
                rightMost = rightMost.right
            
            # attach right half of tree to right-most node of left half
            if rightMost:
                rightMost.right = root.right
                root.right = root.left
                root.left = None
            
            root = root.right
        
        