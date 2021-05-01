# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = seats.index(1)
        start = distance
        end = start+1
        
        while end < len(seats):
            if seats[start] and seats[end]:
                distance = max(distance, int((end-start)/2))
                start = end
                end = start+1
            
            elif not seats[end]:
                end += 1
        
        distance = max(distance, end-start-1)
        return distance
                
        
        
        