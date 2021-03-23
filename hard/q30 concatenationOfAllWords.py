# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

class Solution:
    
    def checkIfValidSubstring(self, substring:str, words: List[str]) -> bool:
        index = 0
        length = len(words[0])
        start = 0
        end = length
        wordCopy = [x for x in words]
        while end <= len(substring):
            if substring[start:end] in wordCopy:
                wordCopy.remove(substring[start:end])
                start = end
                end = start + length
            else:
                return False

        return True
        
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        length = len(words[0]) # length of every word in words
        substrLen = len(words)*length
        startingIndices = set()
        finalList = []
        for word in words:
            startingIndices.add(word[0])
        
        index = 0
        while index <= len(s)-substrLen:
            if s[index] in startingIndices:
                # check if the substring starting here is a valid one
                if self.checkIfValidSubstring(s[index:index+substrLen], words):
                    finalList.append(index)
            index+=1
        
        return finalList
        
        