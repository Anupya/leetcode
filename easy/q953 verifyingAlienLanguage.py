# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

class Solution:
    def areWordSorted(self, word1, word2, order):
        i = 0
        n = min(len(word1), len(word2))
        while i < n and word1[i] == word2[i]:
            i+=1
        
        # shorter word comes first
        if i == n:
            return True if len(word1) <= len(word2) else False
        
        index1 = order.index(word1[i])
        index2 = order.index(word2[i])
        
        return True if index1 < index2 else False
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for x in range(1, len(words)):
            if not self.areWordSorted(words[x-1], words[x], order):
                return False
        
        return True
        