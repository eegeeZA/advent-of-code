try:
    topographic = open("inputs/day10.txt").read()
except FileNotFoundError:
    topographic = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""[1:]
topographic = [[int(x) for x in y] for y in topographic.splitlines()]


def find_summit(previous, i, j):
    if (0 <= i < len(topographic)) and (0 <= j < len(topographic[i])):
        if topographic[i][j] == previous + 1:
            if topographic[i][j] == 9:
                yield i, j
            for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                yield from find_summit(previous + 1, i + a, j + b)


trailheads = 0
rating = 0
for x in range(len(topographic)):
    for y in range(len(topographic[x])):
        if topographic[x][y] == 0:
            trailheads += len(set(find_summit(-1, x, y)))
            rating += len(list(find_summit(-1, x, y)))

print("answer 1:", trailheads)
print("answer 2:", rating)
