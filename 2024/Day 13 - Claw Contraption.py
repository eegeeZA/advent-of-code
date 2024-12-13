import math
import re

try:
    puzzle = open("inputs/day13.txt").read()
except FileNotFoundError:
    puzzle = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""[1:]
puzzle = puzzle.split("\n\n")

least_tokens = 0
for layout in puzzle:
    ax, ay, bx, by, px, py = map(int, re.findall(r"(\d+)", layout))
    tokens = math.inf
    for a in range(100):
        for b in range(100):
            if a * ax + b * bx == px and a * ay + b * by == py:
                tokens = min(tokens, a * 3 + b)
    if tokens < math.inf:
        least_tokens += tokens
print("answer 1:", least_tokens)

least_tokens = 0
for layout in puzzle:
    ax, ay, bx, by, px, py = map(int, re.findall(r"(\d+)", layout))
    px += 10000000000000
    py += 10000000000000

    a = (px * by - py * bx) / (ax * by - ay * bx)
    b = (py * ax - px * ay) / (ax * by - ay * bx)

    if a.is_integer() and b.is_integer():
        least_tokens += a * 3 + b
print("answer 2:", int(least_tokens))
