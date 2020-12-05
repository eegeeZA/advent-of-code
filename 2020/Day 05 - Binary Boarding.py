from functools import reduce
from math import ceil

seat_ids = []
for boarding_pass in open("inputs/day05.txt"):
    row_start, column_start = 0, 0
    row_end, column_end = 127, 7
    for direction in boarding_pass:
        if direction == "B":
            row_start += ceil((row_end - row_start) / 2)
        if direction == "F":
            row_end -= ceil((row_end - row_start) / 2)
        if direction == "R":
            column_start += ceil((column_end - column_start) / 2)
        if direction == "L":
            column_end -= ceil((column_end - column_start) / 2)
    seat_ids.append(row_start * 8 + column_start)

print("answer 1:", max(seat_ids))
print("answer 2:", 1 + reduce(lambda x, y: y if x + 1 == y else x, sorted(seat_ids)))
