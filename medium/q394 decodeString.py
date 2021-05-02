# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:

        # while there needs to be more simplification
        while s.count("[") > 0:
            start = 0
            
            while not s[start].isdigit():
                start+=1
            
            stop = start
            
            while s[stop] != "[":
                stop+=1
            
            outsideNumber = int(s[start:stop])
            
            # find its closing bracket
            stack = []
            i = stop+1
            while True:
                if s[i] == "[":
                    stack.append("[")
                if s[i] == "]" and len(stack) == 0:
                    break
                if s[i] == "]" and len(stack):
                    stack.pop()
                i+=1
            
            # i is now the closing bracket
            pattern = s[stop+1:i]
            repeated = ""
            for x in range(outsideNumber):
                repeated+= pattern
            
            s = s[:start] + repeated + s[i+1:]
        
        return s
                
            
            
        