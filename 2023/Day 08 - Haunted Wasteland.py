import functools
import itertools
import math

documents = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""[1:].splitlines()
documents = open("inputs/day08.txt").read().splitlines()

sequence = documents[0]
nodes = {}
for node in documents[2:]:
    key, values = node.split(" = ")
    left, right = values.replace("(", "").replace(")", "").split(", ")
    nodes[key] = {"L": left, "R": right}

node = "AAA"
steps = 0
for direction in itertools.cycle(sequence):
    node = nodes[node][direction]
    steps += 1
    if node == "ZZZ":
        break
print("answer 1:", steps)

ghost_nodes = [key for key in nodes.keys() if key.endswith("A")]
ghost_distances = []
for ghost_node in ghost_nodes:
    steps = 0
    for direction in itertools.cycle(sequence):
        ghost_node = nodes[ghost_node][direction]
        steps += 1
        if ghost_node.endswith("Z"):
            ghost_distances.append(steps)
            break
print("answer 2:", functools.reduce(math.lcm, ghost_distances))
