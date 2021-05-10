# Print a binary tree in an m x n 2D string array following these rules:

# The row numbers m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exact middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getHeight(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left, right = 0, 0
        if root.left:
            left = 1 + self.getHeight(root.left)
        if root.right: 
            right = 1 + self.getHeight(root.right)
        
        return max(left, right)
        
        
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        height = self.getHeight(root)
        numStrings = (2**height)-1
        
        final = [["" for x in range(numStrings)] for y in range(height)]
        
        def fillList(start, end, node, level):
            mid = start+((end-start)//2)
            final[level][mid] += str(node.val)
            
            if node.left:
                fillList(start, mid, node.left, level+1)
            if node.right:
                fillList(mid, end, node.right, level+1)
                
        fillList(0, len(final[0]), root, 0) 
        
        return final
        