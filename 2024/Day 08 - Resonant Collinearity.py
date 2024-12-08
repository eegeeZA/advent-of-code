import collections
import itertools

try:
    antennas = open("inputs/day08.txt").read()
except FileNotFoundError:
    antennas = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""[1:]
antennas = antennas.splitlines()

locations = collections.defaultdict(list)
max_row = len(antennas)
max_column = len(antennas[0])
antinodes2 = set()
for row in range(max_row):
    for column in range(max_column):
        if antennas[row][column] != ".":
            locations[antennas[row][column]].append((row, column))
            antinodes2.add((row, column))
antinodes = set()
for antenna, nodes in locations.items():
    for (x, y), (a, b) in itertools.permutations(nodes, 2):
        delta_x, delta_y = x - a, y - b
        if 0 <= x + delta_x < max_row and 0 <= y + delta_y < max_column:
            antinodes.add((x + delta_x, y + delta_y))
        while True:
            x, y = x + delta_x, y + delta_y
            if 0 <= x + delta_x < max_row and 0 <= y + delta_y < max_column:
                antinodes2.add((x + delta_x, y + delta_y))
            else:
                break
print("answer 1:", len(antinodes))
print("answer 2:", len(antinodes | antinodes2))
