'''
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

'''
class Solution:
    def check8Possibilities(self, char, board):
        
        # rows
        if board[0][0] == char and board[0][1] == char and board[0][2] == char:
            return True
        if board[1][0] == char and board[1][1] == char and board[1][2] == char:
            return True
        if board[2][0] == char and board[2][1] == char and board[2][2] == char:
            return True
        
        # cols
        if board[0][0] == char and board[1][0] == char and board[2][0] == char:
            return True
        if board[0][1] == char and board[1][1] == char and board[2][1] == char:
            return True
        if board[0][2] == char and board[1][2] == char and board[2][2] == char:
            return True
        
        # diagonal
        if board[0][0] == char and board[1][1] == char and board[2][2] == char:
            return True
        if board[0][2] == char and board[1][1] == char and board[2][0] == char:
            return True
        
        return False
        
    def validTicTacToe(self, board: List[str]) -> bool:
        
        # # of Xs == # of Os or 1 more X
        # at most 1 row/col/diag of Xs or Os
        
        numX = 0
        numO = 0
        for row in board:
            for char in row:
                if char == "X":
                    numX+=1
                if char == "O":
                    numO+=1
        
        if numX < numO or numX > numO+1:
            return False
        
        x = self.check8Possibilities('X', board)
        o = self.check8Possibilities('O', board)
        
        if x and o:
            return False
        if numX == numO and x:
            return False
        if numX == numO+1 and o:
            return False
        
        return True
        
                    
        
        