"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 2:
            # majority element always exists, so whether length is 1 or 2, the first element will be the majority element
            return nums[0]

        nums.sort()
        majorityElement = (nums[0], 1)
        lastIndexOfPreviousLetter = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # if we see a new number, then we can compare it to the last time we saw a new number and see if this number broke the record as majority element
                if i - lastIndexOfPreviousLetter > majorityElement[1]:
                    majorityElement = (nums[i-1], i - lastIndexOfPreviousLetter)
                
                lastIndexOfPreviousLetter = i-1

            elif i == len(nums)-1:
                # check if the last letter is a majority element
                if i - lastIndexOfPreviousLetter > majorityElement[1]:
                    majorityElement = (nums[i-1], i - lastIndexOfPreviousLetter)
                    
        return majorityElement[0]


        