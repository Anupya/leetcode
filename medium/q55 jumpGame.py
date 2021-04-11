# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1: 
            return True
        
        # make an array that has T/F based on whether you can get to that index or not
        # return the last bool in that arr
        
        reachable = [False for x in nums]
        if nums[0] != 0:
            reachable[0] = True
        else:
            return False
        
        coverage = 0
        for i, num in enumerate(nums):
            if reachable[-1]: # already found a way to get to the end
                return True
            
            if num > coverage and reachable[i]: # if can get here, then see what new places you can jump to
                end = min(i+num+1, len(nums))
                for x in range(i, end):
                    reachable[x] = True
                coverage = num
            
            coverage-=1
        
        return reachable[-1]
        
        