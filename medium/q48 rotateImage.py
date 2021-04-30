# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) >= 2:
            
            arr = []
            
            # read matrix and store in string
            for col in range(len(matrix[0])):
                for row in range(len(matrix)-1, -1, -1):
                    arr.append(matrix[row][col])
            
            # read string and put it in matrix
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    matrix[row][col] = arr.pop(0)
                    
        