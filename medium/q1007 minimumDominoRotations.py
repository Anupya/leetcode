# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

# If it cannot be done, return -1.

import collections

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        common = 0
        # find a pair where top = bottom
        for top, bottom in zip(A, B):
            if top == bottom:
                common = top
                break
        
        if common:
            for top, bottom in zip(A, B):
                if top!=common and bottom!=common:
                    return -1
            
            # every pair (A, B) should have common in it
            countA = 0
            countB = 0
            for top, bottom in zip(A, B):
                if top!=bottom:
                    if top == common:
                        countA += 1
                    else:
                        countB += 1
            
            return min(countA, countB)
        
        # no pair where top = bottom
        else:
            countA = collections.Counter(A)
            countB = collections.Counter(B)
            
            for key in countA:
                if key in countA and key in countB and countA[key] + countB[key] == len(A):
                    return min(countA[key], countB[key])
            
            return -1
            
        