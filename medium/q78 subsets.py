# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = [[]]
        length = len(nums)
        
        for i in range(1, length+1):
            # for i=1, combos = ['1', '2', '3']
            # for i=2, combos = ['12', '13', '23']
            combos = combinations(nums, i)
            
            for j in combos:
                newL = [x for x in j] # split string into list of characters
                powerSet.append(newL)
        
        return powerSet
        
        
        