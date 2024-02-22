"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # convert nums to binary tree

        indices = {num: index for index, num in enumerate(nums)}

        # 2 pointers, one on the left, one on the right
        left = 0
        right = len(nums)-1
        while left < right:
            middle = left + ((right-left)//2)
            if nums[middle] == target:
                return middle
            
            elif right - left == 1:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                elif nums[left] < target and target < nums[right]:
                    return left + 1
                elif nums[right] < target:
                    return len(nums)
                elif nums[left] > target:
                    return 0

            elif nums[middle] > target:
                # search left half
                right = middle
            
            else:
                # search right half
                left = middle
        
        # target is inserted at the front or the back at this point
        if target <= nums[0]:
            return 0
        else:
            return len(nums)
