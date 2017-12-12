instructions_input = open("inputs/day05.txt").readlines()
instructions = list(map(int, instructions_input))
i = 0
steps = 0
while i < len(instructions):
    steps += 1
    next_i = instructions[i]
    instructions[i] += 1
    i += next_i
print("answer 1:", steps)

instructions = list(map(int, instructions_input))
i = 0
steps = 0
while i < len(instructions):
    steps += 1
    next_i = instructions[i]
    if instructions[i] >= 3:
        instructions[i] -= 1
    else:
        instructions[i] += 1
    i += next_i
print("answer 2:", steps)
