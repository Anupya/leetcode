# We are given two arrays A and B of words.  Each word is a string of lowercase letters.

# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

# Now say a word a from A is universal if for every b in B, b is a subset of a. 

# Return a list of all universal words in A.  You can return the words in any order.


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universalList = []
        
        # create alphabet array so we can limit our for loop to 26
        # arr[0] = number of times we need a to appear in universal word
        # arr[1] = number of times we need b to appear in universal word
        # ...
        arr = [0 for x in range(0, 26)]
        for word in B:
            setWord = {char for char in word}
            for char in setWord:
                arr[ord(char)-97] = max(arr[ord(char)-97], word.count(char))
        
        # find universal words
        for word in A:
            universal = True
            for x in range(0, 26):
                if arr[x] > word.count(chr(x+97)):
                    universal = False
                    break
            if universal:
                universalList.append(word)
                    
        return universalList
        