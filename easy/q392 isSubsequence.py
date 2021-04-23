# Given two strings s and t, check if s is a subsequence of t.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# 20 ms; faster than 99.17% 
# 14.4 MB; less than 50.25% of memory usage
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        for char in t:
            if char == s[index]:
                index+=1
                if index == len(s):
                    return True
        
        return False
                
            
            
        
