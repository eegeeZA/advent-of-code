import math


def find_visible(centre_x, centre_y):
    visited = []
    for new_x, new_y in filter(lambda a: a != (centre_x, centre_y), asteroids):
        new_distance = abs(new_x - centre_x) + abs(new_y - centre_y)
        for visited_x, visited_y in visited:
            visited_distance = abs(visited_x - centre_x) + abs(visited_y - centre_y)
            same_x = (new_x - centre_x) / new_distance == (visited_x - centre_x) / visited_distance
            same_y = (new_y - centre_y) / new_distance == (visited_y - centre_y) / visited_distance
            if same_x and same_y:
                if new_distance < visited_distance:
                    visited.remove((visited_x, visited_y))
                    visited.append((new_x, new_y))
                break
        else:
            visited.append((new_x, new_y))
    return visited


asteroids = {}
x, y = 0, 0
for los in open("inputs/day10.txt"):
    for x, value in enumerate(list(los.strip())):
        if value == "#":
            asteroids[x, y] = value
    y += 1
grid_size = y

counts = {asteroid: find_visible(*asteroid) for asteroid in asteroids}
optimal_asteroid = max(counts, key=lambda c: len(counts[c]))
print("answer 1:", optimal_asteroid, "=>", len(counts[optimal_asteroid]))


def calc_degrees(from_asteroid, to_asteroid):
    radians = math.atan2(from_asteroid[1] - to_asteroid[1], from_asteroid[0] - to_asteroid[0])
    degrees = radians * (180 / math.pi)
    return (degrees + 180 + 90) % 360


destroys = sorted(counts[optimal_asteroid], key=lambda destroy: calc_degrees(optimal_asteroid, destroy))
destroy_x, destroy_y = destroys[200 - 1]
print("answer 2:", destroy_x * 100 + destroy_y)
