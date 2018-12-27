import pathlib
import itertools
import collections

serialNumber = int(pathlib.Path("inputs/11.txt").read_text().splitlines()[0])

summedAreaTable = collections.defaultdict(int)
for x, y in itertools.product(range(1, 300 + 1), range(1, 300 + 1)):
    rackID = x + 10
    powerLevel = rackID * y
    powerLevel += serialNumber
    powerLevel *= rackID
    powerLevel = (powerLevel // 100) % 10
    powerLevel -= 5
    summedAreaTable[(x, y)] = powerLevel + summedAreaTable[(x, y - 1)] + summedAreaTable[(x - 1, y)] - summedAreaTable[(x - 1, y - 1)]

maxPowerLevel = summedAreaTable[(1, 1)]
coord = (-1, -1)
for x, y in itertools.product(range(1, 298 + 1), range(1, 298 + 1)):
    powerLevel = summedAreaTable[(x + 2, y + 2)] - summedAreaTable[(x + 2, y - 1)] - summedAreaTable[(x - 1, y + 2)] + summedAreaTable[(x - 1, y - 1)]
    if powerLevel > maxPowerLevel:
        maxPowerLevel = powerLevel
        coord = (x, y)
print(*coord, sep=",")
