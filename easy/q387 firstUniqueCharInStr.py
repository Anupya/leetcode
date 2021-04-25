# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # count frequencies in dict
        myDict = {}
        for x in s:
            if x in myDict:
                myDict[x] += 1
            else:
                myDict[x] = 1
        
        for x in s:
            if myDict[x] == 1: # constant lookup
                return s.index(x)
        
        return -1
                
                
        