"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numberOfZeroes = nums.count(0)
        index = 0
        lenNums = len(nums)
        for i, num in enumerate(nums):
            if num != 0:
                nums[index] = num
                index += 1

        for i in range(numberOfZeroes):
            nums[-i-1] = 0

