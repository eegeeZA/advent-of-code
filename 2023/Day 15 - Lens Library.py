import collections
import re

try:
    initialization = open("inputs/day15.txt").read().strip()
except FileNotFoundError:
    initialization = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

total = 0
for step in initialization.split(","):
    hash_value = 0
    for char in step:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    total += hash_value
print("answer 1:", total)

boxes = collections.defaultdict(dict)
for step in initialization.split(","):
    label, *value = re.findall(r"\w+", step)
    hash_value = 0
    for char in label:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    if value:
        boxes[hash_value][label] = value.pop()
    else:
        boxes[hash_value].pop(label, None)
focusing_power = 0
for number in boxes:
    for slot, focal_length in enumerate(boxes[number].values()):
        focusing_power += (number + 1) * (slot + 1) * int(focal_length)
print("answer 2:", focusing_power)
