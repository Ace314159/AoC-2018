import pathlib
import collections

data = [(line[5], line[36]) for line in pathlib.Path("inputs/7.txt").read_text().splitlines()]
edges = collections.defaultdict(lambda: collections.defaultdict(set))
for start, end in data:
    edges[start]["out"].add(end)
    edges[end]["in"].add(start)

instructions = []
roots = [node for node in edges.keys() if len(edges[node]["in"]) == 0]

while len(roots) > 0:
    roots.sort()
    start = roots.pop(0)
    instructions.append(start)
    for end in edges[start]["out"]:
        edges[end]["in"].remove(start)
        if len(edges[end]["in"]) == 0:
            roots.append(end)
    del edges[start]["out"]
print("".join(instructions))
