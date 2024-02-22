"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        unique = set()
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            seen = {}
            for j in range(i+1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    triplet = [nums[i], complement, nums[j]]
                    if tuple(triplet) not in unique:
                        unique.add(tuple(triplet))
                        answer.append(triplet)
                
                else:
                    # complement is not in seen, so add current number to seen because it might be a complement to another number down the line
                    seen[nums[j]] = j
        
        return answer