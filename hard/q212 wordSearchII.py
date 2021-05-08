# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

class Solution:
    def traverse(self, board, word, x, y, visited):
        
        if len(word) == 0:
            return True
        
        left, right, up, down = False, False, False, False
        
        # left (y-1)
        if y-1 >= 0 and board[x][y-1] == word[0] and (x, y-1) not in visited:
            visited.add((x, y-1))
            left = self.traverse(board, word[1:], x, y-1, visited)
            visited.remove((x, y-1))
        
        # right (y+1)
        if y+1 < len(board[0]) and board[x][y+1] == word[0] and (x, y+1) not in visited:
            visited.add((x, y+1))
            right = self.traverse(board, word[1:], x, y+1, visited)
            visited.remove((x, y+1))
        
        # up (x-1)
        if x-1 >= 0 and board[x-1][y] == word[0] and (x-1, y) not in visited:
            visited.add((x-1, y))
            up = self.traverse(board, word[1:], x-1, y, visited)
            visited.remove((x-1, y))
        
        # down (x+1)
        if x+1 < len(board) and board[x+1][y] == word[0] and (x+1, y) not in visited:
            visited.add((x+1, y))
            down = self.traverse(board, word[1:], x+1, y, visited)
            visited.remove((x+1, y))
        
        return True if left or right or up or down else False
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        foundWords = []
        
        filteredWords = []
        charSet = set(board[x][y] for y in range(len(board[0])) for x in range(len(board)))
        for x in words:
            if set(x).issubset(charSet):
                filteredWords.append(x)
        
        words[:] = filteredWords
        
        # find each word
        for word in words:
            n = len(foundWords)
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if board[x][y] == word[0]:
                        visited = set()
                        visited.add((x, y))
                        found = self.traverse(board, word[1:], x, y, visited)
                        if found:
                            foundWords.append(word)
                            break
                
                if n < len(foundWords):
                    break
        
        return foundWords
            
        