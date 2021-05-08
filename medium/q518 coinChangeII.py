# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0]*(amount+1)
        dp[0] = 1
        
        # count all combos with one coin at a time
        for y in coins:
            for x in range(y, amount+1):
                if y <= x:
                    dp[x] += dp[x-y]

        return dp[amount]
        
        
        