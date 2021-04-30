# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

# A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

class Solution:  
    def isValidPart(self, s):
        if len(s) == 0:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        if 0 <= int(s) <= 255:
            return True
        else:
            return False
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        for i in range(1, 4):
            if not self.isValidPart(s[:i]):
                continue
            for j in range(i+1, i+4):
                if not self.isValidPart(s[i:j]):
                    continue
                for k in range(j+1, j+4):
                    if self.isValidPart(s[j:k]) and self.isValidPart(s[k:]):
                        ip = s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
                        result.append(ip)
        
        return result
                            
        
        

            
        