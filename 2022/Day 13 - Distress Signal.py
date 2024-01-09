from functools import cmp_to_key
from itertools import zip_longest

try:
    packets = open("inputs/day13.txt").read()
except FileNotFoundError:
    packets = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""[1:]


def is_ordered(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0
    elif isinstance(a, list) and isinstance(b, list):
        for left, right in zip_longest(a, b):
            if left is None:
                return -1
            if right is None:
                return 1
            ordered = is_ordered(left, right)
            if ordered != 0:
                return ordered
        return 0
    else:
        return is_ordered([a] if isinstance(a, int) else a, [b] if isinstance(b, int) else b)


indices = 0
for i, packet in enumerate(packets.rstrip().split("\n\n")):
    if is_ordered(*map(eval, packet.split("\n"))) <= 0:
        indices += i + 1

print("answer 1:", indices)

decode_key1 = [[2]]
decode_key2 = [[6]]
distress_signal = list(map(eval, packets.strip().replace("\n\n", "\n").splitlines()))
distress_signal.append(decode_key1)
distress_signal.append(decode_key2)
sorted_packets = sorted(distress_signal, key=cmp_to_key(is_ordered))
print("answer 2:", (sorted_packets.index(decode_key1) + 1) * (sorted_packets.index(decode_key2) + 1))
