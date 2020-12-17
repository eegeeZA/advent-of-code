def mutate(new_state, x, y, z, depth=0):
    if depth > 1:
        return
    active_count = 0
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            for c in range(z - 1, z + 2):
                if (a, b, c) != (x, y, z):
                    mutate(new_state, a, b, c, depth + 1)
                    if (a, b, c) in state:
                        active_count += 1
    if (x, y, z) in new_state and not (2 <= active_count <= 3):
        del new_state[x, y, z]
    elif (x, y, z) not in new_state and active_count == 3:
        new_state[x, y, z] = "#"


state = {}
for x, line in enumerate(open("inputs/day17.txt")):
    for y, point in enumerate(line.rstrip()):
        if point == "#":
            state[x, y, 0] = point
for _ in range(6):
    new_state = state.copy()
    for x, y, z in state:
        mutate(new_state, x, y, z)
    state = new_state
print("answer 1:", len(state))


def mutate(new_state, x, y, z, w, depth=0):
    if depth > 1:
        return
    active_count = 0
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            for c in range(z - 1, z + 2):
                for d in range(w - 1, w + 2):
                    if (a, b, c, d) != (x, y, z, w):
                        mutate(new_state, a, b, c, d, depth + 1)
                        if (a, b, c, d) in state:
                            active_count += 1
    if (x, y, z, w) in new_state and not (2 <= active_count <= 3):
        del new_state[x, y, z, w]
    elif (x, y, z, w) not in new_state and active_count == 3:
        new_state[x, y, z, w] = "#"


state = {}
for x, line in enumerate(open("inputs/day17.txt")):
    for y, point in enumerate(line.rstrip()):
        if point == "#":
            state[x, y, 0, 0] = point
for _ in range(6):
    new_state = state.copy()
    for x, y, z, w in state:
        mutate(new_state, x, y, z, w)
    state = new_state
print("answer 2:", len(state))
