# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s if x.isalnum()).lower()
        return s == s[::-1]
        