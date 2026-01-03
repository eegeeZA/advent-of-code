import math

try:
    math_homework = open("inputs/day06.txt").read()
except FileNotFoundError:
    math_homework = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""[1:]
math_homework = math_homework.splitlines()

lines = [list(map(int, line.split())) for line in math_homework[:-1]]
total = 0
for i, operation in enumerate(math_homework[-1].split()):
    if operation == "+":
        total += sum(line[i] for line in lines)
    elif operation == "*":
        prod = 1
        for line in lines:
            prod *= line[i]
        total += prod
print("answer 1:", total)

max_length = [0] * len(math_homework[-1].split())
for line in math_homework[:-1]:
    for i, num in enumerate(line.split()):
        max_length[i] = max(max_length[i], len(num))
lines = [['' for y in range(x)] for x in max_length]
for line in math_homework[:-1]:
    offset = 0
    for i, length in enumerate(max_length):
        columns = []
        for j in range(length):
            columns.append(line[j + offset])
        offset += length + 1
        lines[i] = ["".join(x) for x in zip(lines[i], columns)]
total = 0
for i, operation in enumerate(math_homework[-1].split()):
    if operation == "+":
        total += sum(map(int, lines[i]))
    elif operation == "*":
        total += math.prod(map(int, lines[i]))
print("answer 2:", total)
