'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
         
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        """
        Creates a map of all combinations of words with missing letters mapped 
        to all words in the list that match that pattern.
        E.g. hot -> {'*ot': ['hot'], 'h*t': ['hot'], 'ho*': ['hot']}
        """
        n = len(beginWord)
        patternToWord = defaultdict(list)
        for word in wordList:
            for i in range(n):
                patternToWord[word[:i] + "*" + word[i+1:]].append(word) 

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        # Shortest Path? Use BFS
        # the first time you encounter endWord, that is the shortest transformation sequence
        
        while queue:
            currentWord, level = queue.popleft()
            for i in range(n+1):
                intermediateWord = currentWord[:i] + "*"
                if i != n:
                    intermediateWord += currentWord[i+1:]
                    
                for word in patternToWord[intermediateWord]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        
        return 0
        
    

        