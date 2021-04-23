# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the median array for each window in the original array.

import statistics

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        answers = []
        start = 0
        end = k
        while end <= len(nums):
            answers.append(statistics.median(nums[start:end]))
            start+=1
            end+=1
        return answers
        