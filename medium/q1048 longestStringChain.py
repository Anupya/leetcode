'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.
'''

class Solution:
    def getPredecessors(self, word, words):
        n = len(word)
        pred = set()
        
        for x in words:
            if len(x) == n-1:
                for i in range(n):
                    if x == word[:i] + word[i+1:]:
                        pred.add(x)
                        break
        
        return pred
    
    def getMaxDepth(self, word, predecessors, depths):
        
        if len(predecessors[word]) == 0:
            return 0
        
        maxDepth = 1
        for p in predecessors[word]:
            if p in depths:
                maxDepth = max(maxDepth, depths[p])
            else:
                ans = 1 + self.getMaxDepth(p, predecessors)
                maxDepth = max(maxDepth, ans)
        
        return maxDepth
        
    def longestStrChain(self, words: List[str]) -> int:
        
        predecessors = {}
        for x in words:
            predecessors[x] = self.getPredecessors(x, words)
        
        # dfs dictionary and keep track of max depth
        maxDepth = 1
        depths = {}
        words.sort(key=lambda x:len(x))
        
        for x in words:
            ans = 1 + self.getMaxDepth(x, predecessors, depths)
            
            # if chain ends with x, depth is depths[x]
            depths[x] = ans
            maxDepth = max(maxDepth, ans)
        
        return maxDepth
        
        