# Given two strings s1 and s2, return true if s2 contains the permutation of s1.

# In other words, one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        if not len(s1):
            return True
        
        n = len(s1)
        s1Arr = [0]*26
        s2Arr = [0]*26
        
        for x in s1:
            s1Arr[ord(x)-ord('a')] += 1
        
        for i in range(n):
            s2Arr[ord(s2[i])-ord('a')] += 1
        
        if s1Arr == s2Arr:
            return True
        
        for i in range(1, len(s2)-n+1):

            # update sliding window
            s2Arr[ord(s2[i-1])-ord('a')]-=1
            s2Arr[ord(s2[i+n-1])-ord('a')]+=1
            
            if s1Arr == s2Arr:
                return True
        
        return False
        
        