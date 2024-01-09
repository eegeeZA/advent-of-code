import functools

try:
    lanternfish = list(map(int, open("inputs/day06.txt").read().split(",")))
except FileNotFoundError:
    lanternfish = [3, 4, 3, 1, 2]

for day in range(80):
    lanternfish = [x - 1 for x in lanternfish]
    lanternfish = lanternfish + [8] * lanternfish.count(-1)
    lanternfish = [6 if x < 0 else x for x in lanternfish]
print("answer 1:", len(lanternfish))


@functools.cache
def count_fish(days, fish):
    result = 0
    if days > fish:
        result += count_fish(days - fish - 1, 6)
        result += count_fish(days - fish - 1, 8)
    else:
        return 1
    return result


lanternfish = list(map(int, open("inputs/day06.txt").read().split(",")))
print("answer 2:", sum(count_fish(256, x) for x in lanternfish))
