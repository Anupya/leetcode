# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # use dictionary to keep track of whether i have seen the letter before, clear dictionary when starting to read new substring
        
        longestLength = 0
        lengthSoFar = 0
        index = 0
        mydict = {}
        while(index < len(s)):
            if s[index] in mydict:
                longestLength = max(longestLength, lengthSoFar)
                lengthSoFar = 0
                index = mydict[s[index]] #start from after repeat
                mydict.clear()
            else:
                mydict[s[index]] = index
                lengthSoFar+=1
            
            index+=1
        
        longestLength = max(longestLength, lengthSoFar)
        return longestLength
                
        