import itertools

depths = list(map(int, open("inputs/day01.txt")))
# depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print("answer 1:", sum(y > x for x, y in itertools.pairwise(depths)))

depths = [x + y + z for x, y, z in zip(depths, depths[1:], depths[2:])]
print("answer 2:", sum(y > x for x, y in itertools.pairwise(depths)))
