from itertools import combinations

spreadsheet = open("inputs/day02.txt").readlines()
checksum = 0
for row in spreadsheet:
    values = list(map(int, row.split()))
    values.sort()
    checksum += values[-1] - values[0]
print("checksum 1:", checksum)

checksum = 0
for row in spreadsheet:
    values = list(map(int, row.split()))
    values.sort(reverse=True)
    for x, y in combinations(values, 2):
        if x % y == 0:
            checksum += x // y
print("checksum 2:", checksum)
