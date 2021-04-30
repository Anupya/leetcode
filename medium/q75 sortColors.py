# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        
        index = 0
        while red:
            nums[index] = 0
            index += 1
            red -= 1
        
        while white:
            nums[index] = 1
            index += 1
            white -= 1
        
        while blue:
            nums[index] = 2
            index += 1
            blue -= 1
            
        