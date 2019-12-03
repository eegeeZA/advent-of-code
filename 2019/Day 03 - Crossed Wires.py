from collections import Counter

grid = Counter()
steps = {}
wire_count = 0
for wire in open("inputs/day03.txt"):
    x, y = 0, 0
    visited = {(x, y)}
    wire_count += 1
    step_count = 0
    for action in wire.split(","):
        direction, distance = action[0], int(action[1:])
        for i in range(distance):
            step_count += 1
            if (x, y) not in visited:
                grid[(x, y)] += 1
                visited.add((x, y))
            if direction == "R":
                x += 1
            if direction == "L":
                x -= 1
            if direction == "U":
                y += 1
            if direction == "D":
                y -= 1
            steps[(wire_count, x, y)] = step_count

min_distance = float("inf")
for (x, y), count in grid.most_common():
    if count >= 2:
        min_distance = min(min_distance, abs(x) + abs(y))
print("answer 1:", min_distance)

min_steps = float("inf")
for (x, y), count in grid.most_common():
    if count >= 2:
        min_steps = min(min_steps, steps[(1, x, y)] + steps[(2, x, y)])
print("answer 2:", min_steps)
