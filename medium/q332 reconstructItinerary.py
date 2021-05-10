# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # Hierholzer's Algorithm to find Eulerian path
        
        # {start: [end1, end2, ...]}
        startingAirports = collections.defaultdict(list)
        
        # so when we pop, we choose the smallest lexical destination first
        for start, end in sorted(tickets)[::-1]:
            startingAirports[start].append(end)

        route, stack = [], ['JFK']
        
        # build route in reverse order using Greedy DFS
        # last element in route will be JFK
        while stack:
 
            # look at last airport that we landed in
            while startingAirports[stack[-1]]:
                
                # add where we are going next to stack
                stack.append(startingAirports[stack[-1]].pop())
            
            # once we hit deadend, add it to our route
            # because we will only hit this stop through this path
            route.append(stack.pop())

        return route[::-1]
        
        
        
        