'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

'''

class Solution:
    
    def findPath(self, matrix, row, col, last, dp):

        if row<0 or col<0 or row == len(matrix) or col == len(matrix[0]) or matrix[row][col] <= last:
            return 0
        
        if dp[row][col] > 0:
            return dp[row][col]
        
        cur = matrix[row][col]
        left = 1 + self.findPath(matrix, row, col-1, cur, dp)
        right = 1 + self.findPath(matrix, row, col+1, cur, dp)
        up = 1 + self.findPath(matrix, row-1, col, cur, dp)
        down = 1 + self.findPath(matrix, row+1, col, cur, dp)

        dp[row][col] = max(left, right, up, down)
        return dp[row][col]
               
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        path = float('-inf')
        dp = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # find longest increasing path starting from matrix[i][j]
                ans = self.findPath(matrix, i, j, matrix[i][j] - 1, dp)
                path = max(path, ans)
        
        return path
        