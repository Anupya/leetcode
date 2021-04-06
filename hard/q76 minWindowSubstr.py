# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

class Solution:
        
    def minWindow(self, s: str, t: str) -> str:
        
        # not possible for letters of t to be in s
        if len(t) > len(s) or not all(t.count(a) <= s.count(a) for a in t):
            return ""

        start = 0
        end = -1
        
        tDict = {e: t.count(e) for e in t}
        sDict = {e: 0 for e in s}
        matches = 0
        uniqueLetters = len(tDict.keys())
        minWindow = ""
        
        while start < len(s):
            
            # expand
            if matches < uniqueLetters:
                
                if end == len(s) -1: # reached end of string so return minWindow so far
                    return minWindow
                
                end+=1
                sDict[s[end]] +=1
                if s[end] in t and sDict[s[end]] == tDict[s[end]]: # found the min count of s[end] we need
                    matches+=1
            
            # contract
            else:
                sDict[s[start]] -=1
                if s[start] in t and sDict[s[start]] == tDict[s[start]] - 1: # if we are short of 1 s[start]
                    matches-=1
                start+=1
                
            # update window
            if matches == uniqueLetters:
                if not minWindow:
                    minWindow = s[start:end+1]
                else:
                    if len(minWindow) > end - start:
                        minWindow = s[start:end+1]
                        

        return minWindow
                
        
                
                
                
            
        