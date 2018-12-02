from collections import Counter
from itertools import combinations

twos = 0
threes = 0
for box_id in open("inputs/day02.txt"):
    counts = Counter(box_id).values()
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1
print("answer 1:", twos * threes)

best = ""
for x, y in combinations(open("inputs/day02.txt"), 2):
    common_letters = ""
    for a, b in zip(x, y):
        if a == b:
            common_letters += a
    if len(common_letters) > len(best):
        best = common_letters
print("answer 2:", best)
