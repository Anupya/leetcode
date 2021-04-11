# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0 #nums1
        y = 0 #nums2
        x = 0 #nums3
        
        nums3 = nums1.copy() # store copy of original
        
        while x < m and y < n: # more to read from either list
            if nums2[y] < nums3[x]:
                nums1[i] = nums2[y]
                y+=1
            else:
                nums1[i] = nums3[x]
                x+=1
            i+=1
                
        while y < n: # append rest of nums2 to end of nums1
            nums1[i] = nums2[y]
            i+=1
            y+=1
        
        while x < m: # append rest of nums1 to end of nums2
            nums1[i] = nums3[x]
            i+=1
            x+=1
        