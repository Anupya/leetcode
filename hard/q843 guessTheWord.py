# This is an interactive problem.

# You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

# You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

# This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

# For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def stringSimilarity(self, str1, str2):
        diff = 0
        for x in range(6):
            if str1[x] == str2[x]:
                diff+=1
        return diff
    
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n = len(wordlist)
        
        if n <= 10:
            for word in wordlist:
                num = master.guess(word)
        else:
            self.findSecretWordHelper(wordlist, master)
    
    def findSecretWordHelper(self, wordlist, master):
        
        while wordlist:
            
            # randomize to increase chances of picking a good word
            chosen = random.choice(wordlist)
            wordlist.remove(chosen)

            apiDiff = master.guess(chosen)
            if apiDiff == 6:
                return

            wordlist[:] = [word for word in wordlist if self.stringSimilarity(word, chosen) == apiDiff]
        
        
            
        