import collections
import re

schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""[1:].splitlines()
schematic = open("inputs/day03.txt").read().splitlines()

adjacent = 0
gears = collections.defaultdict(list)
for i, line in enumerate(schematic):
    top = max(0, i - 1)
    bottom = min(len(schematic) - 1, i + 1) + 1
    for m in re.finditer(r"\d+", line):
        start = max(0, m.start() - 1)
        end = min(len(line), m.end() + 1)
        if any(re.search(r"[^.\d]", schematic[x][start:end]) for x in range(top, bottom)):
            adjacent += int(m.group(0))
        if any(re.search(r"\*", schematic[x][start:end]) for x in range(top, bottom)):
            gears[i].append((set(range(*m.span())), int(m.group(0))))
print("answer 1:", adjacent)

ratio = 0
for i, line in enumerate(schematic):
    top = max(0, i - 1)
    bottom = min(len(schematic) - 1, i + 1) + 1
    for m in re.finditer(r"\*", line):
        start = max(0, m.start() - 1)
        end = min(len(line), m.end() + 1)
        if 2 == sum(len(re.findall(r"\d+", schematic[x][start:end])) for x in range(top, bottom)):
            gear_ratio = 1
            for j in range(top, bottom):
                for indices, gear in gears[j]:
                    if indices.intersection(range(start, end)):
                        gear_ratio *= gear
            ratio += gear_ratio
print("answer 2:", ratio)
