# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge2(self, iv1, iv2):
        return [min(iv1[0], iv2[0]), max(iv1[1], iv2[1])]
    
    def isOverlapping(self, iv1, iv2):
        
        # if end point of 1 interval falls on 2nd interval
        return iv2[0] <= iv1[1] <= iv2[1] or iv1[0] <= iv2[1] <= iv1[1]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        finalIntervals = []
        intervals[:] = sorted(intervals, key=lambda x:x[0])
        
        for interval in intervals:
            
            # if empty or cannot overlap with last interval
            if not finalIntervals or not self.isOverlapping(finalIntervals[-1], interval):
                finalIntervals.append(interval)
            
            # can overlap with last interval
            else:
                finalIntervals[-1] = self.merge2(finalIntervals[-1], interval)
        
        return finalIntervals
                
        