import math

heightmap = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]
heightmap = open("inputs/day09.txt").read().splitlines()

low_points = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        height = int(heightmap[i][j])
        top = i == 0 or height < int(heightmap[i - 1][j])
        bottom = i + 1 == len(heightmap) or height < int(heightmap[i + 1][j])
        left = j == 0 or height < int(heightmap[i][j - 1])
        right = j + 1 == len(heightmap[i]) or height < int(heightmap[i][j + 1])
        if top and bottom and left and right:
            low_points.append((i, j))


def basin_size(row, column, visited=None):
    if visited is None:
        visited = []
    if (row, column) in visited:
        return 0
    visited.append((row, column))
    if int(heightmap[row][column]) == 9:
        return 0

    size = 1
    if row > 0:
        size += basin_size(row - 1, column, visited)
    if row + 1 < len(heightmap):
        size += basin_size(row + 1, column, visited)
    if column > 0:
        size += basin_size(row, column - 1, visited)
    if column + 1 < len(heightmap[row]):
        size += basin_size(row, column + 1, visited)
    return size


print("answer 1:", sum(1 + int(heightmap[i][j]) for i, j in low_points))
print("answer 2:", math.prod(sorted((basin_size(i, j) for i, j in low_points), reverse=True)[:3]))
