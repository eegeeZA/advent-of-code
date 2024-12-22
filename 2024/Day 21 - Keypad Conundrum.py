import itertools
import math

try:
    codes = open("inputs/day21.txt").read()
except:
    codes = """
029A
980A
179A
456A
379A
"""[1:]
codes = codes.splitlines()
keypad_numeric = {(0, 0): '7', (0, 1): '8', (0, 2): '9',
                  (1, 0): '4', (1, 1): '5', (1, 2): '6',
                  (2, 0): '1', (2, 1): '2', (2, 2): '3',
                  (3, 1): '0', (3, 2): 'A'}
keypad_directions = {(0, 1): '^', (0, 2): 'A',
                     (1, 0): '<', (1, 1): 'v', (1, 2): '>'}
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def cost(points, depth, path):
    return sum(points[(depth, x, y)] for x, y in itertools.pairwise('A' + path))


def best_score(code, depth):
    level_points = {(0, x, y): 1 for x, y in itertools.product(keypad_directions.values(), repeat=2)}

    grid = keypad_directions
    for level in range(1, depth + 1):
        if level == depth:
            grid = keypad_numeric
        for (x, y), cell1 in grid.items():
            for (a, b), cell2 in grid.items():
                best_x = ('^' if x > a else 'v') * abs(x - a)
                best_y = ('<' if y > b else '>') * abs(y - b)

                cost_horizontal = math.inf
                if (x, b) in grid:
                    cost_horizontal = cost(level_points, level - 1, best_y + best_x + 'A')
                cost_vertical = math.inf
                if (a, y) in grid:
                    cost_vertical = cost(level_points, level - 1, best_x + best_y + 'A')

                level_points[(level, cell1, cell2)] = min(cost_horizontal, cost_vertical)

    return cost(level_points, depth, code)


print("answer 1:", sum(best_score(code, 3) * int(code[:-1]) for code in codes))
print("answer 2:", sum(best_score(code, 26) * int(code[:-1]) for code in codes))
