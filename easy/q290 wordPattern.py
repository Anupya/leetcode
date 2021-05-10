# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = s.split()
        dictionary = {}
        words = set()
        
        if len(pattern) != len(strings):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in dictionary:
                if strings[i] in words:
                    return False
                dictionary[pattern[i]] = strings[i]
                words.add(strings[i])
            elif dictionary[pattern[i]] != strings[i]:
                return False
        
        return True
                
                
        