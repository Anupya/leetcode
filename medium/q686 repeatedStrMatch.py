'''
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".
'''

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        if len(b) < len(a):
            if b in a:
                return 1
            elif b in a+a:
                return 2
            else:
                return -1
         
        numTimes = 1
        aCopy = a
        
        while len(a) <= (len(b)*3):
            if b in a:
                return numTimes
            a += aCopy
            numTimes += 1

        return -1
        
        
        
        
        