import itertools

try:
    image = open("inputs/day11.txt").read().splitlines()
except FileNotFoundError:
    image = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""[1:].splitlines()

galaxies = []
rows = set(range(len(image)))
columns = set(range(len(image[0])))
for i, row in enumerate(image):
    for j, column in enumerate(row):
        if column == "#":
            galaxies.append((i, j))
            rows -= {i}
            columns -= {j}

galaxies1 = galaxies.copy()
for expanse in reversed(sorted(rows)):
    for i, (row, column) in enumerate(galaxies1):
        if row > expanse:
            galaxies1[i] = (row + 2 - 1, column)
for expanse in reversed(sorted(columns)):
    for i, (row, column) in enumerate(galaxies1):
        if column > expanse:
            galaxies1[i] = (row, column + 2 - 1)
print("answer 1:", sum(abs(a - x) + abs(b - y) for (a, b), (x, y) in itertools.combinations(galaxies1, 2)))

galaxies2 = galaxies.copy()
for expanse in reversed(sorted(rows)):
    for i, (row, column) in enumerate(galaxies2):
        if row > expanse:
            galaxies2[i] = (row + 1000000 - 1, column)
for expanse in reversed(sorted(columns)):
    for i, (row, column) in enumerate(galaxies2):
        if column > expanse:
            galaxies2[i] = (row, column + 1000000 - 1)
print("answer 2:", sum(abs(a - x) + abs(b - y) for (a, b), (x, y) in itertools.combinations(galaxies2, 2)))
