# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            
            # heapq is min heap so make it negative so it only keeps closest points
            dist = -(x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
            
        return [(x, y) for (dist, x, y) in heap]
        
        
        
        
        