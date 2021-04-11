# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # check if all zeroes are preceded by 1 or 2
        strList = list(s)
        for i, char in enumerate(strList):
            if char == '0': 
                
                # a zero is not preceded by 1 or 2
                if i-1>=0 and s[i-1] != '1' and s[i-1] != '2': 
                    return 0
                
                # first character is zero then no way to decode it
                if i==0: 
                    return 0
        
        
        # once we know the answer is >0
        # store how many ways to decode got you to ith position
        n = len(s)
        numDecodingsSoFar = [0 for x in range(0, n+1)]
        numDecodingsSoFar[0] = 1
        numDecodingsSoFar[1] = 1
        
        for i in range(2, n+1):
            if s[i-1] > '0':
                numDecodingsSoFar[i] = numDecodingsSoFar[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
                numDecodingsSoFar[i] += numDecodingsSoFar[i-2]
        
        return numDecodingsSoFar[n]
        