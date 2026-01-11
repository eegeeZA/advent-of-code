try:
    prezzies = open("inputs/day12.txt").read()
except FileNotFoundError:
    prezzies = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""[1:]
prezzies = prezzies.split("\n\n")


def normalize(coordinates):
    min_x, min_y = min(x for x, y in coordinates), min(y for x, y in coordinates)
    return tuple(sorted((x - min_x, y - min_y) for x, y in coordinates))


def get_orientations(coordinates):
    orientations = set()
    current = coordinates
    for _ in range(4):
        orientations.add(normalize(current))
        current = [(y, -x) for x, y in current]
    current = [(x, max(y for x, y in coordinates) - y) for x, y in coordinates]
    for _ in range(4):
        orientations.add(normalize(current))
        current = [(y, -x) for x, y in current]
    return [list(orientation) for orientation in orientations]


def backtrack(id, grid, width, height, shape_list, orientations):
    if id == len(shape_list):
        return True

    shape_id = shape_list[id]
    for orientation in orientations[shape_id]:
        max_x, max_y = max(x for x, y in orientation), max(y for x, y in orientation)

        for x1 in range(height - max_x):
            for y1 in range(width - max_y):
                if all(not grid[x1 + x2][y1 + y2] for x2, y2 in orientation):
                    for dr, dc in orientation:
                        grid[x1 + dr][y1 + dc] = id + 1

                    if backtrack(id + 1, grid, width, height, shape_list, orientations):
                        return True

                    for dr, dc in orientation:
                        grid[x1 + dr][y1 + dc] = 0

    return False


def solve(width, height, shape_list):
    if sum(len(presents[s]) for s in shape_list) > width * height:
        return False

    grid = [[0] * width for _ in range(height)]
    shape_list_sorted = sorted(shape_list, key=lambda s: -len(presents[s]))
    orientations = {shape_id: get_orientations(presents[shape_id]) for shape_id in set(shape_list_sorted)}

    return backtrack(0, grid, width, height, shape_list_sorted, orientations)


presents = {}
regions = []

for section in prezzies[:-1]:
    lines = section.split("\n")
    present_id, *present = lines
    presents[int(present_id.rstrip(":"))] = [(i, j) for i, line in enumerate(present)
                                             for j, char in enumerate(line)
                                             if char == '#']

for line in prezzies[-1].rstrip().split("\n"):
    size, counts = line.split(":")
    width, height = map(int, size.split("x"))
    regions.append((width, height, list(map(int, counts.split()))))


results = []
for w, h, counts in regions:
    shape_list = [shape_id for shape_id, quantity in enumerate(counts) for _ in range(quantity)]
    result = solve(w, h, shape_list)
    results.append(result)

total = sum(results)

print("answer 1:", total)
print("answer 2:", "*")
