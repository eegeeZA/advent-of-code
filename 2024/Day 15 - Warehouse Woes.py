try:
    puzzle = open("inputs/day15.txt").read()
except FileNotFoundError:
    puzzle = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""[1:]
grid, instructions = puzzle.split("\n\n")
grid = [list(row) for row in grid.splitlines()]
instructions = instructions.replace("\n", "")
x, y = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '@')
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def move(x, y, dx, dy):
    if grid[x + dx][y + dy] == '.':
        switch(x, y, dx, dy)
        return True
    elif grid[x + dx][y + dy] in ['O', '[', ']']:
        if move(x + dx, y + dy, dx, dy):
            switch(x, y, dx, dy)
            return True
    return False


def switch(x, y, dx, dy):
    grid[x][y], grid[x + dx][y + dy] = grid[x + dx][y + dy], grid[x][y]


for instruction in instructions:
    dx, dy = directions[instruction]
    if move(x, y, dx, dy):
        x, y = x + dx, y + dy
print("answer 1:", sum(100 * i + j for i, row in enumerate(grid) for j, cell in enumerate(grid[i]) if cell == 'O'))


def can_move(x, y, dx, dy):
    if dx == 0:
        return move(x, y, dx, dy)
    if grid[x + dx][y + dy] == '.':
        return True
    elif grid[x + dx][y + dy] == '[':
        if can_move(x + dx, y + dy, dx, dy) and can_move(x + dx, y + dy + 1, dx, dy):
            return True
    elif grid[x + dx][y + dy] == ']':
        if can_move(x + dx, y + dy, dx, dy) and can_move(x + dx, y + dy - 1, dx, dy):
            return True
    return False


def move2(x, y, dx, dy):
    if dx == 0:
        return True
    x, y = x + dx, y + dy
    if grid[x][y] == '.':
        return True
    elif grid[x][y] == '[':
        if move2(x, y, dx, dy) and move2(x, y + 1, dx, dy):
            move(x, y, dx, dy)
            move(x, y + 1, dx, dy)
            return True
    elif grid[x][y] == ']':
        if move2(x, y, dx, dy) and move2(x, y - 1, dx, dy):
            move(x, y, dx, dy)
            move(x, y - 1, dx, dy)
            return True
    return False


grid, _ = puzzle.split("\n\n")
translation = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
grid = [sum([translation[cell] for cell in list(row)], []) for row in grid.splitlines()]
x, y = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '@')
for instruction in instructions:
    dx, dy = directions[instruction]
    if can_move(x, y, dx, dy):
        move2(x, y, dx, dy)
        if dx != 0:
            switch(x, y, dx, dy)
        x, y = x + dx, y + dy
print("answer 2:", sum(100 * i + j for i, row in enumerate(grid) for j, cell in enumerate(grid[i]) if cell == '['))
