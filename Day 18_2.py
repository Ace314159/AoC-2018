import pathlib
import collections
import itertools

lines = pathlib.Path("inputs/18.txt").read_text().splitlines()

graph = collections.defaultdict(lambda: ("."))
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        graph[(x, y)] = char

num = 1000000000

alreadyOccurred = {tuple(sorted(graph.items())): 0}
alreadyOccurredOther = {0: tuple(sorted(graph.items()))}
newGraph = collections.defaultdict(lambda: ("."))
for i in range(1, num + 1):
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
    frozen = tuple(sorted(graph.items()))
    if frozen in alreadyOccurred:
        break
    alreadyOccurred[frozen] = i
    alreadyOccurredOther[i] = frozen
    newGraph = collections.defaultdict(lambda: ("."))

counter = collections.Counter([item[1] for item in alreadyOccurredOther[alreadyOccurred[frozen] + ((num - i) % (i - alreadyOccurred[frozen]))]])
print(counter["|"] * counter["#"])
