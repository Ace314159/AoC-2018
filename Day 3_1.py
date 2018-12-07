import pathlib

claims = [line for line in pathlib.Path("inputs/3.txt").read_text().splitlines()]
fabric = [[0 for _ in range(1000)] for _ in range(1000)]

for claim in claims:
    claim = claim[claim.index("@") + 1:]
    pos, size = claim.split(": ")
    pos = list(map(int, pos.split(",")))
    size = list(map(int, size.split("x")))

    for i in range(pos[0], pos[0] + size[0]):
        for j in range(pos[1], pos[1] + size[1]):
            fabric[i][j] += 1

count = 0
for row in fabric:
    for i in row:
        if i >= 2:
            count += 1
print(count)
