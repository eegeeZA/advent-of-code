import functools

try:
    puzzle = open("inputs/day19.txt").read()
except FileNotFoundError:
    puzzle = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""[1:]
patterns, designs = puzzle.split("\n\n")
patterns = patterns.split(", ")


@functools.cache
def design_possible(design):
    if not design:
        return 1
    possible = 0
    for split in range(1, len(design) + 1):
        if design[:split] in patterns:
            possible += design_possible(design[split:])
    return possible


print("answer 1:", sum(design_possible(design) > 0 for design in designs.split()))
print("answer 2:", sum(design_possible(design) for design in designs.split()))
