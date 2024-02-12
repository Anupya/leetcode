"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        minSubstrings = 0
        seen = set()

        for i, letter in enumerate(s):
            if letter in seen:
                seen = set()
                seen.add(letter)
                minSubstrings += 1
            else:
                seen.add(letter)

        # the last substring should also be counted
        return minSubstrings + 1
            