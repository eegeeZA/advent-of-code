import collections
import functools
import itertools
import re

try:
    remaining_manual = open("inputs/day10.txt").read()
except FileNotFoundError:
    remaining_manual = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""[1:]
remaining_manual = remaining_manual.splitlines()


def all_states(buttons, light_count):
    start_state = "." * light_count
    state_presses = {start_state: 0}
    queue = [start_state]

    while queue:
        state = queue.pop(0)
        current_presses = state_presses[state]

        for button in buttons:
            next_state = list(state)
            for i in button:
                next_state[i] = "#" if state[i] == "." else "."
            next_state = "".join(next_state)

            if next_state not in state_presses:
                state_presses[next_state] = current_presses + 1
                queue.append(next_state)

    return state_presses


press_count = 0
for l in remaining_manual:
    lights, buttons, joltages = re.split(r"] | {", l[1:-1])
    buttons = [list(int(x) for x in button[1:-1].split(",")) for button in buttons.split()]
    joltages = list(int(x) for x in joltages.split(","))

    press_count += all_states(buttons, len(lights))[lights]
print("answer 1:", press_count)


def precompute_combos(buttons, joltage_length):
    combos = collections.defaultdict(list)

    for presses in range(len(buttons) + 1):
        for button_combo in itertools.combinations(range(len(buttons)), presses):
            joltage = [sum(1 for i in button_combo if j in buttons[i]) for j in range(joltage_length)]

            pattern = tuple(j % 2 for j in joltage)
            combos[pattern].append((presses, tuple(joltage)))

    return combos


@functools.cache
def solve(current, combo_index):
    if any(i < 0 for i in current):
        return float('inf')
    if all(i == 0 for i in current):
        return 0

    combos = all_combos[combo_index]
    pattern = tuple(i % 2 for i in current)
    if pattern not in combos:
        return float('inf')

    return min(
        presses + 2 * solve(tuple((current[i] - joltage[i]) // 2 for i in range(len(current))), combo_index)
        for presses, joltage in combos[pattern]
    )


all_combos = []
press_count = 0
for i, l in enumerate(remaining_manual):
    lights, buttons, joltages = re.split(r"] | {", l[1:-1])
    buttons = [list(int(x) for x in button[1:-1].split(",")) for button in buttons.split()]
    joltages = list(int(x) for x in joltages.split(","))

    all_combos.append(precompute_combos(buttons, len(joltages)))
    press_count += solve(tuple(joltages), i)
print("answer 2:", press_count)
