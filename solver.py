import json

with open("dictionary.json", "r") as f:
    data = json.load(f)

running = True

#class for each node in trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

#trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    #insert
    def insert(self, word: str) -> None:
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

#dictionary trie
dictionary = Trie()
for word in data:
    dictionary.insert(word)

# main loop
while running:
    letters = [letter for letter in input("Enter your letters:\n") if letter.isalpha()]
