# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def robCircular(self, nums):
        # there are 3 or more numbers
        # either we rob the current house or we do not
        dp1, dp2 = 0, 0
        
        # ... dp1, dp2, i, i+1, i+2, ...
        for i in nums:
            total = max(dp1 + i, dp2)
            dp1 = dp2
            dp2 = total
        
        return dp2
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        return max(self.robCircular(nums[:-1]), self.robCircular(nums[1:]))
    
        
            
            
            
            
        
        