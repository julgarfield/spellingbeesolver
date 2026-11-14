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

    #insert function
    def insert(self, word: str) -> None:
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    #search function
    def search(self, node, current_word, results_list, allowed_letters, center_letter):
        if (node.isEndOfWord == True and len(current_word) >= 4 and center_letter in current_word):
            results_list.append(current_word)
        for char in node.children:
            if char in allowed_letters:
                self.search(node.children[char], current_word + char, results_list, allowed_letters, center_letter)

#dictionary trie
dictionary = Trie()
for word in data:
    dictionary.insert(word)

# main loop
while running:
    letters = [letter for letter in input("Please enter your letters:\n").lower() if letter.isalpha()]
    if len(set(letters)) != 7:
        print("Please enter 7 unique letters.")
        continue
    center = input("Which letter is in the center?\n").lower().strip()
    if center not in letters:
        print("Please make sure the center letter is one of the 7 letters.")
        continue
    results = []
    dictionary.search(dictionary.root, "", results, letters, center)
    print(results)
    running = False