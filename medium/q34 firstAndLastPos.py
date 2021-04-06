# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        rangeList = []
        if target not in nums:
            return [-1, -1]

        first = 0
        last = 0
        for i, num in enumerate(nums):
            if num == target:
                first = i
                last = first
                break
                
        for x in range(first+1, len(nums)):
            if nums[x] == target:
                last+=1
            else:
                break
        
        rangeList.extend((first, last))
        return rangeList
                
        
        