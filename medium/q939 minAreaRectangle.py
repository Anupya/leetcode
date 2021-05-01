# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

# If there isn't any rectangle, return 0.

class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        
        allPoints = set()
        for x, y in points:
            allPoints.add((x,y))
        
        minRectangle = float('inf')
        points.sort()
        
        for p1 in range(len(points)):
            for p2 in range(p1+1, len(points)):
                
                # if points form a diagonal and the missing 2 points are in set
                if (points[p1][0] != points[p2][0] and points[p1][1] != points[p2][1] and 
                    (points[p1][0], points[p2][1]) in allPoints and (points[p2][0], points[p1][1]) in allPoints):

                    area = (abs(points[p1][0]-points[p2][0]))* (abs(points[p1][1]-points[p2][1]))
                    minRectangle = min(minRectangle, area)

        return minRectangle if minRectangle < float('inf') else 0
        
        