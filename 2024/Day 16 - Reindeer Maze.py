import collections
import heapq

try:
    puzzle = open("inputs/day16.txt").read()
except FileNotFoundError:
    puzzle = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""[1:]
grid = puzzle.splitlines()
start = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(grid[i]) if cell == 'S')
end = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(grid[i]) if cell == 'E')
directions = [('N', (-1, 0)), ('E', (0, 1)), ('S', (1, 0)), ('W', (0, -1))]

checklist = [(0, 'E', start)]
scores = collections.defaultdict(list)
scores[start] = [0]
visited = set()
while checklist:
    cost, facing, (x, y) = heapq.heappop(checklist)

    if (facing, (x, y)) in visited:
        continue
    visited.add((facing, (x, y)))

    for direction, (dx, dy) in directions:
        x_new, y_new = x + dx, y + dy
        if grid[x_new][y_new] != "#" and (direction, (x_new, y_new)) not in visited:
            new_cost = cost + (1 if direction == facing else 1000 + 1)
            if not scores[(x_new, y_new)]:
                scores[x_new, y_new] = [new_cost]
            elif new_cost < max(scores[(x_new, y_new)]):
                scores[x_new, y_new] = [new_cost]
                scores[x, y] = [cost]
            elif new_cost == max(scores[(x_new, y_new)]):
                scores[x_new, y_new] = [new_cost]
                scores[x, y].append(cost)
            heapq.heappush(checklist, (new_cost, direction, (x_new, y_new)))
print("answer 1:", min(scores[end]))


def count_neighbours(x, y, visited=None):
    if visited is None:
        visited = []
    nodes = {(x, y)}
    for _, (dx, dy) in directions:
        x_new, y_new = x + dx, y + dy
        if any((previous - score) in [1, 1000 + 1] for previous in scores[x, y] for score in scores[x_new, y_new]):
            nodes.add((x_new, y_new))
            if (x_new, y_new) not in visited:
                nodes.update(count_neighbours(x_new, y_new, visited + [(x, y)]))
    return nodes


print("answer 2:", len(count_neighbours(*end)))
