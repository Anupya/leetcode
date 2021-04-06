# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for j in range(n)] for i in range(m)] # prefill with 1s
        
        # each cell is visited once
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
        
        return matrix[-1][-1] # return last cell