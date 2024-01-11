import functools

try:
    springs = open("inputs/day12.txt").read().splitlines()
except FileNotFoundError:
    springs = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""[1:].splitlines()


@functools.cache
def count_arrangements(line, conditions):
    if not line:
        return 1 if not conditions else 0
    if not conditions:
        return 0 if "#" in line else 1

    result = 0

    if line[0] in "?.":
        result += count_arrangements(line[1:], conditions)

    if line[0] in "?#":
        if (conditions[0] <= len(line)
                and "." not in line[: conditions[0]]
                and (conditions[0] == len(line) or line[conditions[0]] in ".?")):
            result += count_arrangements(line[conditions[0] + 1:], conditions[1:])

    return result


counts = 0
for row in springs:
    spring, condition = row.split()
    condition = tuple(map(int, condition.split(",")))
    counts += count_arrangements(spring, condition)
print("answer 1:", counts)

counts = 0
for row in springs:
    spring, condition = row.split()
    spring = "?".join([spring] * 5)
    condition = tuple(map(int, condition.split(","))) * 5
    counts += count_arrangements(spring, condition)
print("answer 2:", counts)
