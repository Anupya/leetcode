# In an election, the i-th vote was cast for persons[i] at time times[i].

# Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

# Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

class TopVotedCandidate:

    def winningCandidate(self, t):
        
        # get key highest value in self.timeDict
        maxVal = max(self.timeDict.values())
        highestCandidates = set()
        
        for key, value in self.timeDict.items():
            if value == maxVal:
                highestCandidates.add(key)
 
        if len(highestCandidates) == 1:
            return highestCandidates.pop()
        
        recent = self.stack.copy()
        while recent[-1] not in highestCandidates:
            recent.pop()
        
        return recent[-1]
    
        
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.stack = []
        self.times = times
        self.timesSet = set(times)
        self.timeDict = {}
        self.winner = {}
        self.timesInBetween = {}
        
        # assign all the possible times to an immediately lesser time
        i = 0
        val = 0
        while i <= self.times[-1]:
            if i in self.timesSet:
                val = i
            self.timesInBetween[i] = val
            i+=1
                
        # construct timeDict
        # {c: votes}}
        for person, time in zip(persons, times):
            if person in self.timeDict:
                self.timeDict[person] += 1
            else:
                self.timeDict[person] = 1
            
            self.stack.append(person)
            self.winner[time] = self.winningCandidate(time)
        
    def q(self, t: int) -> int:

        if t > self.times[-1]:
            return self.winner[self.timesInBetween[self.times[-1]]]
        else:
            return self.winner[self.timesInBetween[t]]
            
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)