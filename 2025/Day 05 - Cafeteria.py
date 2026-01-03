try:
    database = open("inputs/day05.txt").read()
except FileNotFoundError:
    database = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""[1:]
ingredients_fresh, ingredients_available = database.strip().split('\n\n')

fresh_ranges = []
for line in ingredients_fresh.splitlines():
    start, end = line.split('-')
    fresh_ranges.append((int(start), int(end)))

fresh = 0
for ingredient in ingredients_available.splitlines():
    ingredient = int(ingredient)
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            fresh += 1
            break
print("answer 1:", fresh)

fresh_ranges = sorted(fresh_ranges)
merged_ranges = [fresh_ranges.pop(0)]
for start, end in fresh_ranges:
    last_start, last_end = merged_ranges[-1]
    if start <= last_end + 1:
        merged_ranges[-1] = (last_start, max(last_end, end))
    else:
        merged_ranges.append((start, end))
print("answer 2:", sum(end - start + 1 for start, end in merged_ranges))
