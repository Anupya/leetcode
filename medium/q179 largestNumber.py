# Given a list of non-negative integers nums, arrange them such that they form the largest number.

class Solution:
    
    def compare(self, x, y):
        return int(x+y) < int(y+x)
    
    def largestNumber(self, nums: List[int]) -> str:
          
        if all(x == 0 for x in nums):
            return '0'
        
        nums = list(map(str, nums))
        
        for x in range(0, len(nums)-1):
            y = x+1
            while y < len(nums):
                if self.compare(nums[x], nums[y]): # swap!
                    nums[x], nums[y] = nums[y], nums[x]
                y+=1
            
        return "".join(nums)
        