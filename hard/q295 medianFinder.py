'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # smaller half of the list, max-heap
        self.large = [] # larger half of the list, min heap

    def addNum(self, num: int) -> None:
        
        # if same length, add to small and move top of small to large
        if len(self.small) == len(self.large):
            maxInSmall = heappushpop(self.small, -num)
            heappush(self.large, -maxInSmall)
        
        # if different length, add to large and move top of large to small
        else:
            minInLarge = heappushpop(self.large, num)
            heappush(self.small, -minInLarge)
        

    def findMedian(self) -> float:
        
        # n is even
        if len(self.small) == len(self.large):
            maxInSmall = -heappop(self.small)
            minInLarge = heappop(self.large)
            heappush(self.small, -maxInSmall)
            heappush(self.large, minInLarge)
            return (maxInSmall+minInLarge)/2
        
        # n is odd
        else:
            minInLarge = heappop(self.large)
            heappush(self.large, minInLarge)
            return minInLarge
            
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()