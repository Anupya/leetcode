# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]]
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        # numRows > 2 here
        results = [[1], [1,1]]
        i = 1
        while i < numRows-1:
            lastRow = results[-1]
            newRow = [1]
            start = 0
            while start < i:
                newRow.append(lastRow[start] + lastRow[start+1])
                start+=1
            newRow.append(1)
            results.append(newRow)
            i+=1
        
        return results
        