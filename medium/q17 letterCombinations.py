#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbersDict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g','h','i'], '5': ['j', 'k', 'l'], 
                      '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        if digits == '':
            return []
        
        letterComboList = numbersDict[digits[0]] # prefill it with the first digit's possible letters
        
        
        for index in range(1, len(digits)): # main string
            # second array
            newArray = []
            for letter1 in numbersDict[digits[index]]: # next letter in main string
                for string in letterComboList:
                    newString = string + letter1
                    newArray.append(newString)
            
            letterComboList = newArray
        
        return letterComboList
                
            
        
        
        
        