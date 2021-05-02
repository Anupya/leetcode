# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxSoFar = 0
        
        start = 0
        end = len(height)-1
        
        # start with left most and right most, the min of those two cannot make a better rectangle
        while start < end:
            if height[start] <= height[end]:
                maxSoFar = max(maxSoFar, height[start]*(end-start))
                start+=1
            else:
                maxSoFar = max(maxSoFar, height[end]*(end-start))
                end -= 1
        
        return maxSoFar
                
                
        