import pathlib

final = 0
changes = [int(line) for line in pathlib.Path("inputs/1.txt").read_text().splitlines()]

for change in changes:
    final += change

print(final)
