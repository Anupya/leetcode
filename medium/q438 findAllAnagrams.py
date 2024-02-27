"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagramPositions = []
        if len(s) < len(p):
            return anagramPositions
        
        pDict = Counter(p)
        lenP, lenS = len(p), len(s)
        sDict = Counter(s[:lenP])
        
        for i in range(lenP, lenS):
            start = i - lenP
            if pDict == sDict:
                anagramPositions.append(start)

            if sDict[start] == 1:
                del sDict[s[start]]
            else:
                sDict[s[start]] -= 1
            
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
        
        # last sliding window
        if sDict == pDict:
            anagramPositions.append(lenS-lenP)

        return anagramPositions
