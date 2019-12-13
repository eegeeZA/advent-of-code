from collections import Counter
from importlib import import_module

initial_int_code = list(map(int, open("inputs/day11.txt").read().split(",")))


def paint_hull(space_hull):
    painter = import_module("Day 09 - Sensor Boost").int_code_compute(initial_int_code)
    x, y = 0, 0
    direction = 0
    while True:
        try:
            next(painter)
            current_colour = 0 if (x, y) not in space_hull else space_hull[x, y]
            new_colour = painter.send(current_colour)
            new_direction = next(painter)
        except StopIteration:
            break
        space_hull[x, y] = new_colour

        if new_direction == 0:
            direction -= 1
        elif new_direction == 1:
            direction += 1

        if direction % 4 == 0:
            y += 1
        elif direction % 4 == 1:
            x += 1
        elif direction % 4 == 2:
            y -= 1
        elif direction % 4 == 3:
            x -= 1
    return space_hull


print("answer 1:", len(paint_hull({})))

registration = Counter(paint_hull({(0, 0): 1}))
print("answer 2:")
for y in reversed(range(-5, 1)):
    for x in range(42):
        print(str(registration[x, y]).replace("0", " ").replace("1", "█"), end="")
    print()
