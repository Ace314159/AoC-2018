import pathlib
import collections

data = [(line[5], line[36]) for line in pathlib.Path("inputs/7.txt").read_text().splitlines()]
edges = collections.defaultdict(lambda: collections.defaultdict(set))
for start, end in data:
    edges[start]["out"].add(end)
    edges[end]["in"].add(start)
roots = [node for node in edges.keys() if len(edges[node]["in"]) == 0]


inProgress = []
inProgressInstructions = []
time = -1
while len(roots) > 0 or len(inProgress) > 0:
    i = 0
    while i < len(inProgress):
        if inProgress[i] > 1:
            inProgress[i] -= 1
            i += 1
        else:
            inProgress.pop(i)
            start = inProgressInstructions.pop(i)
            for end in edges[start]["out"]:
                edges[end]["in"].remove(start)
                if len(edges[end]["in"]) == 0:
                    roots.append(end)
            del edges[start]["out"]

    while len(inProgress) < 5 and len(roots) > 0:
        roots.sort()
        task = roots.pop(0)
        inProgress.append(ord(task) - ord("A") + 1 + 60)
        inProgressInstructions.append(task)
    time += 1
print(time)
