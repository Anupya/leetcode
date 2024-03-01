"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numLen = len(nums)
        nums.sort()

        i = 1
        while i < numLen:
            if nums[i-1] != nums[i]:
                return nums[i-1]
            
            i += 2

        return nums[0] if numLen == 1 else nums[-1]
        