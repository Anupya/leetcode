# In a row of trees, the i-th tree produces fruit with type tree[i].

# You start at any tree of your choice, then repeatedly perform the following steps:

# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

# What is the total amount of fruit you can collect with this procedure?

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # apple - banana - apple - banana - banana - apple
        # longest interval with 2 unique fruits
        
        if len(tree) == 1 or len(tree) == 2:
            return len(tree)
        
        start = 0
        stop = 2
        maxWindow = 2
        fruitDict = {tree[0]: 0} # stores last encountered index of fruit 
        fruitDict[tree[1]] = 1
        
        while stop < len(tree):
            
            # kick out fruit at start
            if tree[stop] not in fruitDict and len(fruitDict) == 2: 
                
                # get key with less value and remove it
                keys = list(fruitDict.keys())
                if fruitDict[keys[0]] < fruitDict[keys[1]]:
                    start = fruitDict[keys[0]]
                    fruitDict.pop(keys[0], None)
                else:
                    start = fruitDict[keys[1]]
                    fruitDict.pop(keys[1], None)
                    
                start += 1
            
            fruitDict[tree[stop]] = stop
            stop += 1
            maxWindow = max(maxWindow, stop-start)
        
        return maxWindow
            
            
        