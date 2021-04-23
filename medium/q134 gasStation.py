# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # if gas >= cost at an index, we can start there and see if we make it around
        # transform both lists so they start with the index
        # gas = [4,5,1,2,3,4] cost = [1,2,3,4,5]
        
        if len(cost) == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
            
        startingIndices = []
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                startingIndices.append(i)
        
        for x in startingIndices:
            gasTransformed = gas[x:] + gas[0:x]
            gasTransformed.append(gas[x])
            costTransformed = cost[x:] + cost[0:x]
            
            i = 0
            fuelSoFar = gasTransformed[0]
            while i < len(costTransformed):
                if fuelSoFar - costTransformed[i] >= 0:
                    fuelSoFar -= costTransformed[i]
                    fuelSoFar += gasTransformed[i+1]
                else:
                    break
                i+=1
            
            # a complete circuit
            if i == len(costTransformed) and fuelSoFar >= 0:
                return x
        
        return -1
                    
        