'''
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

'''
class Solution:
    def isSubsetInOrder(self, s1, s2):
        # s1 = apple, #s2 = abpcplea
        
        s1ptr = 0
        for i in s2:
            if s1[s1ptr] == i:
                s1ptr += 1
            if s1ptr == len(s1):
                return True
        
        return False 
    
    def findLongestWord(self, s: str, listOfWords: List[str]) -> str:
        
        # Python sort is stable so the lexicographical order remains after sorting by descending order of length
        listOfWords.sort() #O(nlogn)
        listOfWords.sort(key=lambda x: len(x), reverse=True)
        
        for word in listOfWords: #O(n)
            if self.isSubsetInOrder(word, s): #O(m)
                return word
        
        return ""
        
        