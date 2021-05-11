# We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# Given a string p, return the number of unique non-empty substrings of p are present in s.

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:

        # number of substrings starting at p[i] stored in dp[i]
        dp = [0 for x in range(len(p))]
        dp[-1] = 1
        streak = 1
        
        for i in range(len(p)-2, -1, -1):
            if (ord(p[i+1]) - ord(p[i]) == 1) or (p[i] == "z" and p[i+1] == "a"):
                streak+=1
                dp[i] = streak
            else:
                streak = 1
                dp[i] = 1
            i-=1
        
        # find highest value for each character in dp and add them
        tracker = {x:0 for x in "abcdefghijklmnopqrstuvwxyz"}
        for i, num in enumerate(dp):
            if tracker[p[i]] < num:
                tracker[p[i]] = num
        
        return sum(tracker.values())
            
        