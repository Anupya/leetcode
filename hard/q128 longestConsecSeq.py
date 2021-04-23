# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not len(nums):
            return 0
        
        # sort it first
        nums = sorted(list(set(nums)))
        
        longest = 1
        start = 0
        index = 1
        while index < len(nums):
            while nums[index] == (nums[index-1] + 1):
                index+=1
                if index == len(nums):
                    break
        
            longest = max(longest, index-start)
            start = index
            index +=1
        
        return longest
                
        