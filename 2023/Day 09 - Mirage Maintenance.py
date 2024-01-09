import itertools

report = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""[1:].splitlines()
report = open("inputs/day09.txt").read().splitlines()

next_value_total = 0
for history in report:
    differences = list(map(int, history.split()))
    next_value = 0
    while any(differences):
        next_value += differences[-1]
        differences = [b - a for a, b in itertools.pairwise(differences)]
    next_value_total += next_value
print("answer 1:", next_value_total)

previous_value_total = 0
for history in report:
    differences = list(map(int, history.split()))
    previous_value = 0
    while any(differences):
        previous_value += differences[0]
        differences = [a - b for a, b in itertools.pairwise(differences)]
    previous_value_total += previous_value
print("answer 2:", previous_value_total)
