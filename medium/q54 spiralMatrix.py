# Given an m x n matrix, return all elements of the matrix in spiral order.
# Faster than 99.85% of submissions! (16 ms)
# Less memory used than 94.37% of submissions! (14.1 MB)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral = []
        while len(matrix) > 0:
            
            numRows = len(matrix)
            numCols = len(matrix[0])
            
            # ADDITION ----
            
            # take first row
            spiral += matrix[0] #1
            
            if numRows > 1:
                
                # take last column - first element
                for x in range(1, numRows):
                    spiral.append(matrix[x][-1]) #2,3,4,5,...,10

                # take last row - last element
                for x in range(numCols-2, -1, -1):
                    spiral.append(matrix[-1][x])

                if numCols > 1:
                    # take first column - first and last element
                    for x in range(numRows-2, 0, -1):
                        spiral.append(matrix[x][0])
           
            # DELETION ----
            
            # remove first row from matrix
            matrix.pop(0)
            
            # if there is a last row, remove that too
            if len(matrix):
                matrix.pop(len(matrix)-1) # last row
            
            # remove first column
            for row in matrix:
                row.pop(0)
                
                # if there is a last column, remove that too
                if len(row):
                    row.pop(-1)
            
            # clean up empty rows
            i = 0
            while i < len(matrix):
                if len(matrix[i]) == 0:
                    matrix.pop(i)
                else:
                    i+=1
        
        return spiral
        