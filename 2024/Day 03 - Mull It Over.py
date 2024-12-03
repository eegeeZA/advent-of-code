import re

try:
    memory = open("inputs/day03.txt").read()
except FileNotFoundError:
    memory = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""[1:]
memory = memory.splitlines()

total = 0
for line in memory:
    operations = re.findall(r"mul\((\d+),(\d+)\)", line)
    for x, y in operations:
        total += int(x) * int(y)
print("answer 1:", total)

total = 0
do = True
for line in memory:
    operations = re.findall(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", line)
    for action, x, y, yes, no in operations:
        if action and do:
            total += int(x) * int(y)
        if yes:
            do = True
        if no:
            do = False
print("answer 2:", total)
