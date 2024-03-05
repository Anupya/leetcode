"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [[root]]
        values = []
        while True:
            level = queue.pop()
            values.append([])
            queue.append([])

            for node in level:
                if not node:
                    continue

                values[-1].append(node.val)
                if node.left:
                    queue[0].append(node.left)
                if node.right:
                    queue[0].append(node.right)

            if queue == [[]]:
                break

        return values

        