# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

class Solution:
    def isOverlap(self, firstList, secondList):
        return True if max(firstList[0], secondList[0]) <= min(firstList[1], secondList[1]) else False
    
    def getIntersection(self, firstList, secondList):
        return [max(firstList[0], secondList[0]), min(firstList[1], secondList[1])]
            
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        
        p1, p2 = 0, 0
        final = []
        while p1 < len(firstList) and p2 < len(secondList):
            if self.isOverlap(firstList[p1], secondList[p2]):
                final.append(self.getIntersection(firstList[p1], secondList[p2]))
            
            # move pointers based on ending of ranges
            if firstList[p1][1] < secondList[p2][1]:
                p1+=1
            elif firstList[p1][1] > secondList[p2][1]:
                p2+=1
            else:
                p1, p2 = p1+1, p2+1
        
        return final
