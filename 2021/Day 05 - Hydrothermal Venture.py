import collections
import itertools

vents = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]
vents = open("inputs/day05.txt")

dangerous_areas1 = collections.defaultdict(int)
dangerous_areas2 = collections.defaultdict(int)
for vent in vents:
    x_start, y_start, x_end, y_end = map(int, vent.replace("->", ",").split(","))

    if x_start < x_end:
        range_x = range(x_start, x_end + 1)
    elif x_start > x_end:
        range_x = range(x_start, x_end - 1, -1)
    else:
        range_x = itertools.repeat(x_start)

    if y_start < y_end:
        range_y = range(y_start, y_end + 1)
    elif y_start > y_end:
        range_y = range(y_start, y_end - 1, -1)
    else:
        range_y = itertools.repeat(y_start)

    for x, y in zip(range_x, range_y):
        if x_start == x_end or y_start == y_end:
            dangerous_areas1[x, y] += 1
        dangerous_areas2[x, y] += 1

print("answer 1:", sum(area >= 2 for area in dangerous_areas1.values()))
print("answer 2:", sum(area >= 2 for area in dangerous_areas2.values()))
