# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # preprocess s
        newS = ""
        for x in s:
            if x == '#' and len(newS):
                newS = newS[:-1]
            if x != '#':
                newS += x
                
        # preprocess t
        newT = ""
        for x in t:
            if x == '#' and len(newT):
                newT = newT[:-1]
            if x != '#':
                newT += x
                
        return newS == newT
        