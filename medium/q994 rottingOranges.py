# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        minutes = 0
        
        # find all fresh oranges in grid and store them
        fresh = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh.add((row, col))

        while len(fresh):
            removed = set()
            for row in range(len(grid)):
                for col in range(len(grid[0])):

                    if grid[row][col] == 1:

                        # check top, left, right, down
                        top, left, right, down = 0, 0, 0, 0

                        if row-1>=0 and grid[row-1][col] == 2:
                            top = 1

                        if row+1<len(grid) and grid[row+1][col] == 2:
                            down = 1

                        if col-1>=0 and grid[row][col-1] == 2:
                            left = 1

                        if col+1< len(grid[0]) and grid[row][col+1] == 2:
                            right = 1

                        if top or left or right or down:
                            removed.add((row, col))
                            fresh.remove((row, col))
            
            # if no fruit rotted after a minute, then there exists 1<= fruits that cannot rot
            if len(removed) == 0:
                return -1
            
            for row, col in removed:
                grid[row][col] = 2
            
            minutes +=1 
        
        return minutes
                    
                        
                        
                    
                
        