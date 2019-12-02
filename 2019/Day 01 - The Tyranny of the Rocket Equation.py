mass = 0
for module in open("inputs/day01.txt"):
    mass += int(module) // 3 - 2
print("answer 1:", mass)

mass = 0
for module in open("inputs/day01.txt"):
    fuel = int(module)
    while (fuel := fuel // 3 - 2) > 0:
        mass += fuel
print("answer 2:", mass)
