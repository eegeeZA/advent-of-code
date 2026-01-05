import collections
import itertools
import math

try:
    junction_boxes = open("inputs/day08.txt").read()
    pairs_count = 1000
except FileNotFoundError:
    junction_boxes = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""[1:]
    pairs_count = 10
junction_boxes = [tuple(map(int, line.split(','))) for line in junction_boxes.splitlines()]


def find(x):
    if circuits[x] != x:
        circuits[x] = find(circuits[x])
    return circuits[x]


distances = sorted((math.dist(a, b), a, b) for a, b in itertools.combinations(junction_boxes, 2))
circuits = {box: box for box in junction_boxes}
for _, a, b in distances[:pairs_count]:
    pa, pb = find(a), find(b)
    if pa != pb:
        circuits[pa] = pb

sizes = collections.Counter(find(box) for box in junction_boxes).most_common(3)
print("answer 1:", math.prod(count for _, count in sizes))

for _, a, b in distances[pairs_count:]:
    pa, pb = find(a), find(b)
    if pa != pb:
        circuits[pa] = pb
        if len(set(find(box) for box in junction_boxes)) == 1:
            ax, ay, az = a
            bx, by, bz = b
            print("answer 2:", ax * bx)
            break
