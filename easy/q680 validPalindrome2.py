"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        lenS = len(s)
        if lenS <= 1:
            return True

        start = 0
        end = lenS-1
        mismatch = False

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                if mismatch: # second mismatch
                    return False
                elif end - start == 1: # only mismatch is in the middle
                    return True 
                else:
                    # unsure which pointer to move
                    mismatch = True
                    addAmt = 1

                    # calculate until we know there is >=1 pointer that should *not* be moved
                    while s[start+addAmt] == s[end-addAmt+1] and s[start+addAmt-1] == s[end-addAmt]:
                        addAmt += 1
    
                    if s[start+addAmt] == s[end-addAmt+1]: # move start
                        start += addAmt
                        end -= addAmt-1
                    elif s[start+addAmt-1] == s[end-addAmt]: # move end
                        start += addAmt-1
                        end -= addAmt
                    else: # neither pointer can be moved to satisfy the problem constraints
                        return False
    
        return True
                        
        