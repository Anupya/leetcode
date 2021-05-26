'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        ptr = len(digits)-1
        while ptr >= 0 and digits[ptr] == 9:
            digits[ptr] = 0
            ptr -= 1
        
        if ptr >= 0:
            digits[ptr] += 1
        else:
            digits = [1] + digits
        
        return digits
        