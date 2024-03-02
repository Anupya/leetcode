"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allNums = set(nums)
        lenNums = len(allNums)

        for i in range(1, lenNums+1):
            if i not in allNums:
                return i
        
        return 0
