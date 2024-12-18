import heapq

try:
    puzzle = open("inputs/day18.txt").read()
except FileNotFoundError:
    puzzle = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""[1:]
falling_bytes = [tuple(map(int, line.split(","))) for line in puzzle.splitlines()]


def shortest_path(x_end, y_end, walls):
    visit_points = [(0, (0, 0))]
    visited = set()
    while visit_points:
        cost, (x, y) = heapq.heappop(visit_points)
        if (x, y) == (x_end, y_end):
            return cost

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x_new, y_new = x + dx, y + dy
            if (0 <= x_new <= x_end and 0 <= y_new <= y_end
                    and (y_new, x_new) not in walls and (x_new, y_new) not in visited):
                heapq.heappush(visit_points, (cost + 1, (x_new, y_new)))
    return 0


print("answer 1:", shortest_path(70, 70, falling_bytes[:1024]))

for i in reversed(range(1024, len(falling_bytes))):
    if shortest_path(70, 70, falling_bytes[:i]):
        x_last, y_last = falling_bytes[i]
        print("answer 2:", f"{x_last},{y_last}")
        break
