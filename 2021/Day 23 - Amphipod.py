import functools
import math
import re

diagram = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""[1:]
diagram = open("inputs/day23.txt").read()
min_hallway, max_hallway = 0, diagram.count(".")
max_depth = diagram.count("A") + 1
diagram = diagram.splitlines()


def parse_layout(layout):
    result = {(0, 0): None, (0, 10): None}
    result.update({(0, y): None for y in range(1, 10, 2)})
    for x, line in enumerate(layout[2:-1]):
        result.update({(x + 1, 2 + 2 * y): amphipod for y, amphipod in enumerate(re.findall(r"\w", line))})
    return frozenset(result.items())


@functools.cache
def next_moves(layout):
    layout = dict(layout)
    result = {}
    for (x1, y1), cell1 in layout.items():
        if not cell1:
            continue
        if any(layout[x2, y1] for x2 in range(1, x1)):
            continue

        moves = {}
        if x1 > 0:
            expected = chr(ord("A") - 1 + y1 // 2)
            if cell1 == expected and all(
                    layout[x2, y1] == expected for x2 in range(x1 + 1, max_depth)):
                continue
            for y2 in range(y1 - 1, min_hallway, -2):
                if not layout[0, y2]:
                    moves[0, y2] = x1 + abs(y1 - y2)
                else:
                    break
            else:
                if not layout[0, 0]:
                    moves[0, 0] = x1 + y1

            for y2 in range(y1 + 1, max_hallway, 2):
                if not layout[0, y2]:
                    moves[0, y2] = x1 + abs(y1 - y2)
                else:
                    break
            else:
                if not layout[0, max_hallway - 1]:
                    moves[0, max_hallway - 1] = x1 + abs(y1 - (max_hallway - 1))
        else:
            y2 = 2 + 2 * (ord(cell1) - ord("A"))
            if any((0, y3) in layout and layout[0, y3] for y3 in range(y2, y1, (y1 - y2) // abs(y1 - y2))):
                continue
            for x2 in reversed(range(1, max_depth)):
                if not layout[x2, y2]:
                    moves[x2, y2] = (abs(x1 - x2) + abs(y1 - y2))
                    break
                elif layout[x2, y2] != cell1:
                    break
        if moves:
            for key in moves.keys():
                moves[key] *= pow(10, ord(cell1) - ord("A"))
            result[x1, y1] = moves

    return result


def final_layout(layout):
    for x in range(1, max_depth):
        for y in range(2, 2 * 4 + 1, 2):
            if layout[x, y] != chr(ord("A") - 1 + y // 2):
                return False
    return True


@functools.cache
def simulate(layout, score=0):
    layout = dict(layout)
    global best_score
    if score > best_score:
        return
    moves = next_moves(frozenset(layout.items()))
    if not moves:
        if final_layout(layout):
            best_score = min(best_score, score)
            yield score
        return

    for x, y in moves.keys():
        for (a, b), next_score in moves[x, y].items():
            layout_copy = layout.copy()
            layout_copy[a, b], layout_copy[x, y] = layout_copy[x, y], layout_copy[a, b]
            yield from simulate(frozenset(layout_copy.items()), score + next_score)


parsed_layout = parse_layout(diagram)
best_score = math.inf
print("answer 1:", min(simulate(parsed_layout)))

diagram.insert(3, "  #D#C#B#A#")
diagram.insert(4, "  #D#B#A#C#")
max_depth += 2
parsed_layout = parse_layout(diagram)
best_score = math.inf
print("answer 2:", min(simulate(parsed_layout)))
