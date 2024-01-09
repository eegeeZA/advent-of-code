coordinates = []
max_range = 0
for xy in open("inputs/day06.txt"):
    x, y = map(int, xy.rstrip().split(", "))
    max_range = max(max_range, x, y)
    coordinates.append((x, y))


def closest(x, y, a, b, desired_x, desired_y):
    return (abs(x - desired_x) + abs(y - desired_y)) < (abs(a - desired_x) + abs(b - desired_y))


largest_safe_zone = 0
inf_zone = set([(0, i) for i in range(max_range)])
inf_zone |= set([(i, 0) for i in range(max_range)])
inf_zone |= set([(max_range - 1, i) for i in range(max_range)])
inf_zone |= set([(i, max_range - 1) for i in range(max_range)])
for coordinate in coordinates:
    safe_zone = set([(i, j) for i in range(max_range) for j in range(max_range)])
    for neighbour in filter(lambda item: item != coordinate, coordinates):
        local_safe_zone = set()
        for i in range(max_range):
            for j in range(max_range):
                if closest(*coordinate, *neighbour, i, j):
                    local_safe_zone.add((i, j))
        safe_zone &= local_safe_zone
    if not inf_zone & safe_zone:
        largest_safe_zone = max(largest_safe_zone, len(safe_zone))
print("answer 1:", largest_safe_zone)

safe_zone = 10000
safe_count = 0
for i in range(max_range):
    for j in range(max_range):
        total_distance = 0
        for coordinate in coordinates:
            x, y = coordinate
            total_distance += (abs(x - i) + abs(y - j))
        if total_distance < safe_zone:
            safe_count += 1
print("answer 2:", safe_count)
