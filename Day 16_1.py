import pathlib

lines = pathlib.Path("inputs/16.txt").read_text().splitlines()
end = 0
t = 0
before = instr = after = None
samples = []
for line in lines:
    if line == "":
        end += 1
    else:
        end = 0
    if end >= 3:
        break
    if end > 0:
        continue

    if t == 0:
        before = list(map(int, line[9:19].split(", ")))
        t += 1
    elif t == 1:
        instr = tuple(map(int, line.split(" ")))
        t += 1
    else:
        after = list(map(int, line[9:19].split(", ")))
        samples.append((before, instr, after))
        t = 0

num = 0
for sample in samples:
    count = 0
    before, instr, after = sample
    opcode, A, B, C = instr
    # Addition
    if after[C] == before[A] + before[B]:  # addr
        count += 1
    if after[C] == before[A] + B:  # addi
        count += 1
    # Multiplication
    if after[C] == before[A] * before[B]:  # mulr
        count += 1
    if after[C] == before[A] * B:  # muli
        count += 1
    # Bitwise AND
    if after[C] == (before[A] & before[B]):  # banr
        count += 1
    if after[C] == (before[A] & B):  # bani
        count += 1
    # Bitwise OR
    if after[C] == (before[A] | before[B]):  # borr
        count += 1
    if after[C] == (before[A] | B):  # bori
        count += 1
    # Assignment
    if after[C] == before[A]:  # setr
        count += 1
    if after[C] == A:  # seti
        count += 1
    # Greater-than testing
    if after[C] == (A > before[B]):  # gtir
        count += 1
    if after[C] == (before[A] > B):  # gtri
        count += 1
    if after[C] == (before[A] > before[B]):  # gtrr
        count += 1
    # Equality testing
    if after[C] == (A == before[B]):  # eqir
        count += 1
    if after[C] == (before[A] == B):  # eqri
        count += 1
    if after[C] == (before[A] == before[B]):  # eqrr
        count += 1

    if count >= 3:
        num += 1

print(num)
