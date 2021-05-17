# A string s of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)
        start = 0
        end = float('-inf')
        visited = set()
        
        # stores the last index we encounter letter in s
        last = {letter: index for index, letter in enumerate(s)}
        
        output = []
        for i in range(n):
            if s[i] not in visited:
                visited.add(s[i])
                
                if last[s[i]] > end:
                    end = last[s[i]]
            
            if i == end:
                output.append(end-start+1)
                start = end+1
                end = float('-inf')
        
        return output
                    
            
        