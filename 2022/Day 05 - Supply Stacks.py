import collections
import re

try:
    cargo = open("inputs/day05.txt").read().splitlines()
except FileNotFoundError:
    cargo = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""[1:].splitlines()

crates_9000 = collections.defaultdict(collections.deque)
crates_9001 = collections.defaultdict(collections.deque)
for i, line in enumerate(cargo):
    if not line:
        break
    parts = re.findall(r"\w| {4}", line)
    for j, part in enumerate(parts):
        if part.strip():
            crates_9000[j + 1].appendleft(part)
            crates_9001[j + 1].appendleft(part)
for i in range(i + 1, len(cargo)):
    count, from_index, to_index = map(int, re.findall(r"\d+", cargo[i]))
    better = []
    for x in range(count):
        crates_9000[to_index].append(crates_9000[from_index].pop())
        better.insert(0, crates_9001[from_index].pop())
    crates_9001[to_index].extend(better)

print("answer 1:", "".join(crates_9000[i].pop() for i in sorted(crates_9000)))
print("answer 2:", "".join(crates_9001[i].pop() for i in sorted(crates_9001)))
