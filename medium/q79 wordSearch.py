# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def traverse (self, board, word, x, y, visited):

        if len(word) == 0:
            return True
        
        left, right, up, down = False, False, False, False
        
        # up
        if x-1 >= 0 and board[x-1][y] == word[0] and (x-1, y) not in visited:
            visited.add((x-1, y))
            up = self.traverse(board, word[1:], x-1, y, visited)
            visited.remove((x-1, y))
    
        # down
        if x+1 < len(board) and board[x+1][y] == word[0] and (x+1, y) not in visited:
            visited.add((x+1, y))
            down = self.traverse(board, word[1:], x+1, y, visited)
            visited.remove((x+1, y))
        
        # left
        if y-1 >= 0 and board[x][y-1] == word[0] and (x, y-1) not in visited:
            visited.add((x, y-1))
            left = self.traverse(board, word[1:], x, y-1, visited)
            visited.remove((x, y-1))
        
        # right
        if y+1 < len(board[0]) and board[x][y+1] == word[0] and (x, y+1) not in visited:
            visited.add((x, y+1))
            right = self.traverse(board, word[1:], x, y+1, visited)
            visited.remove((x, y+1))
        
        return True if left or right or up or down else False
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                
                if board[x][y] == word[0]:
                    visited = set()
                    visited.add((x, y))
                    found = self.traverse(board, word[1:], x, y, visited)
                    if found:
                        return True
        
        return False
        
        