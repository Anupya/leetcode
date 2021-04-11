# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        minStr = min(strs)
        minLen = len(minStr)
        
        i = 0
        while i < minLen:
            char = minStr[i]
            for string in strs:
                if string[i] != char:
                    return prefix
            prefix+=char
            i+=1
        
        return prefix
        