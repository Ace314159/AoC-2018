import pathlib

ids = [line for line in pathlib.Path("inputs/2.txt").read_text().splitlines()]

done = False
for id1 in ids:
    for id2 in ids:
        numDifferent = 0
        final = []
        for i, char in enumerate(id1):
            if char != id2[i]:
                numDifferent += 1
            else:
                final.append(char)
            if numDifferent > 1:
                break
        if numDifferent == 1:
            print("".join(final))
            done = True
            break
    if done:
        break
