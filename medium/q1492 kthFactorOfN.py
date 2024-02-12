"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # the highest factor that n can have is n/2

        currentK = 0 # kth factor

        for i in range(1, (n//2)+1):
            if n % i == 0:
                currentK += 1
            
            if currentK == k:
                return i

        # n itself is a factor
        currentK += 1
        if k == currentK:
            return n
            
        # n has less than k factors
        return -1

        