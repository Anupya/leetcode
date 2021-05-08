# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return amount

        # stores min number of coins to make i amount
        coinSet = set(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for x in range(1, amount+1):
            if x in coinSet:
                dp[x] = 1
                continue
                    
            for y in coinSet: 
                if y < x:
                    dp[x] = min(dp[x], dp[x-y] + 1)
            
        return dp[amount] if dp[amount] != float('inf') else -1
        
        
            
        
        
        