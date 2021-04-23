# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
                
        set1 = set(nums1)
        set2 = set(nums2)
        
        # store numbers in hashmap
        hash1 = {x:0 for x in set1}
                
        results = []
        for x in set2:
            if x in hash1:
                results.append(x)
        
        return results
        
        