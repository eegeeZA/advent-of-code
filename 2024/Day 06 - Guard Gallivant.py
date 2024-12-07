import itertools

try:
    layout = open("inputs/day06.txt").read()
except FileNotFoundError:
    layout = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""[1:]
layout = layout.splitlines()

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
reverse = {'^': '<', '>': '^', 'v': '>', '<': 'v'}

x, y = next((x, y) for x, _ in enumerate(layout) for y, point in enumerate(layout[x]) if point == "^")
compass = itertools.cycle(directions)

visited = set()
direction = next(compass)
while True:
    a, b = directions[direction]
    x, y = x + a, y + b
    if not ((0 <= x < len(layout)) and (0 <= y < len(layout[x]))):
        break
    if layout[x][y] != "#":
        visited.add((x, y))
    else:
        x, y = x - a, y - b
        direction = next(compass)
print("answer 1:", len(visited))

obstructions = 0
x_original, y_original = next((x, y) for x, _ in enumerate(layout) for y, point in enumerate(layout[x]) if point == "^")
for i, j in visited:
    visited2 = []
    x, y = x_original, y_original
    compass = itertools.cycle(directions)
    direction = next(compass)
    while True:
        a, b = directions[direction]
        x, y = x + a, y + b
        if (direction, x, y) in visited2:
            obstructions += 1
            break
        if not ((0 <= x < len(layout)) and (0 <= y < len(layout[x]))):
            break
        if layout[x][y] != "#" and (x != i or y != j):
            visited2.append((direction, x, y))
        else:
            x, y = x - a, y - b
            direction = next(compass)
print("answer 2:", obstructions)
