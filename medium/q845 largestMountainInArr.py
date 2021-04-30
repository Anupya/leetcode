# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        mountain = 0
        
        i = 1
        increasing = 0
        decreasing = 0
        curMountain = 0
        
        while i < len(arr):
            
            # start/keep increasing
            if arr[i-1] < arr[i]: 
                
                # if we were decreasing
                if decreasing: 
                    curMountain += decreasing
                    mountain = max(mountain, curMountain)
                    decreasing = 0
                    increasing = 1 
                else:
                    increasing += 1
                    
                curMountain = 0
                
            # start/keep decreasing
            elif arr[i-1] > arr[i]:
                if increasing:
                    curMountain += increasing
                    increasing = 0
                    decreasing += 2
                elif decreasing:
                    decreasing += 1
            
            # plateau
            else:
                curMountain += decreasing
                mountain = max(curMountain, mountain)
                curMountain, increasing, decreasing = 0, 0, 0

            i+=1
            
        # count the last mountain if any
        if curMountain and decreasing:
            curMountain += decreasing
            mountain = max(curMountain, mountain)
            
        return mountain
                
            
            
        
        