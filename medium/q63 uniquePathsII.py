# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#Now consider if some obstacles are added to the grids. How many unique paths would there be?

#An obstacle and space is marked as 1 and 0 respectively in the grid.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # use obstacleGrid to keep track of unique paths to each cell
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        # obstacle at the goal or at the start
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        # replace obstacles with -1
        for x in range(0, rows):
            for y in range(0, cols):
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = -1
        
        obstacleGrid[0][0] = 1
        
        # populate first col
        counter = 1
        while (counter < rows):
            if obstacleGrid[counter][0] == -1: # everything after obstacle is unreachable
                for x in range(counter+1, rows):
                    obstacleGrid[x][0] = 0
                break
            else:
                obstacleGrid[counter][0] = 1
            counter+=1

        
        # populate first col
        counter = 1
        while (counter < cols):
            if obstacleGrid[0][counter] == -1: # everything after obstacle is unreachable
                for x in range(counter+1, cols):
                    obstacleGrid[0][x] = 0
                break
            else:
                obstacleGrid[0][counter] = 1
            counter+=1
        
        # populate rest of the matrix
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] >= 0: # current cell is not an obstacle
                    
                    # no way of getting to this cell
                    if obstacleGrid[row][col-1] == -1 and obstacleGrid[row-1][col] == -1: 
                        obstacleGrid[row][col] = 0
                    
                    # left or top cell is obstacle
                    elif obstacleGrid[row][col-1] == -1 or obstacleGrid[row-1][col] == -1: 
                        obstacleGrid[row][col] = max(obstacleGrid[row][col-1], obstacleGrid[row-1][col])
                    
                    # top and left cell are not obstacles
                    else:
                        obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
        
        if obstacleGrid[-1][-1] >= 1:
            return obstacleGrid[-1][-1]
        else:
            return 0
                
        
        
        