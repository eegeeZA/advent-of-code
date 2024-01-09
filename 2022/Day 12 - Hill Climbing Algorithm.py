import collections
import math

try:
    heightmap = open("inputs/day12.txt").read().splitlines()
except FileNotFoundError:
    heightmap = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""[1:].splitlines()


def can_reach(current, neighbour):
    return ord(neighbour) - ord(current) <= 1


start = end = None
routes = collections.defaultdict(list)
starts = []
for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if height == "S":
            start = (i, j)
            heightmap[i] = heightmap[i].replace("S", "a")
        if height == "E":
            end = (i, j)
            heightmap[i] = heightmap[i].replace("E", "z")
        if height == "a":
            starts.append((i, j))
for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if i > 0 and can_reach(height, heightmap[i - 1][j]):
            routes[i, j].append((i - 1, j))
        if j > 0 and can_reach(height, heightmap[i][j - 1]):
            routes[i, j].append((i, j - 1))
        if i < len(heightmap) - 1 and can_reach(height, heightmap[i + 1][j]):
            routes[i, j].append((i + 1, j))
        if j < len(row) - 1 and can_reach(height, heightmap[i][j + 1]):
            routes[i, j].append((i, j + 1))

steps = {key: math.inf for key in routes.keys()}
steps[start] = 0
for route in starts:
    steps[route] = 0


def dijkstra(routes, steps):
    while routes:
        next_step = min(routes.keys(), key=lambda x: steps[x])
        if next_step == end:
            return steps[next_step]
        neighbours = routes.pop(next_step)

        for neighbour in neighbours:
            if neighbour not in routes:
                continue
            distance = steps[next_step] + 1
            if distance < steps[neighbour]:
                steps[neighbour] = distance


steps = {key: math.inf for key in routes.keys()}
steps[start] = 0
print("answer 1:", dijkstra(routes.copy(), steps.copy()))
for route in starts:
    steps[route] = 0
print("answer 2:", dijkstra(routes.copy(), steps))
