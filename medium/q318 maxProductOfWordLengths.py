"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
"""
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0

        convertToSets = [set([*i]) for i in words]
        
        for i in range(len(convertToSets)):
            for j in range(i+1, len(convertToSets)):
                if len(convertToSets[i].union(convertToSets[j])) == len(convertToSets[i]) + len(convertToSets[j]):
                    maximum = max(len(words[i])*len(words[j]), maximum)
        
        return maximum