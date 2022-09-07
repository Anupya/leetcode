'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach 2
        m = len(matrix)
        n = len(matrix[0])
        firstCol = False
        
        # go through matrix and mark the topmost and leftmost column as zero as a flag. if matrix[0][0] == 0, then topmost row should be marked zero. if isLeftmostColZero == True,then leftmost col should be marked zero.
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if col == 0:
                        firstCol = True
                    else:
                        matrix[row][0] = 0
                        matrix[0][col] = 0
                        
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(n):
                matrix[0][col] = 0
        
        if firstCol:
            for row in range(m):
                matrix[row][0] = 0


        # Approach 1
        """
        m = len(matrix) #3
        n = len(matrix[0]) #3
        
        currentZeroes = {}
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    currentZeroes[(row, col)] = 0

        ignoreCoordinates = {}
        for coord in currentZeroes:
            # set everything in that row to 0s
            for colsInZeroRow in range(n):
                if (coord[0], colsInZeroRow) not in ignoreCoordinates:
                    matrix[coord[0]][colsInZeroRow] = 0
                    ignoreCoordinates[(coord[0], colsInZeroRow)] = 0;

            # set everything in that col to 0s
            for rowsInZeroCol in range(m):
                if (rowsInZeroCol, coord[1]) not in ignoreCoordinates:
                    matrix[rowsInZeroCol][coord[1]] = 0
                    ignoreCoordinates[(rowsInZeroCol, coord[1])] = 0;
        """
    
