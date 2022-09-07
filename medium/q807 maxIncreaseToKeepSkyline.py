'''
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

'''

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        # for each cell, min (max of that cell's column, max of that cell's row) - cell value
        
        # maxRowDict = {key=row index, val = maxVal}
        # maxColDict = {key=col index, val = maxVal}

        n = len(grid)
        total = 0
        maxRowDict = {}
        maxColDict = {}
        
        for row in range(n):
            maxRowDict[row] = max(grid[row])
        
        for col in range(n):
            maxVal = float('-inf')
            for row in range(n):
                maxVal = max(maxVal, grid[row][col])
            
            maxColDict[col] = maxVal
        
        for row in range(n):
            for col in range(n):
                
                total += min(maxRowDict[row], maxColDict[col]) - grid[row][col]
        
        return total
                
                
        