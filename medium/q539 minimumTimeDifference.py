"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
"""
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert timepoints into minutes only
        for i, tp in enumerate(timePoints):
            hours, minutes = tp.split(':')
            timePoints[i] = (60*int(hours)) + int(minutes)

        # sort the list
        timePoints.sort()

        # check difference between consecutive points and pick the minimum one
        minDiff = float('inf')
        for i in range(1, len(timePoints)):
            minDiff = min(minDiff, timePoints[i]-timePoints[i-1])
        
        # compare first and last elements
        if (1440-timePoints[-1])+timePoints[0] > 0:
            minDiff = min(minDiff, (1440-timePoints[-1])+timePoints[0])
        return minDiff
