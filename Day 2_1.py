import pathlib
import collections

ids = [line for line in pathlib.Path("inputs/2.txt").read_text().splitlines()]

num2 = num3 = 0
for id in ids:
    freq = collections.defaultdict(int)
    for char in id:
        freq[char] += 1
    num2Existed = num3Existed = False
    for count in freq.values():
        if not num2Existed and count == 2:
            num2 += 1
            num2Existed = True
        elif not num3Existed and count == 3:
            num3 += 1
            num3Existed = True
print(num2 * num3)
