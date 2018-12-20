import pathlib
import itertools

coords = [tuple(map(int, line.split(", "))) for line in pathlib.Path("inputs/6.txt").read_text().splitlines()]

minX = minY = 10000000000
maxX = maxY = 0
for x, y in coords:
    minX = min(minX, x)
    minY = min(minY, y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)

area = 0
for x, y in itertools.product(range(minX, maxX + 1), range(minY, maxY + 1)):
    distanceSum = 0
    for coord in coords:
        distanceSum += abs(coord[0] - x) + abs(coord[1] - y)
    if distanceSum < 10000:
        area += 1
print(area)
