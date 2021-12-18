import math

risk_level_map = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""[1:]
risk_level_map = open("inputs/day15.txt").read()


def optimise(risks):
    grid_size = round(math.sqrt(len(risks)))
    neighbours = {(i, j): [(x, y) for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
                           if 0 <= x < grid_size and 0 <= y < grid_size]
                  for i in range(grid_size) for j in range(grid_size)}

    route_costs = {(i, j): math.inf for i in range(grid_size) for j in range(grid_size)}
    route_costs[0, 0] = 0

    unoptimised = True
    while unoptimised:
        unoptimised = False
        for point in risks:
            for neighbour in neighbours[point]:
                if route_costs[neighbour] + risks[point] < route_costs[point]:
                    route_costs[point] = route_costs[neighbour] + risks[point]
                    unoptimised = True
    return route_costs[grid_size - 1, grid_size - 1]


risk_levels = {(i, j): int(point) for i, line in enumerate(risk_level_map.splitlines()) for j, point in enumerate(line)}
print("answer 1:", optimise(risk_levels))

expanded_risk_levels = {}
current_size = len(risk_level_map.splitlines())
for i in range(current_size * 5):
    for j in range(current_size * 5):
        offset = i // current_size + j // current_size
        expanded_risk_levels[i, j] = (risk_levels[i % current_size, j % current_size] + offset)
        if expanded_risk_levels[i, j] > 9:
            expanded_risk_levels[i, j] %= 10
            expanded_risk_levels[i, j] += 1
print("answer 2:", optimise(expanded_risk_levels))
