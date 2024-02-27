"""
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.
"""
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)

        for i in range(len(shifts)):
            shift = shifts[i]
            shifts[i] = total%26
            total -= shift

        newS = ""
        for i in range(len(s)):
            change = ord(s[i]) + shifts[i]
            if change > 122:
                change -= 26
            newS += chr(change)

        return newS