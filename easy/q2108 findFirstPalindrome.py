"""
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        backwards = [word[::-1] for word in words]

        for i in range(len(words)):
            if words[i] == backwards[i]:
                return words[i]
        
        return ""