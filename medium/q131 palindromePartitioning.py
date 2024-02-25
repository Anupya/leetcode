"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
"""
from typing import List

class Solution:
    def is_palindrome(self, s: str):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:     
        answers = []
        def dfs(i: int, curr: List[str]):
            if i == len(s):
                # reached the end so we were able to partition the string!
                answers.append(curr)
                return

            for j in range(i, len(s)):
                prefix = s[i:j+1]
                if self.is_palindrome(prefix):
                    dfs(j+1, curr+[prefix])
            
            return

        dfs(0, [])
        return answers
