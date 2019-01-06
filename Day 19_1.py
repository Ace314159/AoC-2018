import pathlib

lines = pathlib.Path("inputs/19.txt").read_text().splitlines()

registers = [0 for _ in range(6)]
ip = int(lines.pop(0)[4])
registers[ip] = 10

instrs = [(line.split(" ")[0], *map(int, line.split(" ")[1:])) for line in lines]

while 0 <= registers[ip] < len(instrs):
    instr = instrs[registers[ip]]
    print(instr)
    opcode, A, B, C = instr
    # Addition
    if opcode == "addr":
        registers[C] = registers[A] + registers[B]
    if opcode == "addi":
        registers[C] = registers[A] + B
    # Multiplication
    if opcode == "mulr":
        registers[C] = registers[A] * registers[B]
    if opcode == "muli":
        registers[C] = registers[A] * B
    # Bitwise AND
    if opcode == "banr":
        registers[C] = (registers[A] & registers[B])
    if opcode == "bani":
        registers[C] = (registers[A] & B)
    # Bitwise OR
    if opcode == "borr":
        registers[C] = (registers[A] | registers[B])
    if opcode == "bori":
        registers[C] = (registers[A] | B)
    # Assignment
    if opcode == "setr":
        registers[C] = registers[A]
    if opcode == "seti":
        registers[C] = A
    # Greater-than testing
    if opcode == "gtir":
        registers[C] = A > registers[B]
    if opcode == "gtri":
        registers[C] = registers[A] > B
    if opcode == "gtrr":
        registers[C] = registers[A] > registers[B]
    # Equality testing
    if opcode == "eqir":
        registers[C] = int(A == registers[B])
    if opcode == "eqri":
        registers[C] = int(registers[A] == B)
    if opcode == "eqrr":
        registers[C] = int(registers[A] == registers[B])
    registers[ip] += 1
    print(registers)
    input()

print(registers[0])
