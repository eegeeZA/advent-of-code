import re

try:
    puzzle = open("inputs/day17.txt").read()
except FileNotFoundError:
    puzzle = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""[1:]
registers, program = puzzle.split("\n\n")
a, b, c = map(int, re.findall(r"(\d+)", registers))
program = list(map(int, re.findall(r"(\d+)", program)))


def combo(check):
    if 0 <= check <= 3:
        return check
    elif check == 4:
        return a
    elif check == 5:
        return b
    elif check == 6:
        return c


def compute(instruction_pointer=0):
    global a, b, c

    while True:
        if instruction_pointer + 2 > len(program):
            return
        opcode, operand = program[instruction_pointer:instruction_pointer + 2]

        if opcode == 0:
            a = a // pow(2, combo(operand))
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo(operand) % 8
        elif opcode == 3:
            if a != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            yield combo(operand) % 8
        elif opcode == 6:
            b = a // pow(2, combo(operand))
        elif opcode == 7:
            c = a // pow(2, combo(operand))

        instruction_pointer += 2


asdf = ",".join(map(str, list(compute())))
print("answer 1:", asdf)

history = [[]]
possible_a = []
for i, code in enumerate(reversed(program)):
    new_history = []
    while history:
        check = history.pop(0)
        for x in range(8):
            _, b, c = map(int, re.findall(r"(\d+)", registers))
            a = 0
            for j, multiple in enumerate([x] + check):
                a += pow(8, j) * multiple
            if i == len(program) - 1:
                possible_a.append(a)
            if next(compute()) == code:
                new_history.append([x] + check)
    history = new_history

for new_a in possible_a:
    _, b, c = map(int, re.findall(r"(\d+)", registers))
    a = new_a
    result = list(compute())
    if result == program:
        print("answer 2:", new_a)
        break
