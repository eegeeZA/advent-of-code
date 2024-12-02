import itertools

try:
    reports = open("inputs/day02.txt").read()
except FileNotFoundError:
    reports = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""[1:]
reports = reports.splitlines()

levels = [list(map(int, report.split())) for report in reports]

safe = 0
for level in levels:
    deltas = [i - j for i, j in itertools.pairwise(level)]
    in_range = all(1 <= abs(x) <= 3 for x in deltas)
    same_sign = all(x > 0 for x in deltas) or all(x < 0 for x in deltas)
    if in_range and same_sign:
        safe += 1
print("answer 1:", safe)

safe = 0
for level in levels:
    for skip in range(len(level)):
        deltas = [i - j for i, j in itertools.pairwise(level[:skip] + level[skip + 1:])]
        in_range = all(1 <= abs(x) <= 3 for x in deltas)
        same_sign = all(x > 0 for x in deltas) or all(x < 0 for x in deltas)
        if in_range and same_sign:
            safe += 1
            break
print("answer 2:", safe)
