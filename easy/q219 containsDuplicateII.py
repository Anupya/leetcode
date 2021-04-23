# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        
        for i, num in enumerate(nums):
            if num in myDict:
                if abs(i-myDict[num]) <= k:
                    return True
                else:
                    myDict[num] = i
            else:
                myDict[num] = i
        return False
                
        