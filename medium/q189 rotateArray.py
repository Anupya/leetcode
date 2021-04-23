# Given an array, rotate the array to the right by k steps, where k is non-negative.

# move last k elements to the front

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[length-k:] + nums[0:length-k]
        
        