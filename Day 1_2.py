import pathlib
import itertools

changes = [int(line) for line in pathlib.Path("inputs/1.txt").read_text().splitlines()]
final = 0
prevFinals = set([final])

for change in itertools.cycle(changes):
    final += change
    if final in prevFinals:
        break
    prevFinals.add(final)

print(final)
