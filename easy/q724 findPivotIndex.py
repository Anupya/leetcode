# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        accSum = 0
        totalSum = sum(nums)-nums[0]
        for x in range(0, len(nums)-1):
            if accSum == totalSum:
                return x
            else:
                accSum += nums[x]
                totalSum -= nums[x+1]
        
        # check for right edge
        if accSum == totalSum:
            return len(nums)-1
        else:
            return -1
            
            
        