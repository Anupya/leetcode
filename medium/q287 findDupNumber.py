# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                return nums[i]
            i+=1
        