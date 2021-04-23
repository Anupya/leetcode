# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = int(len(nums)/2)
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        
        return TreeNode(nums[mid], left, right)
        