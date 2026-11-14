import json

with open("dictionary.json", "r") as f:
    data = json.load(f)

running = True

# main loop
while running:
    letters = [letter for letter in input("Enter your letters:\n") if letter.isalpha()]
    