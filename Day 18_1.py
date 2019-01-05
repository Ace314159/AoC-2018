import pathlib
import collections
import itertools

lines = pathlib.Path("inputs/18.txt").read_text().splitlines()

graph = collections.defaultdict(lambda: ("."))
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        graph[(x, y)] = char

newGraph = collections.defaultdict(lambda: ("."))
for i in range(10):
    for x, y in itertools.product(range(len(lines[0])), range(len(lines))):
        adjacentCounter = collections.Counter([graph[(x + i, y + j)] for i, j in itertools.product(range(-1, 2), range(-1, 2)) if i != 0 or j != 0])
        newGraph[(x, y)] = graph[(x, y)]
        if graph[(x, y)] == ".":
            if adjacentCounter["|"] >= 3:
                newGraph[(x, y)] = "|"
        elif graph[(x, y)] == "|":
            if adjacentCounter["#"] >= 3:
                newGraph[(x, y)] = "#"
        else:
            if adjacentCounter["#"] < 1 or adjacentCounter["|"] < 1:
                newGraph[(x, y)] = "."
    graph = newGraph.copy()
    newGraph = collections.defaultdict(lambda: ("."))

counter = collections.Counter(graph.values())
print(counter["|"] * counter["#"])
