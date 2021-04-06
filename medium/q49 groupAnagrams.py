# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupList = []
        anagramDict = {} #key: word #value: anagrams
        
        for string in strs: 
            key = "".join(sorted(string))
            if key in anagramDict:
                anagramDict[key].append(string)
            else:
                anagramDict[key] = [string]

        groupList = list(anagramDict.values())
            
        return groupList
        