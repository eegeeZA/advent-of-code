def dance(programs):
    for instruction in open("inputs/day16.txt").read().rstrip().split(","):
        if instruction.startswith('s'):
            spin = int(instruction[1:])
            programs[:] = programs[-spin:] + programs[:-spin]
        if instruction.startswith('x'):
            swap = instruction[1:].split("/")
            a, b = map(int, swap)
            programs[a], programs[b] = programs[b], programs[a]
        if instruction.startswith('p'):
            swap_a, swap_b = instruction[1:].split("/")
            a, b = programs.index(swap_a), programs.index(swap_b)
            programs[a], programs[b] = programs[b], programs[a]


positions = [chr(ord('a') + i) for i in range(16)]
dance(positions)
print("answer 1:", "".join(positions))

positions = [chr(ord('a') + i) for i in range(16)]
original = positions.copy()
for cycle in range(1000000000):
    dance(positions)
    if positions == original:
        for _ in range(1000000000 % (cycle + 1)):
            dance(positions)
        break
print("answer 2:", "".join(positions))
