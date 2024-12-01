import collections

try:
    locations = open("inputs/day01.txt").read()
except FileNotFoundError:
    locations = """
3   4
4   3
2   5
1   3
3   9
3   3
"""[1:]
locations = locations.splitlines()

first, second = zip(*(pair.split() for pair in locations))
distance = sum(abs(int(a) - int(b)) for a, b in zip(sorted(first), sorted(second)))
print("answer 1:", distance)

counts = collections.Counter(second)
similarity = sum(int(x) * counts[x] for x in first)
print("answer 2:", similarity)
