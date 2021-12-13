import collections

instructions = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
instructions = open("inputs/day13.txt").read()

dots_raw, folds_raw = instructions.split("\n\n")
dots = collections.defaultdict(bool)
for dot in dots_raw.splitlines():
    dots[tuple(map(int, dot.split(",")))] = True

first_fold = None
for fold_instruction in folds_raw.splitlines():
    fold, line = fold_instruction[11:].split("=")
    line = int(line)

    for x, y in list(dots.keys()):
        if fold == "x" and x > line:
            dots[line - (x - line), y] |= True
            del dots[x, y]
        if fold == "y" and y > line:
            dots[x, line - (y - line)] |= True
            del dots[x, y]

    if first_fold is None:
        first_fold = len(dots)

print("answer 1:", first_fold)
print("answer 2:")
for y in range(max(y for x, y in dots.keys()) + 1):
    for x in range(max(x for x, y in dots.keys()) + 1):
        print("█" if dots[x, y] else " ", end="")
    print()
