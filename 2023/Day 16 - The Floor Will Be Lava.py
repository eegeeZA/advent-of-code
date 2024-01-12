import sys

try:
    platform = open("inputs/day16.txt").read().splitlines()
except FileNotFoundError:
    platform = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""[1:].splitlines()


def energise(x, y, delta_x, delta_y):
    energised[x][y] = True
    x += delta_x
    y += delta_y
    if not visited:
        x -= delta_x
        y -= delta_y

    if x < 0 or x >= len(platform) or y < 0 or y >= len(platform):
        return
    if (x, y, delta_x, delta_y) in visited:
        return
    visited.append((x, y, delta_x, delta_y))

    if platform[x][y] == ".":
        energise(x, y, delta_x, delta_y)
    if platform[x][y] == "/":
        if delta_y > 0:
            energise(x, y, -1, 0)
        if delta_y < 0:
            energise(x, y, 1, 0)
        if delta_x > 0:
            energise(x, y, 0, -1)
        if delta_x < 0:
            energise(x, y, 0, 1)
    if platform[x][y] == "\\":
        if delta_y > 0:
            energise(x, y, 1, 0)
        if delta_y < 0:
            energise(x, y, -1, 0)
        if delta_x > 0:
            energise(x, y, 0, 1)
        if delta_x < 0:
            energise(x, y, 0, -1)
    if platform[x][y] == "-":
        if delta_y != 0:
            energise(x, y, delta_x, delta_y)
        else:
            energise(x, y, 0, -1)
            energise(x, y, 0, 1)
    if platform[x][y] == "|":
        if delta_x != 0:
            energise(x, y, delta_x, delta_y)
        else:
            energise(x, y, -1, 0)
            energise(x, y, 1, 0)


sys.setrecursionlimit(10000)  # （⊙ｏ⊙） #

visited = []
energised = [[False] * len(platform) for _ in range(len(platform))]
energise(0, 0, 0, 1)
print("answer 1:", sum(sum(energised, [])))

max_energised = 0
for a in range(len(platform)):
    for b in range(len(platform)):
        if a != 0 and b != 0:
            continue

        if a == 0:
            visited = []
            energised = [[False] * len(platform) for _ in range(len(platform))]
            energise(0, b, 1, 0)
            max_energised = max(max_energised, sum(sum(energised, [])))
            visited = []
            energised = [[False] * len(platform) for _ in range(len(platform))]
            energise(len(platform) - 1, b, -1, 0)
            max_energised = max(max_energised, sum(sum(energised, [])))

        if b == 0:
            visited = []
            energised = [[False] * len(platform) for _ in range(len(platform))]
            energise(a, 0, 0, 1)
            max_energised = max(max_energised, sum(sum(energised, [])))
            visited = []
            energised = [[False] * len(platform) for _ in range(len(platform))]
            energise(a, len(platform) - 1, 0, -1)
            max_energised = max(max_energised, sum(sum(energised, [])))
print("answer 2:", max_energised)
