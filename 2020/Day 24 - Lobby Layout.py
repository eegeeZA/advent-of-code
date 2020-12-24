import re
from collections import defaultdict, Counter

tiles = defaultdict(bool)
for instructions in open("inputs/day24.txt"):
    instructions = re.findall(r"(e|se|sw|w|nw|ne)", instructions.rstrip())
    x, y = 0, 0
    for step in instructions:
        if step == "e":
            x += 1
        if step == "w":
            x -= 1
        if step == "ne":
            x += 1
            y -= 1
        if step == "nw":
            y -= 1
        if step == "se":
            y += 1
        if step == "sw":
            x -= 1
            y += 1
    tiles[x, y] ^= True
print("answer 1:", sum(tiles.values()))

tiles = +Counter(tiles)
for _ in range(100):
    black_counts = Counter()
    for x, y in tiles:
        black_counts[x + 1, y] += 1
        black_counts[x - 1, y] += 1
        black_counts[x + 1, y - 1] += 1
        black_counts[x, y - 1] += 1
        black_counts[x, y + 1] += 1
        black_counts[x - 1, y + 1] += 1
    new_tiles = {}
    for xy, black_count in black_counts.items():
        if (xy in tiles and black_count == 1) or black_count == 2:
            new_tiles[xy] = True
    tiles = new_tiles
print("answer 2:", len(tiles))
