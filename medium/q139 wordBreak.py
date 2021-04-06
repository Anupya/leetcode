#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

#Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    
    def splitString(self, s:str, wordDict: List[str], lookup) -> bool:
        n = len(s)
        
        if n == 0:
            return True
        
        if lookup[n] == -1: # never seen this subproblem before
            
            lookup[n] = 0 # mark it as seen
            
            for i in range(1, n+1): # end point has to be 1 more than length because of how : works
                prefix = s[:i]
                if prefix in wordDict and self.splitString(s[i:], wordDict, lookup):
                    lookup[n] = 1
                    return True
        
        return lookup[n] == 1
    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = [-1 for x in range(0, len(s)+1)]
        return self.splitString(s, wordDict, lookup)