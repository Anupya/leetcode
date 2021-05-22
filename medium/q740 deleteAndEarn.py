'''
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        
        # use two variables to track whether you are picking current element or not
        
        prev = None
        pick = 0
        avoid = 0
        
        for elem in sorted(count):
            
            # you can pick this since there is no num immediately less than it
            if prev != elem -1:
                avoid, pick = max(pick, avoid), elem*count[elem] + max(pick, avoid)
            
            # there was a number less than it
            else:
                avoid, pick = max(pick, avoid), elem*count[elem] + avoid
            
            prev = elem
        
        return max(pick, avoid)
                
        
        