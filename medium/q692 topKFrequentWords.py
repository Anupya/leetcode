# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        mostFrequent = []
        
        frequency = collections.Counter(words)

        for word in frequency:
            heappush(mostFrequent, (-frequency[word], word))
        
        output = []
        while k:
            output.append(heappop(mostFrequent)[1])
            k -= 1
            
        return output
        
        