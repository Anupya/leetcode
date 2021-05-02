# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

class Solution:
    def getSuperInterval(self, ivl1, ivl2):
        return [min(ivl1[0], ivl2[0]), max(ivl1[1], ivl2[1])]
    
    def isOverlap(self, ivl1, ivl2):
        return ivl1[0] <= ivl2[0] <= ivl1[1] or ivl2[0] <= ivl1[0] <= ivl2[1]
        
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        # add it in the right spot
        i = 0
        while True:
            if i == len(intervals) or intervals[i][0] > newInterval[0]:
                break
            i += 1

        intervals.insert(i, newInterval)
        
        # get start and stop index of overlapping intervals
        i = 0
        start, end = -1, -1
        while True:
            if start == -1 and self.isOverlap(intervals[i], newInterval):
                start = i
            elif start > -1 and not self.isOverlap(intervals[i], newInterval):
                end = i-1
                break
            if i == len(intervals)-1:
                end = i
                break
            i+=1
        
        if start == end:
            return intervals
        
        bigInterval = self.getSuperInterval(newInterval, self.getSuperInterval(intervals[start], intervals[end]))
        del intervals[start:end+1]
        intervals.insert(start, bigInterval)
        return intervals
