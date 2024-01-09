import copy

try:
    sea_cucumbers = open("inputs/day25.txt").read()
except FileNotFoundError:
    sea_cucumbers = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""[1:]
sea_cucumbers = [[*sea_cucumber] for sea_cucumber in sea_cucumbers.splitlines()]

moving = True
steps = 0
while moving:
    steps += 1
    moving = False

    sea_cucumbers_snapshot = copy.deepcopy(sea_cucumbers)
    for i in range(len(sea_cucumbers)):
        for j in range(len(sea_cucumbers[i])):
            right = (j + 1) % len(sea_cucumbers[i])
            if sea_cucumbers_snapshot[i][j] == ">" and sea_cucumbers_snapshot[i][right] == ".":
                sea_cucumbers[i][j], sea_cucumbers[i][right] = sea_cucumbers[i][right], sea_cucumbers[i][j]
                moving = True

    sea_cucumbers_snapshot = copy.deepcopy(sea_cucumbers)
    for i in range(len(sea_cucumbers)):
        down = (i + 1) % len(sea_cucumbers)
        for j in range(len(sea_cucumbers[i])):
            if sea_cucumbers_snapshot[i][j] == "v" and sea_cucumbers_snapshot[down][j] == ".":
                sea_cucumbers[i][j], sea_cucumbers[down][j] = sea_cucumbers[down][j], sea_cucumbers[i][j]
                moving = True

print("answer 1:", steps)
print("answer 2:", "*")
