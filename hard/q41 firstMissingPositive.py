# Given an unsorted integer array nums, find the smallest missing positive integer.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        integer = 1
        
        if nums == []:
            return integer
        
        maxVal = max(nums)
        
        while integer <= maxVal:
            if integer not in nums:
                return integer
            else:
                integer+=1
        
        return integer
        
        