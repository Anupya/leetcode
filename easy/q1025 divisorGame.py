
#Alice and Bob take turns playing a game, with Alice starting first.

#Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

#Choosing any x with 0 < x < n and n % x == 0.
#Replacing the number n on the chalkboard with n - x.
#Also, if a player cannot make a move, they lose the game.

#Return true if and only if Alice wins the game, assuming both players play optimally.

class Solution:
    def divisorGame(self, n: int) -> bool:
        # 0 = alice, 1 = bob
        turn = 0
        while n > 1:
            n -= 1
            if turn == 0: 
                turn = 1
            else:
                turn = 0
        if turn == 1:
            return True
        else: 
            return False