'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        cur = str(nums[0])
        ranges = []
        
        for i in range(1, len(nums)):
            
            # end the range at number prior to current
            if nums[i] != (nums[i-1] + 1):
                if str(nums[i-1]) == cur:
                    ranges.append(cur)
                else:
                    ranges.append(cur + "->" + str(nums[i-1]))
                cur = str(nums[i])
            
            # if at the last number
            if i == len(nums) - 1:
                if nums[i] != (nums[i-1] + 1):
                    ranges.append(cur)
                else:
                    ranges.append(cur + "->" + str(nums[i]))
        
        return ranges
        
        
                
                
            
            
            
            
            
            
            
            
        