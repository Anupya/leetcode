# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # [5, 2, 3]
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i < len(nums)-1 and nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
            elif i == len(nums)-1 and nums[i]>nums[i-1]:
                return i
            
        return -1
                
                
        
        