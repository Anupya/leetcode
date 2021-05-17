# Given a string s representing an expression, implement a basic calculator to evaluate it.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def evaluate(self, s):
        
        s = s.replace("--", "+")
        
        # read current number
        cur = 0
        
        # stores last sign encountered
        sign = '+'
        
        # stores final value
        result = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                cur *= 10
                cur += int(s[i])
            
            if s[i] == "+" or s[i] == "-" or i == len(s)-1:
                if sign == '+':
                    result += cur
                else:
                    result -= cur
                
                cur = 0
                sign = s[i]
        
        return result
        
    def calculate(self, s: str) -> int:
        
        stack = []

        # simplify all parentheses
        for i in range(len(s)):

            if s[i] != ")":
                stack.append(s[i])
            else:
                newS = ""
                while stack[-1] != "(":
                    newS = str(stack.pop()) + newS
                
                # remove opening parentheses
                stack.pop()
                num = self.evaluate(newS)
                stack.append(num)
        
        # evaluate parentheses-less expression
        finalExpression = "".join(str(x) for x in stack)
        return self.evaluate(finalExpression)       
     