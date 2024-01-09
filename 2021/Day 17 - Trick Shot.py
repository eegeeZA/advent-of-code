try:
    target_area = open("inputs/day17.txt").read().strip()
except FileNotFoundError:
    target_area = "target area: x=20..30, y=-10..-5"

x_min, x_max, y_min, y_max = [int(part) for area in target_area[13:].split(", ") for part in area[2:].split("..")]


def hits_target(x_velocity, y_velocity):
    x, y = 0, 0
    peak_height = 0
    while True:
        x += x_velocity
        y += y_velocity
        x_velocity = max(0, x_velocity - 1)
        y_velocity -= 1
        if y < y_min:
            return None

        peak_height = max(peak_height, y)
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return peak_height


hits = []
for i in range(x_max + 1):
    for j in range(y_min, x_max):
        height = hits_target(i, j)
        if height is not None:
            hits.append(height)

print("answer 1:", max(hits))
print("answer 2:", len(hits))
