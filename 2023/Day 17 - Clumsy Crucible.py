import heapq

try:
    city_block = open("inputs/day17.txt").read().splitlines()
except FileNotFoundError:
    city_block = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""[1:].splitlines()
city_block = [[int(y) for y in x] for x in city_block]


def least_heat(min_distance, max_distance):
    visited = set()
    queue = [(0, 0, 0, 0, 0)]
    while queue:
        heat_loss, x, y, delta_x, delta_y = heapq.heappop(queue)
        if x == len(city_block) - 1 and y == len(city_block) - 1:
            return heat_loss

        if (x, y, delta_x, delta_y) in visited:
            continue
        visited.add((x, y, delta_x, delta_y))

        for delta_x, delta_y in ({(-1, 0), (1, 0), (0, -1), (0, 1)} - {(delta_x, delta_y), (-delta_x, -delta_y)}):
            total_heat_loss = heat_loss
            a, b = x, y
            for distance in range(1, max_distance + 1):
                a += delta_x
                b += delta_y
                if a < 0 or a >= len(city_block) or b < 0 or b >= len(city_block):
                    continue
                total_heat_loss += city_block[a][b]
                if distance >= min_distance:
                    heapq.heappush(queue, (total_heat_loss, a, b, delta_x, delta_y))


print("answer 1:", least_heat(1, 3))
print("answer 2:", least_heat(4, 10))
