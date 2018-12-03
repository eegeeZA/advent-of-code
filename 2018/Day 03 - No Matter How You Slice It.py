from collections import Counter

fabric = Counter()
for claim in open("inputs/day03.txt"):
    claim_id, _, xy, wh = claim.split()
    x, y = map(int, xy.rstrip(":").split(","))
    w, h = map(int, wh.split("x"))
    for row in range(w):
        for col in range(h):
            fabric[x + row, y + col] += 1
overlap = sum(1 for val in fabric.values() if val >= 2)
print("answer 1:", overlap)

fabric = {}
for claim in open("inputs/day03.txt"):
    claim_id, _, xy, wh = claim.split()
    x, y = map(int, xy.rstrip(":").split(","))
    w, h = map(int, wh.split("x"))
    for row in range(w):
        for col in range(h):
            if (x + row, y + col) not in fabric:
                fabric[x + row, y + col] = []
            fabric[x + row, y + col].append(claim_id)
unique = set()
multiple = set()
for val in fabric.values():
    if len(val) == 1:
        unique.add(*val)
    else:
        multiple |= set(val)
unique -= multiple
print("answer 2:", *unique)
