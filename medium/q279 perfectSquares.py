# Given an integer n, return the least number of perfect square numbers that sum to n.

import math

class Solution:
    def numSquares(self, n: int) -> int:
        perfSq = [x**2 for x in range(1, math.floor(sqrt(n))+1)]
        dp = [float('inf') for x in range(0, n+1)]
        
        if n in perfSq:
            return 1
        
        # initialize all perfect squares to be 1
        for x in perfSq:
            dp[x] = 1
        
        # n is not a perfect square
        for x in range(2, n+1):
            for sq in perfSq:
                if sq < x:
                    numSq = dp[sq] + dp[x-sq]
                    dp[x] = min(dp[x], numSq)
                else:
                    break
        
        return dp[n]
        
        
        
        