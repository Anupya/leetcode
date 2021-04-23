# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

class Solution:
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0 for x in range(len(nums))]
        dp[-1] = 1 # initialize
        
        for i in range(len(nums)-2, -1, -1):
            
            # look at other entries in dp array
            cur = len(nums)-1
            while cur > i:
                if nums[i] < nums[cur]:
                    dp[i] = max(dp[i], 1+dp[cur])
                cur-=1
            
            if dp[i] == 0:
                dp[i] = 1
        
        return max(dp)
        
        
        