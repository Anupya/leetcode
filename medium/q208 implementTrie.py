"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for character in word:
            if character not in trie:
                trie[character] = {}
            
            trie = trie[character]
        
        trie["*"] = {}

    def search(self, word: str) -> bool:
        trie = self.trie
        for character in word:
            if character in trie:
                trie = trie[character]
            else:
                return False

        return "*" in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for character in prefix:
            if character in trie:
                trie = trie[character]
            else:
                return False
        
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)