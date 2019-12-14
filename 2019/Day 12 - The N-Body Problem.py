import copy
from itertools import combinations, count
from math import gcd

moons = []
for moon in open("inputs/day12.txt"):
    parts = moon.replace("<", "").replace(">", "").replace(" ", "").strip()
    vectors = {k: int(v) for k, v in map(lambda x: x.split("="), parts.split(","))}
    vectors["dx"], vectors["dy"], vectors["dz"] = 0, 0, 0
    moons.append(vectors)
original = copy.deepcopy(moons)


def orbit():
    global moon
    for moon1, moon2 in combinations(moons, 2):
        for axis in "xyz":
            if moon1[axis] < moon2[axis]:
                moon1["d" + axis] += 1
                moon2["d" + axis] -= 1
            elif moon1[axis] > moon2[axis]:
                moon1["d" + axis] -= 1
                moon2["d" + axis] += 1
    for moon in moons:
        for axis in "xyz":
            moon[axis] += moon["d" + axis]


for step in range(1000):
    orbit()
energy = 0
for moon in moons:
    potential = abs(moon["x"]) + abs(moon["y"]) + abs(moon["z"])
    kinetic = abs(moon["dx"]) + abs(moon["dy"]) + abs(moon["dz"])
    energy += potential * kinetic
print("answer 1:", energy)


def lcm(x1, x2):
    return x1 * x2 // gcd(x1, x2)


moons = copy.deepcopy(original)
x, y, z = 0, 0, 0
for i in count(1):
    orbit()
    if not x and all([a["x"] == b["x"] for a, b, in zip(moons, original)]) \
            and all([a["dx"] == b["dx"] for a, b, in zip(moons, original)]):
        x = i
    if not y and all([a["y"] == b["y"] for a, b, in zip(moons, original)]) \
            and all([a["dy"] == b["dy"] for a, b, in zip(moons, original)]):
        y = i
    if not z and all([a["z"] == b["z"] for a, b, in zip(moons, original)]) \
            and all([a["dz"] == b["dz"] for a, b, in zip(moons, original)]):
        z = i
    if x and y and z:
        break
print("answer 2:", lcm(x, lcm(y, z)))
