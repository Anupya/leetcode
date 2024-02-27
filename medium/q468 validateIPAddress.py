"""
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
"""
from typing import List

class Solution:
    def is_ipv4(self, numbers: List[str]) -> bool:
        for num in numbers:
            if not len(num):
                return False
            elif num[0] == '0' and len(num) > 1:
                return False
            else:
                try:
                    integerified = int(num, 10)
                    if integerified >= 0 and integerified <= 255:
                        continue
                    return False
                except ValueError:
                    return False

        return True

    def is_ipv6(self, hexadecimals: List[str]) -> bool:
        for hd in hexadecimals:
            if len(hd) > 4:
                return False
            try:
                int(hd, 16)
                continue
            except ValueError:
                return False
        
        return True

    def validIPAddress(self, queryIP: str) -> str:
        valid_ipv4 = "IPv4"
        valid_ipv6 = "IPv6"
        neither = "Neither"

        ipv4_split = queryIP.split('.')
        ipv6_split = queryIP.split(':')

        if len(ipv4_split) == 4 and self.is_ipv4(ipv4_split):
            return valid_ipv4
        elif len(ipv6_split) == 8 and self.is_ipv6(ipv6_split):
            return valid_ipv6
        else:
            return neither

