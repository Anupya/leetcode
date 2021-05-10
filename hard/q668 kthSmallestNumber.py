# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

class Solution:
    def findKthNumber(self, m, n, k):
        
        # ensure n >= m for later on
        if m > n: 
            m, n = n, m
        
        # define search space
        lo, hi = 1, m*n
        
        # using binary search since linear solutions are TLEing
        while lo < hi:

            mid = int((lo + hi)/2)
            
            # if anything to the left of mid is not the kth smallest element, update lo
            
            # formula to figure out # of numbers <= mid in multiplication table
            if sum(min(mid//r, n) for r in range(1, m+1)) < k: 
                lo = mid + 1
            else: 
                hi = mid
        
        return lo
                        