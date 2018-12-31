import pathlib

lines = pathlib.Path("inputs/16.txt").read_text().splitlines()
end = 0
t = 0
before = instr = after = None
samples = []
for i, line in enumerate(lines):
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

allPossibilities = {i: set() for i in range(16)}

for sample in samples:
    before, instr, after = sample
    opcode, A, B, C = instr
    oPossibilities = allPossibilities[opcode]
    # Addition
    if after[C] == before[A] + before[B]:  # addr
        oPossibilities.add(0)
    if after[C] == before[A] + B:  # addi
        oPossibilities.add(1)
    # Multiplication
    if after[C] == before[A] * before[B]:  # mulr
        oPossibilities.add(2)
    if after[C] == before[A] * B:  # muli
        oPossibilities.add(3)
    # Bitwise AND
    if after[C] == (before[A] & before[B]):  # banr
        oPossibilities.add(4)
    if after[C] == (before[A] & B):  # bani
        oPossibilities.add(5)
    # Bitwise OR
    if after[C] == (before[A] | before[B]):  # borr
        oPossibilities.add(6)
    if after[C] == (before[A] | B):  # bori
        oPossibilities.add(7)
    # Assignment
    if after[C] == before[A]:  # setr
        oPossibilities.add(8)
    if after[C] == A:  # seti
        oPossibilities.add(9)
    # Greater-than testing
    if after[C] == (A > before[B]):  # gtir
        oPossibilities.add(10)
    if after[C] == (before[A] > B):  # gtri
        oPossibilities.add(11)
    if after[C] == (before[A] > before[B]):  # gtrr
        oPossibilities.add(12)
    # Equality testing
    if after[C] == (A == before[B]):  # eqir
        oPossibilities.add(13)
    if after[C] == (before[A] == B):  # eqri
        oPossibilities.add(14)
    if after[C] == (before[A] == before[B]):  # eqrr
        oPossibilities.add(15)

mapping = {}

while len(mapping) < 16:
    for opcode, possibilities in list(allPossibilities.items()):
        if opcode not in allPossibilities:
            continue
        if len(possibilities) == 1:
            mapping[opcode] = possibilities.pop()
            del allPossibilities[opcode]
            for p in allPossibilities.values():
                p.discard(mapping[opcode])

program = []
for line in lines[i + 1:]:
    program.append(tuple(map(int, line.split(" "))))


registers = [0, 0, 0, 0]

for instr in program:
    opcode, A, B, C = instr
    action = mapping[opcode]
    if action == 0:  # addr
        registers[C] = registers[A] + registers[B]
    if action == 1:  # addi
        registers[C] = registers[A] + B
    # Multiplication
    if action == 2:  # mulr
        registers[C] = registers[A] * registers[B]
    if action == 3:  # muli
        registers[C] = registers[A] * B
    # Bitwise AND
    if action == 4:  # banr
        registers[C] = (registers[A] & registers[B])
    if action == 5:  # bani
        registers[C] = (registers[A] & B)
    # Bitwise OR
    if action == 6:  # borr
        registers[C] = (registers[A] | registers[B])
    if action == 7:  # bori
        registers[C] = (registers[A] | B)
    # Assignment
    if action == 8:  # setr
        registers[C] = registers[A]
    if action == 9:  # seti
        registers[C] = A
    # Greater-than testing
    if action == 10:  # gtir
        registers[C] = A > registers[B]
    if action == 11:  # gtri
        registers[C] = registers[A] > B
    if action == 12:  # gtrr
        registers[C] = registers[A] > registers[B]
    # Equality testing
    if action == 13:  # eqir
        registers[C] = int(A == registers[B])
    if action == 14:  # eqri
        registers[C] = int(registers[A] == B)
    if action == 15:  # eqrr
        registers[C] = int(registers[A] == registers[B])

print(registers[0])
