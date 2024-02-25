"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastOccurrences = {letter:i for i, letter in enumerate(s)}
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                seen.add(char)

                while len(stack) > 0 and char < stack[-1] and lastOccurrences[stack[-1]] > i:
                    seen.remove(stack[-1])
                    stack = stack[:-1] # remove the last character
                
                stack.append(char)

        return ''.join(stack)
        