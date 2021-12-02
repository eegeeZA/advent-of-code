commands = open("inputs/day02.txt")
# commands = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

horizontal = depth = depth_with_aim = 0
for command in commands:
    direction, distance = command.split()
    distance = int(distance)
    if direction == "forward":
        horizontal += distance
        depth_with_aim += depth * distance
    elif direction == "down":
        depth += distance
    elif direction == "up":
        depth -= distance

print("answer 1:", horizontal * depth)
print("answer 2:", horizontal * depth_with_aim)
