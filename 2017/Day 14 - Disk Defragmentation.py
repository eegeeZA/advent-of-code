day10 = __import__("Day 10 - Knot Hash")

input_string = "hxtvlmkl"
hash_string = ""
for i in range(128):
    hash_string += day10.knot_hash(f"{input_string}-{i}")
squares_used = bin(int(hash_string, 16)).count("1")
print("day 14 answer 1:", squares_used)


def count(row, column):
    if disk_layout[row][column] == "1":
        disk_layout[row][column] = ""
        count(row, max(0, min(127, column + 1)))
        count(row, max(0, min(127, column - 1)))
        count(max(0, min(127, row + 1)), column)
        count(max(0, min(127, row - 1)), column)
        return 1

    return 0


disk_layout = []
for i in range(128):
    hash_string = day10.knot_hash(f"{input_string}-{i}")
    disk_layout.append(list(bin(int(hash_string, 16))[2:].zfill(128)))
regions = 0
for row in range(128):
    for column in range(128):
        regions += count(row, column)
print("day 14 answer 2:", regions)
