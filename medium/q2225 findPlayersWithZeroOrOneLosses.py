"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""

from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCount = defaultdict(int)

        for match in matches:
            if match[0] not in loseCount:
                loseCount[match[0]] = 0
            loseCount[match[1]] += 1
        
        answer = [[], []] # players that have never lost, players that have lost only once
        
        for player, loseNumber in loseCount.items():
            if loseNumber == 0:
                answer[0].append(player)
            elif loseNumber == 1:
                answer[1].append(player)
        
        answer[0].sort()
        answer[1].sort()

        return answer

