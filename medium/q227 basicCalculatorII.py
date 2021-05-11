# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

class Solution:
    def calculate(self, s: str) -> int:
        
        # multiplication/division are treated equally, first come first solve
        # addition/subtraction are next in priority
        # we can use an optimized stack to apply these rules
        
        s = s.replace(" ", "")
        if not s:
            return 0
        
        # last stores */ evaluation or +/-
        # cur stores current number we are reading
        # result = evaluated so far
        
        cur, last, result, sign = 0, 0, 0, '+'
        for i in range(len(s)):
            
            char = s[i]
            
            # add new digit to end of number so far
            if char.isdigit():
                cur*=10
                cur+=int(char)
                
            # if we are at +-*/ or end of string, evaluate the previous sign
            if not char.isdigit() or i == len(s)-1:
                if sign == "+" or sign == "-":
                    result += last
                    last = cur if sign == "+" else -cur
                    
                elif sign == "*":
                    last *= cur
                elif sign == "/":
                    last = int(last/cur)
                
                sign = char
                cur = 0

        return result + last

       