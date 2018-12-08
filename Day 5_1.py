import pathlib

polymer = list([line for line in pathlib.Path("inputs/5.txt").read_text().splitlines()][0])

i = 1
while i < len(polymer):
    prevChar = polymer[i - 1]
    char = polymer[i]
    if char.lower() != prevChar.lower() or char == prevChar:
        i += 1
        continue
    
    del polymer[i - 1]
    del polymer[i - 1]
    i -= 1

print(len(polymer))
