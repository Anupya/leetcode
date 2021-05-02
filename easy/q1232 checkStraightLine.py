# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x = (coordinates[1][0] - coordinates[0][0])
        y = (coordinates[1][1] - coordinates[0][1])

        slope = y/x if x else float('inf')

        for x in range(2, len(coordinates)):
            newX = (coordinates[x][0] - coordinates[x-1][0])
            if newX:
                newSlope = (coordinates[x][1]-coordinates[x-1][1])/newX
                if slope != newSlope:
                    return False
            elif slope != float('inf'):
                return False

        return True