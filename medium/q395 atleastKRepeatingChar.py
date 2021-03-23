# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringActual(0, len(s), s, k)
    
    def longestSubstringActual(self, start, end, s, k):
        
        # store frequency of all char in s
        mydict = {}
        substring = s[start:end]
        uniqueChar = set(substring)
        for char in uniqueChar:
            mydict[char] = substring.count(char)
        
        # divide and conquer
        for i in range(start, end):            
            if mydict[s[i]] < k:
                left = self.longestSubstringActual(start, i, s, k)
                right = self.longestSubstringActual(i+1, end, s, k)

                return max(left, right)
             
        return end - start
        