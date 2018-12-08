import pathlib

polymer = list([line for line in pathlib.Path("inputs/5.txt").read_text().splitlines()][0])
letters = set()
for char in polymer:
    letters.add(char.lower())

minLen = len(polymer)
for letter in letters:
    modifiedPolymer = polymer.copy()
    i = 1
    while i < len(modifiedPolymer):
        if modifiedPolymer[i].lower() == letter:
            del modifiedPolymer[i]
            continue
        prevChar = modifiedPolymer[i - 1]
        char = modifiedPolymer[i]
        if char.lower() != prevChar.lower() or char == prevChar:
            i += 1
            continue
        
        del modifiedPolymer[i - 1]
        del modifiedPolymer[i - 1]
        i -= 1
    minLen = min(minLen, len(modifiedPolymer))

print(minLen)
