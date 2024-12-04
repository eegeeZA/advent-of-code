import collections

try:
    puzzle = open("inputs/day04.txt").read()
except FileNotFoundError:
    puzzle = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""[1:]
puzzle = puzzle.splitlines()


def matches(letters, i, j, a, b, path=None):
    if path is None:
        path = []
    if not letters:
        return path
    if (0 <= i < len(puzzle)) and (0 <= j < len(puzzle[i])):
        if puzzle[i][j] == letters.pop(0):
            return matches(letters.copy(), i + a, j + b, a, b, path + [(i, j)])
    return None


total = 0
for direction in {(i, j) for j in range(-1, 2) for i in range(-1, 2) if (i, j) != (0, 0)}:
    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            if matches(list("XMAS"), row, column, *direction):
                total += 1
print("answer 1:", total)

choices = collections.defaultdict(int)
for direction in {(-1, -1), (1, 1), (-1, 1), (1, -1)}:
    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            match = matches(list("MAS"), row, column, *direction)
            if match:
                choices[match[1]] += 1
print("answer 2:", sum(True for x in choices.values() if x == 2))
