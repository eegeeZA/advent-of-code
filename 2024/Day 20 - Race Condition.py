import heapq
import itertools

try:
    racetrack = open("inputs/day20.txt").read()
except FileNotFoundError:
    racetrack = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""[1:]
square = len(racetrack.splitlines())
racetrack = {(i, j): cell for i, row in enumerate(racetrack.splitlines()) for j, cell in enumerate(row)}


def shortest_path(walls):
    visit_points = [(0, next(xy for xy, cell in racetrack.items() if cell == 'S'))]
    visited = {}
    while visit_points:
        cost, (x, y) = heapq.heappop(visit_points)

        if (x, y) in visited:
            continue
        visited[x, y] = cost
        if racetrack[x, y] == "E":
            return visited

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x_new, y_new = x + dx, y + dy
            if (0 <= x_new < square and 0 <= y_new < square
                    and (x_new, y_new) not in walls and (x_new, y_new) not in visited):
                heapq.heappush(visit_points, (cost + 1, (x_new, y_new)))
    return {}


costs = shortest_path({xy for xy, cell in racetrack.items() if cell == '#'})

savings2 = 0
savings20 = 0
for (x, y), (a, b) in itertools.combinations(costs, 2):
    distance = abs(a - x) + abs(b - y)
    if 1 < distance <= 2 and abs(costs[a, b] - costs[x, y]) - distance >= 100:
        savings2 += 1
    if 1 < distance <= 20 and abs(costs[a, b] - costs[x, y]) - distance >= 100:
        savings20 += 1
print("answer 1:", savings2)
print("answer 2:", savings20)
