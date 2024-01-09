try:
    maze = open("inputs/day10.txt").read().splitlines()
except FileNotFoundError:
    maze = """
...........
.F-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--S.L--J.
...........
"""[1:].splitlines()


def neighbours(x, y):
    current = maze[x][y]
    if x > 0 and (current == "S" or current == "|" or current == "L" or current == "J"):
        if maze[x - 1][y] == "|" or maze[x - 1][y] == "7" or maze[x - 1][y] == "F":
            yield x - 1, y
    if x < (len(maze) - 1) and (current == "S" or current == "|" or current == "F" or current == "7"):
        if maze[x + 1][y] == "|" or maze[x + 1][y] == "L" or maze[x + 1][y] == "J":
            yield x + 1, y
    if y > 0 and (current == "S" or current == "-" or current == "7" or current == "J"):
        if maze[x][y - 1] == "-" or maze[x][y - 1] == "L" or maze[x][y - 1] == "F":
            yield x, y - 1
    if y < (len(maze) + 1) and (current == "S" or current == "-" or current == "L" or current == "F"):
        if maze[x][y + 1] == "-" or maze[x][y + 1] == "7" or maze[x][y + 1] == "J":
            yield x, y + 1


start = [(i, j) for i in range(len(maze)) for j in range(len(maze)) if maze[i][j] == "S"][0]
first, second = list(neighbours(*start))
first = [start, first]
second = [start, second]
while first[-1] != second[-1]:
    first.append((set(neighbours(*first[-1])) - set(first)).pop())
    second.append((set(neighbours(*second[-1])) - set(second)).pop())
print("answer 1:", len(first) - 1)


def crossing_number(x, y):
    if (x, y) in loop:
        return 0

    intersections = 0
    ups = 0
    for z in range(y + 1, len(maze[x])):
        if (x, z) in loop:
            if maze[x][z] == "|" or maze[x][z] == "S":  # my 'S' is a '|'
                intersections += 1
            if maze[x][z] == "L" or maze[x][z] == "J":
                ups += 1
    return intersections + (ups % 2)


loop = first + second
inside = 0
for i in range(len(maze)):
    for j in range(len(maze)):
        if crossing_number(i, j) % 2 == 1:
            inside += 1
print("answer 2:", inside)
