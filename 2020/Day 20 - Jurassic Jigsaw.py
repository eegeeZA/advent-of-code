import re
from collections import defaultdict
from itertools import product, permutations
from math import prod, sqrt


def tiles_aligned(data, order):
    for row in order:
        for i, j in zip(row, row[1:]):
            left, right = [row[-1] for row in data[i]], [row[0] for row in data[j]]
            if left != right:
                return False
    for row in range(len(order) - 1):
        for i, j in zip(order[row], order[row + 1]):
            top, bottom = data[i][-1], data[j][0]
            if top != bottom:
                return False
    return True


def flip(matrix):
    return matrix[::-1]


def rotate(matrix):
    return tuple(zip(*flip(matrix)))


def all_states(matrix):
    return [matrix, rotate(matrix), rotate(rotate(matrix)), rotate(rotate(rotate(matrix))),
            flip(matrix), rotate(flip(matrix)), rotate(rotate(flip(matrix))), rotate(rotate(rotate(flip(matrix))))]


def find_pairs():
    pairs = defaultdict(lambda: defaultdict(list))
    for a_tile, b_tile in permutations(tiles, 2):
        a_states, b_states = all_states(tiles[a_tile]), all_states(tiles[b_tile])
        for a_index, b_index in product(range(8), repeat=2):
            if tiles_aligned({a_tile: a_states[a_index], b_tile: b_states[b_index]}, [[a_tile, b_tile]]):
                pairs[a_tile][b_tile].append(("-", a_index, b_index))
            if tiles_aligned({a_tile: a_states[a_index], b_tile: b_states[b_index]}, [[a_tile], [b_tile]]):
                pairs[a_tile][b_tile].append(("|", a_index, b_index))
    return pairs


tiles = {}
for tile in open("inputs/day20.txt").read().rstrip().split("\n\n"):
    tile_id, tile_rows = None, []
    for line in tile.split("\n"):
        if "Tile" in line:
            tile_id = int(re.search(r"\d+", line).group(0))
        else:
            tile_rows.append(tuple(line))
    tiles[tile_id] = tuple(tile_rows)
pairs = find_pairs()
corners = [tile_id for tile_id, pair in pairs.items() if len(pair) < 3]
print("answer 1:", prod(corners))

square = int(sqrt(len(tiles.keys())))
puzzle = [[(0, 0) for _ in range(square)] for _ in range(square)]
actual_image = defaultdict(str)
for i in range(square):
    for j in range(square):
        if i > 0:
            tile_id, tile_state = puzzle[i - 1][j]
            for bottom_id, states in pairs[tile_id].items():
                for direction, top_state, bottom_state in states:
                    if direction == "|" and tile_state == top_state:
                        puzzle[i][j] = bottom_id, bottom_state
        elif j > 0:
            tile_id, tile_state = puzzle[i][j - 1]
            for right_id, states in pairs[tile_id].items():
                for direction, left_state, right_state in states:
                    if direction == "-" and tile_state == left_state:
                        puzzle[i][j] = right_id, right_state
        else:
            right, bottom = pairs[corners[0]].values()
            right_states = {index for direction, index, _ in right if direction == "-"}
            bottom_states = {index for direction, index, _ in bottom if direction == "|"}
            puzzle[0][0] = corners[0], (right_states & bottom_states).pop()

        tile_id, state = puzzle[i][j]
        rows = all_states(tiles[tile_id])[state][1:-1]
        for x, row in enumerate(rows):
            actual_image[i * len(rows) + x] += "".join(row[1:-1])

sea_monster = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']
sea_monster = ["(?={0})".format(line.replace(" ", ".")) for line in sea_monster]
for state in all_states(tuple(actual_image.values())):
    total = 0
    for i in range(len(state) - len(sea_monster) + 1):
        matches = [{match.start() for match in re.finditer(sea_monster[offset], "".join(state[i + offset]))}
                   for offset in range(len(sea_monster))]
        total += len(set.intersection(*matches))
    if total > 0:
        print("answer 2:", sum(row.count("#") for row in state) - total * sum(row.count("#") for row in sea_monster))
        break
