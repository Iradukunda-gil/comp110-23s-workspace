"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730458371"
"""Prompting for input"""
instances: int = 0
word: str = input("Enter 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
Character: str = input("Enter a single Character: ")
if len(Character) != 1:
    print("Error: word must be a single Character.")
    exit()
print("Searching for " + Character + " in " + word)
"""Checking Indices for matches"""
if Character == word[0]:
    print(Character + " found at index 0")
    instances = instances + 1
if Character == word[1]:
    print(Character + " found at index 1")
    instances = instances + 1
if Character == word[2]:
    print(Character + " found at index 2")
    instances = instances + 1
if Character == word[3]:
    print(Character + " found at index 3")
    instances = instances + 1
if Character == word[4]:
    print(Character + " found at index 4")
    instances = instances + 1
if instances == 0:
    print("No instances of " + Character + " found in " + word)
else: 
    if instances > 0:
        if instances == 1:
            print("1 instance of " + Character + " found in " + word)
        else:
            print(str(instances) + " instances of " + Character + " found in " + word)