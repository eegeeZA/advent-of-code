x, y = 0, 0
direction = 0
for instruction in open("inputs/day12.txt"):
    action, value = instruction[0], int(instruction[1:])
    if action == "L":
        direction -= value // 90
    elif action == "R":
        direction += value // 90
    elif action == "F":
        if direction % 4 == 0:
            y += value
        elif direction % 4 == 1:
            x += value
        elif direction % 4 == 2:
            y -= value
        elif direction % 4 == 3:
            x -= value
    elif action == "N":
        x -= value
    elif action == "S":
        x += value
    elif action == "E":
        y += value
    elif action == "W":
        y -= value

print("answer 1:", abs(x) + abs(y))

x, y = -1, 10
a, b = 0, 0
for instruction in open("inputs/day12.txt"):
    action, value = instruction[0], int(instruction[1:])
    if action == "L":
        for i in range(value // 90):
            x, y = -y, x
    elif action == "R":
        for i in range(value // 90):
            x, y = y, -x
    elif action == "F":
        a += value * x
        b += value * y
    elif action == "N":
        x -= value
    elif action == "S":
        x += value
    elif action == "E":
        y += value
    elif action == "W":
        y -= value
print("answer 2:", abs(a) + abs(b))
