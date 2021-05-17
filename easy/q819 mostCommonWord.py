# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # preprocess paragraph
        newPara = ""
        prohibited = set(["!", "?", ";", ",", "'", "."])
        for x in paragraph:
            if x not in prohibited:
                newPara += x.lower()
            else:
                newPara += " "

        words = newPara.split()
        frequency = collections.Counter(words)
        
        for x in banned:
            del frequency[x]
        
        return max(frequency, key=lambda x: frequency[x])
        
        