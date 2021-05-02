# Convert a non-negative integer num to its English words representation.

class Solution:
    def numberToWords(self, num: int) -> str:
        
        word = { 0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 
                8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 
                20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
                70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred", 1000: "Thousand", 
                1000000: "Million", 1000000000: "Billion"}
        
        # 2147483647
        
        n = len(str(num))
        
        if len(str(num)) == 1:
            return word[num]
            
        if len(str(num)) == 2:
            if num in word:
                return word[num]
            else:
                return word[int(str(num)[0] + "0")] + " " + word[int(str(num)[1])]
        
        if len(str(num)) == 3:
            if num % 100 == 0:
                return word[int(str(num)[0])] + " " + word[100]
            else:
                return word[int(str(num)[0])] + " " + word[100] + " " + self.numberToWords(int(str(num)[1:]))
        
        if len(str(num)) == 4:
            if num % 1000 == 0:
                return word[int(str(num)[0])] + " " + word[1000]
            else:
                return word[int(str(num)[0])] + " " + word[1000] + " " + self.numberToWords(int(str(num)[1:]))
        
        if len(str(num)) == 5:
            if num % 1000 == 0:
                return self.numberToWords(int(str(num)[0:2])) + " " + word[1000]
            else:
                return self.numberToWords(int(str(num)[0:2])) + " " + word[1000] + " "+ self.numberToWords(int(str(num)[2:]))
        
        if len(str(num)) == 6:
            if num % 1000 == 0:
                return self.numberToWords(int(str(num)[0:3])) + " " + word[1000]
            
            return self.numberToWords(int(str(num)[0:3])) + " " + word[1000] + " " + self.numberToWords(int(str(num)[3:]))
        
        if len(str(num)) == 7:
            if num % 1000000 == 0:
                return word[int(str(num)[0])] + " " + word[1000000]
            
            return word[int(str(num)[0])] + " " + word[1000000] + " " + self.numberToWords(int(str(num)[1:]))
        
        if len(str(num)) == 8:
            if num % 1000000 == 0:
                return self.numberToWords(int(str(num)[0:2])) + " " + word[1000000]
            
            return self.numberToWords(int(str(num)[0:2])) + " " + word[1000000] +  " " + self.numberToWords(int(str(num)[2:]))
        
        if len(str(num)) == 9:
            if num % 1000000 == 0:
                return self.numberToWords(int(str(num)[0:3])) + " " + word[1000000]
                
            return self.numberToWords(int(str(num)[0:3])) + " " + word[1000000] + " " + self.numberToWords(int(str(num)[3:]))
        
        if len(str(num)) == 10:
            if num % 1000000000 == 0:
                return word[int(str(num)[0])] + " " + word[1000000000]
            
            return word[int(str(num)[0])] + " " + word[1000000000] + " " + self.numberToWords(int(str(num)[1:]))
            