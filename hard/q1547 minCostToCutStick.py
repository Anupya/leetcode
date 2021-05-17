'''
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

'''

class Solution:
    
    def minCost(self, n: int, cuts: List[int]) -> int:

        if len(cuts) == 1:
            return n
        
        # realization: we end up calculating total min cost to cut a stick starting at the 
        # same start and end combo over and over again (sub problem)
        # so use dynamic programming to store total min cost for a stick 
        
        # stores (i, j): total min cost to cut stick starting from i and ending at j
        memo = {}
        
        def dp (start, end):
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            ans = float('inf')
            
            canCut = False
            for cut in cuts:
                if start < cut < end:
                    canCut = True
                    ans = min(ans, dp(start, cut) + dp(cut, end) + end - start)
            
            if not canCut:
                return 0
            
            memo[(start, end)] = ans
            return ans
              
        return dp(0, n)
        
        
        
        