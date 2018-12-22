import pathlib
import collections


data = pathlib.Path("inputs/9.txt").read_text().splitlines()[0].split(" ")
numPlayers = int(data[0])
numMarbles = int(data[6]) * 100

scores = collections.defaultdict(int)
circle = collections.deque([0])
for marble in range(1, numMarbles + 1):
    if marble % 23 == 0:
        circle.rotate(7)
        scores[marble % numPlayers] += marble + circle.popleft()
    else:
        circle.rotate(-2)
        circle.appendleft(marble)

print(max(scores.values()))
