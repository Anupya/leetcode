# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# Given a positive integer n, return the nth term of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        # 1, 11, 1211, 111221, 312211, 13112221, ...
        
        string = "1" # countAndSay(1)
        for x in range(2, n+1): # countAndSay(x)
            
            newString = ""
            
            # look at groups of same character
            count = 1
            cur = 1
            prev = 0
            
            while cur < len(string): 
                if string[prev] != string[cur]:
                    newString+= str(count) + string[prev]
                    count = 1
                else:
                    count += 1
                
                cur+=1
                prev+=1
            
            
            newString += str(count) + string[-1] # add last character group
            string = newString
            
        return string
                    
            
            
            
            
        
        