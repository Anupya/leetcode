# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.


import collections

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def dfs(x, y):
            pointSet.remove((x,y))
            
            # go through all points with same x value
            for r in rows[x]:
                if (x, r) in pointSet:
                    dfs(x, r)
            
            # go through all points with same y value
            for c in cols[y]:
                if (c, y) in pointSet:
                    dfs(c, y)
            
        if len(stones) == 1:
            return 0
        
        # use dfs to count each island
        islands = 0
        pointSet = set((x[0], x[1]) for x in stones)
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        
        # store all points twice, once with row key, once with col key
        for stone in stones:
            rows[stone[0]].append(stone[1])
            cols[stone[1]].append(stone[0])

        for stone in stones:
            if (stone[0], stone[1]) in pointSet:
                islands+=1
                dfs(stone[0], stone[1])
                
        return len(stones) - islands
        