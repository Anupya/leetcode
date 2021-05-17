# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

class Solution:
    def canSplitWord(self, word, wordSet):
        if word == "":
            return True
        
        for i in range(1, len(word)+1):
            if word[:i] in wordSet and (i == len(word) or self.canSplitWord(word[i:], wordSet)):
                return True
        
        return False
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        output = []
        for w in words:
            if w == "":
                continue
            wordSet.remove(w)
            if self.canSplitWord(w, wordSet):
                output.append(w)
            wordSet.add(w)
        
        return output
                
        
        