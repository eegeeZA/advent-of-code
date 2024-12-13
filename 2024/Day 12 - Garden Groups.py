import collections

try:
    puzzle = open("inputs/day12.txt").read()
except FileNotFoundError:
    puzzle = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""[1:]
puzzle = puzzle.splitlines()

regions = collections.defaultdict(list)
region_inverse = collections.defaultdict(str)
for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
        regions[puzzle[row][column]].append((row, column))
        region_inverse[(row, column)] = puzzle[row][column]


def split_regions(flat_region):
    split = [[flat_region.pop()]]
    while flat_region:
        size = len(split[-1])
        for x, y in split[-1]:
            for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (x + a, y + b) in flat_region:
                    split[-1].append(flat_region.pop(flat_region.index((x + a, y + b))))
        if size == len(split[-1]):
            split.append([flat_region.pop()])
    return split


price = 0
price2 = 0
for plant in regions:
    for region in split_regions(regions[plant]):
        perimeter = 0
        for x, y in region:
            for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if region_inverse[x + a, y + b] != plant:
                    perimeter += 1
        price += len(region) * perimeter

        corners = 0
        for x, y in region:
            if (x - 1, y) not in region and (x, y - 1) not in region:
                corners += 1
            if (x - 1, y) not in region and (x, y + 1) not in region:
                corners += 1
            if (x + 1, y) not in region and (x, y - 1) not in region:
                corners += 1
            if (x + 1, y) not in region and (x, y + 1) not in region:
                corners += 1
            if (x - 1, y) in region and (x, y - 1) in region and (x - 1, y - 1) not in region:
                corners += 1
            if (x - 1, y) in region and (x, y + 1) in region and (x - 1, y + 1) not in region:
                corners += 1
            if (x + 1, y) in region and (x, y - 1) in region and (x + 1, y - 1) not in region:
                corners += 1
            if (x + 1, y) in region and (x, y + 1) in region and (x + 1, y + 1) not in region:
                corners += 1
        price2 += len(region) * corners
print("answer 1:", price)
print("answer 2:", price2)
