import collections
import itertools

try:
    puzzle = open("inputs/day24.txt").read()
except FileNotFoundError:
    puzzle = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""[1:]
initials, gates = puzzle.split("\n\n")
initials = {key: int(state) for key, state in (initial.split(": ") for initial in initials.splitlines())}
gates = {gate.split()[4]: gate.split()[:3] for gate in gates.splitlines()}


def gate_value(layout, states, gate):
    gate_a, operation, gate_b = layout[gate]
    gate_a = states[gate_a] if gate_a in states else gate_value(layout, states, gate_a)
    gate_b = states[gate_b] if gate_b in states else gate_value(layout, states, gate_b)

    if operation == "AND":
        states[gate] = gate_a & gate_b
    elif operation == "OR":
        states[gate] = gate_a | gate_b
    elif operation == "XOR":
        states[gate] = gate_a ^ gate_b

    return states[gate]


binary = ""
for key in sorted(gates, reverse=True):
    if key.startswith("z"):
        binary += str(gate_value(gates.copy(), initials.copy(), key))
print("answer 1:", int(binary, 2))


def check_known_patterns(gates, x_pattern, y_pattern):
    z_max = max(int(key[1:]) for key in gates.keys() if key.startswith("z"))

    new_initials = initials.copy()
    binary_x = ""
    binary_y = ""
    for i, x, y in zip(range(z_max), itertools.cycle(x_pattern), itertools.cycle(y_pattern)):
        new_initials[f"x{i:02}"] = x
        new_initials[f"y{i:02}"] = y
        binary_x += str(x)
        binary_y += str(y)

    sum_binary = bin(int(binary_x, 2) + int(binary_y, 2))[2:].zfill(z_max + 1)
    binary = ""
    for key in sorted(gates, reverse=True):
        if key.startswith("z"):
            binary += str(gate_value(gates, new_initials, key))
    print(sum_binary == binary, "->", binary_x, binary_y, '\n', sum_binary, '\n', binary)

    return sum_binary == binary


new_gates = gates.copy()
keys = ['jgb', 'z20', 'rkf', 'z09', 'vcg', 'z24', 'rrs', 'rvc']
for i in range(0, len(keys), 2):
    new_gates[keys[i]], new_gates[keys[i + 1]] = new_gates[keys[i + 1]], new_gates[keys[i]]
success = True
for x_pattern, y_pattern in [([0], [0]), ([1], [1]), ([0, 1], [1, 0]), ([1, 0], [0, 1])]:
    success &= check_known_patterns(new_gates, x_pattern, y_pattern)
print("answer 2:", success, ",".join(sorted(keys)))
