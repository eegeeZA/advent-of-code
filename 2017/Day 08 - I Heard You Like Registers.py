instructions = open("inputs/day08.txt")
registers = {}
temp_largest = 0
for instruction in instructions:
    register, action, amount, _, check, operator, value = instruction.split()
    if register not in registers:
        registers[register] = 0
    if check not in registers:
        registers[check] = 0
    if eval(str(registers[check]) + operator + value):
        if action == "inc":
            registers[register] += int(amount)
        else:
            registers[register] -= int(amount)
    temp_largest = max(temp_largest, registers[register])
largest = 0
for k, v in registers.items():
    largest = max(largest, v)
print("answer 1:", largest)
print("answer 2:", temp_largest)
