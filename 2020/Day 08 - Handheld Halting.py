instructions = []
for instruction in open("inputs/day08.txt"):
    operation, number = instruction.split()
    instructions.append((operation, int(number)))


def exit_value():
    visited = []
    index = 0
    global accumulator
    accumulator = 0
    while index not in visited:
        visited.append(index)
        operation, number = instructions[index]
        if operation == "acc":
            accumulator += number
            index += 1
        if operation == "jmp":
            index += number
        if operation == "nop":
            index += 1
    return accumulator


print("answer 1:", exit_value())

original = instructions.copy()
for i, (operation, number) in enumerate(original):
    instructions = original.copy()
    if operation == "nop":
        instructions[i] = ("jmp", number)
    if operation == "jmp":
        instructions[i] = ("nop", number)
    try:
        exit_value()
    except:
        print("answer 2:", accumulator)
