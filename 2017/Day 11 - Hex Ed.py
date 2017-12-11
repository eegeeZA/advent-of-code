child_path = open("inputs/day11.txt").read().rstrip()
x, y, z = 0, 0, 0
max_distance = 0
for step in child_path.split(","):
    if step == "n":
        x -= 1
        y += 1
    if step == "s":
        x += 1
        y -= 1
    if step == "ne":
        y += 1
    if step == "nw":
        x -= 1
    if step == "se":
        x += 1
    if step == "sw":
        y -= 1
    z = -x + -y
    max_distance = max(max_distance, abs(x), abs(y), abs(z))
print("answer 1:", max(abs(x), abs(y), abs(z)))
print("answer 2:", max_distance)
