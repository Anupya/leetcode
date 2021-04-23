
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0
        
        # [dp1, dp2, n, n+1, ...]
        for n in nums:
            
            # richest we can be at current house
            temp = max(n+dp1, dp2)
            dp1 = dp2
            dp2 = temp
        
        return dp2
            
            
        