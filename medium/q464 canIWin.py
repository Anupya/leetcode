# In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

# What if we change the game so that players cannot re-use integers?

# For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

# Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

class Solution:
   
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        a = 0
        seen = {}
        allInts = [x for x in range(1, maxChoosableInteger+1)]
        sumOfAllInts = sum(allInts)
        
        def helper (nums, remainder):
        
            # we win if largest choice exceeds remainder
            if nums[-1] >= remainder:
                return True

            # if we have seen this set of nums before
            hashed = tuple(nums)
            if hashed in seen:
                return seen[hashed]

            # we have not won yet so next player's turn
            # if they don't win, then we win
            for x in range(len(nums)):
                print(x)
                if not helper(nums[:x] + nums[x+1:], remainder-nums[x]):
                    print("found a split so we win: ", x)
                    seen[hashed] = True
                    return True

            # there is no number we can play that will make us win
            # so other player wins
            seen[hashed] = False
            return False
    
        if sumOfAllInts < desiredTotal:
            return False
        elif sumOfAllInts == desiredTotal:
            return maxChoosableInteger % 2
        else:
            return helper(allInts, desiredTotal)
        