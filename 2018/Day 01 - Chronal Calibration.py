frequency = 0
for change in open("inputs/day01.txt"):
    frequency += int(change)
print("answer 1:", frequency)

frequency = 0
seen = {0}
while True:
    for change in open("inputs/day01.txt"):
        frequency += int(change)
        if frequency in seen:
            break
        seen.add(frequency)
    else:
        continue
    break
print("answer 2:", frequency)
