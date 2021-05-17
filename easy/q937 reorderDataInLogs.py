# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # dictionary with key = art can, val = let1
        letDict = collections.defaultdict(list)
        
        final = []
        for x in logs:
            if not x[-1].isdigit():
                firstSpace = x.index(" ")
                letDict[x[firstSpace+1:]].append(x[0:firstSpace])
        
        for key in sorted(letDict):
            
            for val in sorted(letDict[key]):
                final.append(val + " " + key)
        
        for x in logs:
            if x[-1].isdigit():
                final.append(x)
        
        return final
                
        