import itertools
import re

try:
    puzzle = open("inputs/day07.txt").read()
except FileNotFoundError:
    puzzle = """
1: 10 20 30
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""[1:]
puzzle = puzzle.splitlines()


class SwitchPrecedence(int):
    def __truediv__(self, other):
        return SwitchPrecedence(int(self) + other)

    def __mul__(self, other):
        return SwitchPrecedence(int(self) * other)

    def __mod__(self, other):
        return SwitchPrecedence(str(self) + str(other))


calibration = 0
calibration2 = 0
for line in puzzle:
    total, parts = line.split(": ")
    parts = parts.split()
    for operator in itertools.product('+*', repeat=len(parts) - 1):
        answer = "".join([item for tup in zip(parts, operator) for item in tup]) + parts[-1]
        answer = re.sub(r"(\d+)", r"\1)", answer)
        answer = "(" * answer.count(")") + answer
        if int(total) == eval(answer):
            calibration += int(total)
            break
    else:
        for operator in itertools.product('/*%', repeat=len(parts) - 1):
            answer = "".join([item for tup in zip(parts, operator) for item in tup]) + parts[-1]
            answer = re.sub(r"(\d+)", r"SwitchPrecedence(\1)", answer)
            if int(total) == eval(answer):
                calibration2 += int(total)
                break

print("answer 1:", calibration)
print("answer 2:", calibration + calibration2)
