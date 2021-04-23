# Count the number of prime numbers less than a non-negative number, n.

class Solution:    
    def countPrimes(self, n: int) -> int: 
        
        arrN = [i for i in range(n)]
        primes = 0
        
        # everytime we encounter a non -1 number, it is a prime 
        # because nothing before it changed it to -1
        
        for n in arrN:
            if n<=1: 
                continue
                
            # prime!
            if n != -1:
                primes+=1
                
                # change every multiple of it in arr to -1
                i = n
                while i < len(arrN):
                    arrN[i] = -1
                    i+=n
            
        return primes
                
        
        
        