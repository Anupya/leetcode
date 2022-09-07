'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        if len(ratings) == 1:
            return 1
        
        dp = [1]*len(ratings)
        
        increasing = 1
        
        # left to right
        for i in range(1, len(ratings)):
            
            # increasing
            if ratings[i-1] < ratings[i] and dp[i-1] >= dp[i]:
                dp[i] = dp[i-1] + 1

        # right to left 
        for i in range(len(ratings)-1, 0, -1):
            
            # decreasing 
            if ratings[i-1] > ratings[i] and dp[i-1] <= dp[i]:
                dp[i-1] = dp[i] + 1
         
        return sum(dp)
        