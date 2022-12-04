assignments = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()
assignments = open("inputs/day04.txt").read().splitlines()

fully_contained = 0
partially_contained = 0
for line in assignments:
    first, second = line.split(",")
    first_start, first_end, second_start, second_end = map(int, [*first.split("-"), *second.split("-")])
    if first_start >= second_start and first_end <= second_end:
        fully_contained += 1
    elif second_start >= first_start and second_end <= first_end:
        fully_contained += 1
print("answer 1:", fully_contained)

partially_contained = 0
for line in assignments:
    first, second = line.split(",")
    first_start, first_end, second_start, second_end = map(int, [*first.split("-"), *second.split("-")])
    first_range = set(range(first_start, first_end + 1))
    second_range = set(range(second_start, second_end + 1))
    if first_range & second_range:
        partially_contained += 1
print("answer 2:", partially_contained)
