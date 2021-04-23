# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.


class Solution:
    def calculateSlope(self, p1, p2):
        return (p2[1]-p1[1])/(p2[0]-p1[0])
   

    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points) < 3:
            return len(points)
        
        curMax = 1
        
        # convert lol to lot
        points = [tuple(p) for p in points]
        
        # compare every point with every point
        for i, point1 in enumerate(points):
            
            potentialLines = {} # slope: set(points on this line)
            verticalSet = set({point1})
            
            for j, point2 in enumerate(points):
                if i == j:
                    continue
                else:
        
                    # vertical line
                    if point2[0]-point1[0] == 0:
                        verticalSet.add(point2)
                        continue    
                    
                    # every other line
                    slope = self.calculateSlope(point1, point2)
                    if slope in potentialLines:
                        if point2 in potentialLines[slope]:
                            continue
                        potentialLines[slope].add(point2)
                    else:
                        pointsSoFar = set()
                        pointsSoFar.add(point1)
                        pointsSoFar.add(point2)
                        potentialLines[slope] = pointsSoFar
            
            curMax = max(curMax, len(verticalSet))
            for key, value in potentialLines.items():
                if curMax < len(value):
                    curMax = len(value)
                    
         
        return curMax
            
            
        
        