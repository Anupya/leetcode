# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

import collections

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        countA = collections.Counter(secret)
        countB = collections.Counter(guess)
        
        for i, char in enumerate(list(secret)):
            
            # count bulls
            if char == guess[i]:
                bulls+=1
                countA[char] -=1
                countB[char] -=1
                
        # if char in both countA and countB, increase cows by min value
        for k in countA.keys():
            if k in countB:
                cows += min(countA[k], countB[k])
        
        return str(bulls) + "A" + str(cows) + "B"
        