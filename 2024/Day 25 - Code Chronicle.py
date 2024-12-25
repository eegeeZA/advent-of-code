import itertools

try:
    puzzle = open("inputs/day25.txt").read()
except FileNotFoundError:
    puzzle = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""[1:]
puzzle = puzzle.split("\n\n")

locks, keys = [], []
for combo in puzzle:
    combo = combo.splitlines()

    result = {}
    for x, line in enumerate(combo):
        for y, char in enumerate(line):
            result[(x, y)] = char
    if '#' in combo[0]:
        locks.append(set(k for k, v in result.items() if v == '#'))
    else:
        keys.append(set(k for k, v in result.items() if v == '#'))

print("answer 1:", sum(len(lock | key) > 0 and len(lock & key) == 0
                       for lock, key in itertools.product(locks, keys)))
print("answer 2:", "*")
