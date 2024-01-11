try:
    patterns = open("inputs/day13.txt").read().split("\n\n")
except FileNotFoundError:
    patterns = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""[1:].split("\n\n")

summarize = 0

for pattern in patterns:
    horizontal = pattern.splitlines()
    for size in range(1, len(horizontal) // 2 + 1):
        if horizontal[:size] == horizontal[size:size * 2][::-1]:
            summarize += 100 * size
        if horizontal[-size:] == horizontal[-size * 2:-size][::-1]:
            summarize += 100 * (len(horizontal) - size)

    vertical = list(zip(*horizontal))
    for size in range(1, len(vertical) // 2 + 1):
        if vertical[:size] == vertical[size:size * 2][::-1]:
            summarize += size
        if vertical[-size:] == vertical[-size * 2:-size][::-1]:
            summarize += len(vertical) - size
print("answer 1:", summarize)


def one_smudge(left, right):
    smudges = 0
    for left_line, right_line in zip(left, right):
        for a, b in zip(left_line, right_line):
            if a != b:
                smudges += 1
    return smudges == 1


summarize = 0
for pattern in patterns:
    horizontal = pattern.splitlines()
    for size in range(1, len(horizontal) // 2 + 1):
        if one_smudge(horizontal[:size], horizontal[size:size * 2][::-1]):
            summarize += 100 * size
        if one_smudge(horizontal[-size:], horizontal[-size * 2:-size][::-1]):
            summarize += 100 * (len(horizontal) - size)

    vertical = list(zip(*horizontal))
    for size in range(1, len(vertical) // 2 + 1):
        if one_smudge(vertical[:size], vertical[size:size * 2][::-1]):
            summarize += size
        if one_smudge(vertical[-size:], vertical[-size * 2:-size][::-1]):
            summarize += len(vertical) - size
print("answer 2:", summarize)
