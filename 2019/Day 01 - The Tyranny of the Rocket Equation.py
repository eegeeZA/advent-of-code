mass = 0
for module in open("inputs/day01.txt"):
    mass += int(module) // 3 - 2
print("answer 1:", mass)

mass = 0
for module in open("inputs/day01.txt"):
    module_mass = int(module)
    while True:
        fuel = module_mass // 3 - 2
        if fuel <= 0:
            break
        mass += fuel
        module_mass = fuel
print("answer 2:", mass)
