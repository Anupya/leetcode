# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        for i in range(len(s), 0, -1):
            
            start = 0
            while start+i <= len(s):
                
                # prelim check that first and last character is the same
                if s[start] == s[start+i-1] and s[start:start+i].lower() == s[start:start+i][::-1].lower():
                    return s[start:start+i]
                
                start+=1
        
        return s[0]
        