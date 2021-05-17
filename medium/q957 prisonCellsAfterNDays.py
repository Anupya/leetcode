# There are 8 prison cells in a row and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

# Return the state of the prison after n days (i.e., n such changes described above).


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        # store patterns
        patterns = [cells]
        stringify = "".join(map(str, cells))
        permutations = set()
        
        i = 1
        
        while stringify not in permutations or i == 1:

            permutations.add(stringify)
            newCells = [0]
            for j in range(1, 7):
                if cells[j-1] == cells[j+1]:
                    newCells.append(1)
                else:
                    newCells.append(0)
            
            newCells.append(0)
            patterns.append(newCells)
            cells = newCells
            stringify = "".join(map(str, cells))
            i += 1

        listify = [int(x) for x in stringify]
        index = patterns.index(listify)
        divisor = len(permutations)-index
        
        return patterns[index + ((n-index) % divisor)]
        
                    
        