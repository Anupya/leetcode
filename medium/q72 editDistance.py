"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # create a 2D dynamic programming matrix

        word1len = len(word1)
        word2len = len(word2)

        matrix = [[0 for i in range(word1len+1)] for j in range(word2len+1)]

        # base cases
        for col in range(word1len+1): # first row
            # need col # of inserts to convert to word1
            matrix[0][col] = col
        for row in range(word2len+1): # first col
            # need row # of inserts to convert to word2
            matrix[row][0] = row
        
        for i in range(1, word2len+1):
            for j in range(1, word1len+1):
                # if the letter is the same, do nothing
                if word2[i-1] == word1[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    # if not the same, get min of top, left and topleft sq
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
        
        return matrix[word2len][word1len]

