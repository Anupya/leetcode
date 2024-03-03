"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List

class Solution:
    def findWord(self, board: List[List[str]], word: str, visited: List[List[bool]], row: int, col: int) -> bool:
        if not word:
            return True
        
        numRows = len(board)
        numCols = len(board[0])

        doesWordExist = False

        # go right
        if col+1 < numCols and not visited[row][col+1] and board[row][col+1] == word[0]:
            visited[row][col+1] = True
            doesWordExist = doesWordExist or self.findWord(board, word[1:], visited, row, col+1)
            visited[row][col+1] = False

        # go left
        if col > 0 and not visited[row][col-1] and board[row][col-1] == word[0]:
            visited[row][col-1] = True
            doesWordExist = doesWordExist or self.findWord(board, word[1:], visited, row, col-1)
            visited[row][col-1] = False

        # go up
        if row > 0 and not visited[row-1][col] and board[row-1][col] == word[0]:
            visited[row-1][col] = True
            doesWordExist = doesWordExist or self.findWord(board, word[1:], visited, row-1, col)
            visited[row-1][col] = False

        # go down
        if row+1 < numRows and not visited[row+1][col] and board[row+1][col] == word[0]:
            visited[row+1][col] = True
            doesWordExist = doesWordExist or self.findWord(board, word[1:], visited, row+1, col)
            visited[row+1][col] = False

        return doesWordExist

    def exist(self, board: List[List[str]], word: str) -> bool:
        lenBoard = len(board)
        lenCol = len(board[0])
        visited = [[False for y in range(lenCol)] for x in range(lenBoard)]

        for row in range(lenBoard):
            for col in range(lenCol):
                if board[row][col] == word[0]:
                    visited[row][col] = True
                    if self.findWord(board, word[1:], visited, row, col):
                        return True

                    visited[row][col] = False

        return False
                    