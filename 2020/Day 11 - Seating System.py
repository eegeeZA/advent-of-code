import copy

floor_plan = []
for row in open("inputs/day11.txt"):
    floor_plan.append([*row.strip()])


def simulate(layout):
    result = copy.deepcopy(layout)
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            occupied_count = 0
            for x in range(max(0, i - 1), min(len(layout), i + 2)):
                for y in range(max(0, j - 1), min(len(layout[i]), j + 2)):
                    if layout[x][y] == "#" and not (x == i and y == j):
                        occupied_count += 1
            if layout[i][j] == "L" and occupied_count == 0:
                result[i][j] = "#"
            if layout[i][j] == "#" and occupied_count >= 4:
                result[i][j] = "L"
    return result


while True:
    new_plan = simulate(floor_plan)
    if floor_plan == new_plan:
        occupied_count = 0
        for i in range(len(floor_plan)):
            for j in range(len(floor_plan[i])):
                if floor_plan[i][j] == "#":
                    occupied_count += 1
        break
    else:
        floor_plan = new_plan
print("answer 1:", occupied_count)

floor_plan = []
for row in open("inputs/day11.txt"):
    floor_plan.append([*row.strip()])


def simulate2(layout):
    result = copy.deepcopy(layout)
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            occupied_count = 0
            for x in range(i + 1, len(layout)):
                if layout[x][j] == "#":
                    occupied_count += 1
                    break
                elif layout[x][j] == "L":
                    break
            for x in range(i - 1, -1, -1):
                if layout[x][j] == "#":
                    occupied_count += 1
                    break
                elif layout[x][j] == "L":
                    break
            for y in range(j + 1, len(layout[i])):
                if layout[i][y] == "#":
                    occupied_count += 1
                    break
                elif layout[i][y] == "L":
                    break
            for y in range(j - 1, -1, -1):
                if layout[i][y] == "#":
                    occupied_count += 1
                    break
                elif layout[i][y] == "L":
                    break
            for x, y in zip(range(i + 1, len(layout)), range(j + 1, len(layout[i]))):
                if layout[x][y] == "#":
                    occupied_count += 1
                    break
                elif layout[x][y] == "L":
                    break
            for x, y in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
                if layout[x][y] == "#":
                    occupied_count += 1
                    break
                elif layout[x][y] == "L":
                    break
            for x, y in zip(range(i - 1, -1, -1), range(j + 1, len(layout[i]))):
                if layout[x][y] == "#":
                    occupied_count += 1
                    break
                elif layout[x][y] == "L":
                    break
            for x, y in zip(range(i + 1, len(layout)), range(j - 1, -1, -1)):
                if layout[x][y] == "#":
                    occupied_count += 1
                    break
                elif layout[x][y] == "L":
                    break
            if layout[i][j] == "L" and occupied_count == 0:
                result[i][j] = "#"
            if layout[i][j] == "#" and occupied_count >= 5:
                result[i][j] = "L"
    return result


while True:
    new_plan = simulate2(floor_plan)
    if floor_plan == new_plan:
        occupied_count = 0
        for i in range(len(floor_plan)):
            for j in range(len(floor_plan[i])):
                if floor_plan[i][j] == "#":
                    occupied_count += 1
        break
    else:
        floor_plan = new_plan
print("answer 2:", occupied_count)
