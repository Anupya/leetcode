'''
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        # create 2D matrix where grid[row][col] = 1 if a brick ends there
        # look at each column and the one with most 1s is the vertical line we want
        
        width = sum(wall[0])
        
        # key = column index, val = # of bricks ending there
        brickEnds = {}
        
        for i, row in enumerate(wall):
            ptr = 0
            for j in range(len(row)):
                ptr += row[j]
                if ptr < width:
                    if ptr in brickEnds:
                        brickEnds[ptr] += 1
                    else:
                        brickEnds[ptr] = 1
        
        if len(brickEnds) == 0:
            return len(wall)
        
        return len(wall) - max(brickEnds.values())
    
        
        
        
        
        