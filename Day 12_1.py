import pathlib
import re
import collections

lines = pathlib.Path("inputs/12.txt").read_text().splitlines()
combR = re.compile(r"([#\.]{5}) => ([#\.])")

plants = collections.defaultdict(lambda: ".", zip(range(len(lines[0]) - 15), lines[0][15:]))
combs = dict([combR.search(line).groups() for line in lines[2:]])

minKey = 0
maxKey = len(lines[0]) - 15 - 1

for i in range(20):
    nextGen = collections.defaultdict(lambda: ".")
    setMinKey = False
    for pos in range(minKey - 2, maxKey + 2 + 1):
        comb = plants[pos - 2] + plants[pos - 1] + plants[pos] + plants[pos + 1] + plants[pos + 2]
        nextGen[pos] = combs[comb]
        if nextGen[pos] == "#":
            if not setMinKey:
                minKey = pos
                setMinKey = True
            maxKey = pos
    plants = nextGen

print(sum([pos for pos in range(minKey, maxKey + 1) if plants[pos] == "#"]))
