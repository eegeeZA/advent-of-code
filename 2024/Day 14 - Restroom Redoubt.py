import itertools
import math
import re

try:
    puzzle = open("inputs/day14.txt").read()
except FileNotFoundError:
    puzzle = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""[1:]
puzzle = puzzle.splitlines()

positions = []
velocities = []

for line in puzzle:
    px, py, vx, vy = re.findall(r"(-?\d+)", line)
    positions.append((int(px), int(py)))
    velocities.append((int(vx), int(vy)))

width = 101
height = 103
for _ in range(100):
    for i in range(len(positions)):
        x, y = positions[i]
        vx, vy = velocities[i]
        positions[i] = ((x + vx) % width, (y + vy) % height)
quadrants = [0] * 4
for x, y in positions:
    quadrants[0] += 1 if x < width // 2 and y < height // 2 else 0
    quadrants[1] += 1 if x > width // 2 and y < height // 2 else 0
    quadrants[2] += 1 if x < width // 2 and y > height // 2 else 0
    quadrants[3] += 1 if x > width // 2 and y > height // 2 else 0
print("answer 1:", math.prod(quadrants))

for easter_egg in itertools.count(1):
    for i in range(len(positions)):
        x, y = positions[i]
        vx, vy = velocities[i]
        positions[i] = ((x + vx) % width, (y + vy) % height)
    if all((x, y) in positions for x, y in zip(range(42, 50), range(42, 50))):
        break
print("answer 2:", 100 + easter_egg)
