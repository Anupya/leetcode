"""
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
"""

from heapq import heappush, heappop
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # maintain largest ladder # of jumps and sum of remaining bricks so far
        pq = []
        curBuilding = 0
        while curBuilding < len(heights)-1:
            if heights[curBuilding] < heights[curBuilding+1]:
                htDiff = heights[curBuilding+1]-heights[curBuilding]
                if len(pq) < ladders:
                    heappush(pq, htDiff)
                elif len(pq) > 0 and pq[0] < htDiff:
                    # this height difference needs a ladder
                    smallestHeight = heappop(pq)
                    heappush(pq, htDiff)
                    if smallestHeight <= bricks:
                        bricks -= smallestHeight
                    else:
                        return curBuilding
                else:
                    # bricks are better
                    if bricks >= htDiff:
                        bricks -= htDiff
                    else:
                        return curBuilding
            
            curBuilding += 1
        
        return curBuilding

