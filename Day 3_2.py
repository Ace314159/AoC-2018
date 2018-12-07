import pathlib

claims = [line for line in pathlib.Path("inputs/3.txt").read_text().splitlines()]
fabric = [[set() for _ in range(1000)] for _ in range(1000)]

notOverlapped = {}
for claim in claims:
    claimNum, claim = claim[1:].split(" @ ")
    pos, size = claim.split(": ")
    pos = list(map(int, pos.split(",")))
    size = list(map(int, size.split("x")))
    notOverlapped[claimNum] = True

    for i in range(pos[0], pos[0] + size[0]):
        for j in range(pos[1], pos[1] + size[1]):
            fabric[i][j].add(claimNum)
            if len(fabric[i][j]) > 1:
                for num in fabric[i][j]:
                    notOverlapped[num] = False

for key, value in notOverlapped.items():
    if value:
        print(key)
        break
