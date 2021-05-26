'''
There are n workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly k workers to form a paid group.  When hiring a group of k workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

'''

import heapq
from heapq import heappush, heappushpop, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        # We assume current person will get paid minimum wage. Keep track of max k qualities, sum them up and multiply with ratio of current person to get total money to be paid. 
        # Intuition - We can hire everyone else with lower ratio because they are providing same quality at a lower wage. So arrange in ascending order and go left -> right so everything on the left will always be a lower wage.
        
        workers = sorted(((w/q), q, w) for q, w in zip(quality, wage))
        ans = float('inf')
        heap = [] # max heap for quality
        sumq = 0
        
        for ratio, q, w in workers:
            heappush(heap, -q)
            sumq += q
            
            if len(heap) > k:
                sumq += heappop(heap)
            
            if len(heap) == k:
                ans = min(ans, ratio*sumq)
        
        return ans
            
                
                
                
                
                
        