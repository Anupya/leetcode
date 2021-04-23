# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

import bisect

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answers = []
        start = 0
        end = k
        slidingWindow = sorted(nums[:end])
        answers.append(slidingWindow[-1])
        
        while end < len(nums):
            
            del slidingWindow[bisect.bisect_left(slidingWindow, nums[start])]
            bisect.insort(slidingWindow, nums[end])
            answers.append(slidingWindow[-1])
            start+=1
            end+=1
            
        return answers
        