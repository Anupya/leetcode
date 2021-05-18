'''
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

'''

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.prefixes = collections.defaultdict(set)
        self.suffixes = collections.defaultdict(set)
        self.lastInstance = {}
        
        for j, w in enumerate(words):

            for i in range(1, len(w)+1):
                self.prefixes[w[:i]].add(w)

            for i in range(len(w)-1, -1, -1):
                self.suffixes[w[i:]].add(w)
            
            if (w in self.lastInstance and self.lastInstance[w] < j) or (w not in self.lastInstance):
                self.lastInstance[w] = j
        
    def f(self, prefix: str, suffix: str) -> int:
        
        validP, validS = [], []
        if prefix not in self.prefixes or suffix not in self.suffixes:
            return -1
        else:
            validP = self.prefixes[prefix]
            validS = self.suffixes[suffix]
            valid = validP & validS
            
            # no such word with that prefix and suffix
            if len(valid) == 0:
                return -1
            
            maxIndex = -1
            for w in valid:
                if maxIndex < self.lastInstance[w]:
                    maxIndex = self.lastInstance[w]
            
            return maxIndex
            
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)