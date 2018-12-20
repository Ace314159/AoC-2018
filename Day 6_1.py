import pathlib
import itertools
import collections
from scipy.spatial import KDTree

coords = [tuple(map(int, line.split(", "))) for line in pathlib.Path("inputs/6.txt").read_text().splitlines()]

minX = minY = 10000000000
maxX = maxY = 0
for x, y in coords:
    minX = min(minX, x)
    minY = min(minY, y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)

tree = KDTree(coords)

freqs = collections.defaultdict(int)
edges = set()
for x, y in itertools.product(range(minX, maxX), range(minY, maxY)):
    dists, points = tree.query((x, y), k=2, p=1)
    if x == minX or x == maxX - 1 or y == minY or y == maxY - 1:
        edges.add(points[0])
    if dists[0] != dists[1]:
        freqs[points[0]] += 1

print(freqs)
for point, freq in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
    if point not in edges:
        print(freq)
        break
