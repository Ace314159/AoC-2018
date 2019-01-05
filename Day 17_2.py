import pathlib
import re
import collections

lines = pathlib.Path("inputs/17.txt").read_text().splitlines()
veinR = re.compile(r"([xy]){1}=([0-9]+), ([xy]){1}=([0-9]+)\.\.([0-9]+)")

graph = collections.defaultdict(lambda: collections.defaultdict(lambda: "."))
graph[0][500] = "+"
potential = collections.deque([(500, 1)])
solid = frozenset(["#", "~"])
waterSrc = frozenset(["+", "|"])
water = frozenset(["~", "|"])
minX = minY = 1000000
maxX = maxY = 0
for line in lines:
    groups = veinR.fullmatch(line).groups()
    vein = {groups[0]: int(groups[1]), groups[2]: (int(groups[3]), int(groups[4]))}
    if type(vein["x"]) == int:
        minX = min(minX, vein["x"])
        maxX = max(maxX, vein["x"])
        minY = min(minY, vein["y"][0])
        maxY = max(maxY, vein["y"][1])
        for y in range(vein["y"][0], vein["y"][1] + 1):
            graph[y][vein["x"]] = "#"
    else:
        minX = min(minX, vein["x"][0])
        maxX = max(maxX, vein["x"][1])
        minY = min(minY, vein["y"])
        maxY = max(maxY, vein["y"])
        for x in range(vein["x"][0], vein["x"][1] + 1):
            graph[vein["y"]][x] = "#"

while len(potential) > 0:
    cur = potential.popleft()
    around = {graph[cur[1] - 1][cur[0]], graph[cur[1] + 1][cur[0]], graph[cur[1]][cur[0] - 1], graph[cur[1]][cur[0] + 1]}
    if graph[cur[1]][cur[0]] in solid or cur[1] > maxY:
        continue

    oldPotential = potential.copy()
    potential.appendleft((cur[0] + 1, cur[1]))
    potential.appendleft((cur[0] - 1, cur[1]))
    potential.appendleft((cur[0], cur[1] + 1))

    changed = False

    if graph[cur[1] + 1][cur[0]] in solid:
        # Left
        foundLeft = False
        lPos = (cur[0], cur[1])
        while True:
            if graph[lPos[1] + 1][lPos[0]] in solid:
                if graph[lPos[1]][lPos[0]] != "|":
                    changed = True
                graph[lPos[1]][lPos[0]] = "|"
                if graph[lPos[1]][lPos[0] - 1] == "#":
                    foundLeft = True
                    break
            else:
                if graph[lPos[1]][lPos[0]] != "|":
                    changed = True
                graph[lPos[1]][lPos[0]] = "|"
                potential.appendleft((lPos[0] + 1, lPos[1]))
                potential.appendleft((lPos[0] - 1, lPos[1]))
                potential.appendleft((lPos[0], lPos[1] + 1))
                break
            lPos = (lPos[0] - 1, lPos[1])
        # Right
        foundRight = False
        rPos = (cur[0], cur[1])
        while True:
            if graph[rPos[1] + 1][rPos[0]] in solid:
                if graph[lPos[1]][rPos[0]] != "|":
                    changed = True
                graph[rPos[1]][rPos[0]] = "|"
                if graph[rPos[1]][rPos[0] + 1] == "#":
                    foundRight = True
                    break
            else:
                if graph[lPos[1]][rPos[0]] != "|":
                    changed = True
                graph[rPos[1]][rPos[0]] = "|"
                potential.appendleft((rPos[0] + 1, rPos[1]))
                potential.appendleft((rPos[0] - 1, rPos[1]))
                potential.appendleft((rPos[0], rPos[1] + 1))
                break
            rPos = (rPos[0] + 1, rPos[1])
        # Both
        if foundLeft and foundRight:
            for x in range(lPos[0], rPos[0] + 1):
                if graph[cur[1]][x] != "~":
                    changed = True
                graph[cur[1]][x] = "~"
            potential.appendleft((cur[0], cur[1] - 1))
    elif graph[cur[1] - 1][cur[0]] in waterSrc:
        changed = graph[cur[1]][cur[0]] != "|"
        graph[cur[1]][cur[0]] = "|"

    if not changed:
        potential = oldPotential

total = 0
for y in graph.keys():
    if y < minY or y > maxY:
        continue
    total += sum([graph[y][x] == "~" for x in graph[y].keys()])
print(total)
